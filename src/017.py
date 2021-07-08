file_name = "write_sample.txt"

handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("Bioinformatics\n") #끝에까지 \n 달아줘야 마지막 배시셸 문양 안나옴

with open(file_name, "w") as handle:
    handle.write("ken\n") 

s = "s1,s2,s3" #csv : , 로 구분 / tsv: tab으로 구분
data = s.split(",")
print(data) #['s1', 's2', 's3']

with open(file_name, "a") as handle:
    handle.write("\t".join(data)) #문자열.join을 하게 되면 .앞에 적힌 걸로 문자열 사이를 이어준다. 이번에는 tab으로 이어준다는 것이고, "**"을 해주면 s1**s2**s3로 나오게 된다.

# 끝마다, 빈 줄마다 $는 공백이 어딘지 보여줄 때 사용 -> 지울 때는 :set nolist
