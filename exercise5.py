message = "hello world! 123"
message = list(message)
print(message)
count = len(message)
LETTERS = 0
DIGITS = 0
for messagechar in message:
    if messagechar.isalpha():
        LETTERS = LETTERS+1
    elif messagechar.isdigit():
        DIGITS = DIGITS+1

print(str(LETTERS))
print(str(DIGITS))


