import turtle
import city
import tkinter as tk

cities = city.getCities()
found = []

image = "./images/unnamed.gif"
screen = turtle.Screen()
screen.setup(1250, 712)
screen.addshape(image)

input = ""

def underline(position_x, position_y):
    box = turtle.Turtle()
    box.hideturtle()
    box.penup()
    box.setx(position_x-40)
    box.sety(position_y)
    box.pendown()
    box.forward(80)
    box.reset()
    box.hideturtle()

def putText(text, position_x, position_y, fontsize):
    box = turtle.Turtle()
    box.hideturtle()
    box.penup()
    box.speed(0)
    box.shape("turtle")
    box.setx(position_x)
    box.sety(position_y)
    box.write(text, move=False, align="center", font=("calibri", fontsize, "bold"))


def get_mouse_click_coor(x, y):
    print(x, y)


def isValid(list, value):
    for element in list:
        if element["city"].lower() == value and element["id"] in found:
            return {"message": element["city"] + " is already found.", "statusCode": 409, "reason_city": element}
        if element["city"].lower() == value:
            element["statusCode"] = 200
            return element
    return {"message": "Incorrect.", "statusCode": 404, "reason_city": None}


while True:
    turtle.shape(image)
    input = screen.textinput("User Input", "Write a City Name")
    if input is None:
        break
    result = isValid(cities, input.strip().lower())
    if result["statusCode"] == 200:
        putText(result["city"], int(result["x"]), int(result["y"]), result["fontsize"])
        found.append(result["id"])
    elif result["statusCode"] == 409:
        underline(result["reason_city"]["x"], result["reason_city"]["y"])
        tk.messagebox.showinfo(title=result["statusCode"], message=result["message"])
    elif result["statusCode"] == 404:
        tk.messagebox.showerror(title=result["statusCode"], message=result["message"])
    print(f"Guessed correctly: {len(found)}. And remaning city number is {len(cities) - len(found)}")
