import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename = "practicelog.log", level = logging.DEBUG, format = "[%(asctime)s] %(levelname)s - %(message)s")

#invites = ["Manager","Senior","Engineer"]
guest = {"Luca":"Engineer","Merwin":"Senior","Chris":"Manager"}

class Access():
    def __init__(self):
        self.manager = 5
        self.senior = 4
        self.engineer = 7

    def entry(self):
        name = input("Enter guest's name: ")
        try:
            role = guest[name]
            if role == "Engineer":
                self.engineer -= 1
            elif role == "Senior":
                self.senior -= 1
            else:
                self.manager -= 1
            logger.info("{name} has entered the venue".format(name=name))
            logger.info(f"Remaining - Managers: {self.manager}, Seniors: {self.senior}, Engineers: {self.engineer}")
        except KeyError:
            logger.error("Error! name entered is not on guest list")

entry1 = Access()
entry1.entry()

#logs every drink order and logs money made, every log will print the total money made
logging.getLogger(__name__)
logging.basicConfig(filename = "drinklog.py", level = DEBUG, format = "[%(asctime)s] %(levelname)s - %(message)s")

drink_menu{
    "Jagger Bomb":5,
    "Long Islan Ice Tea":10,
    "Tequilla shot": 4,
    "Blue Lagoon": 9
}

class Bar:

    def __init__(self):
        self.tab = 0
        print("Welcom to Magnus Bar!")

    def buy(self):
        try:
            choice = input("Please select a drink! ")
            



