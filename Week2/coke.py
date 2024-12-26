def main():
    coke()
    
def coke():
    totcoins = 0
    while totcoins<50:
        print("Amount Due: ", 50-totcoins)
        coins = int(input("Insert coin: "))
        if coins in [5,10,25]:
            totcoins+=coins
    else:
        print("Change Owed: ",totcoins-50)
        
main()