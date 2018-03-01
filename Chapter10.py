from tkinter import*

root = Tk()
root.title('Название окна')
root.geometry('200x100')
app = Frame(root)
app.grid()
test = input('Введи меня')
lbl = Label(app, text = test)
lbl.grid()
bttn1 = Button(app, text = 'Я ничего не делаю :D') # Создаем оконо по аналогии с меткой
bttn1.grid() # Вызываем копку
bttn2 = Button(app) # Можно создать пустую кнопку и задавть ей значение при вызове
bttn2.grid()
bttn2.configure(text = 'Я кнопка с конфигурацией')
bttn3 = Button(app)
bttn3.grid()
bttn3['text'] = 'Иной метод' # Данный метод подобен вызову по словарю, вызывается конкретный метод по ключу
root.mainloop()