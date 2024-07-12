class BankInfo:
    def __init__(self, fn, ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address

class BankAccount:
    def __init__(self,bank_info,acno, amount,):
        self.acno = acno
        self.amount = amount
        self.bank_info = bank_info

    # def validate_amount(self, amount):
    #     pass

    # def calculate_interest(self, months):
    #     pass

class Saving(BankAccount):
    minAmount = 10000
    rate = 6  
    sum_int=0.00

    def validate_amount(self):
        if self.amount >= self.minAmount:
            pass
        else:
            for i in range(4):
                if self.amount >= self.minAmount:
                    pass

                elif i==3:
                    print("3 chances done")
                    exit()
                else:
                    self.amount = int(input("Enter Amt w.r.t to min. balance(10000)"))


    def calculate_interest(self, months):
        self.months=months
        year=self.months/12
        self.sum_int=float((self.amount*self.rate*year)/100)

    def viewProfile(self):
        print("------------------------------------------------------------------------------------------------------")        
        print("FirstName=", self.bank_info.fn)
        print("LastName=", self.bank_info.ln)
        print("Gender=", self.bank_info.gender)
        print("Address=", self.bank_info.address)
        print("Account Number=", self.acno)
        print("Amount=", self.amount)
        print("Rate=", self.rate)
        print("Months=", self.months)
        print("Interest=", self.sum_int)



class Current(BankAccount):
    minAmount = 5000
    rate = 0

    def validate_amount(self):
          if self.amount >= self.minAmount:
            pass
          else:
            for i in range(4):
                if self.amount >= self.minAmount:
                    pass

                elif i==3:
                    print("3 chances done")
                    exit()
                else:
                    self.amount = int(input("Enter Amt w.r.t to min. balance(5000)"))

    def viewProfile(self):
        print("------------------------------------------------------------------------------------------------------")
        print("FirstName=", self.bank_info.fn)
        print("LastName=", self.bank_info.ln)
        print("Gender=", self.bank_info.gender)
        print("Address=", self.bank_info.address)
        print("Account Number=", self.acno)
        print("Amount=", self.amount)
        print("Rate=", self.rate)
        print("Months=", self.months)
        print("Interest=", self.sum_int)

class MainClass:
    def __init__(self):
            fn = input("Enter first name: ")
            ln = input("Enter last name: ")
            gender = input("Enter gender: ")
            address = input("Enter address: ") 

            bank_info = BankInfo(fn, ln, gender, address)

            acno = input("Enter account number: ")
            amount = float(input("Enter initial amount: "))
            account_type = input("Select account type (Saving/Current): ")
            if account_type.lower() == "saving":
                bank_account1 = Saving(bank_info,acno, amount)
                bank_account1.validate_amount()
                months=int(input("Enter no. of months: "))
                bank_account1.calculate_interest(months)
                bank_account1.viewProfile()
            elif account_type.lower() == "current":
                bank_account2 = Current(bank_info,acno, amount)
                bank_account2.validate_amount()
                months=int(input("Enter no. of months: "))
                bank_account2.viewProfile()
            else:
                print("Invalid account type")
objectMain = MainClass()