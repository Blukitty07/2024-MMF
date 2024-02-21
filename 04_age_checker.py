#functions go here

#cjecks users enters a number to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an age in number form")

# Main routinue goes here
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit")

    if name == "xxx":
        break

    if name == " xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("sprry you are too young to attend this movie")
        continue
    else:
        print("?????? That looks like a typo, please retry")
        continue

    tickets_sold += 1