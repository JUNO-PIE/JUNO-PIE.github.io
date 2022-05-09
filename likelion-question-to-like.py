total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == 'q':
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer

print(total_dictionary)