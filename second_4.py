while True:
    print("Who are you?")
    name = input()
    if name != 'Me':
        continue
    print("Hello, Me. What is the password?")
    password = input()
    if password == 'test':
        break
print("Done")