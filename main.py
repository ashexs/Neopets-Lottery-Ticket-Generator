import random

def generate_ticket_numbers():
    ticket_numbers = []
    for j in range(6):
        ticket_numbers.append(random.randint(1, 30))
    return ticket_numbers

def main():
    for i in range(20):
        ticket_numbers = generate_ticket_numbers()
        print(f"Ticket {i+1}: {ticket_numbers}")
