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

from tkinter import *
from amaryllis_mederovargas_ILA10_CLASS import Bank, Account


class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.new_account_widget()
        self.bank = Bank() #create a Bank object
 
    def new_account_widget(self):
        
        # ********************* create widgets *********************
        label_fname = Label(self, text = "First name: ")
        self.entry_fname = Entry(self, width=15)
        label_lname = Label(self, text = "Last name: ")
        self.entry_lname = Entry(self, width=15)

        label_type = Label(self, text="Account Type: ")
        self.entry_accounttype = Entry(self, width = 15)

        label_username = Label(self, text = "Username: ")
        self.entry_username = Entry(self, width=15)
        label_pin = Label(self, text = "Pin: ")
        self.entry_pin = Entry(self, width=15)

        
        button_create  = Button(self, text = "Create account", \
                                command=self.create_account_button_click)
        button_main_menu  = Button(self, text = "Main Menu", \
                                command=self.main_menu_button_click)

        

        
 
        # ********************* Layout Widgets *********************
        #name
        label_fname.grid(row=0, column = 0)
        self.entry_fname.grid(row=0, column = 1)
        label_lname.grid(row = 1, column = 0)
        self.entry_lname.grid(row = 1, column = 1)
        
        #account type
        label_type.grid(row=2, column = 0)
        self.entry_accounttype.grid(row=2, column =1)
        #login info
        label_username.grid(row=3, column = 0)
        self.entry_username.grid(row=3, column = 1)
        label_pin.grid(row=4, column = 0)
        self.entry_pin.grid(row=4, column = 1)

        
        #button
        button_create.grid(row = 5, column = 0)
        button_main_menu.grid(row = 5, column = 1)
 
    def create_account_button_click(self):
        cfname= self.entry_fname.get()
        clname= self.entry_lname.get()

        #your code here
        #get type, username, user_pin from entries
        cacctype = self.entry_accounttype.get()
        cusername = self.entry_username.get()
        cpin = self.entry_pin.get()
 
        caccount_no = 'XXXX' # a set account number

        #your code here
        #create an account object here
        self.account = Account(fname = cfname, lname = clname,\
                               account_no = caccount_no, acctype = cacctype,\
                               username = cusername, pin = cpin)
                               #fill out rest of the parameters
                               #notice the keys fname, lname from Account class

        self.bank.display() #displays the object created
        
    def main_menu_button_click(self):
        pass
 
#driver
root = Tk()
frame = MyFrame(root)
frame.pack()
root.mainloop()
