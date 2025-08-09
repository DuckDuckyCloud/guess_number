import random

welcome_text = 'Привет'

secret_num = random.randint(1,100)
guess = 0
# комментарий

user_try = 0
while secret_num != guess:
    guess = int(input('Попробуй угадать число: '))
    if guess > secret_num:
        user_try += 1
        print('Ваше число больше того, что загадано')
    elif guess < secret_num:
        user_try += 1
        print('Ваше число меньше того, что загадано')
    else:
        print(f'Отличная интуиция! Вы угадали число: {secret_num} за ' \
              f'{user_try} попыток!')
        break
 
print("Конекц игры! И новый коммит!")