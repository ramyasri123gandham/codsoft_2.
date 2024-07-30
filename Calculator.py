'''Design a simple calculator with basic arithmetic operations.
 Prompt the user to input two numbers and an operation choice.
 Perform the calculation and display the result.'''

def add (x,y):
    return x+y
def subt (x,y):
    return x-y
def multiply (x,y):
    return x*y
def div (x,y):
    if y!=0:
        return x/y
    else:
        return 'Division by 0 is not defined'
# def mod (x,y):
#     return x%y

if __name__=="__main__"   :
    m,n=map(int,input('Enter two numbers ').split())
    ch=input('Enter the arthematic operation symbol(+, -, *, /, %)  ')
    if ch=='+':
        print(add(m,n))
    elif ch=='-':
        print(subt(m,n))    
    elif ch=='*':
        print(multiply(m,n))
    elif ch=='/':
        print(div(m,n))
    # elif ch=='%':
    #     print(mod(m,n))
    else:
        print("Invalid operator")    
