import os


def sub_folders_deletion(folder_dir):
    global full_non_empty_list
    not_empty_folder = []
    if os.path.isdir(folder_dir):
        folder_names = os.listdir(folder_dir)
        folders_to_delete = [os.path.join(folder_dir,i) for i in folder_names if os.path.isdir(os.path.join(folder_dir,i)) and i not in (".idea", "venv")]
        for folder in folders_to_delete:
            try:
                os.rmdir(folder)
            except OSError:
                not_empty_folder.append(folder)
                full_non_empty_list.append(folder)
    return not_empty_folder


def check_empty_folders(folder_dir_list):
    new_list = []
    for sub_folder in folder_dir_list:
        sub_folder_not_empty = sub_folders_deletion(sub_folder)
        if len(sub_folder_not_empty):
            check_empty_folders(sub_folder_not_empty)


# files and folders creation
os.makedirs("Dir1/Dir3/Dir4")
os.mkdir("Dir1/Dir2")
with open("File.txt", "w") as fd:
    pass

# folders deletion
user_input = input(f"Do you want to delete the folder? If yes, please enter 'yes':\n")

if user_input == 'yes':

    full_non_empty_list = []
    current_dir = os.getcwd()

    check_empty_folders(sub_folders_deletion(current_dir))
    full_non_empty_list = sorted(full_non_empty_list, reverse=True)

    for path in full_non_empty_list:
        os.rmdir(path)
