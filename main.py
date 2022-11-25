import turtle
import city

numberOfCities = 81
count = 0
cities = city.getCities()
found = []

image = "./images/unnamed.gif"

screen = turtle.Screen()
screen.setup(1250, 712)
screen.addshape(image)

input = ""

def putText(text, position_X, positiyon_Y):
    box = turtle.Turtle()
    box.penup()
    box.speed(0)
    box.shape("turtle")
    box.hideturtle()
    box.setx(position_X)
    box.sety(positiyon_Y)
    box.write(text, move=False, align="center")

def get_mouse_click_coor(x, y):
    print(x, y)

def isValid(list, key, value):
    for element in list:
        print(element[key] == value)
        if element[key] == value:
            return element
    return {}



while input != "-1":
    turtle.shape(image)
    input = screen.textinput("User Input", "Write a City Name")

    # turtle.onscreenclick(get_mouse_click_coor)
    result = isValid(cities,"city", input.strip())
    if result != {}:
        putText(result["city"], int(result["x"]), int(result["y"]))
        count += 1
        print(f"Guessed correctly: {count}. And remaning city number is {numberOfCities-count}")
