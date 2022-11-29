"""
180209023 İlayda Bakırcıoğlu
190209019 Mehmet Ali Mergen
190209031 Burak Taşçı
"""

import random
import turtle
import city
import tkinter as tk
import itertools as it

cities = city.get_cities()
founds = set()
wildcard_counter = 5  # the user will have 5 joker right.

# importing image
image = "./images/unnamed.gif"

# creating game screen, and its settings.
screen = turtle.Screen()
screen.setup(1250, 712)
screen.addshape(image)

# creating instructor object to draw a circle for repeating answers.
instructor = turtle.Turtle()

# creating score table object to display score and other details related with score.
score_table = turtle.Turtle()

# creating wildcard object to display it.
wildcard = turtle.Turtle()

score = 0
stack = 0
adding_score = 10

# draws wildcards to the right of the screen
def draw_wildcards():
    wildcard.reset()
    wildcard.hideturtle()
    wildcard.penup()
    wildcard.speed(0)
    wildcard.sety(280)
    wildcard.setx(480)
    wildcard.color("#FEDE00")
    icon = ""
    for i in range(wildcard_counter):
        icon += "💡"
    wildcard.write(icon, move=False, align="center", font=("calibri", 21, "bold"))


# picks random city which is not found yet.
def get_random_city():
    #collection: will store data of (cities - founds) transaction
    collection = [x for x, y in it.zip_longest(cities, founds) if x != y]
    index = random.randint(0, len(collection))
    print(collection[index])
    return collection[index]


# draws circle to show duplicate city.
def draw_circle(position_x, position_y, letter_count, font_size):
    r = letter_count * 7 * (font_size / 10)
    instructor.hideturtle()
    instructor.width(3)
    instructor.penup()
    instructor.speed(0)
    instructor.setx(position_x - letter_count * 5 * (font_size / 10))
    instructor.sety(position_y)
    instructor.speed(0.5)
    instructor.pendown()
    instructor.seth(-45)
    for i in range(2):
        instructor.circle(r, 90)
        instructor.circle(r // 3, 90)


# hide the circle which draws for duplicate city.
def hide_circle():
    instructor.reset()
    instructor.hideturtle()


# shows score table with its details. (score, guessed city/total city, motivation, adding score)
def show_score_table(score=0):
    score_table.reset()
    score_table.hideturtle()
    score_table.penup()
    score_table.speed(0)
    score_table.sety(280)
    score_table.write(score, font=("calibri", 40, "bold"),  align="center")
    score_table.goto(score_table.xcor() + 20, score_table.ycor()+47)

    if len(founds) < len(cities):
        score_table.write(f"+{adding_score}", font=("calibri", 15, "bold"), align="left")
        score_table.goto(score_table.xcor() - 20, score_table.ycor() - 47)
        score_table.goto(0, score_table.ycor() - 10)
        score_table.write(f"{len(founds)}/{len(cities)}",font=("calibri", 12, "normal"), align="center")

        if stack > 1:
            score_table.goto(0, score_table.ycor() - 15)
            style = ("calibri", 8, "normal")
            if stack == 2:
                score_table.write(f"You are doing well. Keep going.", font=style, align="center")
            if stack == 3:
                score_table.write(f"Hey! Slow down!", font=style, align="center")
            if stack == 4:
                score_table.write(f"Amazing!", font=style, align="center")
            if stack == 5:
                score_table.write(f"You are on fire!!!", font=style, align="center")


# calculates the adding score according to stack.
def adding_score_calc():
    if stack > 1:
        return ((stack-1) * 5) + 10
    else:
        return 10


# puts the city name to the map according to its coordinate
def put_text(text, position_x, position_y, font_size):
    box = turtle.Turtle()
    box.hideturtle()
    box.penup()
    box.speed(0)
    box.shape("turtle")
    box.setx(position_x)
    box.sety(position_y)
    box.write(text, move=False, align="center", font=("calibri", font_size, "bold"))


# it used to get coordinate for the cities to create a dataset.
def get_mouse_click_coor(x, y):
    print(x, y)


# We are not sure the user has turkish keyboard, so we are converting the input as a global version.
def local_lower_case(text):
    text = text.replace(" ", "")
    text = text.replace("İ", "i")
    text = text.replace("I", "i")
    text = text.replace("ı", "i")
    text = text.lower()

    text = text.replace("ş", "s")
    text = text.replace("ö", "o")
    text = text.replace("ç", "c")
    text = text.replace("ğ", "g")
    text = text.replace("ü", "u")

    return text


# it checks the value is valid or not. If it is valid return the city with 200 status code. If it is not,
# return the error status code with the other details.
def is_valid(list, value):
    for element in list:
        if value in element["alias"] and element["id"] in founds:
            return {"message": element["city"] + " is already founds.", "statusCode": 409, "reason_city": element}
        if value in element["alias"]:
            element["statusCode"] = 200
            return element
    return {"message": "Incorrect.", "statusCode": 404, "reason_city": None}


turtle.shape(image)
show_score_table()

# the screen will display until the cities are over.
while len(founds) < len(cities):
    draw_wildcards()
    if wildcard_counter > 0:
        infoMessage = "Write a City Name\nType h to use joker"
    else:
        infoMessage = "Write a City Name"

    input = screen.textinput("User Input", infoMessage)

    if input is None:
        break

    result = is_valid(cities, local_lower_case(input.strip()))

    if input.strip() == "h":
        if wildcard_counter == 0:
            tk.messagebox.showinfo(title="Bad request", message="Your jokers are over")
        else:
            jokerCity = get_random_city()
            put_text(jokerCity["city"], int(jokerCity["x"]), int(jokerCity["y"]), jokerCity["font_size"])
            wildcard_counter -= 1
            founds.add(jokerCity["id"])
            score = score + adding_score
    elif result["statusCode"] == 200:
        if stack < 5:
            stack = stack + 1
        put_text(result["city"], int(result["x"]), int(result["y"]), result["font_size"])
        founds.add(result["id"])
        score = score + adding_score

    elif result["statusCode"] == 409:
        stack = 0
        result_city = result["reason_city"]
        draw_circle(result_city["x"], result_city["y"], len(result_city["city"]), result_city["font_size"])
        tk.messagebox.showinfo(title=result["statusCode"], message=result["message"])
        hide_circle()
    elif result["statusCode"] == 404:
        stack = 0
        tk.messagebox.showerror(title=result["statusCode"], message=result["message"])

    adding_score = adding_score_calc()
    show_score_table(score)

if len(founds) == len(cities):
    tk.messagebox.showinfo(title="Congrats", message=f"You found all the cities! Your score is {score}")




