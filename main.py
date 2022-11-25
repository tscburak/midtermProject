import turtle
import images

found = []

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



cities = [{"id":22,"city":"Edirne", "x": -515.0, "y": 197.0 ,"rotate": 0, "fontsize":12 },
{"id":39,"city":"Kırklareli", "x": -459.0, "y": 238.0 ,"rotate": 0, "fontsize":12 },
{"id":59,"city":"Tekirdağ", "x": -468.0, "y": 187.0 ,"rotate": 0 ,"fontsize":12 },
{"id":34,"city":"İstanbul", "x": -402.0, "y": 191.0 ,"rotate": 0, "fontsize":12 },
{"id":41,"city":"Kocaeli", "x": -319.0 , "y":159.0 ,"rotate": 0, "fontsize":12 },
{"id":77,"city":"Yalova", "x":-371.0, "y":145.0 ,"rotate": 0, "fontsize":12 }]

image = "./images/unnamed.gif"
screen = turtle.Screen()
screen.setup(1250,712)
screen.addshape(image)
input = ""

while input != "-1":
    turtle.shape(image)
    input = screen.textinput("User Input", "Write a City Name")

    # turtle.onscreenclick(get_mouse_click_coor)
    result = isValid(cities,"city", input.strip())
    if result != {}:
        putText(result["city"], int(result["x"]), int(result["y"]))
