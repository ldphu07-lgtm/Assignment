import requests

def get_weather():
    api_key = "YOUR_API_KEY_HERE"  
    city = input("Nhập tên thành phố: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            description = data['weather'][0]['description']
            temp_kelvin = data['main']['temp']
            temp_celsius = temp_kelvin - 273.15
            
            print(f"Thời tiết tại {city}: {description}")
            print(f"Nhiệt độ: {temp_celsius:.2f}°C")
        else:
            print("Không tìm thấy thành phố hoặc lỗi API.")
    except Exception as e:
        print(f"Lỗi kết nối: {e}")

if __name__ == "__main__":
    get_weather()