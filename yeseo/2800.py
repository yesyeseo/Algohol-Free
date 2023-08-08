import sys
input = sys.stdin.readline

from collections import deque

exp = input().split()[0]
que = deque([])
# (3+4) => ['(', '3+4', ')']
# 위처럼 만들고 쌍에 맞는 인덱스도 각각 저장

lr_index = []

for i, v in enumerate(exp):
    if v != ')': que.append([v, i])
    else: # if v == ')'
        r, count = i, 0
        while que:
            q = que.pop()
            if q[0] == '(': 
                l = q[1]
                break
        lr_index.append([l, r])

from itertools import combinations
ans_list = []

# 가능한 모든 조합을 출력하는 과정 진행
# right_index의 크기가 '()' 쌍의 갯수임
lr_pick = [i for i in range(len(lr_index))]
for i in range(1, len(lr_index) + 1):
    # i: 제거할 괄호의 수
    # 입력(아무 괄호도 제거하지 않은 것)은 출력하지 않아야 하므로 1부터 시작함
    lr_list = list(combinations(lr_pick, i))
    # if lr_list = [[1, 2]] => lr_index의 1, 2번째 괄호가 제거됨
    for lr in lr_list:
        lr_all_ind = [ind for l in lr for ind in lr_index[l]]
        # (0, 1) => [3, 7, 0, 10]
        ans = [e for (ind, e) in enumerate(exp) if ind not in lr_all_ind]
        ans_list.append(''.join(ans))
        # 사전 순 출력

ans_list = list(set(ans_list))
ans_list.sort()
for a in ans_list: print(a)




# from itertools import combinations

# # TC: (0/(0))
# que = deque([])

# exp = input().split()[0]
# # ['0/', '0', ')', ')'] 꼴로 만들어 줌
# exp = exp.replace(')', '()(')
# exp = list(exp.split('('))
# exp = [e for e in exp if e != '']

# right_index = [i for i, v in enumerate(exp) if v == ')']
# # ')' 괄호의 인덱스만 추출

# # 가능한 모든 조합을 출력하는 과정 진행
# # right_index의 크기가 '()' 쌍의 갯수임
# for i in range(1, len(right_index) + 1):
#     # i: 제거할 괄호의 수
#     # 입력(아무 괄호도 제거하지 않은 것)은 출력하지 않아야 하므로 1부터 시작함
#     c_list = list(combinations(right_index, i))
#     # 여기에서 추출된 c_list 내부에 있는 숫자가 제거되지 않은 괄호를 말하는 것
#     for c in c_list:
#         ans = [v for e, v in enumerate(exp) if e not in c]
#         print(*ans)
#     print(c_list, exp)