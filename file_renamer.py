import os

def rename_files_in_folder(folder_path, prefix='', suffix=''):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    files = os.listdir(folder_path)
    for filename in files:
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{name}{suffix}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)

    print("Files renamed successfully.")

if __name__ == "__main__":
    path = input("Enter folder path: ")
    prefix = input("Enter prefix to add (or leave blank): ")
    suffix = input("Enter suffix to add (or leave blank): ")
    rename_files_in_folder(path, prefix, suffix)
