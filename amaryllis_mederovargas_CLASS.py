# name: Amaryllis Medero-Vargas
# final project class file
class Bank(object):
    """account list Holds all the list of accounts"""
    accountList=[]
    def display(self): #for printing purposes only
        for account in Bank.accountList:
            print ("*********************")
            for k,v in account.options.items():
                print ('{}: {}'.format(k,v))
            print ("*********************")

    def login_validity(self, u, p): #checks for the correct login 
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return True
        return False

    def load_account(self,u, p): #loads current account
        for account in Bank.accountList:
            if u == account['username'] and p == account['pin']:
                return account #account object
        return None #no object found
    
    
        
class Account(object):
    default_options = {'accountno':None,'acctype': None, \
               'balance': 0, 'fname': None, 'lname': None, 'line1':None, \
                       'line2': None, 'username': None, 'pin': None}
    def __init__(self, **kwargs):
        """initialization"""
        #part of ILA
        self.options = Account.default_options.copy()
        self.options.update(kwargs)
        Bank.accountList.append(self)

    def __getitem__(self, key): #get an item by key
        """get item by key"""
        return self.options[key]
    
    def __setitem__(self, key, new_value): #set an item by key
        """set item by key"""
        self.options[key] = new_value
        
    def getBalance(self, accno):
        """returns account's balance"""
        if accno == self['accountno'] :
                return self['balance']
 
    def deposit(self, amount_to_deposit, accno):
        """calculates account balance after deposit"""
        #your code here
        #please see getBalance on how to access an attribute
        #deposits amount_to_deposit to current user
        if accno == self['accountno'] :
                self.amount_to_deposit = amount_to_deposit
                self['balance'] = float(self.getBalance(accno))
                self['balance'] = self['balance'] + float(self.amount_to_deposit)
                return self['balance']


    def summary(self, accno):
        """returns account summary information"""
        #your code here
        #return full name, address, account type and current balance
        if accno == self['accountno']:
                self['balance'] = self.getBalance(accno)
                self.name = self['fname']+ " " + self['lname']
                self.address = self['line1'] + " " + self['line2']
                self.acctype = self['acctype']
                self.balance = self['balance']
                return self.name, self.address, self.acctype, self.balance

       
class Saving(Account):
    """calculates new balance after withdrawal in savings account"""
    withdraw_charge = 2.53 #flat rate to subtract from saving account
        
    def withdraw(self, amount_to_withdraw, accno):
        #your code here
        if accno == self['accountno'] :
                self.amount_to_withdraw = float(amount_to_withdraw) + self.withdraw_charge
                self['balance'] = float(self.getBalance(accno))
                self['balance'] = self['balance'] - self.amount_to_withdraw
                return self['balance']

class Checking(Account):
    """calculates new balance after checking withdrawal"""
    withdraw_charge = 1.00
    def withdraw(self, amount_to_withdraw, accno):
        #your code here
        if accno == self['accountno'] :
                self.amount_to_withdraw = float(amount_to_withdraw) + self.withdraw_charge
                self['balance'] = float(self.getBalance(accno))
                self['balance'] = self['balance'] - self.amount_to_withdraw
                return self['balance']
