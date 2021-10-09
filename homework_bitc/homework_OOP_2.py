class Person:
    def __init__(self, name, surname, age, gender, email, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.email = email
        self.add_address = address

    def present(self):
        return f"Hi, I am {self.name} {self.surname}, I am {self.age}-years-old!"

    def change_email(self, email):
        self.email = email

    def change_address(self, address):
        self.add_address = address


class Student(Person):
    def __init__(self, name, surname, age, gender, email, address, university):
        super().__init__(name, surname, age, gender, email, address)
        self.university = university


class Country:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

    def present(self):
        return f"The name: {self.name}, the continent: {self.continent}"


class Brand:
    def __init__(self, name, business_start_date):
        self.name = name
        self.business_start_date = business_start_date

    def present(self):
        return f"The name: {self.name}, the business start date: {self.business_start_date}"


class Season:
    def __init__(self, name, average_temperature):
        self.name = name
        self.average_temperature = average_temperature

    def present(self):
        return f"The name: {self.name}, the average temperature: {self.average_temperature}"


class Product(Country, Brand, Season):
    def __init__(self, name, type_, price, quantity):
        self.name = name
        self.type_ = type_
        self.price = price
        self.quantity = quantity

    def present(self):
        return f"The name of the product is: {self.name}, the type: {self.type}, the price: ${self.price} and quantity: {self.quantity}"

    def discount(self, percent):
        return self.price * (1 - percent / 100)

    def increase_quantity(self, new_quantity):
        self.quantity += new_quantity

    def decrease_quantity(self, new_quantity):
        self.quantity -= new_quantity


class Hotel:
    def __init__(self, hotel_name, place, mid_rooms_number, mid_room_price, lux_rooms_number, lux_room_price):
        self.hotel_name = hotel_name
        self.place = place
        self.rooms_mid = {"room" + str(i): "free" for i in range(1, mid_rooms_number + 1)}
        self.mid_room_price = mid_room_price
        self.rooms_lux = {"room" + str(i): "free" for i in range(1, lux_rooms_number + 1)}
        self.lux_room_price = lux_room_price

    def presentation(self):
        return f"The {self.hotel_name} is located in {self.place}. It has {len(self.rooms_mid)} middle room with ${self.mid_room_price} " \
               f"each and {len(self.rooms_lux)} lux rooms with ${self.lux_room_price} each."

    def book_mid_room(self, room_number):
        self.rooms_mid[room_number] = "busy"

    def book_lux_room(self, room_number):
        self.rooms_lux[room_number] = "busy"

    def available_mid_room_check(self):
        if "free" in self.rooms_mid.values():
            return True
        else:
            return False

    def available_lux_room_check(self):
        if "free" in self.rooms_lux.values():
            return True
        else:
            return False

    def discount_mid(self, percent):
        return self.mid_room_price * (1 - percent / 100)

    def discount_lux(self, percent):
        return self.lux_room_price * (1 - percent / 100)


class Taxi:
    def __init__(self, taxi_name, car_types, price_for_tour):
        self.taxi_name = taxi_name
        self.car_types = car_types
        self.price_for_tour = price_for_tour

    def presentation(self):
        return f"The {self.taxi_name} has {self.car_types} type of cars and the price for tour is ${self.price_for_tour}."

    def discount(self, percent):
        return self.price_for_tour * (1 - percent / 100)


class Tour(Hotel, Taxi):
    def __init__(self, hotel_name, place, mid_rooms_number, mid_room_price, lux_rooms_number, lux_room_price,
                 taxi_name, car_types, price_for_tour, tour_name):
        Hotel.__init__(self, hotel_name, place, mid_rooms_number, mid_room_price, lux_rooms_number, lux_room_price)
        Taxi.__init__(self, taxi_name, car_types, price_for_tour)
        self.tour_name = tour_name
        self.price_lux = mid_room_price + price_for_tour
        self.price_mid = lux_room_price + price_for_tour

    def presentation(self):
        return f"Hello, we offer {self.tour_name} ! We have two options {self.price_mid} and {self.price_lux} " \
               f"which includes transport with {self.taxi_name} company which provides {self.car_types} cars and price" \
               f"for it is {self.price_for_tour}. We will stay at {self.hotel_name} which offers two types of rooms middle" \
               f" ${self.mid_room_price} and lux {self.lux_room_price} "


