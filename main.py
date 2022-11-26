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

instructor = turtle.Turtle()

scoreTable = turtle.Turtle()



def draw_circle(position_x, position_y, letter_count):
    r = letter_count * 7
    instructor.hideturtle()
    instructor.width(3)
    instructor.penup()
    instructor.speed(0)
    instructor.setx(position_x - letter_count*5)
    instructor.sety(position_y)
    instructor.speed(0.5)
    instructor.pendown()
    instructor.seth(-45)
    for i in range(2):
        instructor.circle(r, 90)
        instructor.circle(r // 3, 90)

def hide_circle():
    instructor.reset()
    instructor.hideturtle()

def changeScore(score=0):
    scoreTable.reset()
    scoreTable.hideturtle()
    scoreTable.penup()
    scoreTable.speed(0)
    scoreTable.sety(330)
    scoreTable.write(f"Guessed correctly: {len(found)}. And remaning city number is {len(cities) - len(found)}", align="center")
    scoreTable.write(f"Guessed correctly: {len(found)}. And remaning city number is {len(cities) - len(found)}", align = "center")


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

def local_lower_case(text):
    # Iğdır => iğdır
    text = text.replace(" ", "")
    text = text.replace("İ","i")
    text = text.replace("I","i")
    text = text.replace("ı","i")
    text = text.lower()

    text = text.replace("ş", "s")
    text = text.replace("ö", "o")
    text = text.replace("ç", "c")
    text = text.replace("ğ", "g")
    text = text.replace("ü", "u")

    return text

def isValid(list, value):
    for element in list:
        if value in element["alias"] and element["id"] in found:
            return {"message": element["city"] + " is already found.", "statusCode": 409, "reason_city": element}
        if value in element["alias"]:
            element["statusCode"] = 200
            return element
    return {"message": "Incorrect.", "statusCode": 404, "reason_city": None}

turtle.shape(image)
changeScore()

while len(found) < len(cities):
    input = screen.textinput("User Input", "Write a City Name")
    if input is None:
        break
    result = isValid(cities, local_lower_case(input.strip()))
    if result["statusCode"] == 200:
        putText(result["city"], int(result["x"]), int(result["y"]), result["fontsize"])
        found.append(result["id"])
        changeScore()
    elif result["statusCode"] == 409:
        result_city = result["reason_city"]
        draw_circle(result_city["x"], result_city["y"], len(result_city["city"]))
        tk.messagebox.showinfo(title=result["statusCode"], message=result["message"])
        hide_circle()
    elif result["statusCode"] == 404:
        tk.messagebox.showerror(title=result["statusCode"], message=result["message"])
if len(found) == len(cities):
    tk.messagebox.showinfo(title="Congrats", message="You found all the cities!")
