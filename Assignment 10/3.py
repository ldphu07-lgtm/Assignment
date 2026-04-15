from flask import Flask
import json

app = Flask(__name__)

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

@app.route('/prime_number/<int:number>')
def check_prime(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host =  '127.0.0.1', port = 6000)
