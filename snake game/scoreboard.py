from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = -1
        with open("high_score.txt", 'r') as data:
            self.high_score = int(data.read())
        self.color('black')
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(-190, 235)
        self.write(f"🍎 {self.score}", align='center', font=('courier', 30, 'normal'))
        self.goto(190, 235)
        self.write(f"🏆 {self.high_score}", align='center', font=('courier', 30, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        if self.score > self.high_score:
            with open("high_score.txt", 'w') as data:
                data.write(f"{self.score}")
            self.high_score = self.score
            text = "NEW HIGH SCORE!"
        else:
            text = "GAME OVER!"
        self.write(text, align='center', font=('courier', 30, 'normal'))

