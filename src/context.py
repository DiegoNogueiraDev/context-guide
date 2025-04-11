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
        except ImportError as e:
            logger.error(f"Erro ao importar dependências: {e}")
            logger.warning("Funcionando em modo limitado sem LlamaIndex e ChromaDB")
        
        logger.info(f"ContextManager inicializado com documentos em '{self.docs_dir}' e ChromaDB em '{self.db_dir}'")
    
    def _initialize_index(self) -> None:
        """Inicializa ou carrega o índice existente."""
        logger.info("Método _initialize_index chamado (stub)")
        return None
    
    def update_index(self) -> None:
        """Atualiza o índice com novos documentos ou alterações."""
        logger.info("Método update_index chamado (stub)")
        return None
    
    def get_relevant_context(self, query: str, num_results: int = 5) -> Dict[str, Any]:
        """
        Consulta o índice para obter contexto relevante para uma consulta.
        
        Args:
            query: A consulta para buscar contexto relevante
            num_results: Número máximo de resultados a retornar
            
        Returns:
            Dicionário com o contexto relevante
        """
        logger.info(f"Consulta recebida: {query} (stub)")
        return {
            "context": f"Contexto simulado para a consulta: {query}",
            "sources": [{"content": "Conteúdo de teste", "metadata": {"file_path": "docs/test.md"}}]
        }