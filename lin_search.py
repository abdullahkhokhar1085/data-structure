4554

class LinearSearchDemo:
    n = 0
    Data = []
    size = 0

    def __init__(self,size):
        self.size = size

    def LinearSearch(self,t):
        tt = 0
        for j in range(self.n):
            if((t== self.Data[j])):
                tt=1
                break
        if(tt==1):
            return (j+1)
        else:
            return 0   
    
#Class definition ends

ls = LinearSearchDemo(100) #Object is created
t = 0 
#I/O operations to take data from user

print("Welcome to the NUV\n")
ls.n = int(input("Enter How many elements do you want to enter? : "))
if(ls.n > ls.size):
    print("Array size is not supporting")
else:
    for i in range(ls.n):
        t = int(input("Enter Value : "))
        ls.Data.append(t)

print("Values available in the Array")
      

t = int(input("Enter Value to find : "))

#Function Call

isAvailable = ls.LinearSearch(t)

#Checking return value

if(isAvailable == 0):
    print("Entered Value is not available in the given Array")
else:
    print("Entered Value is available on ", isAvailable ," Position")