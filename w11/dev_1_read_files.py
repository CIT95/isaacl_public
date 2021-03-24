import pyinputplus as pyip
import os
from pathlib import Path


# Locate theme folders that will be used.
rel_p = os.path.relpath('isaacl_public/w11/mad_libs_themes', Path.cwd())
p = Path(os.path.abspath(Path.cwd() / rel_p))


# Create a function that appends all possible themes into a list.
def theme_list():
    themes = []
    # Irriterate through theme folder to extract all theme names.
    # Subfolder names are the name of the theme.
    for folders, subfolders, files in os.walk(p):
        for subfolder in subfolders:
            themes.append(subfolder)

    return themes


# Give the user an option to choose from all available themes.
def choose_theme(theme_list):
    print('Choose your theme:')
    user_theme = pyip.inputMenu(theme_list)  # displays all themes

    return user_theme


def create_file_path(theme):
    # Add .txt to choosen theme.
    file_name = theme + '.txt'
    # Create new file path.
    file_path = p / theme / file_name

    return file_path


def read_placeholder_text(txt_file_path):
    # Open .txt file.
    theme_file = open(txt_file_path)
    # Display .txt file for user.
    placeholder_content = theme_file.read()

    print(placeholder_content)


themes = theme_list()
user_theme = choose_theme(themes)
theme_path = create_file_path(user_theme)
display_text = read_placeholder_text(theme_path)
