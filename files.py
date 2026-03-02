with open('numbers.txt', 'w+', encoding='utf-8') as file:
    for num in range(5, 16, 5):
        file.write(str(num) + '\n')
    file.seek(0)
    result = 0
    for line in file:
        result += int(line)
    print(result)