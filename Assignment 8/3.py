class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.current_floor += 1
        while self.current_floor > target_floor:
            self.current_floor -= 1

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom_floor = bottom
        self.top_floor = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        if 0 <= elevator_num < len(self.elevators):
            self.elevators[elevator_num].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n!!! BÁO CHÁY !!!")
        for i, el in enumerate(self.elevators):
            el.go_to_floor(self.bottom_floor)
            print(f"Thang máy số {i} đã về tầng {el.current_floor}")

if __name__ == "__main__":
    city_hall = Building(1, 20, 4)
    
    city_hall.run_elevator(0, 15)
    city_hall.run_elevator(1, 10)
    city_hall.run_elevator(2, 18)
    
    city_hall.fire_alarm()