

# Домашнее задание по уроку "Пространство имен"

def test_function():
    # Функция inner_function находится в области видимости test_function
    def inner_function():
        print("Я в области видимости функции test_function")


    inner_function()

test_function()     # функция inner_function() будет вызвана

# inner_function()  # функция inner_function() не будет вызвана


'''''
функция inner_function() локальна и ее область видимости ограничена функцией test_function()
вызвать функцию глобально невозможно. 

'''''







