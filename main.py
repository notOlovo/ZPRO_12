from models import ReservationBook

def validate_date(date_text):
    try:
        parts = date_text.split('.')
        if len(parts) != 3:
            return False
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        if 1 <= day <= 31 and 1 <= month <= 12 and 2000 <= year <= 2100:
            return True
        return False
    except ValueError:
        return False

def validate_time(time_text):
    try:
        if ":" not in time_text:
            return False
        parts = time_text.split(':')
        if len(parts) != 2:
            return False
        hour, minute = int(parts[0]), int(parts[1])
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            return True
        return False
    except ValueError:
        return False

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
                if not num: 
                    print("Error: Room number cannot be empty.")
                    continue
                build = input("Building: ")
                cap_str = input("Capacity: ")
                if not cap_str.isdigit():
                    print("Error: Capacity must be a number!")
                    continue
                cap = int(cap_str)
                eq = input("Equipment (comma separated): ").split(",")
                eq = [item.strip() for item in eq if item.strip()] 
                my_book.add_classroom(num, build, cap, eq)

            elif choice == "2":
                num = input("Room Number: ")
                name = input("Your Name: ")
                purp = input("Purpose: ")
                while True:
                    date = input("Date (DD.MM.YYYY): ")
                    if validate_date(date):
                        break
                    print("Invalid date format! Please use DD.MM.YYYY (e.g. 20.01.2024)")
                while True:
                    start = input("Start Time (HH:MM): ")
                    if validate_time(start):
                        break
                    print("Invalid time format! Please use HH:MM (e.g. 09:00)")
                while True:
                    end = input("End Time (HH:MM): ")
                    if validate_time(end):
                        break
                    print("Invalid time format! Please use HH:MM")
                my_book.add_reservation(num, name, purp, date, start, end)

            elif choice == "3":
                my_book.print_classrooms()

            elif choice == "4":
                my_book.print_reservations()

            elif choice == "5":
                num = input("Room Number: ")
                date = input("Date (DD.MM.YYYY): ")
                start = input("Start Time (HH:MM): ")
                my_book.delete_reservation(num, date, start)

            elif choice == "6":
                fname = input("Filename (e.g. data.json): ")
                if not fname.endswith(".json"):
                    fname += ".json"
                my_book.save_to_file(fname)

            elif choice == "7":
                fname = input("Filename (e.g. data.json): ")
                my_book.load_from_file(fname)
            
            elif choice == "8":
                my_book.delete_all_reservations()
            elif choice == "9":
                confirm = input("Are you sure? (yes/no): ")
                if confirm.lower() == "yes":
                    my_book.delete_book()

            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()