import sys

try:
    with open("hahaha.txt", 'r') as handle:
        data = handle.readlines()
except FileNotFoundError as err: #except만 써도 에러 잡히는데 이렇게 자세하게 error넣는 이유는, 그냥 잡으면 모든 에러가 잡혀서 어느에런지 모르기 때문
    print(err)
    sys.exit()

print(data)
