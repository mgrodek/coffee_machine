word = input()
output = ''
for letter in word:
    output += '_' + letter.lower() if letter.isupper() else letter

print(output)