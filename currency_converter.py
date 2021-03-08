import requests

r_usd = requests.get("http://www.floatrates.com/daily/usd.json")
r_eur = requests.get("http://www.floatrates.com/daily/eur.json")

cache = {
    'usd': r_usd.json(),
    'eur': r_eur.json()
}

main_currency = input().lower()
if main_currency not in cache:
    cache[main_currency] = requests.get("http://www.floatrates.com/daily/{}.json".format(main_currency)).json()
target_currency = input().lower()
while target_currency != "":
    main_balance = int(input())
    if target_currency in cache:
        print("""Checking the cache...
Oh! It is in the cache!""")
        print(
            f"You received {cache[main_currency][target_currency]['rate'] * main_balance} "
            f"{target_currency.upper()}.")
    else:
        print("""Checking the cache...
Sorry, but it is not in the cache!""")
        new_r = requests.get("http://www.floatrates.com/daily/{}.json".format(main_currency))
        print(f"You received {new_r.json()[target_currency]['rate'] * main_balance} {target_currency.upper()}.")
        cache[target_currency] = requests.get("http://www.floatrates.com/daily/{}.json".format(target_currency))
    target_currency = input().lower()
