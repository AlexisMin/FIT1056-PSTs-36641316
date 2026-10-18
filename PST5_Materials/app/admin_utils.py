import logging
import shutil
from datetime import datetime
from pathlib import Path

def init_logger(log_file="msms.log"):
    """Set up Python's logging module."""
    root = logging.getLogger()
    if root.handlers:  # Don't add duplicate handlers if called twice
        return root
    root.setLevel(logging.INFO)
    
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)
    
    logging.info("Logger initialised.")
    return root

def backup_data(data_path="data/msms.json", backup_dir="backups"):
    """Copy the data file with a timestamp."""
    src = Path(data_path)
    if not src.exists():
        return
        
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = backup_dir / f"{src.stem}_{stamp}{src.suffix}"
    shutil.copy2(src, dest)
    logging.info(f"Backup created: {dest}")