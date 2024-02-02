import shutil

def copy_image():
    # Get source image path from the user
    source_image_path = input("Enter the path of the source image: ")

    # Get destination folder from the user
    destination_folder = input("Enter the path of the destination folder: ")

    try:
        # Copy the image to the destination folder
        shutil.copy(source_image_path, destination_folder)
        print(f"Image copied from {source_image_path} to {destination_folder}")
    except FileNotFoundError:
        print("Error: Source image not found.")
    except IsADirectoryError:
        print("Error: Destination should be a folder, not a file.")
    except PermissionError:
        print("Error: Permission denied. Make sure you have the necessary permissions.")

if __name__ == "__main__":
    copy_image()
