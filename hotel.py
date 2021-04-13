class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.name} {self.last_name}'


class Room:

    def __init__(self, room_number):
        self.room_number = room_number
        self.guest = None

    def __repr__(self):
        return f'Room {self.room_number}'


class Floor:

    def __init__(self, floor):
        self.rooms = []
        self.floor = floor

    def __repr__(self):
        return f'Floor {self.floor}: {self.rooms}'

    def __iter__(self):
        yield from self.rooms


class Hotel:

    def __new__(cls, floor_number, rooms_number):
        if floor_number > rooms_number:
            raise Exception("Not enough rooms for that much floors!")
        return super(Hotel, cls).__new__(cls)

    def __init__(self, floor_number, rooms_number):
        self.floor_number = floor_number
        self.rooms_number = rooms_number
        self.building = []
        self.placeholder_counter = 0
        self.room_dict = {}
        self.number_of_free_rooms = 0

    def change_placeholder(self, building_list, rooms_list):
        for index, item in enumerate(building_list):
            if isinstance(item, Floor):
                self.change_placeholder(item, rooms_list)
            elif item.startswith('N'):
                building_list.rooms[index] = rooms_list[self.placeholder_counter]
                self.placeholder_counter += 1
        return building_list

    def create_floors(self):
        for i in range(self.floor_number):
            self.building.append(Floor(i))

    def create_hotel(self):
        i = 0
        ok = True
        rooms_list = []
        while ok:
            for floor in self.building:
                while i != self.rooms_number:
                    floor.rooms.append('None')
                    i += 1
                    break
                continue
            if i == self.rooms_number:
                ok = False
        for number in range(1, self.rooms_number + 1):
            rooms_list.append(Room(number))

        self.change_placeholder(self.building, rooms_list)
        print(f'Hotel created, here is plan of the building:\n{self.building}')
        return True

    def move_in(self, floor_number, room, guest):
        try:
            if floor_number == self.building[floor_number].floor:
                rooms_on_floor = self.building[floor_number].rooms
                for r in rooms_on_floor:
                    if r.room_number == room:
                        r.guest = guest
                        print(f'Guest {guest} is moved in to room number {room}, on floor number {floor_number}')
                        return True
                print("Incorrect room number!")
                return False

        except IndexError:
            print('Incorrect floor number!')
            return False

    def generate_map_of_free_rooms(self, building_list):
        for index, item in enumerate(building_list):
            if isinstance(item, Floor):
                self.generate_map_of_free_rooms(item)
            elif item.guest is None:
                self.room_dict[f'Room number {item.room_number}'] = 'Free'
            elif isinstance(item.guest, Person):
                self.room_dict[f'Room number {item.room_number}'] = 'Taken'
        return True

    def show_free_rooms(self):
        self.generate_map_of_free_rooms(self.building)
        for v in self.room_dict.values():
            if v == 'Free':
                self.number_of_free_rooms += 1
        print(f'There is {self.number_of_free_rooms} free rooms, here is plan o free rooms:\n{self.room_dict}')
        return True


if __name__ == '__main__':
    # Tworzenie gościa
    g = Person('Kamil', 'Cieszkowski')

    # Generowanie Hotelu
    h = Hotel(5, 17)
    h.create_floors()
    h.create_hotel()

    # Generowanie hotelu z wywołaniem błędu
    # h = Hotel(10,2)

    # Zameldowanie Gościa na piętro 2 do pokoju 11
    h.move_in(2, 11, g)

    # Pokazanie wolnych pokoi
    h.show_free_rooms()

