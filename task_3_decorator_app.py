import requests
from datetime import datetime


def log(file_path):
    def log_inner(function):
        def new_function(*args, **kwargs):
            func_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = function.__name__
            result = function(*args, **kwargs)
            with open(f"{file_path}", 'a', encoding='UTF-8') as file:
                file.write(f'Дата и время вызова функции: {func_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args}\n'
                           f'Результат: {result}\n'
                           f'---\n')
            return result
        return new_function
    return log_inner


@log('log.txt')
def get_smartest_superhero(hero_list):
    API_BASE_URL = 'https://superheroapi.com/api/2619421814940190'
    hero_dict = {}
    for hero in hero_list:
        req = requests.get(API_BASE_URL + '/search/' + hero)
        hero_dict[hero] = int(req.json()['results'][0]['powerstats']['intelligence'])
    result = max(hero_dict, key=hero_dict.get)
    print(f'Самый умный супергерой - {result}')
    return result


get_smartest_superhero(['Hulk', 'Captain America', 'Thanos'])
