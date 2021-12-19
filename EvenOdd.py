#Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.
#Input : 11 Output : Odd Number
#Input : 8 Output : Even Number

def ChkNum(value):
    if (value%2==0):
        print("Given number is Even Number ")
    else:
        print("Given number is Odd Number ")
    

def main():
    no=int(input("Enter the number : ")) 
    ChkNum(no)

if __name__=="__main__":
    main()