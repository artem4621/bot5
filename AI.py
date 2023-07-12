from random import choice

answers = [
    'Опеределенно да',
    'Сомневаюсь',
    'Точно нет',
    'Думаю нет',
    'Непонятно',
    'Скорее всего да'
]


def generate_answer():
    return choice(answers)