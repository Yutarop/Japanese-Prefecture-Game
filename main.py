import turtle
import pandas as pd

# show the image
screen = turtle.Screen()
screen.setup(width=800, height=871)
screen.title("Japan Prefecture Game")
image = "japan.gif"
screen.addshape(image)
turtle.shape(image)

correct_guesses = []
score_track = 0

# read the csv file and store it in a dataframe
df = pd.read_csv('prefectures.csv')
prefectures = df['prefectures'].to_list()
prefectures_answer = df['prefectures'].to_list()

def write_prefecture(x, y, answered_prefectures, pen_color):
    prefecture_name = turtle.Turtle()
    prefecture_name.speed("fastest")
    prefecture_name.color(pen_color)
    prefecture_name.penup()
    prefecture_name.hideturtle()
    prefecture_name.goto(x, y)
    prefecture_name.write(answered_prefectures, True, align="center")


while len(correct_guesses) < 47:
    answer_prefectures = screen.textinput(title=f'Guess {score_track}/50',
                                    prompt='What\'s another prefecture? \n (Answers: Type "Give up")').lower()
    if answer_prefectures == "give up":
        screen.tracer(0)
        for prefecture in prefectures_answer:
            coordinate_x = df.loc[prefectures.index(prefecture), "x"]
            coordinate_y = df.loc[prefectures.index(prefecture), "y"]
            write_prefecture(coordinate_x, coordinate_y, prefecture, "red")
        screen.update()
        break
    if answer_prefectures in prefectures and answer_prefectures not in correct_guesses:
        correct_guesses.append(answer_prefectures)
        score_track += 1
        coordinate_x = df.loc[prefectures.index(answer_prefectures), "x"]
        coordinate_y = df.loc[prefectures.index(answer_prefectures), "y"]
        write_prefecture(coordinate_x, coordinate_y, answer_prefectures, "black")
        prefectures_answer.remove(answer_prefectures)

screen.exitonclick()