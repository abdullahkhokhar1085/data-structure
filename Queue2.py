import sys
class StackDemo:
    top = 0
    stackData = []
    size = 0



    def __init__(self,size):

        self.size = size



    def isFull(self):

        if(self.top==self.size):

            return 0

        else:

            return 1

        

    def isEmpty(self):

        if(self.top==0):

            return 0

        else:

            return 1

        

    

    def push(self,x):

        t = self.isFull()

        

        if(t==0):

            print("Stack is Overflow")

        else:

            self.stackData.append(x)

            self.top = self.top + 1

            print("One Element is Pushed")

            print(self.top)

    

    def pop(self):

        t = self.isEmpty()

        

        if(t==0):

            print("Stack is Underflow")

        else:

            self.top = self.top - 1

            print("One Element is Poped")

            print(self.top)



    def peek(self):

        t = self.isEmpty()

        

        if(t==0):

            print("Stack is Underflow")

        else:

            print("One Element is Peeked",self.stackData[self.top-1])




    def display(self):

        if(self.top == 0):

            print("Stack is Underflow")

        else:

            for n in range(self.top):

                print("Element -> ",self.stackData[n]) 

            

    



stack1 = StackDemo(5)

choice = 0

print("Welcome to the NUV\n")

print("1: Push \n2: Pop \n3: Peek \n4: Display \n5: Exit")

while(5==5):

    choice = int(input("Enter Your Choice : "))

    if(choice==1):

        t = input("Enter Value : ")

        stack1.push(t)

    elif(choice==2):

        stack1.pop()

    elif(choice==3):

        stack1.peek()

    elif(choice==4):

        stack1.display()

    elif(choice==5):

        sys.exit() 

    else:

        print("Invalid Data")