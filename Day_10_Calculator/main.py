from art import *
from replit import clear
def operate(oper,f_num,s_num):
    if oper=='+':
        return f_num+s_num
    elif oper=='-':
        return f_num-s_num
    elif oper=='*':
        return f_num*s_num
    elif oper=='/':
        return f_num/s_num
    else:
        return "invalid operation"
    
def calculator():
    print(logo)
    f_num = float(input("what's the first number?: "))
    repeat = True
    while repeat:
        oper = input("+\n-\n*\n/\nPick an operation: ")
        s_num = float(input("What's the next Number?: "))
        res = operate(oper, f_num, s_num)
        print("{} {} {} = {}".format(f_num, oper, s_num, res))
        if input("Type 'y' to continue calculating with {res} or type 'n' to start a new calculator: ").lower()=='y':
            repeat=True
            f_num = res
        else:
            clear()
            calculator()

calculator()
        