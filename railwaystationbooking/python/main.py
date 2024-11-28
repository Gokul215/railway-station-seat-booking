from Ticketbooking import Ticketbooking
from Ticket import Ticket
booker=Ticketbooking()


while True:
    print(" 1.Book ticket \n 2.Cancel ticket \n 3.Print chart \n 4. exit")
    choice=int(input("Enter your choice: "))
    match(choice):
        case 1:
            fromstation=input("Enter the from station: ").upper()
            tostation=input("Enter the to station: ").upper()
            seats=int(input("Enter the number of seat: "))
        
            t=Ticket(fromstation,tostation,seats)
            booker.bookticket(t)
        case 2:
            booker.cancelticket()
        case 3:
            booker.printchart()
        case 4:
            break
        case _:
            print(" invalid option")
            break 