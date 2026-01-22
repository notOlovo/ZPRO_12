import json

class Classroom:
    def __init__(self, room_number, building, capacity, equipment):
        self.room_number = room_number
        self.building = building
        self.capacity = capacity
        self.equipment = equipment

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "building": self.building,
            "capacity": self.capacity,
            "equipment": self.equipment
        }

class Reservation:
    def __init__(self, room_number, name_person, purpose, date, start_time, end_time):
        self.room_number = room_number
        self.name_person = name_person
        self.purpose = purpose
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "name_person": self.name_person,
            "purpose": self.purpose,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

class ReservationBook:
    def __init__(self):
        self.classrooms = []
        self.reservations = []

    def add_classroom(self, room_number, building, capacity, equipment):
        if self.find_room(room_number):
             print(f"Error: Classroom {room_number} already exists.")
             return
        new_room = Classroom(room_number, building, capacity, equipment)
        self.classrooms.append(new_room)
        print(f"Classroom {room_number} added.")

    def add_reservation(self, room_number, name_person, purpose, date, start_time, end_time):
        if not self.find_room(room_number):
            print(f"Error: Room {room_number} does not exist! Create it first.")
            return
        if start_time >= end_time:
            print("Error: Start time must be before end time!")
            return
        if self.check_conflict(room_number, date, start_time, end_time):
            print(f"Error: Room {room_number} is ALREADY RESERVED at this time interval!")
            return
        new_reservation = Reservation(room_number, name_person, purpose, date, start_time, end_time)
        self.reservations.append(new_reservation)
        print(f"Success: Reservation for {name_person} added.")

    def check_conflict(self, room_number, date, start_time, end_time):
        for res in self.reservations:
            if res.room_number == room_number and res.date == date:
                if start_time < res.end_time and end_time > res.start_time:
                    return True
        return False
    
    def find_room(self, room_number):
        for room in self.classrooms:
            if room.room_number == room_number:
                return True
        return False

    def print_reservations(self):
        print("\n--- All Reservations ---")
        if not self.reservations:
            print("No reservations yet.")
        for res in self.reservations:
            print(f"Room: {res.room_number} | Date: {res.date} | Time: {res.start_time}-{res.end_time} | For: {res.name_person}")
        print("------------------------\n")

    def print_classrooms(self):
        print("\n--- Classrooms ---")
        if not self.classrooms:
            print("No classrooms yet.")
        for room in self.classrooms:
            print(f"Room {room.room_number} ({room.building}) - Capacity: {room.capacity}")
        print("------------------\n")

    def delete_reservation(self, room_number, date, start_time):
        for res in self.reservations:
            if res.room_number == room_number and res.date == date and res.start_time == start_time:
                self.reservations.remove(res)
                print(f"Reservation for room {room_number} deleted.")
                return
        print("Error: Reservation to delete not found.")

    def delete_all_reservations(self):
        self.reservations = []
        print("All reservations deleted.")

    def delete_book(self):
        self.classrooms = []
        self.reservations = []
        print("Reservation book deleted completely.")

    def save_to_file(self, filename):
        data = {
            "classrooms": [c.to_dict() for c in self.classrooms],
            "reservations": [r.to_dict() for r in self.reservations]
        }
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.classrooms = []
            self.reservations = []
            for c in data["classrooms"]:
                self.classrooms.append(Classroom(c["room_number"], c["building"], c["capacity"], c["equipment"]))
            for r in data["reservations"]:
                self.reservations.append(Reservation(r["room_number"], r["name_person"], r["purpose"], r["date"], r["start_time"], r["end_time"]))
            print(f"Loaded from {filename}. Total rooms: {len(self.classrooms)}, Total reservations: {len(self.reservations)}")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error loading file: {e}")