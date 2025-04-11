"""
Módulo para monitorar alterações em arquivos markdown e atualizar o índice.
"""

import time
import logging
from pathlib import Path
from typing import Callable, Optional

# Configuração de logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FileWatcher:
    """Classe para monitorar alterações em arquivos markdown."""
    
    def __init__(self, directory: str, callback: Callable[[], None]):
        """
        Inicializa o observador de arquivos.
        
        Args:
            directory: Diretório a ser monitorado
            callback: Função a ser chamada quando uma mudança for detectada
        """
        self.directory = Path(directory)
        self.callback = callback
        self.observer = None
    
    def start(self) -> None:
        """Inicia o monitoramento de alterações."""
        logger.info(f"Iniciado monitoramento simulado em {self.directory}")
        try:
            from watchdog.observers import Observer
            from watchdog.events import FileSystemEventHandler
            
            class MarkdownChangeHandler(FileSystemEventHandler):
                def __init__(self, callback):
                    self.callback = callback
                
                def on_any_event(self, event):
                    if event.is_directory or not event.src_path.endswith('.md'):
                        return
                    logger.info(f"Detectada alteração em {event.src_path}")
                    self.callback()
            
            self.observer = Observer()
            event_handler = MarkdownChangeHandler(self.callback)
            self.observer.schedule(event_handler, str(self.directory), recursive=True)
            self.observer.start()
            logger.info(f"Monitoramento real iniciado em {self.directory}")
        except ImportError:
            logger.warning("Watchdog não encontrado, usando monitoramento simulado")
    
    def stop(self) -> None:
        """Para o monitoramento de alterações."""
        if self.observer:
            try:
                self.observer.stop()
                self.observer.join()
            except Exception as e:
                logger.error(f"Erro ao parar observador: {e}")
        logger.info("Monitoramento encerrado")