import requests

def get_weather():
    api_key = "3be9b36581b2a9829eda850499b76b7f"  
    
    city = input("Nhập tên thành phố (vd: Hanoi, Ho Chi Minh, London): ")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            description = data['weather'][0]['description']
            
            temp_kelvin = data['main']['temp']
            
            temp_celsius = temp_kelvin - 273.15
            
            print(f"\nThời tiết tại {city}: {description}")
            print(f"Nhiệt độ: {temp_celsius:.2f}°C")
            
        elif response.status_code == 401:
            print("\nLỖI: API Key không hợp lệ hoặc chưa được kích hoạt.")
            print("Lưu ý: API key mới tạo đôi khi cần 10-15 phút để bắt đầu hoạt động.")
            
        elif response.status_code == 404:
            print(f"\nLỖI: Không tìm thấy thành phố '{city}'. Vui lòng thử nhập tên tiếng Anh hoặc không dấu.")
            
        else:
            print(f"\nLỖI API (Mã {response.status_code}): {response.text}")
            
    except Exception as e:
        print(f"Lỗi kết nối mạng: {e}")

if __name__ == "__main__":
    get_weather()
