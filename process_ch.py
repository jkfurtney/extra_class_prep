
questions = []
with open("ch7.org", "r") as f:
    for line in f.readlines():
        start, *end = line.strip().split(" ")
        for e in end:
            questions.append(start+e)

questions.sort()
with open("ch7_full.org", "w") as f:
    for q in questions:
        print(q, file=f)
