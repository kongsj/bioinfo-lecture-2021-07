cnt_all = 0
cnt_pass = 0

# filTER 위치를 코딩으로 잡기

with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        if data[filter_idx] == "PASS":
            cnt_pass += 1

print(cnt_all, cnt_pass, cnt_pass / cnt_all)
