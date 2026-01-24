"""
Prthon Alchemy

Module:
chapters.chapter_08_storing_and_reading_data.user_preferences_configuration

Simple JSON Processor: Storing and retrieving user preferences.
This script demonstrates:
1. Saving configuration data (user preferences) to a JSON file.
2. Reading the configuration back into a Python program.
3. Updating configuration values and rewriting them safely.
"""

import json
import os

def save_preferences(filename, preferences):
    """
    Save user preferences (Python dictionary) to a JSON file.

    Parameters:
    filename (str): Path to the JSON file.
    preferences (dict): User preferences to save.

    Returns:
    None
    """
    with open(filename, "w") as file:
        json.dump(preferences, file, indent=4) # Pretty format with indentation


def load_preferences(filename):
    """
    Load user preferences from a JSON file.

    Parameters:
    filename (str): Path to the JSON file.

    Returns:
    dict: Loaded user preferences. If file doesn’t exist, returns empty dict.
    """
    if not os.path.exists(filename):
        return {} # Return empty if file not found
    with open(filename, "r") as file:
        return json.load(file)
    

def update_preference(filename, key, value):
    """
    Update a specific preference in the JSON file.

    Parameters:
    filename (str): Path to the JSON file.
    key (str): The preference key to update.
    value (Any): The new value to assign.

    Returns:
    None
    """
    prefs = load_preferences(filename) # Load existing preferences
    prefs[key] = value # Update or add the key-value pair
    save_preferences(filename, prefs) # Save back to file


def main():
    """
    Main function to demonstrate JSON preference handling.
    """
    config_file = ".\\data\\user_prefs.json"
    # Example initial preferences
    preferences = {
        "theme": "dark",
        "font_size": 14,
        "language": "English",
        "notifications": True
    }

    # Step 1: Save preferences
    save_preferences(config_file, preferences)
    print(f"Preferences saved to {config_file}")

    # Step 2: Load preferences
    loaded_prefs = load_preferences(config_file)
    print("Loaded preferences:", loaded_prefs)

    # Step 3: Update a preference
    update_preference(config_file, "theme", "light")
    update_preference(config_file, "font_size", 16)
    
    # Step 4: Reload and verify updates
    updated_prefs = load_preferences(config_file)
    print("Updated preferences:", updated_prefs)

# Run the script
if __name__ == "__main__":
    main()