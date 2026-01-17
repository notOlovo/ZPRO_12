from models import ReservationBook 

def main():
    my_book = ReservationBook()

    while True:
        print("\n=== CLASSROOM SYSTEM ===")
        print("1. Add Classroom")
        print("2. Add Reservation")
        print("3. Show Classrooms")
        print("4. Show Reservations")
        print("5. Delete Reservation")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Delete ALL Reservations")
        print("9. Delete Book (Reset All)")
        print("0. Exit")

        choice = input("Select option: ")

        try:
            if choice == "1":
                num = input("Room Number: ")
                build = input("Building: ")
                cap = int(input("Capacity: "))
                eq = input("Equipment (comma separated): ").split(",")
                my_book.add_classroom(num, build, cap, eq)

            elif choice == "2":
                num = input("Room Number: ")
                name = input("Your Name: ")
                purp = input("Purpose: ")
                date = input("Date (DD.MM.YYYY): ")
                start = input("Start Time (HH:MM): ")
                end = input("End Time (HH:MM): ")
                my_book.add_reservation(num, name, purp, date, start, end)

            elif choice == "3":
                my_book.print_classrooms()

            elif choice == "4":
                my_book.print_reservations()

            elif choice == "5":
                num = input("Room Number: ")
                date = input("Date: ")
                start = input("Start Time: ")
                my_book.delete_reservation(num, date, start)

            elif choice == "6":
                fname = input("Filename (e.g. data.json): ")
                my_book.save_to_file(fname)

            elif choice == "7":
                fname = input("Filename (e.g. data.json): ")
                my_book.load_from_file(fname)
            
            elif choice == "8":
                my_book.delete_all_reservations()

            elif choice == "9":
                confirm = input("Are you sure? (yes/no): ")
                if confirm == "yes":
                    my_book.delete_book()

            elif choice == "0":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice, try again.")
        
        except ValueError:
            print("Input Error: Please enter numbers where required (like Capacity).")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()