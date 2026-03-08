import random
import string

string = string.ascii_lowercase + string.ascii_uppercase
random.seed(int(input()))
pass_len = int(input())
password = ''

for char in range(pass_len):
    password += random.choice(string)

print(password)