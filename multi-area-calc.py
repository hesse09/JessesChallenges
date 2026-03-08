# Jesse France
# 3/7/26
# Calculates the area of various shapes

# IMPORTS
import math

# VARS
shapeChoice: str = ""


# HELPERS
def circleArea(radius: float) -> float:
    if radius < 0:
        return 0
    return math.pi * (radius**2)


def squareArea(side: float) -> float:
    if side < 0:
        return 0
    return side**2


def rectangleArea(length: float, width: float) -> float:
    if length < 0 or width < 0:
        return 0
    return length * width


def triangleArea(base: float, height: float) -> float:
    if base < 0 or height < 0:
        return 0
    return (base * height) / 2


# MAIN LOOP
print("Welcome to Area Calculator!\n Enter 'q' to quit\n\n")

while shapeChoice != "q":
    print(
        "MENU: \n 1. Circle \n 2. Square \n 3. Rectangle \n 4. Triangle \n -0- means invalid entry"
    )
    shapeChoice = str(
        input("Please enter the shape you would like to calculate the area of: ")
    )
    if shapeChoice == "Circle":
        inputRadius = float(input("Please enter the radius of the circle: "))
        success = circleArea(inputRadius)
        print("The area of your circle is %.2f\n\n" % success)
    elif shapeChoice == "Square":
        inputSide = float(input("Please enter the side of the square: "))
        success = squareArea(inputSide)
        print("The area of your square is %.2f\n\n" % success)
    elif shapeChoice == "Rectangle":
        inputLength = float(input("Please enter the length of the rectangle: "))
        inputWidth = float(input("Please enter the width of the rectangle: "))
        success = rectangleArea(inputLength, inputWidth)
        print("The area of your rectangle is %.2f\n\n" % success)

    elif shapeChoice == "Triangle":
        inputBase = float(input("Please enter the base of the triangle: "))
        inputHeight = float(input("Please enter the height of the triangle: "))
        success = triangleArea(inputBase, inputHeight)
        print("The area of your triangle is %.2f\n\n" % success)
    else:
        if shapeChoice == "q":
            print("See you next time!")
        else:
            print("Please enter a valid shape.\n\n")
            continue
