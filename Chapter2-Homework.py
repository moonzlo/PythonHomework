"""
Домашние задание из второй главы:

1 - Напишите программу симулятор пирожка 'С сюрпризом'/(печенье с предсказанием). Который бы при запуски выводил
случайный сюрприз/предсказание
p.s - Это моя личная инициатива сделать предсказания ^__^

2 - [ Моё любимое ] Напишите программу которя бы подбрасывала условную монету сто раз и сообщала, сколько раз
выпала орел или решка.

3 - *Пропустим так-как требуется улучшить код из книги.* (естественно что я выполнил данное задание, но увы стёр)

4 - Напишите программу "Отгадай число", где игрок загадывает число от 1 до 100 а компютер должен отгадать
(модефицирую программу путем добавление подсказок для компюетра, и добавив ему интелекта однако на рандоме)
"""
import random
print('''
Добро пожаловать в лавку предсказаний :3 
Сегодня ты узнаешь свою судьбу из печенья :D 
''')
# Когда я делал эту программу в первый раз, я использовал просто список, на этот раз я сделаю словарь
cookie = []