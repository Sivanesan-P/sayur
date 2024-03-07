parking=[]
id=0
rows=0
colm=0
entryTime=0.0
exitTime=0.0
hour=0.0
amt=0.0

def initialize(rows,colm):
    global parking
    parking=[[0 for i in range(0,rows)] for j in range(0,colm)]

def enterParking(id):
    global parking
    global entryTime
    for i in range(0,rows):
        for j in range(0,colm):
             if parking[i][j]==id:
                 print("id is already given")
                 return
             if parking[i][j]==0:
                parking[i][j]=id 
                entryTime=input("enter the entry timing:")                                                                                             
                print("your parking space : ",i,":",j)
                print("your parking id : ", id)
                return
    
def leaveParking(id):
    global parking
    for i in range(0,rows):
        for j in range(0,colm):
            if  parking[i][j]==id:
                parking[i][j]=0
                print(parking)
                return

def display():
    print(parking)

def TollCollection(id):
    global exitTime
    global hour
    exitTime=input("Enter the exit time: ")
    hour=float(input("Enter the total hours: "))

def bill(id):

    if hour<1:
        amt=5
    elif hour>=1 and hour<2:
        amt=10
    elif hour>=2 and hour<3:
        amt=15
    else:
        amt=25
    print("------------------------------------------------")
    print("you have entered at: ",entryTime)
    print("you had leave at: ",exitTime)
    print("----------------------BILL----------------------")
    print("   id                 HOURS                TOTAL")
    print("   ",id,end="")
    print("                 ",hour,end="")
    print("                  ",amt)

    
def main():
    global parking
    global rows
    global colm
    while True:
        print("--------------------------------------------")
        print("1.initialize")
        print("2.Enter parking")
        print("3.leave parking")
        print("4.Display parking spot")
        print("5.TollCollection")
        print("6.Bill")
        print("7.Exit")
        c=int(input("Entre your choice : "))
        print("-----------------------------------")
        if c==1:
            rows=int(input("Enter row: "))
            colm=int(input("Enter column: "))
            initialize(rows,colm)
        elif c==2:
            id=int(input("Enter id for vehical :"))
            enterParking(id)
        elif c==3:
            id=int(input("Enter the id of parked vehical: "))
            leaveParking(id)
        elif c==4:
            display()
        elif c==5:
            id=input("Enter the id: ")
            TollCollection(id)
        elif c==6:
            id=input("Enter the id: ")
            bill(id)
        else:
            return

main()