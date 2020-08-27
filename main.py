import os.path

def move_file():
    if os.path.isfile('folder_1/some_text.txt') == True:
        return os.rename('folder_1/some_text.txt', 'folder_2/some_text.txt')
    elif os.path.isfile('folder_2/some_text.txt') == True:
        return os.rename('folder_2/some_text.txt', 'folder_1/some_text.txt')

move_file()