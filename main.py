import random
import turtle
import city
import tkinter as tk
import itertools as it

cities = city.getCities()
found = []
wildCardCounter = 5  # the user will have 5 joker right.

image = "./images/unnamed.gif"
screen = turtle.Screen()
screen.setup(1250, 712)
screen.addshape(image)


input = ""

instructor = turtle.Turtle()

scoreTable = turtle.Turtle()

wildCard = turtle.Turtle()

score = 0
stack = 0

def drawWildCards():
    wildCard.reset()
    wildCard.hideturtle()
    wildCard.penup()
    wildCard.speed(0)
    wildCard.sety(280)
    wildCard.setx(480)
    wildCard.color("#FEDE00")
    icon = ""
    for i in range(wildCardCounter):
        icon += "💡"
    wildCard.write(icon, move=False, align="center", font=("calibri", 21, "bold"))

def getRandomCity():
    #collection: will store datas of (cities - found) transaction
    collection = [x for x, y in it.zip_longest(cities, found) if x != y]
    index = random.randint(0, len(collection))
    return collection[index]


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
    scoreTable.sety(290)
    scoreTable.write(str(score), font=("calibri", 40, "bold"),  align="center")
    scoreTable.goto(0, scoreTable.ycor() - 10)
    scoreTable.write(f"{len(found)}/{len(cities) - len(found)}",font=("calibri", 12, "normal"), align="center")

def addscore(current):
    if stack == 1:
        text_score = 10
    else:
        text_score = (stack * 5) + 10
    return current + text_score

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
        if local_lower_case(element["city"]) == value and element["id"] in found:
            return {"message": element["city"] + " is already found.", "statusCode": 409, "reason_city": element}
        if local_lower_case(element["city"]) == value:
            element["statusCode"] = 200
            return element
    return {"message": "Incorrect.", "statusCode": 404, "reason_city": None}


turtle.shape(image)
changeScore()


while len(found) < len(cities):
    drawWildCards()
    if wildCardCounter > 0:
        infoMessage = "Write a City Name\nType h to use joker"
    else:
        infoMessage = "Write a City Name"

    input = screen.textinput("User Input", infoMessage)

    if input is None:
        break

    result = isValid(cities, local_lower_case(input.strip()))

    #wildCard feature
    if input == "h":
        if(wildCardCounter == 0):
            tk.messagebox.showinfo(title="Bad request", message="Your jokers are over")
        else:
            jokerCity = getRandomCity()
            print(jokerCity)
            putText(jokerCity["city"], int(jokerCity["x"]), int(jokerCity["y"]), jokerCity["fontsize"])
            wildCardCounter -= 1
            found.append(jokerCity["id"])
            changeScore()
    #end of wildCard feauture
    elif result["statusCode"] == 200:
        stack = stack + 1
        putText(result["city"], int(result["x"]), int(result["y"]), result["fontsize"])
        found.append(result["id"])
        score = addscore(score)
        changeScore(score)
    elif result["statusCode"] == 409:
        result_city = result["reason_city"]
        draw_circle(result_city["x"], result_city["y"], len(result_city["city"]))
        tk.messagebox.showinfo(title=result["statusCode"], message=result["message"])
        hide_circle()
    elif result["statusCode"] == 404:
        tk.messagebox.showerror(title=result["statusCode"], message=result["message"])

if len(found) == len(cities):
    tk.messagebox.showinfo(title="Congrats", message="You found all the cities!")




