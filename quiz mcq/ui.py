from tkinter import *
from quiz_brain import QuizBrain
from play_sound import happy_sound, sad_sound

FONT = ('apple symbols', 55)

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.canvas = Canvas(width=1200, height=700)
        bg_image = PhotoImage(file="images/bg2_resized.png")
        self.canvas.create_image(600, 350, image= bg_image)
        self.question_text = self.canvas.create_text(900, 250, font=FONT, width=500)
        self.canvas.grid(row=0, column=0)

        self.score_text = self.canvas.create_text(1100, 50, text="Score: 0", font=(FONT[0], 30))
        self.question_no_text = self.canvas.create_text(570, 240, font=(FONT[0], 70), fill='white', text='0')


        self.options_image = PhotoImage(file="images/blank_resized.png")
        self.red_image = PhotoImage(file='images/red_resized.png')
        self.green_image = PhotoImage(file='images/green_resized.png')
        
        self.optionA = Button(image=self.options_image, text="Option", highlightthickness=0, compound="center", font=(FONT[0], 35), command=self.optionA_pressed)
        self.optionB = Button(image=self.options_image, text="Option", highlightthickness=0, compound="center", font=(FONT[0], 35), command=self.optionB_pressed)
        self.optionC = Button(image=self.options_image, text="Option", highlightthickness=0, compound="center", font=(FONT[0], 35), command=self.optionC_pressed)
        self.optionD = Button(image=self.options_image, text="Option", highlightthickness=0, compound="center", font=(FONT[0], 35), command=self.optionD_pressed)

        self.optionA.place(x=100, y=180)
        self.optionB.place(x=100, y=280)
        self.optionC.place(x=100, y=380)
        self.optionD.place(x=100, y=480)

        self.option_buttons = [self.optionA, self.optionB, self.optionC, self.optionD]
        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_no_text, text=self.quiz.question_number+1)
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question['question'])
            for i, option in enumerate(question['options']):
                self.option_buttons[i].config(text=option, image=self.options_image)

        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of questions!")
            for button in self.option_buttons:
                button.config(state=DISABLED)
    
    def flash_light(self, chosen_button):
        self.quiz.check_answer(chosen_button.cget('text'))
        correct_text = self.quiz.current_question.answer
        for button in self.option_buttons:
            if button.cget("text") == correct_text:
                correct_button = button
        correct_button.config(image=self.green_image)
        if correct_button != chosen_button:
            sad_sound()
            chosen_button.config(image=self.red_image)
        else:
            happy_sound()
        self.window.after(1000, self.get_next_question)


    def optionA_pressed(self):
        self.flash_light(self.optionA)

    def optionB_pressed(self):
        self.flash_light(self.optionB)

    def optionC_pressed(self):
        self.flash_light(self.optionC)

    def optionD_pressed(self):
        self.flash_light(self.optionD)
