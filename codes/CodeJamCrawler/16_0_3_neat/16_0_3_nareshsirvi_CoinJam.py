from math import sqrt

def get_div(coin, base):
    num = 0
    mul = 1
    for j in range(len(coin) - 1, -1, -1):
        if coin[j] == "1":
            num += mul
        mul = mul * base

    for j in range(2, int(sqrt(num)) + 1):
        if num % j == 0:
            return j

    return 1

def get_coins(coin, idx, J, coins):
    if len(coins) == J or idx == len(coin) - 1:
        return

    coin_str = "".join(coin)
    if coin_str not in coins and len(coins) < J:
        divs = []
        for base in range(2, 11):
            div = get_div(coin, base)
            if div == 1:
                break
            divs.append(div)
        else:
            coins[coin_str] = divs

    get_coins(coin, idx + 1, J, coins)

    coin[idx] = "1"
    coin_str = "".join(coin)
    if coin_str not in coins and len(coins) < J:
        divs = []
        for base in range(2, 11):
            div = get_div(coin, base)
            if div == 1:
                break
            divs.append(div)
        else:
            coins[coin_str] = divs

    get_coins(coin, idx + 1, J, coins)
    coin[idx] = "0"


if __name__ == "__main__":
    T = input()
    for i in range(1, T + 1):
        N, J = map(int, raw_input().split())
        coins = {}
        coin = ["1"] + ["0"] * (N - 2) + ["1"]
        get_coins(coin, 1, J, coins)

        print "Case #%d:" % i
        for k, v in coins.items():
            print k, " ".join([str(x) for x in v])

