import datetime

def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise and 2 for food \n"))
        if (c==1):
            value=input("Type here\n")
            with open ("harryex.py","a")as ND:
                ND.write(str([gettime()])+":"+value+"\n")
            print("Successfully written")
        elif (c==2):
            value=(input("Type here \n"))
            with open ("harryfood.py","a")as ND:
                ND.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for food \n1"))
        if (c==1):
            value=input("Type here\n")
            with open ("rohanex.py","a")as ND:
                ND.write(str([gettime()])+":"+value+"\n")
            print("Successfully written")
        elif (c==2):
            value=(input("Type here \n"))
            with open ("rohanfood.py","a")as ND:
                ND.write(str([str(gettime())])+":"+value+"\n")
            print("Successfully written")
    elif k==3:
        c=int(input("Enter 1 for exercise and 2 for food \n"))
        if (c==3):
            value=input("Type here\n")
            with open ("hamadex.py","a")as ND:
                ND.write(str([gettime()])+":"+value+"\n")
            print("Successfully written")
        elif (c==2):
            value=(input("Type here \n"))
            with open ("hamadfood.py","a")as ND:
                ND.write(str([str(gettime())])+":"+value+"\n")
            print("Successfully written")
def retrieve(k):
    if k==1:
        c= int(input("Enter 1 for exercise and 2 for food \n"))
        if (c==1) :
            with open ("harryex.py") as ND:
                for i in ND:
                    print(i, end=" ")
        elif(c==2):
            with open ("harryfood.py") as ND:
                for i in ND:
                    print(i , end = " ")
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for food \n"))
        if (c==1):
            with open ("rohanex.py") as ND:
                for i in ND:
                    print( i , end=" ")     
        elif (c==2) :
            with open ("rohanfood.py") as ND:
                for i in ND:
                    print( i ,end=" ")  
    elif k==3:                     
        c=int(input("Enter 1 for exercise and 2 for food \n"))
        if (c==1):
            with open ("hamadex.py") as ND:
                for i in ND:
                    print( i , end=" ")     
        elif (c==2) :
            with open ("hamadfood.py") as ND:
                for i in ND:
                    print( i ,end=" ") 
    else:
        print("Enter a valid input")   

print("HEALTH MANAGEMENT SYSTEM")   
a=int(input("Press 1 for log and 2 to retrieve \n"))
if a==1:
    b= int(input("Press 1 for harry , 2 for rohan and 3 for hamad  \n"))
    take(b)
else :
    b=int(input("Press 1 for harry , 2 for rohan and 3 for hamad  \n"))
    retrieve(b)