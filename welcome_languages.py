print("Welcome to THE BANK")
print("Choose a language")


while True:
    response = input('SELECT FROM FOLLOWING OPTIONS: \nEnglish__(EN) \nLithanian___(LT) \nLatvian__(LV) \nType The Letters Of Your Choices: ').lower()
    valid_responses = ['en', 'lt', 'lv']
    response = response.lower()
    if response == 'en':
        import functions

    elif response == 'lt':
        print('I DO NOT TALK IN LITHUANIAN, PLEASE CHOOSE ENGLISH')

    elif response == 'lv':
        print('I DO NOT TALK IN LATVIAN, PLEASE CHOOSE ENGLISH')