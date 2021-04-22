from tkinter import *
from PIL import ImageTk, Image
import sys


root = Tk()

# Setting the window size.
root.geometry('600x400')


# This is the function for clicking a button in the main menu.
def main_menu_click(value):
    # Deletes the frame with all displayed content
    main_frame.pack_forget()

    if value == 'play':
        display_theme()
        # test_play = Label(root, text='Playing madlibs coming soon...').pack()
    elif value == 'stats':
        test_stats = Label(root, text='Display statistics coming soon...').pack()
        # function for viewing statistics
    else:
        sys.exit()  # ends program


# Displays theme options for user to choose from.
def display_theme():
    # Create a label to instruct user.
    choose_theme_label = Label(root, text='Choose a theme:')
    choose_theme_label.grid(row=0, column=0)

    # Create a variable to store value from radiobutton.
    theme_var = StringVar()

    themes = ['Vaction', 'Zoo', 'Park']
    for theme in themes:
        Radiobutton(
            root,
            text=theme,
            variable=theme_var,
            value=theme
            ).grid(row=themes.index(theme) + 1, column=0)


# Main frame
main_frame = Frame(root)
main_frame.pack()

# Main menu prompt label
menu_label = Label(main_frame, text='Please select from one of the following:')
menu_label.grid(row=0, column=0)

# Variable that radiobutton below will set.
user_menu_option = StringVar()

# Menu option stored in a list. Each tuple is an option, value 0 in the tuple
# is the displayed string, value 1 is the value assigned to user_menu_option.
menu_options = [
    ('Play Madlibs', 'play'),
    ('View Statistics', 'stats'),
    ('Quit', 'quit')
    ]

# Define and display the menu options in radiobuttion.
rb_play = Radiobutton(
    main_frame,
    text=menu_options[0][0],
    variable=user_menu_option,
    value=menu_options[0][1]
    )
rb_stats = Radiobutton(
    main_frame,
    text=menu_options[1][0],
    variable=user_menu_option,
    value=menu_options[1][1]
    )
rb_quit = Radiobutton(
    main_frame,
    text=menu_options[2][0],
    variable=user_menu_option,
    value=menu_options[2][1]
    )
rb_play.grid(row=1, column=0)
rb_stats.grid(row=2, column=0)
rb_quit.grid(row=3, column=0)

# Button for the main menu radiobuttons.
main_menu_button = Button(
    main_frame,
    text='Enter',
    command=lambda: main_menu_click(user_menu_option.get())
)
main_menu_button.grid(row=4, column=0)

# for text, option in menu_options:
#     for row in range(1, len(menu_options) + 1):
#         Radiobutton(main_frame, text=text, value=option).grid(row=row, column=0)


root.mainloop()
