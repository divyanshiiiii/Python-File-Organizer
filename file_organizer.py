import os
import shutil
import time

def organize_files(path):
    """
    Organizes files in a given path into subdirectories based on their extension.
    """
    if not os.path.isdir(path):
        print(f"Error: The path '{path}' is not a valid directory.")
        return

    # Dictionary mapping folder names to file extensions
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat"],
        "Other": [] # A catch-all for unclassified file types
    }

    print(f"Scanning directory: {path}\n")
    time.sleep(1) # Pause for effect

    try:
        # Get all items in the directory
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        if not files:
            print("The directory is empty. Nothing to organize.")
            return

        organized_count = 0
        for filename in files:
            # Get the file extension
            file_ext = os.path.splitext(filename)[1].lower()

            # Determine the destination folder
            destination_folder = "Other" # Default folder
            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    destination_folder = folder
                    break

            # Create the destination folder if it doesn't exist
            dest_path = os.path.join(path, destination_folder)
            if not os.path.exists(dest_path):
                print(f"Creating folder: {destination_folder}")
                os.makedirs(dest_path)

            # Move the file
            source_file_path = os.path.join(path, filename)
            destination_file_path = os.path.join(dest_path, filename)
            
            # To avoid overwriting, check if a file with the same name exists
            if os.path.exists(destination_file_path):
                print(f"Skipping '{filename}' as it already exists in '{destination_folder}'.")
                continue

            print(f"Moving '{filename}' -> {destination_folder}")
            shutil.move(source_file_path, destination_file_path)
            organized_count += 1
            time.sleep(0.1) # Small delay to see the process

        print(f"\n✅ Organization complete! {organized_count} file(s) moved.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    print("--- Automatic File Organizer ---")
    # Get the directory path from the user
    target_directory = input("Enter the full path of the directory you want to organize: ")
    
    organize_files(target_directory.strip())
