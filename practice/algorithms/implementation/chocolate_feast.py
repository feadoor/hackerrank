def number_of_chocolates(money, price, offer):
    chocolates = money / price
    wrappers = chocolates
    while wrappers >= offer:
        new_chocolates, wrappers = divmod(wrappers, offer)
        chocolates += new_chocolates
        wrappers += new_chocolates
    return chocolates

def do_test_case():
    money, price, offer = map(int, raw_input().strip().split(' '))
    print number_of_chocolates(money, price, offer)

def main():
    for _ in xrange(input()):
        do_test_case()

if __name__ == "__main__":
    main()