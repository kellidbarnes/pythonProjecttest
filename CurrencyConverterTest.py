# Currency converter

import requests

print("Currency Converter")
print("Convert between the currencies of the world in real time!")

location = input("Currency Location: ")
destination = input("Currency Destination: ")

while True:
    try:
        amount = float(input("Conversion Amount: "))
    except:
        print("The conversion amount must be a numerical value!")
        continue

    if amount < 0:
        print("The conversion amount must be greater than 0")
        continue
    else:
        break

url = "https://api.apilayer.com/fixer/convert?to=" + destination + "&from=" + location + "&amount=" + str(amount)

payload = {}
headers = {
    "apikey": "2Vu3M0UIPDO6cdUSJFLbEJ0mlK0V3anK"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code

if status_code != 200:
    print("Uh oh, there was a problem. Please try again later")
    quit()

result = response.json()

print("Result: " + str(result))
