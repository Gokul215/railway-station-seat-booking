class Ticket:
    id=1
    def __init__(self,fromstation,tostation,seats):
        self.pnr=Ticket.id
        Ticket.id+=1
        self.fromstation=fromstation
        self.tostation=tostation
        self.seats=seats
        self.alloted=False
        self.seatnumber=[]
        
    def __str__(self):
        return f"pnr: {self.pnr}, from: {self.fromstation}, to: {self.tostation}, seats: {self.seats}, seatnumber: {self.seatnumber}"
        