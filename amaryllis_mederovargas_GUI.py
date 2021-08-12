# -------------------------------------------------------------------------------
# Final Project: Banking Application
# Name: Amaryllis Medero-Vargas
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



from tkinter import *
from amaryllis_mederovargas_CLASS import Saving, Checking, Account, Bank
from amaryllis_mederovargas_UTILITY import createAccountNo

class MyFrame(Frame):
    def __init__(self, root):
        """initialization"""
        Frame.__init__(self, root)
        self.bank = Bank()
        self.welcome()

    def clear_frame(self): #clears the previous frame
        """clears frame of widget"""
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        """exits application"""
        root.destroy()

    def logout(self):
        """logs out of account"""
        del self.account
        self.welcome()
        
    def welcome(self): #welcome screen
        """welcome screen"""
        self.clear_frame()
        
        welcome_label = Label(self, text = 'Welcome to 209 Banking!')
        self.b1  = Button(self, text = "Existing User", \
                     command=self.existing_account_widget)
        self.b2  = Button(self, text = "New User", \
                     command=self.new_account_widget)
        self.b3  = Button(self, text = "Exit Application", \
                     command=self.exit_application)

        #Your code here
        #layout  manager for label, b1, b2 and b3
        welcome_label.grid(row=0)
        self.b1.grid(row=1)
        self.b2.grid(row=2)
        self.b3.grid(row=3)
        
    def new_account_widget(self):
        """user enters new user information"""
        self.clear_frame()
        # ********************* create widgets *********************
        label_fname = Label(self, text = "First name: ")
        self.entry_fname = Entry(self, width=15)
        label_lname = Label(self, text = "Last name: ")
        self.entry_lname = Entry(self, width=15)


        label_line1 = Label(self, text= "Address line1: ")
        self.entry_line1 = Entry(self, width = 15)

        label_line2 = Label(self, text= "Address line2: ")
        self.entry_line2 = Entry(self, width = 15)

        label_type = Label(self, text="Account Type: ")
        self.entry_accounttype = Entry(self, width = 15)

        label_username = Label(self, text = "Username: ")
        self.entry_username = Entry(self, width=15)
        label_pin = Label(self, text = "Pin: ")
        self.entry_pin = Entry(self, width=15)

        
        button_create  = Button(self, text = "Create account", \
                                command=self.create_account_button_click)
        button_main_menu  = Button(self, text = "Main Menu", \
                                command=self.welcome)

        # ********************* Layout Widgets *********************
        #name
        label_fname.grid(row=0, column = 0)
        self.entry_fname.grid(row=0, column = 1)
        label_lname.grid(row = 1, column = 0)
        self.entry_lname.grid(row = 1, column = 1)
        #address
        label_line1.grid(row = 2, column = 0)
        self.entry_line1.grid(row = 2, column = 1)
        label_line2.grid(row = 3, column = 0)
        self.entry_line2.grid(row = 3, column = 1)
        #account type
        label_type.grid(row=4, column = 0)
        self.entry_accounttype.grid(row=4, column =1)
        #login info
        label_username.grid(row=5, column = 0)
        self.entry_username.grid(row=5, column = 1)
        label_pin.grid(row=6, column = 0)
        self.entry_pin.grid(row=6, column = 1)

        
        #button
        button_create.grid(row = 7, column = 0)
        button_main_menu.grid(row = 7, column = 1)

 

    #Create account object
    def create_account_button_click(self):
        """command for clicking account button"""
        cfname= self.entry_fname.get()
        clname= self.entry_lname.get()

        cline1= self.entry_line1.get()
        cline2= self.entry_line2.get()

        t = self.entry_accounttype.get().lower()
        u = self.entry_username.get()
        p = self.entry_pin.get()

        self.clear_frame()
        label_accountno = Label(self, text = "Your account no: ")
        self.accountno  = StringVar(self, '') #create StringVar object
        label_final_accountno  = Label(self, \
                                       textvariable=self.accountno) #associate self.result with this label


        s = createAccountNo()
        self.accountno.set(s) #setting 

        #create account object for each type of account

        if t.lower() == 'saving': #creating saving object
            d = {'fname':cfname, 'lname':clname,\
                 'line1':cline1, 'line2':cline2, 'accountno':s,\
                 'balance':0, 'acctype':t,'username':u, 'pin':p}
            self.account= Saving(**d)
        #your code here
        elif t.lower() == 'checking':
            #your code here
            #same as saving
            w = {'fname': cfname, 'lname': clname, \
                 'line1': cline1, 'line2': cline2, 'accountno': s, \
                 'balance': 0, 'acctype': t, 'username': u, 'pin': p}
            self.account= Checking(**w)
        self.bank.display() #for printing purpose
        self.button_next  = Button(self, text = "Please Login Again", command=self.existing_account_widget)
        label_accountno.grid(column=0, columnspan = 2)
        label_final_accountno.grid(column=0, columnspan = 2)
        self.button_next.grid(column = 0, columnspan = 2)
 

    def existing_account_widget(self):
        """ allows existing user enters username and pin"""
        self.clear_frame()
        #your code here step 4 in spec
        #login widget
        #username, pin: label and entry
        label_username = Label(self, text="Username:")
        self.entry_username = Entry(self, width=15)
        label_pin = Label(self, text="Pin:")
        self.entry_pin = Entry(self, width=15)
        #login, main menu: buttons
        button_login = Button(self, text="Login", command=self.login_button_click)
        button_main_menu = Button(self, text="Main Menu", command=self.welcome)
        #layout
        label_username.grid(row=0,column=0)
        self.entry_username.grid(row=0, column=1)
        label_pin.grid(row=1,column=0)
        self.entry_pin.grid(row=1,column=1)
        button_login.grid(row=2)
        button_main_menu.grid(row=3)

    def login_button_click(self):
        """command for clicking login button"""
        self.entry_exist_username = self.entry_username
        self.entry_exist_pin = self.entry_pin
        u = self.entry_exist_username.get()
        p = self.entry_exist_pin.get()
        if (self.bank.login_validity(u, p)):
            self.account = self.bank.load_account(u, p) #returns account object
            self.existing_user_options()
        else:
            self.existing_account_widget()
            

    def existing_user_options(self):
        """interface for buttons of existing user"""
        self.clear_frame()
        self.deposit_button = Button(self, text = "Deposit", \
                                      command=self.deposit_interface)
        self.deposit_button.grid(row=0)
        #your code here
        #withdraw, summary, logout and exit application
        #button step 5 in spec
        self.withdraw_button = Button(self, text="Withdraw", command=self.withdraw_interface)
        self.summary_button= Button(self, text="Summary", command=self.summary_interface)
        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.exit_app_button = Button(self, text="Exit Application", command=self.exit_application)

        self.withdraw_button.grid(row=1)
        self.summary_button.grid(row=2)
        self.summary_button.grid(row=3)
        self.logout_button.grid(row=4)
        self.exit_app_button.grid(row=5)

    def summary_interface(self):
        """creates interface window that allows user to specify account to provide summary"""
        self.clear_frame()
        #your code here
        #create label and entry for Account Number
        self.label_accountno = Label(self, text="Account Number")
        self.entry_accno = Entry(self, width=15)
        #button: Options: command = existing_user_options method
        self.options_button = Button(self, text="Options", command=self.existing_user_options)
        #button: Next: command = summary method
        self.button_next = Button(self, text="Next", command=self.summary)
        #layout
        self.label_accountno.grid(row=0, column=0)
        self.entry_accno.grid(row=0, column=1)
        self.options_button.grid(row=1, column=0)
        self.button_next.grid(row=1, column=1)

    def summary(self):
        """summary of account specified in summary_interface method"""
        accno = self.entry_accno.get() #obtains account no from user
        name, address, acctype, balance = self.account.summary(accno)
        
        self.clear_frame()
        self.info_label = Label(self, text = "Account Information")
        self.name_label = Label(self, text = name)
        self.address_label = Label(self, text = address)
        self.acctype_label = Label(self, text = acctype)
        self.balance_label = Label(self, text = str(balance))
        self.info_label.pack()
        self.name_label.pack()
        self.address_label.pack()
        self.acctype_label.pack()
        self.balance_label.pack()
        

        self.button_options = Button(self, text = "Options", command=self.existing_user_options)
        self.button_options.pack()
        
    def deposit_interface(self):
        """creates deposit interface window"""
        self.clear_frame()
        #your code here
        #step 6 in spec
        #Next button will call deposit, please see summary interface function
        self.amt_label = Label(self, text="Amount to deposit")
        self.amt_deposit_entry = Entry(self, width=15)
        self.label_accountno = Label(self, text="Account Number")
        self.entry_accno = Entry(self, width=15)
        self.options_button = Button(self, text="Options", command=self.existing_user_options)
        self.button_next = Button(self, text="Next", command=self.deposit)
        #layout
        self.amt_label.grid(row=0, column = 0)
        self.amt_deposit_entry.grid(row=0, column = 1)
        self.label_accountno.grid(row=1, column = 0)
        self.entry_accno.grid(row=1, column = 1)
        self.options_button.grid(row=2, column = 0)
        self.button_next.grid(row=2, column = 1)

    def deposit(self):
        """deposits user specified amount"""
        self.entry_deposit = self.amt_deposit_entry
        d = self.entry_deposit.get()
        accno = self.entry_accno.get()
        self.account.deposit(d, accno)
        self.check_balance(accno)

        
    def withdraw_interface(self):
        """creates withdraw interface window"""
        self.clear_frame()
        self.clear_frame()
        #your code here
        #same as deposit interface, see step 7 in spec
        self.amt_label = Label(self, text="Amount to withdraw")
        self.amt_withdraw_entry = Entry(self, width=15)
        self.label_accountno = Label(self, text="Account Number")
        self.entry_accno = Entry(self, width=15)
        self.options_button = Button(self, text="Options", command=self.existing_user_options)
        self.button_next = Button(self, text="Next", command=self.withdraw)
        #layout
        self.amt_label.grid(row=0, column=0)
        self.amt_withdraw_entry.grid(row=0, column=1)
        self.label_accountno.grid(row=1, column=0)
        self.entry_accno.grid(row=1, column=1)
        self.options_button.grid(row=2, column=0)
        self.button_next.grid(row=2, column=1)

    def withdraw(self):
        """withdraws user specified amount"""
        self.entry_withdraw = self.amt_withdraw_entry
        #your code here
        #same as deposit
        w = self.entry_withdraw.get()
        accno = self.entry_accno.get()
        self.account.withdraw(w, accno)
        self.check_balance(accno)

        
    def check_balance(self, accno):
        """checks current balance"""
        self.clear_frame()
        label_balance = Label(self, text = 'Current balance: ' + \
                              str(self.account.getBalance(accno)))
        label_balance.grid()
        
        self.options_button  = Button(self, text = "Options", \
                                            command=self.existing_user_options)
        self.options_button.grid()


             
#driver
root = Tk()
frame = MyFrame(root)
frame.pack()
root.mainloop()
