# ===============================================[ ШПОРА ]==============================================================
# Данная замтека будет служить фиксацией знаний полученных из книги
# Тут содержаться фрагменты кода, и мои коментарии к нему.

'''
                                   Работа с классами и инкапсуляцией

Класс это фрагмент кода в котором обявлены
атрибуты(характеристики) и методы(способ поведения/умение). Классы подобны чертежам - это НЕ объект Но схема объекта !

Параметр self автоматичиски становиться ссылкой на объект по отнашению к которому вызван метод.

Класссы принято называть с Болшой буквы !
'''

# ===============================================[ ГЛАВА 9 ]============================================================
'''
                                  ОБЪЕКТНОРИЕНТИРОВАНННОЕ ПРОГРАММИРОВАНИЕ 
'''

# Терминалогия: ['Отправка сообщения' - объекты вызывают методы друг-друга]
# Пример работы метода приведен ниже.

class Player(object):
    """ A player in a shooter game. """
    def blast(self, enemy): # Функция принимает в себя Цель которой в данном случае является Alien
        # Так называемая 'Отправка сообщения происходит посредствам команды' hero.blast(invader)
        print("The player blasts an enemy.\n")
        enemy.die() # данный метод будет вызывать атрибут внутри класса Alien
        # enemy в данном случае будет Alien следовательно после точки будет вызван метод его функции

class Alien(object):
    """ An alien in a shooter game. """
    def die(self):
        print("The alien gasps and says, 'Oh, this is it.  This is the big one. \n" \
              "Yes, it's getting dark now.  Tell my 1.6 million larvae that I loved them... \n" \
              "Good-bye, cruel universe.'")

# main
print("\t\tDeath of an Alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)
# ----------------------------------------------------------------------------------------------------------------------
'''
                                              [ НАСЛЕДОВАНИЕ ]
'''


# class Name(ClassName) имя наследуюемого класса помощается внутрь скобок
# Переопределением метод называют изменение унаследованного метода
# Полиформизм это когда предметы одной группы неоднакртано реагируют наодну и туже операцию,
# в конктексте ООП это означает что одно и тоже сообщение можно посылать бъекам разных классов

class Positionable_Card(Card):
    """ Функция позволяет определить положение карты Лицом/Рубашкой вверх """
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit) # функция super вызывает метод Базавого класса
        # Такие функции называются НАДклассом
        self.is_face_up = face_up



# Конструкция запуска модуля только через себя
# [ if __name__ == "__main__": ]
# Истинно только тогда когда программа запускается напрямую а НЕ импортируется !

# ======================================================================================================================
# ==============================================[ РАБОТА С GUI ]========================================================

from tkinter import* # Импортируем всю библиотеку ткинтер

root = Tk() # Создает окно
root.title('Название окна') # Заголовок окна печтаеться справа от кнопок (свернуть, рзавернуть, закрыть)
root.geometry('500x500') # Размер окна в px
app = Frame(root) # 'Рамка' элмент внутри которого могут распологаться другие элменты (как второе окно внутри основго)
# Необходимо передать родительский элемент в данном случае root
app.grid() # Вызываем метод (grid отвечает ща вызов и размещение элементов в окне)
lbl = Label(app, text = 'Это метка внутри окна') # Создаем объект Метку, в скобка указана первым параметром Рамка
# А вторым содержимое.
lbl.grid()
bttn1 = Button(app, text = 'Я ничего не делаю :D') # Создаем оконо по аналогии с меткой
bttn1.grid() # Вызываем копку

bttn2 = Button(app) # Можно создать пустую кнопку и задавть ей значение при вызове
bttn2.grid()
bttn2.configure(text = 'Я кнопка с конфигурацией')

bttn3 = Button(app)
bttn3.grid()
bttn3['text'] = 'Иной метод' # Данный метод подобен вызову по словарю, вызывается конкретный метод по ключу
root.mainloop() # Запуск основного цикла *выводит окно !
# ----------------------------------------------------------------------------------------------------------------------
'''
                                    Реализация GUI с помощью класса
'''


class Application(Frame): # Наследуем класс от Frame который есть в библеотке ткинтер
    ''' Если представлять себе абстракцию то этот класс всего лишь РАМКА с определёнными парметрами'''
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self): # Класс пеюредающий и создающий по параметрам Окна
        # create first button
        self.bttn1 = Button(self, text="I do nothing!")
        self.bttn1.grid()

        # create second button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Me too!")

        # create third button
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"


# main
root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root) # Таким образом мы инстанцируем класс Apl* с рюодительским элементом root
root.mainloop()