'''Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects.''' # Ans -- Nothing happens

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def Book(aryan, fro, to):
        print(f"Ticket is booked in train no: {aryan.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(12399)
t.Book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")