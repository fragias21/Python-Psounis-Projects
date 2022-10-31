from mod_pupils import *
from mod_teachers import *

def main():
    print("\n=================")
    print("     MENU ")
    print("1 - Create Pupil")
    print("2 - Print")
    print("3 - Update Pupil")
    print("4 - Delete Pupil")
    print("5 - Create Teacher")
    print("6 - Read Teacher")
    print("7 - Update Teacher")
    print("8 - Delete Teacher")
    print("9 - Exit")
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

def menu_3():
    print("\n=================")
    print("     UPDATE ")
    print("1 - Update Pupil (search by ID)")
    print("2 - Update Pupil (search by surname)")
    print("3 - Return to Main Menu")
    x = int(input("Pick one: "))
    return x

def menu_4():
    print("\n=================")
    print("     DELETE ")
    print("1 - Delete Pupil (by ID)")
    print("2 - Delete Pupil (by surname)")
    print("3 - Return to Main Menu")
    x = int(input("Pick one: "))
    return x

while True:
    choice = main()
    while choice not in range (1,10):
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
        choice_3 = menu_3
        while choice_3 not in range (1,4):
            choice_3 = menu_3()
        if choice_3 == 1:
            pupil_id = int(input("Give pupil's ID: "))
            pupil = search_pupil_by_id(pupil_id)
            if pupil is None:
                print("ERROR ! There is no pupil with this id!")
                continue
            else:
                pupil_update(pupil)
        elif choice_3==2:
            surname = input("Give surname: ")
            matching_pupils = search_pupil_by_surname(surname)
            if matching_pupils == []:
                print("No matching pupils with this surname!")
                continue
            elif len(matching_pupils) == 1:
                pupil = matching_pupils[0]
            else:
                for p in matching_pupils:
                    print_pupil(p)
                    print(f"ID = {p['id']}")
                    print("-" * 15)
                pupil_id = int(input("Give ID: "))  
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("ERROR ! There is no pupil with this id!")
                    continue
                else:
                    pupil_update(pupil)
        elif choice_3==3:
            continue
    elif choice==4:
        choice_4 = menu_4
        while choice_4 not in range (1,4):
            choice_4 = menu_4()
        if choice_4 == 1:
            pupil_id = int(input("Give pupil's ID: "))
            pupil = search_pupil_by_id(pupil_id)
            if pupil is None:
                print("ERROR ! There is no pupil with this id!")
                continue
            else:
                delete_pupil_by_id(pupil)
        elif choice_4==2:
            surname = input("Give surname: ")
            matching_pupils = search_pupil_by_surname(surname)
            if matching_pupils == []:
                print("No matching pupils with this surname!")
                continue
            elif len(matching_pupils) == 1:
                pupil = matching_pupils[0]
                delete_pupil_by_id(pupil)
            else:
                for p in matching_pupils:
                    print_pupil(p)
                    print(f"ID = {p['id']}")
                    print("-" * 15)
                pupil_id = int(input("Give ID: "))  
                pupil = search_pupil_by_id(pupil_id)
                if pupil is None:
                    print("ERROR ! There is no pupil with this id!")
                    continue
                else:
                    delete_pupil_by_id(pupil)
        elif choice_4==3:
            continue
    elif choice==5:
        print("   New Teacher's info")
        print_teacher(create_teacher(teachers)) 
        print("Next avalaible ID: " + str(next_id(teachers))) 
    elif choice==6:
        teacher_id = int(input("Give teacher's ID: "))
        teacher = search_teacher_by_id(teacher_id)
        if teacher is None:
            print("Teacher does not exist (with this id)")
        else:
            print("        TEACHER")
            print_teacher(teacher)
    elif choice==7:
        teacher_id = int(input("Give teacher's ID: "))
        teacher = search_teacher_by_id(teacher_id)
        if teacher is None:
            print("ERROR ! There is no teacher with this id!")
            continue
        else:
            teacher_update(teacher)
    elif choice==8:
        teacher_id = int(input("Give teacher's ID: "))
        teacher = search_teacher_by_id(teacher_id)
        if teacher is None:
            print("ERROR ! There is no teacher with this id!")
            continue
        else:
            delete_teacher_by_id(teacher)
    elif choice==9:
        print("\nBye bye!\n")
        break
