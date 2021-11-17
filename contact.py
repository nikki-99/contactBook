import csv
import datetime

file = "main.csv"

fields = ['Name', 'Number', 'Email', 'DOB', 'Address']
file = "main.csv"

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
       3. Exit
       '''
    )
    ch = int(input("Enter choice: "))
    name = ""
    number = ""
    if ch == 1:
        name = input("Enter name: ").lower()
    elif ch == 2:
        number = input("Enter number: ")
    else:
        return
    
    f = open(file, 'r', newline='\n')
    r = csv.reader(f)
    result = []
    
    if name:
        print("search result for " + name + ": ")
        for rec in r:
            sea = rec[0].lower()
            if sea.find(name, 0, len(sea)) != -1:
                result.append(rec)
    if number:
        print("search result for " + number + ": ")
        for rec in r:
            if rec[1].find(number, 0, len(rec[1])) != -1:
                result.append(rec)
    if result:
        print(result)
    else:
        print("No contact found.. !.")
    f.close()

def delete(name = "", number=""):
    
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
        print("are you sure want to delete " + result[0][0] +" (y/n): ")
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
        print("more than 1 contact found, which one you want to delete ?")
        print(result)
        n = input("Enter name: ")
        delete(name=n)

def delete_contact():
    print(
       '''
       1. delete through name
       2. delete through number
       3. Exit
       '''
    )
    ch = int(input("Enter choice: "))
    if ch == 1:
        name = input("Enter name: ").lower()
        delete(name=name)
    elif ch == 2:
        number = input("Enter number: ")
        delete(number=number)

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
        print("are you sure want to update " + result[0][0] +" (y/n): ")
        ch = input().lower()
        if(ch != 'y'):
            return
        
        print("Enter name: ")
        nm = input()
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
        print("more than 1 contact found, which one you want to delete ?")
        print(result)
        n = input("Enter name: ")
        update(name=n)

def update_contact():
    print(
       '''
       1. update through name
       2. update through number
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
    l = len(list(r))
    if l==1:
        print("No contacts listed")
        return
    for rec in r:
        print(rec)

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
#     c = Contact()
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
            
        