print("Добро пожаловать квиз по стартапам!")
print("Ответь на следующие вопросы: ")

# question = "Как называется компания, которая создана для развития новой идеи"
#
# answer = "Стартап"
# print(question)
# user_input = input("Введи ответ: ")
#
# if user_input.lower() == answer.lower():
#     print("Правильно")
# else:
#     print("Неправильно")
score = 0

question = [
    "1. Как называется компания, которая создана для развития новой идеи",
    "2. Как назвается человек или компания, который вкладывает деньги в бизнес с целью получения прибыли?",
    "3. Как называется капитал, который дают инвесторы на развитие стартапа?",
    "4. Как пишется минимально жизнеспособный продукт, который создается для тестирования идей и концепций?",
    "5. Какой план создают перед тем, как открывать стартап и занимать деньги?",
    "6. Как называются другие компании на рынке, которые предлагают аналогичные товары или услуги?",
    "7. Как называется разница между выручкой и затратами компании?",
]
answers = [
    "Стартап",
    "Инвестор",
    "Инвестиция",
    "MVP",
    "Бизнес-план",
    "Конкуренты",
    "Прибыль",
]
print(question[0])
user_input = input("Введи ответ: ")
if user_input.lower() == answers[0].lower():
    print("Правильно")
    score += 1
else:
    print("Неправильно")
print(question[1])
user_input = input("Введи ответ: ")
if user_input.lower() == answers[1].lower():
    print("Правильно")
    score += 1
else:
    print("Неправильно")
print(question[2])
user_input = input("Введи ответ: ")
if user_input.lower() == answers[2].lower():
    print("Правильно")
    score += 1
else:
    print("Неправильно")
print(question[3])
user_input = input("Введи ответ: ")
if user_input.lower() == answers[3].lower():
    print("Правильно")
    score += 1
else:
    print("Неправильно")
print(question[4])
user_input = input("Введи ответ: ")
if user_input.lower() == answers[4].lower():
    print("Правильно")
    score += 1
else:
    print("Неправильно")
print(question[5])
user_input = input("Введи ответ: ")
if user_input.lower() == answers[5].lower():
    print("Правильно")
    score += 1
else:
    print("Неправильно")
print(question[6])
user_input = input("Введи ответ: ")
if user_input.lower() == answers[6].lower():
    print("Правильно")
    score += 1
else:
    print("Неправильно")

print("Спасибо за прохождение квиза! Ты ответил правильно на",score,"из 7 вопросов")
if score > 5:
    print("Это очень хороший результат, ты молодец!")
elif score > 3:
    print("Это средний результат, ты справился хорошо!")
else:
    print("Это плохой результат, советую поизучать эту тему в интернете!")




