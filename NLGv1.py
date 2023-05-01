import random
import tkinter as tk

class LotteryTicketGenerator:

    def __init__(self, master):
        self.master = master
        master.title("Lottery Ticket Generator")

        # create a button that generates lottery tickets
        self.generate_button = tk.Button(master, text="Generate", command=self.generate_tickets)
        self.generate_button.pack()

        # create a text widget to display the generated tickets
        self.ticket_display = tk.Text(master, height=20, width=50)
        self.ticket_display.pack()

    def generate_tickets(self):
        self.ticket_display.delete("1.0", tk.END)
        for i in range(20):
            ticket_numbers = []
            while len(ticket_numbers) < 6:
                number = random.randint(1, 30)
                if number not in ticket_numbers:
                    ticket_numbers.append(number)
            self.ticket_display.insert(tk.END, f"Ticket {i+1}: {ticket_numbers}\n")

root = tk.Tk()
app = LotteryTicketGenerator(root)
root.mainloop()
