# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
#Input : 11 5 Output : 16

def Add(value1,value2):
    result=value1+value2
    return result

def Sub(value1,value2):
    result=value1-value2
    return result

def Sub(value1,value2):
    result=value1-value2
    return result
    
def Mult(value1,value2):
   result=value1*value2
   return result

def Div(value1,value2):
   result=value1/value2
   return result


def main():
    no1=int(input("Enter first number : "))
    no2=int(input("Enter second number : "))
    
    ret=Add(no1,no2)
    print("Addition is : ", ret)
    
    ret=Sub(no1,no2)
    print("Substration is : ", ret)
    
    ret=Mult(no1,no2)
    print("Multiplication is : ", ret)

    ret=Div(no1,no2)
    print("Division is : ", ret)

if __name__=="__main__":
    main()