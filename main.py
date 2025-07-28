import pymupdf4llm
import pathlib
import re
import json

#######################
#        总题库        #
#######################
# PDF 转文字
content = pymupdf4llm.to_markdown("总题库.pdf")
# 删去页码
result = re.sub(r'^\d$', '', content, flags=re.MULTILINE)
# 删去所有换行符
result = re.sub(r'\n', '', result, flags=re.MULTILINE)
# 左括号前加入新行
result = re.sub(r'\[', '\n[', result, flags=re.MULTILINE)
# 每个题目，即[J]前加入新行
result = re.sub(r'\[J', '\n[J', result, flags=re.MULTILINE)
# 删除开头的换行符
result = result[2:].strip()
# 保存
pathlib.Path("总题库.txt").write_bytes(result.encode())
print("文字版总题库已保存")

# 构建新的题库合集
questions = []

with open('总题库.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.startswith("["):
            # 新的问题
            if line[1] == "J":
                # 构建问题框架
                question = {"J": '',"P": '', "index": '', "question": '', "answer": [], "choice": []}
                question["J"] = line[3:].strip()
            if line[1] == "P":
                question["P"] = line[3:].strip()
            if line[1] == "I":
                question["index"] = line[3:].strip()
            if line[1] == "Q":
                question["question"] = line[3:].strip()
            if line[1] == "T":
                temp_answer = line[3:].strip()
                # 多选分割
                while len(temp_answer)>0:
                    question["answer"].append(temp_answer[0])
                    temp_answer = temp_answer[1:]
            if line[1] == "A":
                choice = {"A": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "B":
                choice = {"B": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "C":
                choice = {"C": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "D":
                choice = {"D": line[3:].strip()}
                question["choice"].append(choice)
                # 插入问题进题库
                questions.append(question)

with open('总题库_结构化.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)
print("数据结构化总题库已保存")

#######################
#       A类题库        #
#######################
#pdf转文字
content = pymupdf4llm.to_markdown("A类题库.pdf")
# 删去页码
result = re.sub(r'^\d$', '', content, flags=re.MULTILINE)
# 删去所有换行符
result = re.sub(r'\n', '', result, flags=re.MULTILINE)
# 左括号前加入新行
result = re.sub(r'\[', '\n[', result, flags=re.MULTILINE)
# 每个题目，即[J]前加入新行
result = re.sub(r'\[J', '\n[J', result, flags=re.MULTILINE)
# 删除开头的换行符
result = result[2:].strip()
# 保存
pathlib.Path("A类题库.txt").write_bytes(result.encode())
print("A类文字版题库已保存")

# 构建新的题库合集
questions = []

with open('A类题库.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.startswith("["):
            # 新的问题
            if line[1] == "J":
                # 构建问题框架
                question = {"J": '',"P": '', "index": '', "question": '', "answer": [], "choice": []}
                question["J"] = line[3:].strip()
            if line[1] == "P":
                question["P"] = line[3:].strip()
            if line[1] == "I":
                question["index"] = line[3:].strip()
            if line[1] == "Q":
                question["question"] = line[3:].strip()
            if line[1] == "T":
                temp_answer = line[3:].strip()
                # 多选分割
                while len(temp_answer)>0:
                    question["answer"].append(temp_answer[0])
                    temp_answer = temp_answer[1:]
            if line[1] == "A":
                choice = {"A": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "B":
                choice = {"B": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "C":
                choice = {"C": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "D":
                choice = {"D": line[3:].strip()}
                question["choice"].append(choice)
                # 插入问题进题库
                questions.append(question)

with open('A类题库_结构化.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)
print("A类数据结构化题库已保存")

#######################
#       B类题库        #
#######################
#pdf转文字
content = pymupdf4llm.to_markdown("B类题库.pdf")
# 删去页码
result = re.sub(r'^\d$', '', content, flags=re.MULTILINE)
# 删去所有换行符
result = re.sub(r'\n', '', result, flags=re.MULTILINE)
# 左括号前加入新行
result = re.sub(r'\[', '\n[', result, flags=re.MULTILINE)
# 每个题目，即[J]前加入新行
result = re.sub(r'\[J', '\n[J', result, flags=re.MULTILINE)
# 删除开头的换行符
result = result[2:].strip()
# 保存
pathlib.Path("B类题库.txt").write_bytes(result.encode())
print("B类文字版题库已保存")

# 构建新的题库合集
questions = []

with open('B类题库.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.startswith("["):
            # 新的问题
            if line[1] == "J":
                # 构建问题框架
                question = {"J": '',"P": '', "index": '', "question": '', "answer": [], "choice": []}
                question["J"] = line[3:].strip()
            if line[1] == "P":
                question["P"] = line[3:].strip()
            if line[1] == "I":
                question["index"] = line[3:].strip()
            if line[1] == "Q":
                question["question"] = line[3:].strip()
            if line[1] == "T":
                temp_answer = line[3:].strip()
                # 多选分割
                while len(temp_answer)>0:
                    question["answer"].append(temp_answer[0])
                    temp_answer = temp_answer[1:]
            if line[1] == "A":
                choice = {"A": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "B":
                choice = {"B": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "C":
                choice = {"C": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "D":
                choice = {"D": line[3:].strip()}
                question["choice"].append(choice)
                # 插入问题进题库
                questions.append(question)

with open('B类题库_结构化.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)
print("B类数据结构化题库已保存")

#######################
#       C类题库        #
#######################
#pdf转文字
content = pymupdf4llm.to_markdown("C类题库.pdf")
# 删去页码
result = re.sub(r'^\d$', '', content, flags=re.MULTILINE)
# 删去所有换行符
result = re.sub(r'\n', '', result, flags=re.MULTILINE)
# 左括号前加入新行
result = re.sub(r'\[', '\n[', result, flags=re.MULTILINE)
# 每个题目，即[J]前加入新行
result = re.sub(r'\[J', '\n[J', result, flags=re.MULTILINE)
# 删除开头的换行符
result = result[2:].strip()
# 保存
pathlib.Path("C类题库.txt").write_bytes(result.encode())
print("C类文字版题库已保存")

# 构建新的题库合集
questions = []

with open('C类题库.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.startswith("["):
            # 新的问题
            if line[1] == "J":
                # 构建问题框架
                question = {"J": '',"P": '', "index": '', "question": '', "answer": [], "choice": []}
                question["J"] = line[3:].strip()
            if line[1] == "P":
                question["P"] = line[3:].strip()
            if line[1] == "I":
                question["index"] = line[3:].strip()
            if line[1] == "Q":
                question["question"] = line[3:].strip()
            if line[1] == "T":
                temp_answer = line[3:].strip()
                # 多选分割
                while len(temp_answer)>0:
                    question["answer"].append(temp_answer[0])
                    temp_answer = temp_answer[1:]
            if line[1] == "A":
                choice = {"A": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "B":
                choice = {"B": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "C":
                choice = {"C": line[3:].strip()}
                question["choice"].append(choice)
            if line[1] == "D":
                choice = {"D": line[3:].strip()}
                question["choice"].append(choice)
                # 插入问题进题库
                questions.append(question)

with open('C类题库_结构化.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)
print("C类数据结构化题库已保存")
