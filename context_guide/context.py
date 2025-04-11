"""
Módulo de gerenciamento de contexto usando LlamaIndex e ChromaDB.
"""

import os
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path

# Configuração de logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ContextManager:
    """Gerencia a indexação e consulta de documentos markdown para fornecer contexto."""
    
    def __init__(self, docs_dir: str = "docs", db_dir: str = "chroma_db", collection_name: str = "markdown_docs"):
        """
        Inicializa o gerenciador de contexto.
        
        Args:
            docs_dir: Diretório contendo os arquivos markdown
            db_dir: Diretório para armazenar o banco de dados ChromaDB
            collection_name: Nome da coleção no ChromaDB
        """
        self.docs_dir = Path(docs_dir)
        self.db_dir = Path(db_dir)
        self.collection_name = collection_name
        
        # Garantir que os diretórios existam
        self.docs_dir.mkdir(exist_ok=True)
        self.db_dir.mkdir(exist_ok=True)
        
        try:
            # Importações que podem falhar
            from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
            from llama_index.vector_stores.chroma import ChromaVectorStore
            from llama_index.core.embeddings import resolve_embed_model
            from llama_index.core.node_parser import SentenceSplitter
            import chromadb
            
            # Configurar o modelo de embeddings
            embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")
            Settings.embed_model = embed_model
            Settings.chunk_size = 512
            
            # Inicializar ChromaDB
            self.client = chromadb.PersistentClient(path=str(self.db_dir))
            self._initialize_index()
            self.llama_available = True
        except ImportError as e:
            logger.error(f"Erro ao importar dependências: {e}")
            logger.warning("Funcionando em modo limitado sem LlamaIndex e ChromaDB")
            self.llama_available = False
        
        logger.info(f"ContextManager inicializado com documentos em '{self.docs_dir}' e ChromaDB em '{self.db_dir}'")
    
    def _initialize_index(self) -> None:
        """Inicializa ou carrega o índice existente."""
        if not self.llama_available:
            logger.info("Método _initialize_index chamado (stub)")
            return None
            
        try:
            from llama_index.core import VectorStoreIndex
            from llama_index.vector_stores.chroma import ChromaVectorStore
            
            # Tentar obter a coleção existente
            self.chroma_collection = self.client.get_or_create_collection(self.collection_name)
            
            # Configurar o vector store do LlamaIndex
            vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
            
            # Criar ou carregar o índice
            if self.chroma_collection.count() == 0:
                logger.info("Criando novo índice de documentos...")
                self._create_index(vector_store)
            else:
                logger.info(f"Carregando índice existente com {self.chroma_collection.count()} documentos...")
                self.index = VectorStoreIndex.from_vector_store(vector_store)
        except Exception as e:
            logger.error(f"Erro ao inicializar índice: {e}")
            raise
    
    def _create_index(self, vector_store) -> None:
        """
        Cria um novo índice a partir dos documentos markdown.
        
        Args:
            vector_store: ChromaVectorStore para armazenar os embeddings
        """
        if not self.llama_available:
            return None
            
        from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
        from llama_index.core.node_parser import SentenceSplitter
        
        if not any(self.docs_dir.glob("*.md")):
            logger.warning(f"Nenhum arquivo markdown encontrado em '{self.docs_dir}'")
            # Criar um índice vazio para evitar erros
            self.index = VectorStoreIndex.from_vector_store(vector_store)
            return
        
        # Carregar documentos do diretório
        documents = SimpleDirectoryReader(
            input_dir=str(self.docs_dir),
            required_exts=[".md"]
        ).load_data()
        
        logger.info(f"Carregados {len(documents)} documentos markdown")
        
        # Dividir documentos em chunks menores
        parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
        nodes = parser.get_nodes_from_documents(documents)
        
        # Criar índice
        self.index = VectorStoreIndex(nodes, vector_store=vector_store)
        logger.info(f"Índice criado com {len(nodes)} nodes")
    
    def update_index(self) -> None:
        """Atualiza o índice com novos documentos ou alterações."""
        if not self.llama_available:
            logger.info("Método update_index chamado (stub)")
            return None
            
        logger.info("Atualizando índice de documentos...")
        
        # Deletar coleção existente e recriar
        self.client.delete_collection(self.collection_name)
        self.chroma_collection = self.client.create_collection(self.collection_name)
        
        # Reconfigurar vector store e recriar índice
        from llama_index.vector_stores.chroma import ChromaVectorStore
        vector_store = ChromaVectorStore(chroma_collection=self.chroma_collection)
        self._create_index(vector_store)
        
        logger.info("Índice atualizado com sucesso")
    
    def get_relevant_context(self, query: str, num_results: int = 5) -> Dict[str, Any]:
        """
        Consulta o índice para obter contexto relevante para uma consulta.
        
        Args:
            query: A consulta para buscar contexto relevante
            num_results: Número máximo de resultados a retornar
            
        Returns:
            Dicionário com o contexto relevante
        """
        if not self.llama_available:
            logger.info(f"Consulta recebida: {query} (stub)")
            return {
                "context": f"Contexto simulado para a consulta: {query}",
                "sources": [{"content": "Conteúdo de teste", "metadata": {"file_path": "docs/test.md"}}]
            }
            
        if not hasattr(self, 'index') or self.chroma_collection.count() == 0:
            logger.warning("Índice vazio ou não inicializado. Retornando contexto vazio.")
            return {"context": "", "sources": []}
        
        try:
            # Criar query engine e realizar consulta
            query_engine = self.index.as_query_engine(similarity_top_k=num_results)
            response = query_engine.query(query)
            
            # Extrair nós fonte
            source_nodes = response.source_nodes
            sources = []
            
            # Processar fontes para incluir nome do arquivo e conteúdo
            for node in source_nodes:
                source_info = {
                    "content": node.text,
                    "metadata": node.metadata,
                    "score": node.score if hasattr(node, 'score') else None
                }
                sources.append(source_info)
            
            # Retornar contexto formatado
            return {
                "context": str(response),
                "sources": sources
            }
        except Exception as e:
            logger.error(f"Erro ao consultar contexto: {e}")
            return {"context": "", "sources": [], "error": str(e)} 