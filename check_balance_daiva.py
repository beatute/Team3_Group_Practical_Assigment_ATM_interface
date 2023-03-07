def balance():
        print()
total = 0
with open("deposit.txt", "r") as f:
    for line in f:
        total += int(line)
total2 = 0
with open("withdrawal.txt", "r") as f:
    for line2 in f:
        total2 += int(line2)
print("Deposit EUR: ", total)
print("Withdrawal EUR: ", total2)
print("Balance EUR: ", total - total2)