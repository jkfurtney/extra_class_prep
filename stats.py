import re

question_pattern = re.compile("(^E\d[A-Z]\d\d)\s+\(([A-Z])\)")

questions = {}

with open("./questions.txt") as f:
    lines=[]
    for line in f.readlines():
        line = line.strip()
        lines.append(line.strip())
    while lines:
        line = lines.pop(0)
        matches = question_pattern.match(line)
        if matches:
            qid, answer = matches.groups()
            question = lines.pop(0)
            a, b, c, d = lines.pop(0), lines.pop(0), lines.pop(0), lines.pop(0)
            assert a[0:3] == "A. "
            assert b[0:3] == "B. "
            assert c[0:3] == "C. "
            assert d[0:3] == "D. "
            choices = {"A": a[3:], "B": b[3:], "C": c[3:], "D": d[3:]}
            questions[qid] = [question, choices, answer]


longest = 0
total = 0
for q, (_, ch, ans) in questions.items():
    letters = ["A","B","C","D"]
    letters.remove(ans)
    if len(ch["A"])>100:
        total+=1
        if len(ch[ans]) > max([len(ch[_]) for _ in letters]):
            longest+=1

print(longest/total, total)
