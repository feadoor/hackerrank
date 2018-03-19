#!/usr/local/bin/pypy

def maximum_games_bought(starting_dollars, starting_price, decrement, minimum_price):
    total_price, next_game_price, games_bought = 0, starting_price, 0

    while total_price + next_game_price <= starting_dollars:
        total_price += next_game_price
        games_bought += 1
        if next_game_price > minimum_price + decrement:
            next_game_price -= decrement
        else:
            next_game_price = minimum_price

    return games_bought

def main():
    starting_price, decrement, minimum_price, starting_dollars = map(int, raw_input().strip().split(' '))
    print maximum_games_bought(starting_dollars, starting_price, decrement, minimum_price)

if __name__ == "__main__":
    main()