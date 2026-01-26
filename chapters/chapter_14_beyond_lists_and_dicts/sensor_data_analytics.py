"""
Python Alchemy

Module:
chapters.chapter_14_beyond_lists_and_dicts.sensor_data_analytics

Sensor Data Analytics Pipeline
--------------------------------
This module simulates a sensor data stream and processes it using
a lazy evaluation pipeline to compute average temperatures per sensor.
"""

import itertools
import random
import time
from collections import defaultdict

# --- Step 1: Simulating Continuous Sensor Data Stream ---
def sensor_data_stream(sensor_ids):
    """Simulate continuous temperature readings from multiple sensors."""
    for timestamp in itertools.count():  # infinite stream of timestamps
        sensor_id = random.choice(sensor_ids)
        temperature = round(random.uniform(18.0, 35.0), 2)
        yield (timestamp, sensor_id, temperature)
        time.sleep(0.01)  # simulate slight delay between readings


# --- Step 2: Building a Lazy Pipeline to Process Data ---
def process_data_stream(stream, limit=20):
    """
    Lazily process data stream:
    - Take only a limited number of readings
    - Sort and group by sensor
    - Compute average temperature
    """
    # Take only the first N readings lazily (no full stream in memory)
    sliced = itertools.islice(stream, limit)
    
    # Sort by sensor_id for grouping
    sorted_stream = sorted(sliced, key=lambda x: x[1])

    # Group by sensor_id
    grouped = itertools.groupby(sorted_stream, key=lambda x: x[1])
    
    # Aggregate averages per sensor
    results = {}
    for sensor, readings in grouped:
        temps = [r[2] for r in readings]
        results[sensor] = sum(temps) / len(temps)
    return results


# --- Step 3: Running the Pipeline ---
if __name__ == "__main__":
    sensors = ['Sensor-A', 'Sensor-B', 'Sensor-C']
    stream = sensor_data_stream(sensors)
    
    summary = process_data_stream(stream)
    
    print("=== Average Temperature Summary ===")
    for sensor, avg_temp in summary.items():
        print(f"{sensor}: {avg_temp:.2f}°C")