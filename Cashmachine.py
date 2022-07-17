
from cmcsv import record_log
import csv 

class customer:

    counter = 0     #count how many registered customers
    withdrawal_fee = 1.005      
    identifier_dict = {}
    objects = []
    header_switch = True    #makes the header of csv show up only once

    def __init__(self, first, last, balance):
        self.first = first
        self.last = last
        self.email = f"{first}_{last}@email.com"
        self.balance =  balance
        self.log_type = "Register"
        
        customer.counter += 1       # plus 1 to counter for every customer that has been registered
        self.counter = customer.counter
        self._id = self.counter
        customer.identifier_dict.update({str(customer.counter) : str(self.id)})     #add customer's counter and id into identifier_dict
        customer.objects.append(self)
        record_log(self, "N/A")

    #-----------------------------------------------------------------------------------------------------------
    # Make id attribute
    @property
    def id(self) -> str:
        return str(self._id).zfill(5)       #set id by placing zeroes infront of object's customer_id

    # Ability to set new id of the object
    @id.setter
    def id(self, assigned_id):              
        if assigned_id != customer.identifier_dict.values():
            self._id = str(assigned_id)         #set id to newly assigned value
            customer.identifier_dict.update({str(self.counter) : str(self.id)})     #update newly assigned id in the identifier_dict
        elif assigned_id == self.id:
            print("You're entering your current ID. Please enter different ID")
    #-----------------------------------------------------------------------------------------------------------

    #Create new instance with register method (Alternative Constructor)
    #Example : by calling Customer1 = customer.register("George", "Smilth"), we can create Customer1 instance with name George Smilth
    @classmethod
    def register(cls, first, last, balance=0):
        return cls(first, last, balance)
    
    def deposit(self, amount):
        self.log_type = "deposit"
        self.balance = self.balance + int(amount)
        record_log(self, amount)

    def withdraw(self, amount):     #don't forget fee of withdrawal,trasnfering between customers, payment, log,, id of users cannot be the same
        self.log_type = "withdraw"

        # Cannot withdraw if balance is less than the amount withdrawal plus fee of 0.5%
        if self.balance >= (int(amount) * customer.withdrawal_fee):
            self.balance = self.balance - (int(amount) * customer.withdrawal_fee)
            record_log(self, amount)
        else:
            print("Sorry, Your balance is not sufficient to make a withdrawal")
            
        # Tell customer to enter the withdrawal amount if the amount is left 0
        if amount == 0:
            print("Please enter the amount you want to withdraw")

    def transfer(self, id, amount):     #transfer balance between users

        self.log_type = "transfer"

        @staticmethod                   
        def attr_to_obj(attr):          #link id with obj name, so that it is possible to transfer balance with just customer's id
            for obj in customer.objects:
                if obj.id == attr:
                    return obj
                    
        if id in customer.identifier_dict.values():     #check if recipient id exist in the system
            self.balance -= int(amount)                   #substract balance from self
            attr_to_obj(id).balance += amount           #add blance to recipient
            print(f"Transfer to {id} is successful")
            record_log(self, amount)
        elif id == self.id:
            print("You're entering your own ID, Please reenter the recepient ID")
        else:
            print("The recipient ID does not exist")


    def statement(self):
            list_csv = []
            with open(f"log{self.id}.csv", "r", newline='') as csv_file2:

                csv_reader = csv.reader(csv_file2, delimiter="-")

                next(csv_reader)        #skip header texts

                for log in csv_reader:
                    list_csv.append(str(log))

                return "\n".join(list_csv[-5:])         #"\n".join()  to join all the elements of an iterable (list, string, tuple), separated by a "\n", which makes each takes linebreak 



    



customer1 = customer("George", "Smilth", 0)

customer2 = customer("Jane", "Aothenberg", 0)



print(customer1.balance, "customer1")
customer1.deposit(50000)
print(customer1.balance)

print(customer2.balance, "customer2")
customer2.deposit(10000)
print(customer2.balance)

customer1.transfer("00002", 5000)
print(customer1.balance)
print(customer2.balance)


