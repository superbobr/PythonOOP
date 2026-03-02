with open('numbers.txt', 'w+', encoding='utf-8') as file:
    for num in range(5, 16, 5):
        file.write(str(num) + '\n')
    file.seek(0)
    result = 0
    for line in file:
        result += int(line)
    print(result)

with open('data.txt', 'w+', encoding='utf-8') as file:
    file.write('hello world' + '\n')
    file.write('python is great')
    file.seek(0)
    res = file.readlines()
    for word in res:
        print(word.strip().upper())

lines = ['Строка 1', 'Строка 2', 'Строка 3']
with open('list_data.txt', 'w+', encoding='utf-8') as file:
    file.writelines(f'{line}\n' for line in lines)
    file.seek(0)
    for line in file:
        print(line, end='')