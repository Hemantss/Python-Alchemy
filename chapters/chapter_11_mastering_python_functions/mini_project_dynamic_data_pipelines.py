"""
Python Alchemy

Module:
chapters.chapter_11_mastering_python_functions.mini_project_dynamic_data_pipelines

Mini Project: Dynamic Data Processing Pipelines with Generators and Closures
-----------------------------------------------------------
This program demonstrates practical use of:
- Generators for memory-efficient data processing
- Closures for creating customizable filter functions
"""


def make_filter(keyword):
    """
    Creates a closure that generates a filter function for dynamic keywordbased filtering.
    
    Parameters:
    keyword (str): The keyword to search for within each line of text.
    
    Returns:
    function: A generator function that yields only lines containing thespecified keyword.
    """

    def filter_func(lines):
        """
        Filters lines that contain the specified keyword.
        
        Parameters:
        lines (iterable): An iterable sequence of text lines.
        
        Yields:
        str: Lines containing the keyword (case-insensitive).
        """
        for line in lines:
            if keyword.lower() in line.lower():
                yield line
    return filter_func
    

def read_data(source):
    """
    A generator that reads data line by line from a given source file.

    Parameters:
    source (str): Path to the input file.

    Yields:
    str: Each line from the file, stripped of leading and trailing whitespace.
    """

    with open(source, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def transform(lines):
    """
    Transforms lines of text by converting them to uppercase.
    Parameters:
    lines (iterable): An iterable sequence of text lines.
    Yields:
    str: The transformed (uppercase) version of each line.
    """
    for line in lines:
        yield line.upper()


def output(lines):
    """
    Outputs the final processed lines to the console.
    Parameters:
    lines (iterable): An iterable sequence of processed text lines.
    Returns:
    None
    """
    for line in lines:
        print(line)


# --- Building the data processing pipeline dynamically ---
if __name__ == "__main__":
    source = ".\\data\\data.txt"
    keyword = "python"
    # Constructing the pipeline: read → filter → transform → output
    pipeline = transform(make_filter(keyword)(read_data(source)))
    output(pipeline)