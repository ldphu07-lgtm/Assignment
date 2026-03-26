class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

test_car = Car("TEST-1", 200)
test_car.travelled_distance = 2000
test_car.current_speed = 60
test_car.drive(1.5)

print(f"Quãng đường mới sau khi đi 1.5h: {test_car.travelled_distance} km")