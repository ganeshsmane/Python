class arithmatic:
  def __init__(self,a,b):
    self.No1=a
    self.No2=b
    c=0
  def addition(self):
    c=self.No1+self.No2
    return c

def main():
  obj=arithmatic(10,20)
  ret=obj.addition()
  print("Addition is: ",ret)

if __name__=="__main__":
  main()
