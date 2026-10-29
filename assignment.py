def turtle_drawing():
    import turtle
    import math

    screen = turtle.Screen()
    screen.title("My Little Turtle")
    screen.setup(800, 750)
    screen.bgcolor("#EAF7FF")

    pen = turtle.Turtle()
    pen.speed(8)
    pen.pensize(3)
    pen.hideturtle()

    def ellipse(x, y, width, height, colour, angle=0):
        rotation = math.radians(angle)
        points = []

        for i in range(61):
            t = 2 * math.pi * i / 60
            dx = width * math.cos(t)
            dy = height * math.sin(t)
            px = x + dx * math.cos(rotation) - dy * math.sin(rotation)
            py = y + dx * math.sin(rotation) + dy * math.cos(rotation)
            points.append((px, py))

        pen.penup()
        pen.goto(points[0])
        pen.pendown()
        pen.color("#285438", colour)
        pen.begin_fill()

        for point in points[1:]:
            pen.goto(point)

        pen.goto(points[0])
        pen.end_fill()

    def polygon(points, colour):
        pen.penup()
        pen.goto(points[0])
        pen.pendown()
        pen.color("#285438", colour)
        pen.begin_fill()

        for point in points[1:]:
            pen.goto(point)

        pen.goto(points[0])
        pen.end_fill()

    ellipse(-115, 65, 65, 32, "#8BCF75", -35)
    ellipse(115, 65, 65, 32, "#8BCF75", 35)
    ellipse(-105, -100, 58, 32, "#8BCF75", 35)
    ellipse(105, -100, 58, 32, "#8BCF75", -35)

    polygon([(-20, -140), (0, -205), (20, -140)], "#8BCF75")

    ellipse(0, 145, 35, 55, "#8BCF75")
    ellipse(0, 205, 60, 65, "#9DDD86")
    ellipse(0, -10, 140, 165, "#B4DB70")
    ellipse(0, -10, 122, 147, "#4D984F")

    centre = [
        (-45, 35),
        (0, 65),
        (45, 35),
        (45, -45),
        (0, -75),
        (-45, -45)
    ]

    polygon(centre, "#80BC59")

    outer = [
        (-100, 75),
        (0, 137),
        (100, 75),
        (100, -95),
        (0, -157),
        (-100, -95)
    ]

    pen.pencolor("#285438")
    pen.pensize(4)

    for start, end in zip(centre, outer):
        pen.penup()
        pen.goto(start)
        pen.pendown()
        pen.goto(end)

    ellipse(-23, 222, 14, 19, "white")
    ellipse(23, 222, 14, 19, "white")

    for x in [-23, 23]:
        pen.penup()
        pen.goto(x, 220)
        pen.dot(14, "#182A22")
        pen.goto(x - 3, 224)
        pen.dot(5, "white")

    for x in [-39, 39]:
        pen.penup()
        pen.goto(x, 199)
        pen.dot(15, "#F4AD9D")

    pen.penup()
    pen.goto(-18, 195)
    pen.setheading(-60)
    pen.pencolor("#285438")
    pen.pensize(3)
    pen.pendown()
    pen.circle(21, 120)

    pen.penup()
    pen.goto(0, -270)
    pen.write(
        "Hello! I am a little turtle.",
        align="center",
        font=("Arial", 18, "bold")
    )

    screen.exitonclick()


def qa_bot():
    import re

    print("\nWelcome to the QA Bot!")
    print("Ask about HKU, robot, jetson, ai, or human.")
    print("Type quit to exit.")

    while True:
        question = input("\nYou: ").strip().lower()
        words = re.findall(r"[a-z]+", question)

        if question in ("quit", "exit"):
            print("Bot: Goodbye!")
            break
        elif "hku" in words:
            print("Bot: HKU stands for the University of Hong Kong.")
        elif "robot" in words or "robots" in words:
            print("Bot: A robot is a machine that can perform tasks automatically.")
        elif "jetson" in words:
            print("Bot: NVIDIA Jetson is a computing platform for AI and robotics.")
        elif "ai" in words:
            print("Bot: AI means artificial intelligence. It helps computers recognise images and understand language.")
        elif "human" in words or "humans" in words:
            print("Bot: Humans are people who can learn, think, communicate, and create.")
        else:
            print("Bot: Please ask a question containing HKU, robot, jetson, ai, or human.")


def read_number(prompt):
    import math

    while True:
        try:
            number = float(input(prompt))
            if math.isfinite(number):
                return number
            print("Please enter a finite number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def simple_calculator():
    print("\nSimple Calculator")

    first = read_number("Enter the first number: ")
    second = read_number("Enter the second number: ")

    while True:
        operator = input("Choose an operator (+, -, *, /): ").strip()
        if operator in ("+", "-", "*", "/"):
            break
        print("Invalid operator. Please choose +, -, *, or /.")

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    else:
        if second == 0:
            print("Error: Cannot divide by zero.")
            return
        result = first / second

    print(f"Result: {first:g} {operator} {second:g} = {result:g}")


def main():
    print("Assignment 1 - Python Basics")
    print("1. Turtle Drawing")
    print("2. QA Bot")
    print("3. Simple Calculator")

    while True:
        choice = input("Choose a task (1, 2, or 3): ").strip()

        if choice == "1":
            turtle_drawing()
            break
        elif choice == "2":
            qa_bot()
            break
        elif choice == "3":
            simple_calculator()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()