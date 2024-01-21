from turtle import Turtle
import random

FOODS = ['🍏', '🌼', '🍐', '🍊', '🍋', '🍌', '🍉', 
         '🍇', '🍓', '🍈', '🍒', '🍑', '🍍', '🥝', 
         '🥥', '🍅', '🍆', '🥑', '🍞', '🥐', '🥕', 
         '🌽', '🌶', '🥒', '🍔', '🍟', '🍕', '🥪', 
         '🍭', '🍫', '🍿', '🍩', '🥜', '🌻', '🍄']

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.refresh()

        
    def refresh(self):
        self.clear()
        self.goto((random.randint(-180, 180), random.randint(-180, 180)))
        self.write(random.choice(FOODS), align='center',font=("Courier", 20, "normal"))

# class Food(Turtle):
#     def __init__(self) -> None:
#         super().__init__()
#         self.shape('circle')
#         self.penup()
#         self.shapesize(0.7, 0.7)
#         self.color('white')
#         self.fillcolor('#c81663')
#         self.speed(0)
#         self.refresh()

        
#     def refresh(self):
#         self.goto((random.randint(-190, 190), random.randint(-190, 190)))
