pupils = [{ "id": 1001,
            "name": "John",
            "surname": "Doe",
            "fathers_name": "Michael",
            "age": 15,
            "class": 1,
            "id_number": "AN123949"},
          { "id": 1002,
            "name": "Mary",
            "surname": "Poppins",
            "fathers_name": "Chris",
            "age": 10,
            "class": 3,
            "id_number": "AE123981"},
          { "id": 1003,
            "name": "John",
            "surname": "Wick",
            "fathers_name": "Chiwetel",
            "age": 7,
            "class": 6,
            "id_number": "AN456589"}]

def pupil_update(pupil):
    print_pupil(pupil)
    print("=" * 15)
    print("1- Name")
    print("2- Surname")
    print("3- Father's name")
    print("4- Age")
    print("5- Class")
    print("6- ID number")
    print("=" * 15)
    update_choice = int(input(print("Pick one to update: ")))
    if update_choice == 1:
        pupil["name"] = input("Give new name: ")
    elif update_choice == 2:
        pupil["surname"] = input("Give new surname: ")
    elif update_choice == 3:
        pupil["fathers_name"] = input("Give new father's name: ")
    elif update_choice == 4:
        pupil["age"] = input("Give new age: ")
    elif update_choice == 5:
        pupil["class"] = input("Give new class: ")
    elif update_choice == 6:
        pupil["id_number"] = input("Give new ID number: ")
    print("=" * 15)
    print_pupil(pupil)
    print("Pupil UPDATED !")
   
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

def search_pupil_by_surname(surname):
    match_pupils = []
    for pupil in pupils:
        if surname == pupil["surname"]:
            match_pupils.append(pupil)
    return match_pupils

def print_pupils_details():
    for pupil in pupils:
        print("=" * 15)
        print_pupil(pupil)
        
def print_pupils_names():
    for pupil in pupils:
        print(f"{pupil['name']} {pupil['fathers_name'][0]}. {pupil['surname']}")

def delete_pupil_by_id(pupil):
    if pupil in pupils:
        pupils.remove(pupil)
        print("\nDelete successful !")
        return
