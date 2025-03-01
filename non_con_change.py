# input coins = [5,7,1,1,2,3,22]
# output 20
coins = [1,2,5]
def change_coin(coins: list) -> int: 
    coins.sort()
    change = 0

    for coin in coins:
        if coin > change + 1:
            return change + 1
        else: 
            change += coin

    return change

print(change_coin(coins))

