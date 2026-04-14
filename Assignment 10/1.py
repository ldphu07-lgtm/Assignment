import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        data = response.json()
        print(data['value'])
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    get_chuck_norris_joke()