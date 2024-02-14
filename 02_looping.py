# main routine starts here

#set maximum number of tickets below
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit").lower()

    if name == 'xxx':
        break

    if name == ' xxx': #because I like to put in spaces when testing
        break

    tickets_sold += 1


# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("congratulations you have sold all the tickets")

else:
    print(f"you have purchased {tickets_sold}. There are {MAX_TICKETS - tickets_sold} ticket/s remaining")