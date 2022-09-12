class User():
    def __init__(self, property_name, user, income, income_amount, expense, expense_amount, investment, investment_amount):
        self.user = user
        self.property_name = property_name
        self.income = income
        self.income_amount = income_amount
        self.expense = expense 
        self.expense_amount = expense_amount
        self.investment = investment
        self.investment_amount = investment_amount
        
    
class ROI():
    def __init__(self):
        self.users = {}

    def create_property(self, user, property_name, income, income_amount, expense, expense_amount, investment, investment_amount):

        new_property = User(property_name, income, income_amount, expense, expense_amount, investment, investment_amount)
        self.users[user] = new_property 
        
        """"
        adds property to that specific user 

        """
    def portfolio(self):
        
        for user, roi in self.users.items():

            roi_total = (roi.investment_amount / roi.investment_amount) * 100
            print(f"Hello {user.title()}")
            print(f"Your ROI for this is {roi_total}%")
            


        """
        shows the name of the property and the ROI 
        example 
        property 1 - 9.7% ROI

        you have a total of 1 

        ^ return the amount of properties that user has
        """

    def choose_property():
        pass
        """
        i dont get this wat 
        """
    def modify():
        pass

        """
        modify income/expense/investments

        basically adding more ^

        option to keep modifying if not then return to interface
        """

    def delete():
        pass

        """"
        show cases all the properties of that user
        let's user delete the property by number assosciated with it
        """

    def create_user(self, user, property_name, income, income_amount, expense, expense_amount, investment, investment_amount):
        
        new_user = User(user, property_name, income, income_amount, expense, expense_amount, investment, investment_amount)
        self.users[user] = {}
        self.users[user]['Properties'] = {}
        self.users[user]['Properties'][property_name] = {income : income_amount}
        self.users[user]['Properties'][property_name] = {expense : expense_amount}
        self.users[user]['Properties'][property_name] = {investment: investment_amount}
        self.users[user] = new_user
        
        for user, user_info in self.users.items():
            print(f"{user} has {user_info}")
            print(f"You have successfully created an account {user.title()} \n")
            print(f"Your property {user_info.property_name} has an income of {user_info.income_amount} \n")
            print(f"expenses of {user_info.expense_amount} \n")
            print(f"with a total investment of ${user_info.investment_amount} \n")

  
        """
        users = self.users
        users[self.user] = {}
        users[self.user][property] = {}
        users[self.user][property][income] = 'income_amount'
        users[self.user][property][expense] = 'expense_amount'
        users[self.user][property][invesement] = 'investment_amount'

        {victor, {property: {'income': '#', 'expense': '#', 'investment': '#'}}}
        creating a new user refer back to lecture about classes 
        that allows object to have it's own separate data 


        """



    def switch_user():
        pass
        """
        allows user to switch accounts taht has a separate data 
        refer back to old "class" lecture 
        """


        
    # income information
    """
    income name 
    income amount 
    option to add more income 
    """
    #expense information 
    """
    expense name 
    expense amount 
    option to add more expenses
    """
    #investment info
    """"
    investment name 
    investment amount 
    option to add more investments 
    """

# run the program
class User_interface():
    def __init__(self):
        self.roi = ROI()
    def main(self):
        while True:
            print(f"What would you like to do? \n")
            
            print(f"[1] Add property")
            print(f"[2] Portfolio")
            print(f"[3] Choose property")
            print(f"[4] Modify property")
            print(f"[5] delete property")
            print(f"[6] Create an Account")
            print(f"[7] Switch Accounts")
            print(f"[0] Quit\n")

            nav = input(f"Welcome What would you like to do?")
            if nav == "1":
                property_name = input("Please choose name for your property: ")

                income = input("Enter name for income: ").lower()
                income_amount = int(input("Enter an amount for income: "))
                
                expense = input("Enter name for expense: ").lower()
                expense_amount = int(input("Enter an amount for expense/s: "))
                
                investment = input("Enter name for Investment: ").lower()
                investment_amount = int(input("Enter an amount for your investment/s: "))
                
                self.roi.create_property(property_name, income, income_amount, expense, expense_amount, investment, investment_amount)
            elif nav == "2":
                ROI.portfolio()
            elif nav == "3":
                ROI.choose_property()
            elif nav == "4":
                ROI.modify()
            elif nav == "5":
                ROI.delete()
            elif nav == "6":
                user = input(str("Choose a Username: ")).lower()
                
                property_name = input(str("Please choose name for your property: "))

                income = input(str("Enter name for income: ")).lower()
                income_amount = int(input("Enter an amount for income: "))
                
                expense = input(str("Enter name for expense: ")).lower()
                expense_amount = int(input("Enter an amount for expense/s: "))
                
                investment = input(str("Enter name for Investment: ")).lower()
                investment_amount = int(input("Enter an amount for your investment/s: "))
                
                self.roi.create_user(user, property_name, income, income_amount, expense, expense_amount, investment, investment_amount)
                
            elif nav == "7":
                ROI.switch_user()
            elif nav == "0":
                print("Returning to Main Menu")
                break

run = User_interface()
run.main()