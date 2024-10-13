# Outline: Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?
buy = 100
selled = int(input("sell something you bought for 100: "))
if selled >buy:
    profit = selled-buy
    print("you got profit by",profit)
else:
    print("no profit gained")

