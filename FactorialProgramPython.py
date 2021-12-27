def fact(value):
    sum=1
    for i in range(value,0,-1):
        sum=sum*i
    return sum

def main():
    no=0
    no=int(input("Enter the values"))
    
    ret=fact(no)
    print(ret)

if __name__=="__main__":
    main()
