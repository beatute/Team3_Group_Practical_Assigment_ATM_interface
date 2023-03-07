def testwithd():
    print()
testwithd()

# ✅ Save user input to file
file_name = 'withdrawal.txt'

with open(file_name, 'w', encoding='utf-8') as my_file:
    my_file.write(input("Withdrawal EUR: "))

