from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'italic')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
          self.high_score = int(file.read())  
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0.00, 280.00)
        self.update_scoreboard()

    def increase_score(self):
      self.score += 1
      self.clear()
      self.update_scoreboard()
      
    
    def update_scoreboard(self):
      self.clear()
      self.write(f"Score: {self.score}   High Score: {self.high_score}",False,align="center",font=('Arial', 16, 'italic'))
      
    def reset(self):
      if self.score > self.high_score:
        self.high_score = self.score
        with open("data.txt","w") as file:
          file.write(str(self.high_score))
      self.score = 0  
      self.update_scoreboard()