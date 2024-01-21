import turtle as t 
import tkinter as tk
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from play_sound import PlaySound

screen = t.Screen()
screen.setup(600,650)
screen.title("snake game")
screen.bgcolor('black')
screen.bgpic('logo.png')

size = 420

def countdown():
    beep_noise = PlaySound()
    # to cleat the logo image
    screen.clear()
    screen.bgpic("bg5.png")
    n = t.Turtle()
    n.penup()
    n.hideturtle()
    # seemed like this cordinate looks centered
    n.goto(0, -100)
    for i in range(3, 0, -1):
        n.write(i, align='center',font=("Courier", 150, 'normal'))
        beep_noise.beep_noise()
        # 1 sec gap btw each beep
        time.sleep(1)
        # clearing it to not overlap the numbers
        n.clear()
    n.clear()

# border
def draw_border():
    # draws a square with a given size after going to the 
    # x and y cordinates of the top left corner of the square
    def square(size, x_cor, y_cor):
        tutu.penup()
        tutu.goto(x_cor, y_cor)
        tutu.pendown()
        for _ in range(4):
            tutu.forward(size)
            tutu.right(90)

    half_size = size//2
    tutu = t.Turtle()
    tutu.color('black')
    tutu.pensize(4)
    tutu.hideturtle()
    # inner square
    square(size, -1*half_size, half_size)
    # outer square
    square(size+20, -1*(half_size+10), half_size+10)


def play_game():
    screen.clear()
    # set background to this gradient
    screen.bgpic("bg5.png")
    # does't show any animation
    screen.tracer(0)
    draw_border()
    # creating objects from classes
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    play_sound = PlaySound()

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left') 
    screen.onkey(snake.right, 'Right')


    # wall is the x y point such that when the snake touches it, the game is over
    wall = (size//2)
    is_on = True # game is on
    # runs till is_on is set to False when the gave is over
    while is_on:
        # updates the screen when called. calling this because we set tracer to 0.
        # whenever we say update, the current happenings are loaded
        screen.update()
        # decides the speed of the game
        time.sleep(0.1)
        snake.move()

        # detect collision with food 
        if snake.head.distance(food) < 15:
            food.refresh() 
            scoreboard.update_score()
            snake.new_segment(snake.segments[-1].position())
            play_sound.eat_noise()

        # detetct collision with wall
        if (
            snake.head.xcor() > wall 
            or snake.head.xcor() < -wall 
            or snake.head.ycor() > wall 
            or snake.head.ycor() < -wall
        ):
            scoreboard.game_over()
            play_sound.game_over()
            is_on = False            

        # detect collision with its tail
        # starting from the 2nd segment cuz the we're comparing every seg to the first one which is the head
        for segment in snake.segments[1:]:
            if segment.distance(snake.head) < 10:
                is_on = False
                scoreboard.game_over()
                play_sound.game_over()

def button_clicked():
    countdown()
    play_game()

play_button = tk.Button(text="PLAY", font=("Courier", 25), width=15, height=2, command=button_clicked, bd=8).pack()
# TODO: get this button to pause the game
# button2 = tk.Button(text="PAUSE", font=("Courier", 25), width=15, height=2).pack(side='right')

screen.exitonclick()
