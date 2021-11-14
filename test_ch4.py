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

active_qids = []
with open("./ch6_full.org") as f:
    for line in f.readlines():
        qid= line.strip()
        active_qids.append(qid)


for qid in active_qids:
    question, choices, answer = questions[qid]
    answered_correctly = False
    while not answered_correctly:
        print()
        print(question)
        print()
        for letter in "ABCD":
            print(f"{letter}.", choices[letter])
        print()
        a = input()
        if a.upper() == answer:
            print()
            print("Correct")
            answered_correctly = True
        else:
            print()
            print("Wrong")
