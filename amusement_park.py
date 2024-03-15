from datetime import date,datetime



def main():
    global name
    name=input("Enter the name: ")
    dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
    age1(dob_str)
    

def age1(dob_str):
    global dob
    global age
    age=0
    dob=datetime.strptime(dob_str, "%Y-%m-%d")
    dat=date.today()
    age=dat.year-dob.year
    ticket(age)

def ticket(age):
    total=0
    if age<15 or age>60:
        total=50
    elif age>15 and age<60:
        total=75
    bill(total)

def bill(total):
    ticket_date=input("Enter the date for ticket to be booked(YYYY-MM-DD): ")
    day=datetime.strptime(ticket_date,"%Y-%m-%d")
    current_day_name = day.strftime('%A')
    if current_day_name=='Thursday' or current_day_name=='Tuesday':
        disc=total*20/100
        total-=disc
    print("your name: ",name)
    print("date of birth: ",dob)
    print("Age: ",age)
    print("you have booked on: ",ticket_date," , ",current_day_name)
    print("Total: ",total)

main()
