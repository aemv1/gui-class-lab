import random, string

def createAccountNo():
    """randomly create account number"""
    number = ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))
    return number

print(createAccountNo())
