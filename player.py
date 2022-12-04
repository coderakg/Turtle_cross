from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#creating the ability to move the turtle in forward directions
class Player(Turtle):
    
    def __init__(self): 
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90) # to initialise the direction of the turtle we will use the setheading function


    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
            print("Finished")
        else:
            return False
            
    
