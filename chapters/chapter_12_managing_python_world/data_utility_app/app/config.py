import configparser
import os

CONFIG_FILE = os.path.join("config", "settings.ini")

def load_config():
    """Load configuration from settings.ini file."""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return {
        "data_file": config.get("APP", "data_file", fallback="data/records.json"),
        "log_dir": config.get("LOGGING", "log_dir", fallback="logs"),
        "log_level": config.get("LOGGING", "log_level", fallback="INFO"),
    }
