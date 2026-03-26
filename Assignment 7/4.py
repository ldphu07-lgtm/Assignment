import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed = max(0, min(self.current_speed + speed_change, self.max_speed))

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = [Car(f"ABC-{i}", random.randint(150, 200)) for i in range(1, 11)]

race_finished = False
while not race_finished:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True

print(f"{'Biển số':<10} | {'Tốc độ tối đa':<10} | {'Tốc độ cuối':<10} | {'Tổng quãng đường':<15}")

print("-" * 55)

for car in cars:
    print(f"{car.registration_number:<10} | {car.max_speed:<10} | {car.current_speed:<10} | {car.travelled_distance:<15.1f}")