print("Hello, i am Trading Bot")
print("Start from easly questions")
name = input("What is your name? ").strip().title()
print(f"Hello {name}, nice to meet you!")
age = input("How old are you? ").strip()
if age >= '18':
    print("You are old enough to trade!")
else:
    print("Sorry, you are too young to trade.")
print("Let's start trading!")


def parse_volume(input_str):
    cleaned = input_str.strip().replace('%', '').replace(',', '.')
    try:
        return float(cleaned)
    except ValueError:
        print("Invalid input, please enter a numeric value.")
        return None
btc_volume = input("Bitcoin 24h volume (in %): ")
btc_volume = parse_volume(btc_volume)
eth_volume = input("Etherium 24h volume (in %): ")
eth_volume = parse_volume(eth_volume)
if btc_volume > eth_volume:
    print("Bitcoin has a higher trading volume than Etherium. Better to invest in Bitcoin.")
else:
    print("Etherium has a higher trading volume than Bitcoin. Better to invest in Etherium.")


print("Thank you for using the Trading Bot!")
print("Goodbye!")