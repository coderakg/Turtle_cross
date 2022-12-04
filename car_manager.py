from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple","pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) :
        self.all_cars = [] # a list that contains all the cars 
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self): # a function that will create cars
        # to reduce the numbers of cars formed we will do this:
        random_chance = random.randint(1,6)
        if random_chance == 1 : # now this will decrease the number of cars created
            new_car = Turtle("square") # the new car will be an object of the Turtle class 
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup() # to avoid the turtle drawing 
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-220,220)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car) # the new car object will be appended to the all cars list

    def move_cars(self):
        # to make the cars move accross the screen
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
        
        
