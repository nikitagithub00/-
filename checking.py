print("Привет зарегистрируйтесь на нашем системе для дальшего использования!")
name = input("Введите ваше имя\n>")
age = int(input("Отлично, теперь введите свой возраст\n>"))
email = input("Осталось совсем немного...\n Введите свой email\n>")
password = input("Введите свой пароль\n>")
password1 = input("Введите снова свой пароль\n>")
if password1 != password:
    while(password1 != password):
        print("Пароли не совпадают!")
        password1 = input("Введите снова свой пароль\n>")

print("Отлично! Вы зарегистрироваоись в нашей системе:3")
print("Желаете войти в систему?(Напишите 1 либо 2)\n1.Да\n2.Нет(Выйти)")
check = int(input('\n>'))
if check == 1:
    a = input("Введите свой email(который вы указывали при регистрации)\n>")
    if a != email:
        print("Неверный email")
        while(a != email):
            a = input("Введите свой email(который вы указывали при регистрации)\n>")
    b = input("Введите пароль\n>")
    if b != password:
        print("Пароль неверен(Попробуйте снова)")
        while (b != password):
            b = input("Введите пароль\n>")
    if a == email and b == password:
        print("Добро пожаловать!!!")
if check == 2:
    exit()