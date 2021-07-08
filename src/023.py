
file_name = "covid19.fasta"

data = dict() #data = {} 초기화한다는 뜻 / 같은 의미, 빈 dict초기화

with open(file_name, 'r') as handle: #handle로 읽어라
    for line in handle:
        if line.startswith(">"):
            continue #건너뛰어서 그 다음 for문으로 감
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] +=1

print(data)


"""
import gzip
file_name = "covid19.fasta.gz"

data = dict() #data = {} 초기화한다는 뜻 / 같은 의미, 빈 dict초기화

# with gzip.open(file_name, 'rb') as handle:
with gzip.open(file_name, 'rt') as handle:
    for line in handle:
          # line = line.decode("utf-8")
    if line.startswith(">"):
           continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] +=1
print(data)
"""
