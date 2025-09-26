# Python-File-Organizer
1-  Automatic File Organizer
     A simple but powerful Python script to automatically organize files in a directory into categorized subfolders based on their file extension.

  Description
  This script helps you clean up messy folders like "Downloads" or "Desktop" by moving files into specific directories for Images, Documents, Videos, Audio, and more. It's a great tool for maintaining a tidy        file system without manual effort.

  How to Use
1- Clone or download this repository.

2- Run the script from your terminal:

   python file_organizer.py

3- Enter the full path to the directory you want to organize when prompted.

4- The script will scan the directory, create new folders for different file types if they don't already exist, and move the files accordingly.

Features
* Categorization: Sorts files into logical folders (Images, Documents, Videos, etc.).

* Automatic Folder Creation: Creates destination folders if they don't exist.

* Safe Moving: Checks if a file with the same name already exists in the destination to prevent overwriting.

* User-Friendly: Simple command-line interface.

Technologies Used

* Python 3

* Standard Libraries:
  
  os: For interacting with the operating system and file paths.

  shutil: For high-level file operations (moving files).

  time: For adding small delays to enhance user experience.


time: For adding small delays to enhance user experience.
