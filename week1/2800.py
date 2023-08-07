from itertools import combinations
import sys

data = list(sys.stdin.readline().strip())

stack = []
bracket = []
comb = []
temp = []

result = set()

for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        bracket.append([stack.pop(), i])

for i in range(1, len(bracket)+1):
    comb = combinations(bracket, i)
    for j in comb:
        temp = data[:]
        for left, right in j:
            temp[left]=''
            temp[right]=''
            result.add(''.join(temp))
            
result = list(sorted(result))
for i in range(len(result)):
    print(result[i])