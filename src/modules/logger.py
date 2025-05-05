# ✅ SUPREMO BLOCK: Logger centralizado
# Localização correta: src/modules/logger.py

import logging
import os
from datetime import datetime

def criar_logger():
    logger = logging.getLogger('PrintA')
    logger.setLevel(logging.DEBUG)

    # Evitar duplicação de handlers
    if not logger.handlers:
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../logs')
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(log_dir, f'log_{datetime.now().strftime("%Y%m%d")}.log')
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger
