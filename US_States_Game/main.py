import turtle
import pandas

FONT = ("Courier", 24, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x_coors = data.x.to_list()
y_coors = data.y.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in states if state not in guessed_states]
        learn = pandas.DataFrame(states_to_learn)
        learn.to_csv("states_to_learn.csv")
        break

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.write(arg="Congrats! You Guessed All 50 States Correctly", align="center", font=FONT)
screen.exitonclick()
