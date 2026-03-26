class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

new_car = Car("ABC-123", 142)

print(f"Biển số: {new_car.registration_number}")
print(f"Tốc độ tối đa: {new_car.max_speed} km/h")
print(f"Tốc độ hiện tại: {new_car.current_speed} km/h")
print(f"Quãng đường đã đi: {new_car.travelled_distance} km")