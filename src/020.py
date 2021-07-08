import sys

try:
    num = int(input("Enter: "))
except ValueError as err:
    print("값을 넣지 않았음")
    sys.exe()


try:
    num = int(input(10 / num))

except ZeroDivisionError as err:
    print("0으로 나눌 수 없음") #이러한 문구를 넣지 않을 떄 print(err)

    sys.exe()
