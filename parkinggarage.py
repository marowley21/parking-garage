class ParkingGarage():

    # ParkingGarage constructor definition
    def __init__(self):
        self.tickets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

    # takeTicket function definition
    def takeTicket(self):

        if len(self.parkingSpaces)==0:
            print('Sorry, the Parking Garage is full!')

        else:
            # decrease the amount of tickets available by 1
            self.tickets.remove(self.tickets[-1])

            # decrease the amount of parkingSpaces available by 1
            self.parkingSpaces.remove(self.parkingSpaces[-1])

    # function definition for payForParking
    def payForParking(self):

        amount = input('Enter 1 to pay now: ')

        if amount == '1':

            # update the "currentTicket" dictionary key "paid" to True
            self.currentTicket['Paid'] = True
            print('ticket has been paid, you have 15 minutes to leave')

    # leaveGarage function definition
    def leaveGarage(self):

        if self.currentTicket['Paid']==True:
            print('Thank you, have a nice day!')

        else:

            amount = input('Enter 1 to pay now: ')

            while amount!='1':
                amount = input('Enter 1 to pay now: ')

            # increase the amount of tickets available by 1
            self.tickets.append(self.tickets[-1]+1)

            # increase the amount of parkingSpaces available by 1
            self.parkingSpaces.append(self.parkingSpaces[-1]+1)


##################

# Fingers Crossed
def main():
    
    car = ParkingGarage()
    print('Welcome to the Parking Garage!\n')

    print('Please take a ticket.')

    printedTicket = input('Enter T to take ticket: ')

    if printedTicket.upper() == "T":
        car.takeTicket()

        car.payForParking()

        car.leaveGarage()

    else:
        print('Error')

main()
