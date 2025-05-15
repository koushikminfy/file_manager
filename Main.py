import os
import shlex

def create_file_with_content(filename, content):
    if not filename.endswith(".txt"):
        filename += ".txt"
    try:
        with open(filename, 'x') as f:
            f.write(content)
        print(f"Created file '{filename}' with content.")
    except FileExistsError:
        print(f"Error: '{filename}' already exists.")

def list_directory():
    files = os.listdir()
    if not files:
        print("Directory is empty.")
    else:
        print(f"\nContents of {os.getcwd()}:")
        for item in files:
            label = "[DIR]" if os.path.isdir(item) else "[FILE]"
            print(f"{label} {item}")

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")

def run_file_manager():
    print("Welcome to the File Manager!")
    print("Available commands: touch <filename> <content>, ls, cd <directory>, exit")  
    print("Type 'exit' to quit the file manager.")
    print("Type 'ls' to list files in the current directory.")
    while True:
        try:
            command_line = input(">> ").strip()
            if not command_line:
                continue

            args = shlex.split(command_line)  # handles quoted strings correctly
            command = args[0]

            if command == "exit":
                print("Exiting file manager.")
                break

            elif command == "ls":
                list_directory()

            elif command == "cd" and len(args) > 1:
                change_directory(args[1])

            elif command == "touch" and len(args) > 2:
                filename = args[1]
                content = " ".join(args[2:])
                create_file_with_content(filename, content)

            else:
                print("Invalid command. Try: touch, ls, cd, exit.")

        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_file_manager()
