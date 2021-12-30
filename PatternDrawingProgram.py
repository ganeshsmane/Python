 
def fun(value):
    j=0;
    i=0;
    for i in range(value):
     
        for j in range(value):
            print("*",end=' ')
        print()

def main():
    no=int(input("Enter the number"))
    
    ret=fun(no)
   
    

if __name__=="__main__":
    main()
