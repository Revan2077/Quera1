n = int(input())

numbers = []
max_unique_letters = 0
word_with_most_unique = ""

for i in range(n):
    num = input()
    numbers.append(num)
    unique_letters = len(set(num))
    
    if unique_letters > max_unique_letters:
        max_unique_letters = unique_letters
        word_with_most_unique = num

print(max_unique_letters)
