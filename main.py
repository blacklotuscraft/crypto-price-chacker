import cryptocompare

coin = ["BTC", "SOL", "ETH", "XPR", "SHIBA", "DODGE"]

def get_crypto_price(crypto, currency='EUR'):
    price = cryptocompare.get_price(crypto, currency=currency)
    if price and crypto in price:
        return price[crypto][currency]
    return None
def main():
    user_input = input("What cryptocurrency price do you want to check? ").upper()

    if user_input in coin:
        price = get_crypto_price(user_input)
        if price:
            print(f"The price of {user_input} is: {price} EUR")
        else:
            print(f"Sorry, couldn't fetch the price for {user_input}.")
    else:
        print(f"{user_input} is not a valid option. Please choose from the available list of coins: {', '.join(coin)}")
if __name__ == "__main__":
    main()