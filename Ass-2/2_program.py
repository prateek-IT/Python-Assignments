# 2.  Write a function that reads a text file and returns its lines.
#     - Use with open(...) as f:
#     - Catch and handle FileNotFoundError with a user-friendly message.
#     - From main(), prompt user for file name, call read_lines, then print line count

def read_lines(file_name: str) -> list[str]:
    try:
        with open(file_name, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    
if __name__ == "__main__":
    file_name = input("Please enter the file name: ")
    lines = read_lines(file_name)
    print(f"Number of lines in '{file_name}': {len(lines)}")
        
