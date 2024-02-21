#functions go here


#checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry but this cannot be blank. Please retry")

        else:
            return response

#main routine goes here
while True:
    name = not_blank("Enter your name (or xxx to quit) ")
    if name == "xxx":
        break

    if name == " xxx":
        break

print("we are done")