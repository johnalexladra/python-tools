import os
import shutil

def create_folder_if_not_exists(folder_path):
    """Create a folder if it does not exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def move_file(file_path, destination_folder):
    """Move a file to a destination folder."""
    if not os.path.isfile(file_path):
        return
    create_folder_if_not_exists(destination_folder)
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

def organize_files_by_extension(directory):
    """Organize files in the given directory by their extensions."""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            # Get file extension
            _, extension = os.path.splitext(item)
            extension = extension[1:]  # Remove the dot
            if extension:
                # Create a folder named after the file extension
                destination_folder = os.path.join(directory, extension)
                move_file(item_path, destination_folder)

if __name__ == "__main__":
    # Change this to the directory you want to organize
    target_directory = os.getcwd()
    organize_files_by_extension(target_directory)
    print(f"Files in '{target_directory}' have been organized by their extensions.")
