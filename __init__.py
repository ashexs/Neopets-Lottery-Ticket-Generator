import random

# generate 20 lottery tickets
for i in range(20):
    # generate 6 random numbers between 1 and 30
    ticket_numbers = []
    for j in range(6):
        ticket_numbers.append(random.randint(1, 30))

    # print the ticket numbers
    print(f"Ticket {i+1}: {ticket_numbers}")
