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

def isValid(list, value):
    for element in list:
        if element["city"].lower() == value and element["id"] in found:
            return {"message": element["city"] + " is already found.", "statusCode": 409, "reason_id": element["id"]}
        if element["city"].lower() == value:
            element["statusCode"] = 200
            return element
    return {"message": "Incorrect.", "statusCode": 404, "reason_id": None}

while input != "-1":
    turtle.shape(image)
    input = screen.textinput("User Input", "Write a City Name")

    result = isValid(cities, input.strip().lower())
    if result["statusCode"] == 200:
        putText(result["city"], int(result["x"]), int(result["y"]))
        found.append(result["id"])
    elif result["statusCode"] == 409:
        tk.messagebox.showinfo(title=result["statusCode"], message=result["message"])
    elif result["statusCode"] == 404:
        tk.messagebox.showerror(title=result["statusCode"], message=result["message"])
    print(f"Guessed correctly: {len(found)}. And remaning city number is {len(cities)-len(found)}")
