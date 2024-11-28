from collections import deque
from Ticket import Ticket

class Ticketbooking:
    availableseat=8
    availablewaitinglist=2
    
    seatlist=[1,2,3,4,5,6,7,8]
    waitingseat=[1,2]
    
    waitinglist=deque()
    
    seatingchart={}
    
    ticketlist={}
    
    def __init__(self):
        for i in range(1,Ticketbooking.availableseat+1):
            Ticketbooking.seatingchart[i]=["-","-","-","-","-"]
        # print(Ticketbooking.seatingchart)
    
    def bookticket(self,t):
        if Ticketbooking.availablewaitinglist<1:
                print("No tickets")
                return
        if t.seats<=Ticketbooking.availableseat:
            fromindex=self.getstationindex(t.fromstation)
            toindex=self.getstationindex(t.tostation)
           
            i=0
            count=t.seats
            while count>0 and i<len(Ticketbooking.seatlist):
                # print(Ticketbooking.seatlist)
                seatnumber=Ticketbooking.seatlist[i]
                i+=1
                # print(seatnumber)
                if self.seatavailable(fromindex,toindex,seatnumber):
                        count-=1
                        t.seatnumber.append(seatnumber)
                    
                        seatinglistinchart=Ticketbooking.seatingchart[seatnumber]
                        for j in range(fromindex,toindex):
                            seatinglistinchart[j]='*'
                        Ticketbooking.seatingchart[seatnumber]=seatinglistinchart
                        for k in range(len(Ticketbooking.seatingchart[seatnumber])-1):
                            if Ticketbooking.seatingchart[seatnumber][k] == '-' :
                                break
                        else:
                            Ticketbooking.availableseat-=1
                            # print(Ticketbooking.availableseat)
                # else:
                    # print('Alreday booked')
                    # continue
            print("Ticket booked successfully")
            Ticketbooking.ticketlist[t.pnr]=t
            print(t)
        else:
            
            if Ticketbooking.availablewaitinglist>0 and t.seats<=Ticketbooking.availablewaitinglist:
                Ticketbooking.waitinglist.append(t)
                wseatlist=Ticketbooking.waitingseat[:]
                for i in range(t.seats):
                    Ticketbooking.availablewaitinglist-=1
                    seatnumber=str(wseatlist.pop(0))+'WL'
                    t.seatnumber.append(seatnumber)
                print("waiting list given")
                print(t)
            else:
                print(Ticketbooking.availablewaitinglist,"waiting list only available")
                
        
                
    def getstationindex(self,station):
        stations={
            'A':0,
            'B':1,
            'C':2,
            'D':3,
            'E':4
        }
        return stations[station]
    
    def seatavailable(self,fromindex,toindex,seats):
        # for i in range(seats+1):
            seatinglist=Ticketbooking.seatingchart[seats]
            for j in range(fromindex,toindex):
                if seatinglist[j] == '*':
                    return False
            return True
        
    def cancelticket(self):
        id=int(input("Enter the id to cancel: "))
        cseats=int(input("Enter the number of seats to cancel: "))
        if id not in Ticketbooking.ticketlist:
            print("Invalid id")
            return
        if cseats > Ticketbooking.ticketlist[id].seats:
            print("seats are more ")
            return
        passenger=Ticketbooking.ticketlist[id]
        if passenger.seats<1:
            del Ticketbooking.ticketlist[id]
        # Ticketbooking.availableseat +=  passenger.seats
        cancelfrom=self.getstationindex( passenger.fromstation)
        cancelto=self.getstationindex( passenger.tostation)
        seatnumbers=passenger.seatnumber
        for i in range(cseats):
            cancelseatinglist=Ticketbooking.seatingchart[seatnumbers[0]]
            for j in range(cancelfrom,cancelto):
                cancelseatinglist[j]='-'
            Ticketbooking.seatingchart[seatnumbers[0]]=cancelseatinglist
            for k in range(len(Ticketbooking.seatingchart[seatnumbers[0]])-1):
                if cancelseatinglist[k] == '*' :
                    break
            else:
                Ticketbooking.availableseat +=  1
                # print(Ticketbooking.availableseat)
            passenger.seatnumber.pop(0)
            
                     
        if len(Ticketbooking.waitinglist)>0:
            # for i in range(len(Ticketbooking.waitinglist)):
                waitingpassenger=Ticketbooking.waitinglist.popleft()
                Ticketbooking.availablewaitinglist+=waitingpassenger.seats
                waitingpassenger.seatnumber=[]
                a=self.bookticket(waitingpassenger)
                # if (a):
                #     self.availablewaitinglist+=1
        print("Ticket cancelled successfully")
            
        
    
    def printchart(self):
        print("---------------")
        print("  A B C D E")
        for seatno, seatlist in Ticketbooking.seatingchart.items():
            print(seatno,*seatlist)
        print("---------------")
        
    