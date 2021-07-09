#A simple busbooking system

class Bus:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("**************************************************")
        print(f"The name of the Bus is {self.name}")
        print(f"The seats available in the Bus are {self.seats}")
        print("**************************************************")

    def ticketInfo(self):
        print(f"The price of the ticket is: Rs {self.ticketInfo}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this Bus is full! Kindly try another one")

    def cancelTicket(self, seatNo):
        pass

udupi = Bus("Kundapur Express: 1000", 50, 2)

udupi.getStatus() 
udupi.bookTicket()
udupi.bookTicket()
udupi.bookTicket()
udupi.getStatus()
