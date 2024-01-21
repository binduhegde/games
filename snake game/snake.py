from turtle import Turtle
from play_sound import PlaySound
import colorsys as cs

play_sound = PlaySound()
move_dist = 20

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.hue = 0.55
        self.create_snake()
        self.head = self.segments[0]
        #self.head.color('black')
        self.head.shapesize(1.1, 1.1)

    def create_snake(self):
        position = (0, 0)
        for _ in range(3): # 2 segments to start with
            self.new_segment(position)
            position = (position[0]-20, position[1])

    def new_segment(self, position):
        new_turtle = Turtle('square')
        new_turtle.color(cs.hsv_to_rgb(self.hue, 0.5, 0.7))
        new_turtle.pensize(5)
        #new_turtle.fillcolor(cs.hsv_to_rgb(self.hue, 1, 1))#18424f')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)
        self.hue += 0.01


    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()    
            new_y = self.segments[i-1].ycor()    
            self.segments[i].goto(new_x, new_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)
            play_sound.move_noise()
    
    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)
            play_sound.move_noise()
    
    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)
            play_sound.move_noise()
    
    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)
            play_sound.move_noise()

    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0] 