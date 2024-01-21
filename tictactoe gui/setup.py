from tkinter import *
from play_sound import PlaySound
# CLASS SETUP:
# intialise it
# get setup.level which is an int
# level - 0 => play with a friend
# level - 1 => easy
# level - 2 => medium
# level - 3 => hard


class Setup:
    def __init__(self, root) -> None:
        # this takes root as the input so this class and the UserInterface class both work on the same window
        self.root = root
        self.root.title("Setup")

        self.sound = PlaySound()
        # creating a frame widget on which we're gonna have all the other widgets
        self.frame = Frame(self.root)  # , height=900, width=1440)
        self.frame.grid(row=0, column=0)

        # creating the canvas and setting the bg image
        bg_image = PhotoImage(file="images/choose_level_resized.png")
        self.canvas = Canvas(master=self.frame, height=900, width=1440)
        self.canvas.grid(row=0, column=0)
        self.canvas_bg = self.canvas.create_image(720, 450, image=bg_image)

        self.button_image = PhotoImage(file="images/blank_button_resized.png")
        # just giving a random value to level. 1 is just a placeholder
        self.level = 1
        self.draw_buttons()

        # when the var changes, the drame gets destroyed so that the actual game can be desplayed in the UserInterface class
        self.var = BooleanVar()
        self.root.wait_variable(self.var)
        self.frame.destroy()

    def draw_buttons(self):
        self.easy_button = Button(master=self.frame, image=self.button_image, text='Easy', compound='center', bd=0, borderwidth=0, highlightthickness=0, font=(
            "courier", 35, 'italic'), command=self.easy_clicked, fg='white')
        self.easy_button.place(x=380, y=450)

        self.medium_button = Button(master=self.frame, image=self.button_image, text='Medium', compound='center',bd=0, borderwidth=0, highlightthickness=0, font=(
            "courier", 35, 'italic'), command=self.medium_clicked, fg='white')
        self.medium_button.place(x=760, y=450)

        self.hard_button = Button(master=self.frame, image=self.button_image, text='Impossible', compound='center', bd=0, borderwidth=0, highlightthickness=0, font=(
            "courier", 35, 'italic'), command=self.hard_clicked, fg='white')
        self.hard_button.place(x=380, y=600)

        self.friend_button = Button(master=self.frame, image=self.button_image, compound='center', text='Two players', bd=0, borderwidth=0,
                                    highlightthickness=0, font=("courier", 35, 'italic'), command=self.friend_clicked, fg='white')
        self.friend_button.place(x=760, y=600)

    # updating the self.level in these functions and changing the var value so that the frame can be destroyed
    def easy_clicked(self):
        self.level = 1
        self.var.set(False)
        self.sound.button_noise()

    def medium_clicked(self):
        self.var.set(False)
        self.level = 2
        self.sound.button_noise()

    def hard_clicked(self):
        self.level = 3
        self.var.set(False)
        self.sound.button_noise()

    def friend_clicked(self):
        self.level = 0
        self.var.set(False)
        self.sound.button_noise()


if __name__ == '__main__':
    window = Tk()
    su = Setup(window)
    print(su.level)
