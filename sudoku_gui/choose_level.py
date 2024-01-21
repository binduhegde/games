import random
from tkinter import *
from tkmacosx import Button # lets us change the bg color of button

# phosphate noteworthy
BG = "#283547"
BUTTON_BG = "#16202e"
FONT = ('phosphate', 50)
def choose_level():
    root = Tk()
    root.geometry("500x900")
    root.config(bg=BG)
    global levels
    # these are the values we can put inside Sudoku module difficulty level
    levels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    # whenever a button is clicked, this var value changes
    var = BooleanVar()

    def easy():
        global chosen_level, levels
        chosen_level = random.choice(levels[:3])
        var.set(False)
    def medium():
        global chosen_level, levels
        chosen_level = random.choice(levels[3:6])
        var.set(False)
    def hard():
        global chosen_level, levels
        chosen_level = random.choice(levels[6:8])
        var.set(False)
    def extreme():
        global chosen_level, levels
        chosen_level = levels[8]
        var.set(False)

    sudoku_image = PhotoImage(file="images/sudoku_title.png")
    choose_level_image = PhotoImage(file="images/choose_level.png")

    title_label = Label(image=sudoku_image, bg=BG)
    title_label.place(x=250, y=150, anchor='center')
    
    choose_level_label = Label(image=choose_level_image, bg=BG)
    choose_level_label.place(x=250, y=300, anchor='center')

    easy_button = Button(text="EASY", command=easy, bg=BUTTON_BG, font=FONT, fg='white', width= 300)
    easy_button.place(x=250, y=400, anchor='center')
    medium_button = Button(text="MEDIUM", command=medium, bg=BUTTON_BG, font=FONT, fg='white', width= 300)
    medium_button.place(x=250, y=500, anchor='center')
    hard_button = Button(text="HARD", command=hard, bg=BUTTON_BG, font=FONT, fg='white', width= 300)
    hard_button.place(x=250, y=600, anchor='center')
    extreme_button = Button(text="EXTREME", command=extreme, bg=BUTTON_BG, font=FONT, fg='white', width= 300)
    extreme_button.place(x=250, y=700, anchor='center')

    # the window waits till the var value is changed.
    # after that it will destroy the window and reutrns chosen_value
    root.wait_variable(var)
    root.destroy()
    return chosen_level

if __name__ == '__main__':
    print(choose_level())