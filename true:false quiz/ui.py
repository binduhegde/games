from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(padx=20, pady=20)
        self.window.config(bg=THEME_COLOR)
        self.window.title('Quizzler')

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('ariel', 20, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.question_no_label = Label(text="Question", bg=THEME_COLOR, fg='white', font=('ariel', 20, 'italic'))
        self.question_no_label.grid(row=0, column=0)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=40)
        self.question_text = self.canvas.create_text(150, 125, text='This is a sample question', font=('futura', 20, 'italic'), fill=THEME_COLOR, width=250)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.question_no_label.config(text=f"Question {self.quiz.question_number+1}/{len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of questions!")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def flash_light(self, correct):
        if correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, self.get_next_question)
        
    def true_pressed(self):
        ans = self.quiz.check_answer('true')
        self.flash_light(ans)

    def false_pressed(self):
        ans = self.quiz.check_answer('false')
        self.flash_light(ans)
