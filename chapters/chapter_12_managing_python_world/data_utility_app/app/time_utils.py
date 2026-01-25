from datetime import datetime

def current_timestamp():
    """Return current timestamp as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def timestamp_difference(start, end):
    """Calculate the difference between two timestamps."""
    fmt = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start, fmt)
    end_dt = datetime.strptime(end, fmt)
    return (end_dt - start_dt).total_seconds()
