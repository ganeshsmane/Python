#Write a program which accept one number for user and check whether number is prime or not.
#Input : 5 Output : It is Prime Number 

def div(a):
    for j in range(2, int(a/2) + 1):  
        if (a % j) == 0:  
            print(a, "is not a prime number")  
            break  
        # Else it is a prime number  
        else:  
            print(a, "is a prime number")  

def main():
    no=0
    no=int(input("Enter the number"))
    
    ret=div(no)
    #print(ret)

if __name__=="__main__":
    main()


