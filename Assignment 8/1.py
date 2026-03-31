class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Thang máy đang ở tầng: {self.current_floor}")
        else:
            print("Đã đạt tầng cao nhất.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Thang máy đang ở tầng: {self.current_floor}")
        else:
            print("Đã đạt tầng thấp nhất.")

    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor or target_floor < self.bottom_floor:
            print(f"Tầng {target_floor} không tồn tại!")
            return

        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Đã đến tầng {self.current_floor}.")

if __name__ == "__main__":
    h = Elevator(1, 10)
    
    h.go_to_floor(10)
    
    h.go_to_floor(1)