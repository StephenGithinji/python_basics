# Error Handling Lab 🧪

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\nFile content:\n")
        print(content)
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
