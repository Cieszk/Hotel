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
        rooms_on_floor = self.building[floor_number].rooms
        for r in rooms_on_floor:
            if r.room_number == room:
                r.guest = guest
        print(f'Guest {guest} is moved in to room number {room}, on floor number {floor_number}')

if __name__ == '__main__':
    g = Person('Kamil', 'Cieszkowski')
    h = Hotel(5, 17)
    h.create_floors()
    h.create_hotel()
    h.move_in(2, 9, g)
    print(h.building[2].rooms[0].guest)
