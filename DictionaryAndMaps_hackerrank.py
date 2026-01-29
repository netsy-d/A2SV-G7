# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.read().strip().split('\n')
n = int(data[0])
phone_book = {}

for i in range(1, n+1):
    name, phone = data[i].split()
    phone_book[name] = phone

for query in data[n+1:]:
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
