pupils = [
    {
        "id": 1001,
        "name": "John",
        "surname": "Doe",
        "fathers_name": "Michael",
        "age": 15,
        "class": 1,
        "id_number": "AN123949"
    },
    {   
        "id": 1002,
        "name": "Mary",
        "surname": "Poppins",
        "fathers_name": "Chris",
        "age": 10,
        "class": 3,
        "id_number": "AE123981"
    },
    {
        "id": 1003,
        "name": "John",
        "surname": "Wick",
        "fathers_name": "Chiwetel",
        "age": 7,
        "class": 6,
        "id_number": "AN456589"
    }
        ]

def main():
    print("\n=================")
    print("     MENU ")
    print("1 - Create Pupil")
    print("2 - Print")
    print("3 - Update Pupil")
    print("4 - Delete Pupil")
    print("5 - Exit")
    x = int(input("Pick one: "))
    return x

def menu_2():
    print("\n=================")
    print("     PRINT ")
    print("1 - Print Pupil")
    print("2 - Print all pupils (details)")
    print("3 - Print all pupils (only names)")
    print("4 - Return to Main Menu")
    x = int(input("Pick one: "))
    return x
    
def create_pupil(pupils):
    print("\n      NEW PUPIL")
    print("=======================")
    name = input("Give name: ")
    surname = input("Give surname: ")
    fathers_name = input("Give father's name: ")
    
    for p in pupils:
        if name==p["name"] and surname==p["surname"] and fathers_name==p["fathers_name"]:
            print("This pupil already exist.")
            ch = input("Do you want to continue? (y-yes, n-no): ")
            if ch=="n":
                break
        else:
            age = int(input("Give age: "))
            pupil_class = int(input("Give class: "))
            id_card = input("Does he/she has an id card: (y-true, n-false): ")
            if id_card=="y":
                id_number = input("Give id card number: ")
            else: 
                id_number = 0
            break
    
    pupil = {}
    pupil["name"]=name
    pupil["surname"]=surname
    pupil["fathers_name"]=fathers_name
    pupil["age"]=age
    pupil["class"]=pupil_class
    pupil["id_number"]=id_number
        
    ids = []
    for p in pupils:
        ids.append(p["id"])
    pupil["id"] = max(ids) + 1
        
    pupils.append(pupil)
    return pupil

def next_id(pupils):
    ids = []
    for p in pupils:
        ids.append(p["id"])
    next_id = max(ids) + 1
    return next_id
    
def print_pupil(pupil):  
    print("=======================")
    print(f"ID: {pupil['id']}")
    print(f"Name: {pupil['name']}")
    print(f"Surname: {pupil['surname']}")
    print(f"Father's Name: {pupil['fathers_name']}")
    print(f"Age: {pupil['age']}")
    print(f"Class: {pupil['class']}")
    if pupil['id_number']!=0 :
        print(f"ID card number: {pupil['id_number']}")
    else:
        print(f"ID card number: - ")
        
def search_pupil_by_id(pupil_id):
    for pupil in pupils:
        if pupil_id == pupil["id"]:
            return pupil
    return None    

def print_pupils_details():
    for pupil in pupils:
        print("=" * 15)
        print_pupil(pupil)
        
def print_pupils_names():
    for pupil in pupils:
        print(f"{pupil['name']} {pupil['fathers_name'][0]}. {pupil['surname']}")

while True:
    choice = main()
    while choice not in range (1,6):
        choice = main()
    if choice==1:
        print("   New Pupil's info")
        print_pupil(create_pupil(pupils)) 
        print("Next avalaible ID: " + str(next_id(pupils))) 
    elif choice==2:
        choice_2 = menu_2()
        while choice_2 not in range (1,5):
            choice_2 = menu_2()
        if choice_2==1:
            pupil_id = int(input("Give pupil's ID: "))
            pupil = search_pupil_by_id(pupil_id)
            if pupil is None:
                print("Pupil does not exist (with this id)")
            else:
                print("        PUPIL")
                print_pupil(pupil)
        elif choice_2==2:
            print_pupils_details()
        elif choice_2==3:
            print_pupils_names()
        elif choice_2==4:
            continue
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("\nBye bye!")
        break
