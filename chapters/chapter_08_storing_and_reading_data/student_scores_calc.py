"""
Python Alchemy

Module:
chapters.chapter_08_storing_and_reading_data.student_scores_calc

Simple CSV Processor: Read student scores, calculate averages, and write results.
This script demonstrates:
1. Reading CSV data using Python's built-in `csv` module.
2. Processing numerical values to compute averages.
3. Writing the processed results to a new CSV file.
"""

import csv
def read_scores(filename):
    """
    Reads student scores from a CSV file.

    Parameters:
    filename (str): The path to the input CSV file.

    Returns:
    list: A list of lists containing student names and their scores.
        Example: [["Ivaan", "80", "90", "85"], ["Laisha", "70", "60", "75"]]
    """

    with open(filename, "r") as file:
        reader = csv.reader(file)
        header = next(reader) # Skip header row
        data = [row for row in reader]
        return data
    

def calculate_averages(data):
    """
    Calculates average scores for each student.

    Parameters:
    data (list): List of rows, each containing a student's name and scores.

    Returns:
    list: Processed results with student name and their average score.
        Example: [["Ivaan", 85.0], ["Laisha", 68.3]]
    """
    results = []
    for row in data:
        name = row[0]
        # Convert scores from strings to integers
        scores = list(map(int, row[1:]))
        average = sum(scores) / len(scores)
        results.append([name, round(average, 2)]) # Rounded to 2 decimals

    return results


def write_results(filename, results):
    """
    Writes student averages to a new CSV file.

    Parameters:
    filename (str): The path to the output CSV file.
    
    results (list): List of [name, average] rows to be written.
    """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Average Score"]) # Header
        writer.writerows(results)


def main():
    """
    Main function to run the CSV processor.
    """
    import os
    print("Current Working Directory:", os.getcwd())
    # Input file: CSV with student scores
    input_file = ".\\data\\scores.csv"
    # Output file: CSV with student averages
    output_file = ".\\data\\averages.csv"

    # Step 1: Read scores
    data = read_scores(input_file)
    
    # Step 2: Calculate averages
    results = calculate_averages(data)
    
    # Step 3: Write results to a new CSV
    write_results(output_file, results)
    print(f"Processed {len(results)} students. Results saved to '{output_file}'.")
    

# Run the script
if __name__ == "__main__":
    main()