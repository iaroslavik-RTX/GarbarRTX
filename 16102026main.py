product = {
    "mouse": {
        "id": 1,
        "name": "Компьютерная мышь",
        "category": "Компьютерные гаджеты",
        "price": 1700,
        "quantity": 1234
    },
    "keyboard": {
        "id": 2,
        "name": "Клавиатура",
        "category": "Компьютерные гаджеты",
        "price": 4700,
        "quantity": 133
    },
    "monitor": {
        "id": 3,
        "name": "Монитор",
        "category": "Мониторы",
        "price": 8900,
        "quantity": 67
    },
    "headphones": {
        "id": 4,
        "name": "Наушники",
        "category": "Аудиотехника",
        "price": 1900,
        "quantity": 4
    },
    "web_camera": {
        "id": 5,
        "name": "Веб-камера",
        "category": "Компьютерные гаджеты",
        "price": 3300,
        "quantity": 268
    },
    "microphone": {
        "id": 6,
        "name": "Микрофон",
        "category": "Аудиотехника",
        "price": 9000,
        "quantity": 0
    },
    "speakers": {
        "id": 7,
        "name": "Колонки",
        "category": "Аудиотехника",
        "price": 5000,
        "quantity": 18
    },
    "usb_flash": {
        "id": 8,
        "name": "USB-флешка",
        "category": "Накопители",
        "price": 700,
        "quantity": 993
    }
}

print("Добро пожаловать в наш магазин!")
print("Для вывода интересующих вас вопросов используйте следующие команды")
print("Введите: task1 - для вывода ассортимента")
print("Введите: task2 - для поиск товаров")
print("Введите: task3 - для фильтрация по категории")
print("Введите: task4 - для работы с остатками на складе")
print("Введите: task5 - для изменение количества товара")
print("Введите: task6 - для продажи товара")
print("Введите: task7 - для статистики магазина")
print("Введите: task8 - для сортировка товаров")
print("Введите: task9 - для меню программы")

taskEditor = (input("Введите задание: "))

#Задание №1
def task1():
    print("Вот наш полный ассортимент: ", product)
    print("Общая стоимость товаров на нашем складе: ", (product["mouse"]["price"] * product["mouse"]["quantity"])
            + (product["keyboard"]["price"] * product["keyboard"]["quantity"]) 
            + (product["monitor"]["price"] * product["monitor"]["quantity"]) 
            + (product["headphones"]["price"] * product["headphones"]["quantity"]) 
            + (product["web_camera"]["price"] * product["web_camera"]["quantity"]) 
            + (product["microphone"]["price"] * product["microphone"]["quantity"]) 
            + (product["speakers"]["price"] * product["speakers"]["quantity"]) 
            + (product["usb_flash"]["price"] * product["usb_flash"]["quantity"]))

# Задание №2
def task2():
    searchName = input("Введите название товара: ").lower()
    found = False

    for p in product.values():
        if searchName in p["name"].lower():
            print("ID:", p["id"])
            print("Название:", p["name"])
            print("Категория:", p["category"])
            print("Цена:", p["price"], "руб.")
            print("Количество:", p["quantity"])
            print("--------------------")
            found = True

    if found == False:
        print("Товар не найден")

# Задание №3
def task3():
    categories = set()

    for p in product.values():
        categories.add(p["category"])

    print("Все категории:", categories)

    searchCategory = input("Введите категорию: ").lower()
    found = False

    for p in product.values():
        if p["category"].lower() == searchCategory:
            print("Название:", p["name"])
            print("Цена:", p["price"], "руб.")
            print("Количество:", p["quantity"])
            print("--------------------")
            found = True

    if found == False:
        print("В данной категории товаров нет")

# Задание №4
def task4():
    print("Товаров нет на складе:")

    for p in product.values():
        if p["quantity"] == 0:
            print(p["name"], "-", p["quantity"], "шт.")

    print("Товаров меньше 5 единиц:")

    for p in product.values():
        if p["quantity"] > 0 and p["quantity"] < 5:
            print(p["name"], "-", p["quantity"], "шт.")

    print("Товаров 5 единиц или больше:")

    for p in product.values():
        if p["quantity"] >= 5:
            print(p["name"], "-", p["quantity"], "шт.")

