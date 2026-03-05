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

with open('events.log', 'a+', encoding='utf-8') as file:
    for _ in range(3):
        file.write(input() + '\n')
    file.seek(0)
    for line in file:
        print(line, end='')

with open('text.txt', 'w+', encoding='utf-8') as f:
    f.write('словам\n')
    f.write('программирование\n')
    f.write('строка.')
    f.seek(0)
    s = f.readlines()
    s.sort(key=len)
    print(s[-1])

n = int(input())
with open('times_table.txt', 'w+', encoding='utf-8') as file:
    for num in range(1, 11):
        file.write(f'{n} x {num} = {n * num}\n')
    file.seek(0)
    for line in file:
        print(line, end='')

with open('lines.txt', 'w+', encoding='utf-8') as file:
    file.write("alpha\n")
    file.write("beta\n")
    file.write("gamma")
    file.seek(0)
    s = file.readlines()
    s.reverse()
    with open('reversed_lines.txt', 'w+', encoding='utf-8') as f:
        for line in s:
            f.write(line.strip() + '\n')
        f.seek(0)
        for line in f:
            print(line, end='')