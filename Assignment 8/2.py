class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Tầng: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Tầng: {self.current_floor}")

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom_floor = bottom
        self.top_floor = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, target_floor):
        if 0 <= elevator_num < len(self.elevators):
            print(f"\n[Điều khiển Thang máy số {elevator_num}]")
            self.elevators[elevator_num].go_to_floor(target_floor)
            print(f"Thang máy số {elevator_num} đã dừng tại tầng {target_floor}")
        else:
            print("Số hiệu thang máy không hợp lệ.")

if __name__ == "__main__":
    my_building = Building(0, 12, 3)
    
    my_building.run_elevator(0, 10)
    
    my_building.run_elevator(2, 5)