# Задание №5
def task5():
    try:
        productId = int(input("Введите ID товара: "))
        amount = int(input("Введите количество для пополнения: "))

        if amount <= 0:
            print("Количество должно быть положительным числом")
            return

        for p in product.values():
            if p["id"] == productId:
                p["quantity"] = p["quantity"] + amount

                print("Склад успешно пополнен!")
                print("Название:", p["name"])
                print("Цена:", p["price"], "руб.")
                print("Новое количество:", p["quantity"])
                return

        print("Товар с таким ID не найден")

    except ValueError:
        print("Ошибка! Введите целое число")

# Задание №6
def task6():
    try:
        productId = int(input("Введите ID товара: "))
        amount = int(input("Введите количество для продажи: "))

        if amount <= 0:
            print("Количество должно быть положительным числом")
            return

        for p in product.values():
            if p["id"] == productId:
                if p["quantity"] >= amount:
                    p["quantity"] = p["quantity"] - amount
                    totalPrice = p["price"] * amount

                    print("Продажа успешно выполнена!")
                    print("Товар:", p["name"])
                    print("Количество:", amount)
                    print("Итоговая стоимость:", totalPrice, "руб.")
                    print("Остаток на складе:", p["quantity"])
                else:
                    print("Недостаточно товара на складе")
                return

        print("Товар с таким ID не найден")

    except ValueError:
        print("Ошибка! Введите целое число")

# Задание №7
def task7():
    print()


# Задание №8
def task8():
    print("1 - Сортировка по цене от меньшей к большей")
    print("2 - Сортировка по цене от большей к меньшей")
    print("3 - Сортировка по названию")
    print("4 - Сортировка по количеству на складе")

    choice = input("Выберите способ сортировки: ")

    if choice == "1":
        sortedProducts = sorted(product.values(), key=lambda p: p["price"])
    elif choice == "2":
        sortedProducts = sorted(product.values(), key=lambda p: p["price"], reverse=True)
    elif choice == "3":
        sortedProducts = sorted(product.values(), key=lambda p: p["name"].lower())
    elif choice == "4":
        sortedProducts = sorted(product.values(), key=lambda p: p["quantity"])
    else:
        print("Неверный пункт сортировки")
        return

    for p in sortedProducts:
        print(p["name"], "-", p["price"], "руб.", "- Остаток:", p["quantity"])

# Задание №9
def task9():
    status = True

    while status:
        print("\n--- ГЛАВНОЕ МЕНЮ ---")
        print("1 - Показать все товары")
        print("2 - Найти товар по названию")
        print("3 - Показать товары по категории")
        print("4 - Проверить остатки на складе")
        print("5 - Пополнить склад")
        print("6 - Продать товар")
        print("7 - Показать статистику")
        print("8 - Отсортировать товары")
        print("9 - Завершить программу")

        choice = input("Выберите действие: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "6":
            task6()
        elif choice == "7":
            task7()
        elif choice == "8":
            task8()
        elif choice == "9":
            print("Работа программы завершена")
            status = False
        else:
            print("Неизвестный пункт меню. Попробуйте ещё раз")

#Дополнительно
status = True
while status:
    if taskEditor == "task1":
        task1() 
        if (input("Еще раз?") != "Да"):
            status = False  
    elif taskEditor == "task2":
        task2()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task3":
        task3()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task4":
        task4()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task5":
        task5()
        if (input("Еще раз?") != "Да"):
            status = False
    elif taskEditor == "task6":
        task6()
        if (input("Еще раз?") != "Да"):
            status = False
    elif taskEditor == "task7":
        task7()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task8":
        task8()
        if (input("Еще раз?") != "Да"):
            status = False 
    elif taskEditor == "task9":
        task9()
        if (input("Еще раз?") != "Да"):
            status = False 
    else:
        print("Не удалось понять задачу")
        if (input("Еще раз?") != "Да"):
            status = False 