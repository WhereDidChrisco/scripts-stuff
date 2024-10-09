import math

results = list()
while input("Press Enter to continue, or to quit, type 'quit' and press enter: ") != "quit":   
    maths = input("Would you like to find the area of a circle, rectangle, or triangle?: ")
    if maths.lower() == "circle":
        radius = input("Enter the radius of the circle: ")
        areaOfCircle = (math.pi) * float(radius) ** 2
        print("Area of circle =", areaOfCircle)
        results.append(areaOfCircle)
        continue       
    elif maths.lower() == "rectangle":
        baseRect = input("Enter the base length: ")
        heightRect = input("Enter the height length: ")
        areaOfRect = float(baseRect) * float(heightRect)
        print("Area of rectangle is", areaOfRect)
        results.append(areaOfRect)
        continue      
    elif maths.lower() == "triangle":
        baseTri = input("Enter the base length: ")
        heightTri = input("Enter the height length: ")
        areaOfTri = (float(baseTri) * float(heightTri)) / 2
        print("Area of Triangle is", areaOfTri)
        results.append(areaOfTri)
        continue

        


# Area of a circle

    # radius = input("Enter the radius of the circle: ")