import sys
from os import system
from time import sleep



def start():
    
    print("""Игрок, приветствуем тебя!
Тебе предстоит ряд заданий.
При верном выборе -переход к новому заданию.
В противном случае...

    Итак, приступим!

    """)
    step_1()
    
def step_1():
    system('clear')   
    print('Ты стоишь на улице')    
    print('Выбор: Ждать - нажми 0, Пойти - нажми 1')

    x = int(input('Сделай выбор!: '))

    if x == 0:
        system('clear')
        print('В тебя выстрелили из-за угла!')
        print('Game over! :)')
        sleep(3)
        sys.exit()
                          
    elif x == 1:
        system('clear')
        print('Ты увидел убегающую тень и пошел за ней!')
        
        step_2()

    else:
        system('clear')       
        print('Ты ввел неверные данные. Введи 0 или 1: ')
        step_1()


def step_2():
    system('clear')
    print('Он тебя не видел и привел к бандитам')
    print('Выбор: Подслушать разговор - нажми 0, Тихонько уйти - нажми 1')

    x = int(input('Сделай выбор!: '))

    if x == 0:
        system('clear')
        print('Ты наступил на сухую веточку.Тебя услышали и застрелили!')
        print('Game over! :)')
        sleep(3)
        sys.exit()
        
    elif x == 1:
        system('clear')        
        print('Идешь в сторону дома')
        step_3()

    else:
        system('clear')      
        print('Вы ввели неверные данные. Введите 0 или 1')
        step_2()
        
      
def step_3():
    system('clear')
    print('По пути ты нашел чемодан.')
    print('Выбор: Пройти мимо-нажми 0,Открыть чемодан - нажми 1')

    x = int(input('Сделай выбор!: '))

    if x == 1:
        system('clear')
        print('В чемодане была бомба.Тебя больше нет!')
        print('Game over! :)')
        sleep(3)
        sys.exit()
        
    elif x == 0:
        system('clear')
        print('Неожиданно тебя останавливает полиция.')
        step_4()

    else:
        system('clear')
        print('Вы ввели неверные данные. Введите 0 или 1')
        step_3()


def step_4():
    system('clear')
    print('Ты решил, что тебя в чем-то подозревают.')
    print('Выбор: Остановиться -нажми 0,Бежать! - нажми 1')

    x = int(input('Сделай выбор!: '))

    if x == 1:
        system('clear')
        print('Ты был застрелен при попытке бегства! Нечего бегать от полиции :)))')
        print('Game over! :)')
        sleep(3)
        sys.exit()
        
    elif x == 0:
        system('clear')
        print('У тебя проверили документы и отпустили')
        step_5()

    else:
        system('clear')
        print('Вы ввели неверные данные. Введите 0 или 1')
        step_4()

def step_5():
    system('clear')
    print('Ты дошел до прекрестка')
    print('Выбор: Повернуть направо -нажми 0,Повернуть налево - нажми 1')

    x = int(input('Сделай выбор!: '))

    if x == 0:
        system('clear')
        print('Упс! На тебя упал кирпич... Не стоит ходить по стройке! :)')
        print('Game over! :)')
        sleep(3)
        sys.exit()
        
    elif x == 1:
        system('clear')
        print('Ты повернул по направлению к дому')
        step_6()

    else:
        system('clear')
        print('Вы ввели неверные данные. Введите 0 или 1')
        step_5()

def step_6():
    system('clear')
    print('Но через квартал за тобой погнались собаки')
    print('Выбор: Остановиться - нажми 0, Бежать!-нажми 1')

    x = int(input('Сделай выбор!: '))

    if x == 0:
        system('clear')
        print('Тебя загрызли. Какая жалость!')
        print('Game over! :)')
        sleep(3)
        sys.exit()
        
    elif x == 1:
        system('clear')
        print('Ты перелез через забор и собаки тебя не достали')
        step_7()

    else:
        system('clear')
        print('Вы ввели неверные данные. Введите 0 или 1')
        step_6()
        
def step_7():
    system('clear')
    print('Дошел до дороги')
    print('Выбор: Подождать зеленый и перейти -нажми 0, Перебежать на красный! - нажми 1')

    x = int(input('Сделай выбор!: '))

    if x == 1:
        system('clear')
        print('Тебя сбила машина!')
        print('Game over! :)')
        sleep(3)
        sys.exit()
        
    elif x == 0:
        system('clear')
        print('Тебя сбила машина, которая нарушила и проехала на красный!')
        print('"Ну и день!" подумал ты и отключился...')
        step_8()

    else:
        system('clear')
        print('Вы ввели неверные данные. Введите 0 или 1')
        step_7()

def step_8():
    system('clear')
    print('Ты очнулся в своей постеле. Это был просто сон!')

 
start()

