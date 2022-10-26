teachers = [{   "id": 1001,
                "name": "Severus",
                "surname": "Snape"},
            {   "id": 1002,
                "name": "Charles",
                "surname": "Xavier"},
            {   "id": 1003,
                "name": "Sergio",
                "surname": "Marquina"}]

def create_teacher(teachers):
    print("\n   NEW TEACHER")
    print("=======================")
    name = input("Give name: ")
    surname = input("Give surname: ")
    for t in teachers:
        if name==t["name"] and surname==t["surname"]:
            print("This teacher already exist.")
            ch = input("Do you want to continue? (y-yes, n-no): ")
            if ch=="n":
                break       
    teacher = {}
    teacher["name"]=name
    teacher["surname"]=surname
    ids = []
    for t in teachers:
        ids.append(t["id"])
    teacher["id"] = max(ids) + 1
    teacher.append(teacher)
    return teacher

def print_teacher(teacher):  
    print("=======================")
    print(f"ID: {teacher['id']}")
    print(f"Name: {teacher['name']}")
    print(f"Surname: {teacher['surname']}")

def search_teacher_by_id(teacher_id):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            return teacher

def teacher_update(teacher):
    print_teacher(teacher)
    print("=" * 15)
    print("1- Name")
    print("2- Surname")
    print("=" * 15)
    update_choice = int(input(print("Pick one to update: ")))
    if update_choice == 1:
        teacher["name"] = input("Give new name: ")
    elif update_choice == 2:
        teacher["surname"] = input("Give new surname: ")
    print("=" * 15)
    print_teacher(teacher)
    print("Teacher UPDATED !")
    
def delete_teacher_by_id(teacher):
    if teacher in teachers:
        teachers.remove(teacher)
        print("\nDelete successful !")
        return

def read_teacher(teacher_id):
    for teacher in teachers:
        if teacher_id == teacher["id"]:
            return teacher

