#-------------------------------------------------------------------------------
# ILA10.py
# Name: FirstName LastName
# Python Version:  3.XX
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments to grader: 
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

class Bank(object):
    accountList = [] #class variable contains all the account objects
    
    def display(self):
        for account in Bank.accountList:
            print ("*********************")
            for k, v in account.items():
                print ('{} : {}.'.format(k, v))
            print ("*********************")
    

class Account(object):
    default_options = {'accountno':None,'acctype': None, \
               'balance': 0, 'fname': None, 'lname': None,  \
                       'username': None, 'pin': None}
    def __init__(self, **kwargs):
        self.options = Account.default_options.copy() #copy the default options to options
        #your code here
        #update the self.options by kwargs
        #append the self.options to accountList in Bank class
        for keyword, value in kwargs.items():
            self.options[keyword] = value
        Bank.accountList.append(self.options)