import csv
import datetime

file = "main.csv"

fields = ['Name', 'Number', 'Email', 'DOB', 'Address']
file = "main.csv"

df = open(file, 'r')
df1 = csv.reader(df)

if not df1:
    with open(file, 'w+') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerow(fields)


def create():
    nrec = []
    f = open("main.csv", 'r', newline='\n')
    r = csv.reader(f)
    for rec in r:
        nrec.append(rec)
    cont = []
    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")
    email = input("Enter email: ")
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    dob = datetime.date(year, month, day)
    address = input("Enter Address: ")
    cont.append(name)
    cont.append(number)
    cont.append(email)
    cont.append(dob)
    cont.append(address)
    print("\nContact is created successfully!")
    with open(file, "w+", newline='') as data:
        w = csv.writer(data)
        if nrec:
            w.writerows(nrec)
        w.writerow(cont)
        f.close()
        data.close()


def search():
    print(
       '''
       1. Search through name
       2. Search through number
       3. Search through email
       4. Exit
       '''
    )
    ch = int(input("Enter choice: "))
    name = ""
    number = ""
    email = ""
    if ch == 1:
        name = input("Enter name: ").lower()
    elif ch == 2:
        number = input("Enter number: ")
    elif ch == 3:
        email = input("Enter email address: ")
    else:
        return
    f = open(file, 'r', newline='\n')
    r = csv.reader(f)
    result = []
    if name:
        print("Search result for " + name + ": ")
        for rec in r:
            sea = rec[0].lower()
            if sea.find(name, 0, len(sea)) != -1:
                result.append(rec)
    if number:
        print("Search result for " + number + ": ")
        for rec in r:
            if rec[1].find(number, 0, len(rec[1])) != -1:
                result.append(rec)

    if email:
        print("Search result for " + email + ": ")
        for rec in r:
            if rec[2].find(email, 0, len(rec[2])) != -1:
                result.append(rec)
    if result:
        print(result)
    else:
        print("No contacts found.. !.")
    f.close()


def delete(name = "", number="", email=""):
    nrec = []
    result = []
    f = open("main.csv", 'r', newline='\n')
    r = csv.reader(f)
    if name:
        for rec in r:
            sea = rec[0].lower()
            if sea.find(name, 0, len(sea)) != -1:
                result.append(rec)
    if number:
         for rec in r:
            if rec[1].find(number, 0, len(rec[1])) != -1:
                result.append(rec)
    
    if email:
         for rec in r:
            if rec[2].find(email, 0, len(rec[2])) != -1:
                result.append(rec)
    
    f.close()
    if not result:
        print("No contact found !")
        return   
    if len(result) == 1:
        print("Are you sure! You want to delete " + result[0][0] +" (y/n): ")
        ch = input().lower()
        if(ch != 'y'):
            return  
        fil = open(file, 'r', newline='\n')
        rea = csv.reader(fil)
        for rec in rea:
#             print(rec)
            if rec[0] == result[0][0]:
                continue;
            nrec.append(rec)
        print(nrec)
        fil.close()   
        with open(file, "w+", newline='') as data:
            w = csv.writer(data)
            w.writerows(nrec)
            data.close()
    else:
        print("More than 1 contact found, which one you want to delete ?")
        print(result)
        n = input("Enter name: ")
        delete(name=n)


def delete_contact():
    print(
       '''
       1. Delete through name
       2. Delete through number
       3. Delete through email
       4. Exit
       '''
    )
    ch = int(input("Enter choice: "))
    if ch == 1:
        name = input("Enter name: ").lower()
        delete(name=name)
    elif ch == 2:
        number = input("Enter number: ")
        delete(number=number)
    elif ch == 3:
        email = input("Enter email address: ")
        delete(email=email)

def update(name = "", number=""):
    nrec = []
    result = []
    f = open("main.csv", 'r', newline='\n')
    r = csv.reader(f)
    if name:
        for rec in r:
            sea = rec[0].lower()
            if sea.find(name, 0, len(sea)) != -1:
                result.append(rec)
    if number:
         for rec in r:
            if rec[1].find(number, 0, len(rec[1])) != -1:
                result.append(rec)
    
    f.close()
    if not result:
        print("No contact found !")
        return   
    if len(result) == 1:
        print("Are you sure! You want to update " + result[0][0] +" (y/n): ")
        ch = input().lower()
        if(ch != 'y'):
            return
        fil = open(file, 'r', newline='\n')
        rea = csv.reader(fil)
        for rec in rea:
#             print(rec)
            if rec[0] == result[0][0]:
                print("Do you want to update name:(y/n) " + rec[0] )
                inp = input().lower()
                if(inp == 'y'):
                    rec[0] = input("Enter correct name: ")
                print("Do you want to update number:(y/n) " + rec[1] )
                inp = input().lower()
                if(inp == 'y'):
                    rec[1] = input("Enter correct number: ")
                print("Do you want to update email:(y/n) " + rec[2] )
                inp = input().lower()
                if(inp == 'y'):
                    rec[2] = input("Enter correct email")
                print("Do you want to update DOB:(y/n) " + rec[3] )
                inp = input().lower()
                if(inp == 'y'):
                    date_entry = input('Enter a date in YYYY-MM-DD format: ')
                    year, month, day = map(int, date_entry.split('-'))
                    rec[3] = datetime.date(year, month, day)
                print("Do you want to update address:(y/n) " + rec[4] )
                inp = input().lower()
                if(inp == 'y'):
                    rec[4] = input("Enter correct address")
            nrec.append(rec)
        print(nrec)
        fil.close()   
        with open(file, "w+", newline='') as data:
            w = csv.writer(data)
            w.writerows(nrec)
            data.close()
    else:
        print("More than 1 contact found, which one you want to delete ?")
        print(result)
        n = input("Enter name: ")
        update(name=n)


def update_contact():
    print(
       '''
       1. Update through name
       2. Update through number
       3. Exit
       '''
    )
    ch = int(input("Enter choice: "))
    if ch == 1:
        name = input("Enter name: ").lower()
        update(name=name)
    elif ch == 2:
        number = input("Enter number: ")
        update(number=number)


def show():
    f = open(file, 'r', newline='\n')
    r = csv.reader(f)
    c=0
    for rec in r:
        c+=1
        print(rec)
    if c==1:
        print("\nNo contacts listed")



menu = '''
         CONTACT BOOK
         
          1.Create
          2.Update
          3.Show Contacts
          4.Search
          5.Delete
          6.Exit
'''


if __name__ == "__main__":
    a = True
    while a:
        print('\n', menu, '\n')
        choice = int(input('\nEnter your Choice: '))
        if choice == 1:
            create()
        elif choice == 2:
            update_contact()
        elif choice == 3:
            show()
        elif choice == 4:
            search()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            a = False
        else:
            break
            
        