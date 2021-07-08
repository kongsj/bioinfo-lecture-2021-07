class ValueCalculator:
    def __init__(self, val: str):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

if __name__ == "__main__": #이거 자체를 실행할 때는 hi가 나오지만, ValueCalculatorRunner를 통해 실행할 때는 import에 Calculator의 파일이름으로 들어가기에 name이 아니라서..? print('hi')가 실행되지 않는다. 
    print('hi') #자체를 실행할 때는 나오지만, 얘를 import를 통해 걸어서 나오게 하고 싶을 떈 안나오게 할 때 쓰는 게 if __name__ == "__main__"이다.


