#Team Members: Matt Cardano
#Course: CS 151, Prof. Mehri
#Date: 9/27/21
#Programming Assignment: 1
#Programming Inputs: asks the user for the dimensions (length, width, and height) of a room in feet
#Programming Outputs: computes the total area of the four walls and ceiling and determines the amount of primer and paint in gallons necessary to cover them


length = int(input("enter length: "))
width = int(input("enter width: "))
height = int(input("enter height: "))
area = (length * width * height) * 5
primer = area / 200
paint = area / 350
print("area: ", area, "ft**2")
print("primer: ", primer, "gallons")
print("paint: ", paint, "gallons")
