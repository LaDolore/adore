from random import *
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
            'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
            'Пока неясно, попробуй снова позже', 'Спроси позже', 'Лучше не рассказывать',
            'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай',
            'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
            'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.', 'Как тебя зовут?', sep = '\n')
print('Привет,', input())
while True:    
    print('Задай свой вопрос')
    question = input()
    print(choice(answers), 'Хочешь задать ещё один вопрос?', sep = '\n')
    question = input()
    if question == 'да':
        continue
    else:
        break