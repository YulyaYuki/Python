playing = input("Хочешь пройти тест на тревожность? (да/нет) \n")

if playing.lower() == "нет":
    print("Тогда займись чем-то, что принесет тебе радость.")
    quit()
if playing.lower() != "да":
    quit()

print("После каждого вопроса введи номер выбранного варианта ответа.")
answer = int()
answer_count = 0

def result_count():
    global answer 
    global answer_count
    if answer == 1:
        answer_count += 0
    elif answer == 2:
        answer_count += 1
    elif answer == 3:
        answer_count += 2
    elif answer == 4:
        answer_count += 3
    return answer_count

def check_answer():
    global answer
    while answer != 1 and answer != 2 and answer != 3 and answer != 4 :
      answer = int(input("Такого варианта ответа нет. \n"))
      if answer == (1 or 2 or 3 or 4):
        return answer
    

print("""
Я испытываю напряжение, мне не по себе.
1 - Совсем не испытываю.
2 - Время от времени, иногда.
3 - Часто
4 - Все время \n""")
answer = int(input())  
check_answer()
result_count()

print("""
Я испытываю страх, кажется, что что-то ужасное
вот-вот может случиться.
1 - Совсем не испытываю.
2 - Иногда, но меня это не беспокоит.
3 - Да, это так, но страх не очень велик.
4 - Определенно, это так, и страх очень велик \n""")
answer = int(input())  
check_answer()
result_count()

print("""
Беспокойные мысли крутятся у меня в голове.
1 - Только иногда.
2 - Время от времени и не так часто.
3 - Большую часть времени
4 - Постоянно \n""")
answer = int(input())  
check_answer()
result_count()

print("""
Я легко могу присесть и расслабиться.
1 - Определенно, это так.
2 - наверно, это так.
3 - Лишь изредка это так.
4 - Совсем не могу \n""")
answer = int(input())  
check_answer()
result_count()

print("""
Я испытываю внутреннее напряжение или дрожь.
1 - Совсем не испытываю.
2 - Иногда.
3 - Часто.
4 - Очень часто \n""")
answer = int(input())  
check_answer()
result_count()

print("""
Я испытываю неусидчивость, мне постоянно нужно двигаться.
1 - Совсем не испстываю.
2 - Лишь в некоторой степени.
3 - Наверно, это так.
4 - Определенно, это так. \n""")
answer = int(input())  
check_answer()
result_count()

print("""
У меня бывает внезапное чувство паники.
1 - Совсем не бывает.
2 - Не так уж часто.
3 - Довольно часто.
4 - Очень часто. \n""")
answer = int(input())  
check_answer()
result_count()

print("\n Набранное количество баллов: ", answer_count)
print("""0-7 баллов - норма
8-10 баллов - субклинически выраженная тревога
11 баллов и выше - клинически выраженная тревога
""")



