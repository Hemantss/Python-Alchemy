import json
import os
from logger import log_info, log_error
from time_utils import current_timestamp
from config import load_config

config = load_config()
DATA_FILE = config["data_file"]

def save_record(data):
    """Save a record to JSON file with timestamp."""
    try:
        record = {"timestamp": current_timestamp(), "data": data}
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                records = json.load(file)
        else:
            records = []

        records.append(record)

        with open(DATA_FILE, "w") as file:
            json.dump(records, file, indent=4)

        log_info(f"Record saved successfully: {record}")
    except Exception as e:
        log_error(f"Error saving record: {e}")

def load_records():
    """Load all records from JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            records = json.load(file)
        log_info(f"Loaded {len(records)} records.")
        return records
    except FileNotFoundError:
        log_error("No records found. Returning empty list.")
        return []
    except Exception as e:
        log_error(f"Error reading records: {e}")
        return []