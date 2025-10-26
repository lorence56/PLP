import os

def modify_file_content(filepath):
    try:
        with open(filepath, 'r') as infile:
            content = infile.read()
        modified_content = content.upper()

        new_filename = f"modified_{os.path.basename(filepath)}"
        new_filepath = os.path.join(os.path.dirname(filepath), new_filename)

        with open(new_filepath, 'w') as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified file created successfully: {new_filepath}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("🚫 Error: Permission denied.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Main
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = input("Enter the filename to read: ")
filepath = os.path.join(script_dir, filename)
print(f"🔍 Looking for file at: {filepath}")
modify_file_content(filepath)
