# file_read_write.py

def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ Modified content written to '{output_file}'")

    except FileNotFoundError:
        print("❌ The input file does not exist.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# Example usage:
modify_file("sample.txt", "modified_sample.txt")



# error_handling_lab.py

def safe_file_reader():
    filename = input("Enter the filename you want to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📂 File Content:")
            print(content)

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the name and try again.")
    except PermissionError:
        print("⚠️ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the lab
safe_file_reader()

