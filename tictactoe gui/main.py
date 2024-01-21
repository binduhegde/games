from tkinter import *
from brain import GameBrain
from setup import Setup
from play_sound import PlaySound


class UserInterface:
    def __init__(self) -> None:
        # creating a window and making it enter fullsccreen by default
        self.window = Tk()
        self.window.attributes('-fullscreen', True)
        # we are sending this window as the imput to Setup
        setup = Setup(self.window)
        # this level can be easy, medium, hard or play against a friend
        # 1: easy, 2: medium, 3:hard and 0: play against a friend
        self.level = setup.level
        # we're passing the level int as the input to gamebrain and it will
        # figure out the next moves according to the difficulty level
        self.brain = GameBrain(self.level)

        self.window.title("Tic-Tac-Toe")

        self.play_sound = PlaySound()

        # *-------------------ALL THE IMAGES-------------------#
        self.bg_image = PhotoImage(file="images/bg_resized.png")
        self.o_image = PhotoImage(file="images/o_resized.png")
        self.x_image = PhotoImage(file="images/x_resized.png")
        self.blank_image = PhotoImage(file="images/blank_resized.png")
        self.green_o = PhotoImage(file="images/green_o_resized.png")
        self.green_x = PhotoImage(file="images/green_x_resized.png")
        self.x_won = PhotoImage(file="images/x_won_resized.png")
        self.o_won = PhotoImage(file="images/o_won_resized.png")
        self.draw = PhotoImage(file="images/draw_resized.png")
        self.restart_image = PhotoImage(file="images/replay_image_resized.png")
        self.level_image = PhotoImage(file="images/level_image_resized.png")

        # explained this at the bottom of the file
        self.ind = 0
        self.players = ['X', 'X']
        self.player_images = [self.x_image, self.x_image]
        if self.level == 0:
            self.players = ['X', 'O']
            self.player_images = [self.x_image, self.o_image]

        # *-----------------SETTING UP THE CANVAS-------------------#
        self.canvas = Canvas(height=900, width=1440)
        self.canvas.grid(row=0, column=0)
        self.canvas_bg = self.canvas.create_image(
            720, 450, image=self.bg_image)
        self.whose_turn_text = self.canvas.create_text(
            1000, 200, text="X turn", font=('courier', 30), fill="#b3a8aa")

        # *-------------DRAWING ALL THE BUTTONS-----------------#
        self.draw_buttons()

        # *-----------RESTART BUTTON--------------#
        self.restart_button = Button(
            image=self.restart_image, command=self.restart, bd=0, borderwidth=0, highlightthickness=0)
        self.restart_button.place(x=770, y=820)

        self.level_button = Button(
            image=self.level_image, command=self.restart, bd=0, borderwidth=0, highlightthickness=0)
        self.level_button.place(x=1000, y=820)

        self.window.mainloop()

    # when a user clicks a place to draw X
    def button_pressed(self, i: int) -> None:
        self.play_sound.click_noise()
        # updates the board
        self.brain.board[i] = self.players[self.ind]
        # updates the image of the button in the said place
        self.buttons[i].config(image=self.player_images[self.ind])
        # explained this at the bottom of the file
        self.ind = (self.ind + 1) % 2

        self.canvas.itemconfig(self.whose_turn_text, text=f"{
                               self.players[self.ind]} turn")
        # gets a dict from the brain object about what to do next
        # {board: [[]], is_complete: true/false, winner: 0/1/2, line:[0, 1, 2]}
        # winner 1: computer X (us), winnner 2: user O, winner 0: tie
        # is_complete returns true if the game is over
        next_move = self.brain.next_move()
        # the next_move updates the board so we need to update the button image too
        # hence calling this func
        self.draw_buttons()
        # disabling the marked buttons so that the user won't click them
        self.disable_buttons(all_buttons=False)
        # means the game is over
        if next_move['is_complete']:
            if next_move['winner'] == 1:  # X won
                self.highlight(next_move['line'], 'X')
            elif next_move['winner'] == 2:  # O won
                self.highlight(next_move['line'], 'O')
            else:  # it's a tie
                self.highlight(next_move['line'], 'T')

    # this function looks at the board if board[i] == None, it will draw a black image button
    # if board[i] == 'X', it'll draw a X button and so on
    def draw_buttons(self) -> None:
        self.buttons = []
        # to get the indices of the button because we're using two for loops
        # will increase it by one everytime we create a button
        ind = 0
        # these are the numbers found through trial and error.
        # each row starts at 230 y cor and increases by 180 for each button
        # since we have 3 buttons, the last button would be at 590. hence 591
        for y in range(230, 591, 180):
            # each column starts at 760 x cor and increases by 165 for each button
            # since we have 3 buttons, the last button would be at 1090. hence 1091
            for x in range(760, 1091, 165):
                if self.brain.board[ind] is None:
                    current_image = self.blank_image
                elif self.brain.board[ind] == 'X':
                    current_image = self.x_image
                else:
                    current_image = self.o_image
                # lambda ind=ind ensures that the respective index value is is passed and
                # not the last one. because by the time these for loops are done, the ind value would be 9
                button = Button(image=current_image, bd=0, borderwidth=0,
                                highlightthickness=0, command=lambda ind=ind: self.button_pressed(ind))
                button.place(x=x, y=y)
                self.buttons.append(button)
                ind += 1

    # when a player has won, this changes the background color of the winning line so that it looks highlighted
    # line stores the index value of the line which won. winner could be 'X' or 'O' or anything else.
    # as long as it's neither 'X' not 'O' it does'nt matter what is it, we're gonna assume it's a tie
    def highlight(self, line: list, winner: str) -> None:
        self.play_sound.game_over()
        # we're disabling all the buttons cuz the game is over
        self.disable_buttons(all_buttons=True)
        if winner == 'X':
            for i in line:
                # changing the button image
                self.buttons[i].config(image=self.green_x)
            # changing the bg image
            self.canvas.itemconfig(self.canvas_bg, image=self.x_won)
        elif winner == 'O':
            for i in line:
                # changing the button image
                self.buttons[i].config(image=self.green_o)
            # changing the bg image
            self.canvas.itemconfig(self.canvas_bg, image=self.o_won)
        else:  # it's a tie hence no line to highlight
            # changing the bg image
            self.canvas.itemconfig(self.canvas_bg, image=self.draw)

    # disables the buttons, if all buttons is True, it will disable all the buttons
    # else it only disables the buttons where it's already marked X or O
    def disable_buttons(self, all_buttons: bool) -> None:
        if not all_buttons:
            for i in range(9):
                if self.brain.board[i] != None:
                    self.buttons[i].config(state='disabled')
        else:
            for button in self.buttons:
                button.config(state='disabled')

    # runs when the restart_button is clicked
    def restart(self) -> None:
        # makes another instance of the brain with the same level which clears the board
        # then draws all the buttons
        self.play_sound.button_noise()
        self.brain = GameBrain(self.level)
        self.draw_buttons()
        # when the game ends, the bg image would be changed. this just resets it
        self.canvas.itemconfig(self.canvas_bg, image=self.bg_image)


if __name__ == '__main__':
    ui = UserInterface()


# if the user chose to play against a friend, we have to keep changing the button image to x image and o image alternatively
# we also have to update the board with X and O alternatevely
# so we have to toggle between two values. easiest way to do is:
    # count = 0
    # for i in range(5):
    #     count = (count + 1) % 2
    #     print(count)
# this count will switch between 0 and 1. that's what we did above.
# self.ind is the count and players and player_images are a list with two values so we can access them with the index value
# if the user chose to play against a friend, we need to toggle. otherwise we need to stick to 'X'
# hence the default items in the players and player_list are same. we added an if statement to see if the user chose to play against a friend
# in that case, we change the 2nd value in both the list to that of 'O'.
# after the user presses a button, we do (ind+1) % 2 to change its value
