import requests

def main():
    response = requests.get("https://data.fixer.io/api/latest?access_key=2dc9a8fbc242c12a170e15b67889c51e&base=USD&symbols=EUR")

    if response.status_code != 200:
        raise Exception("ERROR API request unsuccesful")

    data = response.json()
    print(data)
    print(data["error"]["info"])


if __name__=="__main__":
    main()
