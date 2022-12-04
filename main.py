import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player() # this is the turtle
car_manager = CarManager() # these are the cars
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"Up")

game_is_on = True
#defining a variable game_is_on and default setting it to true, using while loop to make an infinite loop to update it again and again
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #Detecting the collision of turtle with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20: 
            game_is_on = False 
            scoreboard.game_over()
            print("Game over")
            
    #detect if the player has crossed the finish line 
    if player.is_finish() :
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
