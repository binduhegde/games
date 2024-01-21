from tkinter import *
from tkmacosx import Button # lets us change the bg color of button

THEME_COLOR = "#375362"
FONT = ('apple braille', 30)

class Setup:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('Setup')

        bg_image = PhotoImage(file='images/blank_image_resized.png')
        self.canvas = Canvas(width=1200, height=700)
        self.canvas.create_image(600, 350, image= bg_image)
        self.canvas.grid(row=0, column=0, rowspan=5, columnspan=2)
        
        self.canvas.create_text(600, 150, text="Please select the following", font=(FONT[0],40, 'bold'), fill = 'white')

        self.submit_button = Button(text='Submit', command=self.submit_clicked, font=FONT, highlightthickness=0, bg="#002d47", fg='white')
        self.submit_button.place(x=600, y=550)
        
        self.display_category()
        self.display_difficulty()
        self.display_no_questions()

        self.result = {}
        self.window.mainloop()

    def display_difficulty(self):
        self.difficulty_text = self.canvas.create_text(500, 250, text="Difficulty", font=FONT, fill='white')

        difficulty_options = ['Easy', 'Medium', 'Hard']
        # setting variable for Integers
        self.difficulty_variable = StringVar()
        self.difficulty_variable.set(difficulty_options[0])

        # creating widget
        self.difficulty_dropdown = OptionMenu(
            self.window,
            self.difficulty_variable,
            *difficulty_options,
        )
        self.difficulty_dropdown.config(highlightthickness=0, borderwidth="0", bg=THEME_COLOR, width=15)
        # positioning widget
        self.difficulty_dropdown.place(x=700, y=240)


    def display_category(self):
        self.category_text = self.canvas.create_text(500, 350, text="Category", font=FONT, fill='white')

        self.category_options = ['General Knowledge', 'Books', 'Films', 'Music', 'Computer Science', 'Mathametics', 'Sports', 'History', 'Politics', 'Animals', 'celebrities']
        # setting variable for Integers
        self.category_variable = StringVar()
        self.category_variable.set(self.category_options[9])

        # creating widget
        self.category_dropdown = OptionMenu(
            self.window,
            self.category_variable,
            *self.category_options,
        )
        self.category_dropdown.config(highlightthickness=0, borderwidth="0", bg=THEME_COLOR, width=15)
        # positioning widget
        self.category_dropdown.place(x=700, y=340)


    def display_no_questions(self):
        self.number_text = self.canvas.create_text(500, 450, text="No of Questions", font=FONT, fill='white')

        number_options = ['10', '15', '20', '25', '30']
        # setting variable for Integers
        self.number_variable = StringVar()
        self.number_variable.set(number_options[0])

        # creating widget
        self.number_dropdown = OptionMenu(
            self.window,
            self.number_variable,
            *number_options,
        )
        self.number_dropdown.config(highlightthickness=0, borderwidth="0", bg=THEME_COLOR, width=15)
        # positioning widget
        self.number_dropdown.place(x=700, y=440)


    def submit_clicked(self):
        difficulty = self.difficulty_variable.get()
        category = self.category_variable.get()
        number_questions = self.number_variable.get()
        self.result = {'difficulty': difficulty, 'category':category, 'amount':int(number_questions)}
        self.window.destroy()


if __name__ == '__main__':
    setup = Setup()
    print(setup.result)