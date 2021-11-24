from datetime import datetime


def logger(function):
    def new_function(*args, **kwargs):
        func_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_name = function.__name__
        result = function(*args, **kwargs)
        with open('log.txt', 'a', encoding='UTF-8') as file:
            file.write(f'Дата и время вызова функции: {func_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args}\n'
                       f'Результат: {result}\n'
                       f'---\n')
        return result
    return new_function


@logger
def multiply(a, b):
    result = a * b
    return result


multiply(3, 3)
multiply(4, 10)
