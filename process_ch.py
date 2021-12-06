import re

question_pattern = re.compile("(^E\d[A-Z]\d\d)\s+\(([A-Z])\)")

_questions = {}

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
            _questions[qid] = [question, choices, answer]



questions = []
with open("ch9.org", "r") as f:
    for line in f.readlines():
        start, *end = line.strip().split(" ")
        for e in end:
            questions.append(start+e)
            assert start+e in _questions

questions.sort()
with open("ch9_full.org", "w") as f:
    for q in questions:
        print(q, file=f)
