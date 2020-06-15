n = int(input('Сколько будет строк?'))
arr=[]
number_vowels = 0
number_consonants = 0
for i in range(n):
    arr.append(input())
vowels = set("уеыаоэяиюё")
consonants = set("йцкнгшщзхфвпрлжчсмтб")
for word in arr:
    word = word.replace(' ', '')
    number_consonants += sum(letter in consonants for letter in word)
    number_vowels += sum(letter in vowels for letter in word)
print(f"Количество гласных: {number_vowels}")
print(f"Количество согласных: {number_consonants}")

