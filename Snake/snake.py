from turtle import Turtle

STARTING_POSITIONS = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_body()
        self.head = self.snakes[0]

    def create_body(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setpos(position)
        self.snakes.append(snake)
        
    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_body()
        self.head = self.snakes[0]    

    def extend(self):
        self.add_body(self.snakes[-1].position())

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
