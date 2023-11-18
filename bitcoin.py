import sys
import requests


if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoin = r.json()

bitcoin_value = bitcoin["bpi"]["USD"]["rate_float"]

cost = bitcoin_value * amount

print(f"${cost:,.4f}")


