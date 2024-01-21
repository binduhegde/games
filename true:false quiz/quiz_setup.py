from tkinter import *
from tkmacosx import Button # lets us change the bg color of button

THEME_COLOR = "#375362"
FONT = ('apple braille', 30)

class Setup:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('PythonGuides')
        self.window.config(bg=THEME_COLOR, padx=20, pady=40)

        self.label = Label(text="Please select the following", font=(FONT[0],FONT[1], 'bold'), bg=THEME_COLOR, fg = 'white')
        self.label.grid(row=0, column=0, pady=30, padx=10, columnspan=2)

        self.submit_button = Button(text='Submit', command=self.submit_clicked, font=FONT, highlightthickness=0, bg="#192d38", fg='white')
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=30)
        
        self.display_category()
        self.display_difficulty()
        self.display_no_questions()

        self.result = {}
        self.window.mainloop()

    def display_difficulty(self):
        self.difficulty_label = Label(text="Difficulty", font=FONT, bg=THEME_COLOR, fg='white')
        self.difficulty_label.grid(row=1, column=0, pady=10)

        difficulty_options = ['Easy', 'Medium', 'Hard']
        # setting variable for Integers
        self.difficulty_variable = StringVar()
        self.difficulty_variable.set(difficulty_options[2])

        # creating widget
        self.difficulty_dropdown = OptionMenu(
            self.window,
            self.difficulty_variable,
            *difficulty_options,
        )
        self.difficulty_dropdown.config(highlightthickness=0, borderwidth="0", bg=THEME_COLOR, width=10)
        # positioning widget
        self.difficulty_dropdown.grid(row=1, column=1)


    def display_category(self):
        self.category_label = Label(text="Category", font=FONT, bg=THEME_COLOR, fg='white')
        self.category_label.grid(row=2, column=0, pady=10)

        self.category_options = ['General Knowledge', 'Books', 'Films', 'Music', 'Computer Science', 'Mathametics', 'Sports', 'History', 'Politics', 'Animals', 'celebrities']
        # setting variable for Integers
        self.category_variable = StringVar()
        self.category_variable.set(self.category_options[2])

        # creating widget
        self.category_dropdown = OptionMenu(
            self.window,
            self.category_variable,
            *self.category_options,
        )
        self.category_dropdown.config(highlightthickness=0, borderwidth="0", bg=THEME_COLOR, width=10)
        # positioning widget
        self.category_dropdown.grid(row=2, column=1)


    def display_no_questions(self):
        self.number_label = Label(text="No of Questions", font=FONT, bg=THEME_COLOR, fg='white')
        self.number_label.grid(row=3, column=0, pady=10)

        number_options = ['10', '15', '20', '25', '30']
        # setting variable for Integers
        self.number_variable = StringVar()
        self.number_variable.set(number_options[2])

        # creating widget
        self.number_dropdown = OptionMenu(
            self.window,
            self.number_variable,
            *number_options,
        )
        self.number_dropdown.config(highlightthickness=0, borderwidth="0", bg=THEME_COLOR, width=10)
        # positioning widget
        self.number_dropdown.grid(row=3, column=1)


    def submit_clicked(self):
        difficulty = self.difficulty_variable.get()
        category = self.category_variable.get()
        number_questions = self.number_variable.get()
        self.result = {'difficulty': difficulty, 'category':category, 'amount':int(number_questions)}
        self.window.destroy()


if __name__ == '__main__':
    setup = Setup()
    print(setup.result)