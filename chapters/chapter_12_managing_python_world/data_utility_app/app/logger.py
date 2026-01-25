import logging
from datetime import datetime
import os
from config import load_config

config = load_config()
LOG_DIR = config["log_dir"]
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"app_log_{datetime.now().strftime('%Y%m%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=getattr(logging, config["log_level"].upper(), logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message: str):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message: str):
    logging.error(message)
    print(f"[ERROR] {message}")