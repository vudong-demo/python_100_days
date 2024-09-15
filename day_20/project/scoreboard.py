from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(0, 270)
    self.update_scoreboard()

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)

  def game_over(self):
    self.goto(0, 0)
    self.write("Game Over", align=ALIGMENT, font=FONT)
