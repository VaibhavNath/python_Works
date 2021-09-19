class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    
    def getStatus(self):
        print(f'The name of the train is {self.name} with fare Rs.{self.fare} and number of seats {self.seats}')
    
    def booktickets(self):
        if(self.seats>0):
            print(f'Ticket booked with seat number {self.seats}')
            self.seats=self.seats-1
        else:
            print(f'sorry train if full,kindly try in tatkaal')

interCity=Train("Intercity express:14015",352,2)
interCity.getStatus()
interCity.booktickets()
interCity.booktickets()
interCity.booktickets()
interCity.getStatus()