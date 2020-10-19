import requests

def main():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    if response.status_code != 200:
        raise Exception("ERROR API request unsuccesful")

    data = response.json()
    code = input("Seleccione el código de moneda: ")
    rate = data["bpi"][code]["rate"]
    print("1 bitcoin equals {} {}".format(rate, code))

if __name__=="__main__":
    main()
