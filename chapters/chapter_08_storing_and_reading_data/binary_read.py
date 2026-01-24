"""
Python Alchemy

Module:
chapters.chapter_08_storing_and_reading_data.binary_read

Binary File Handling Example:
Reading and writing binary data (e.g., an image or binary log file).
This script demonstrates:
1. Writing raw bytes to a binary file.
2. Reading the binary file back into Python.
3. Interpreting the binary content safely.
"""

def write_binary_file(filename):
    """
    Write sample byte content to a binary file.

    Parameters:
    filename (str): Path of the binary file to create.

    Returns:
    None
    """
    # Sample binary content (simulating raw data, like an image header or log bytes
    data = b"\x89PNG\r\n\x1a\nBinaryDataExample12345"
    with open(filename, "wb") as file:
        file.write(data)
        print(f"Binary data written to {filename}")


def read_binary_file(filename):
    """
    Read and display byte content from a binary file.
    Parameters:
    filename (str): Path of the binary file to read.
    Returns:
    bytes: Raw binary content of the file.
    """
    with open(filename, "rb") as file:
        content = file.read()
        print(f"Binary data read from {filename}:")
        print(content) # Raw bytes (may include unreadable symbols)
        
        # If the content contains readable text, decode safely
        try:
            decoded = content.decode("utf-8")
            print("Decoded (UTF-8) content:", decoded)
        except UnicodeDecodeError:
            print("Content includes non-textual binary data (not fully decodable).")
        return content
    

def main():
    """
    Main function to demonstrate binary file handling.
    """
    filename = ".\\data\\sample_binary.bin"
    
    # Step 1: Write binary data
    write_binary_file(filename)
    
    # Step 2: Read binary data
    read_binary_file(filename)


# Run script
if __name__ == "__main__":
    main()