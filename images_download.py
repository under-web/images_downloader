import requests
from bs4 import BeautifulSoup


def get_response(url_gen):  # принимает сгенерированый адрес для парсинга ссылок
    r = requests.get(url_gen)  # передаем в переменную ответ метода
    return r.text  # возвращаем ответ в виде текста


def get_page(page_html):  # передаем значение r.text для формирования списка урлов
    urls = []  # создаем пустой список
    soup = BeautifulSoup(page_html, 'lxml')  # создаем обьект супа передаем параметр ф-ции
    links = soup.find_all('img', class_='wallpapers__image')  # находим все ссылки с jpg на странице
    for el in links:  # в цикле ищем для каждого элемента src и извлекаем из неё ссылку
        raw_url = str(el.get('src')).replace('300x168.jpg', '1280x720.jpg')  # в теле ссылки меняем разрешение
        urls.append(raw_url)  # добавляем готовую ссылку в список urls
    return urls  # возвращаем список урлов для последующего скачивания


def get_file(url):  # ф-ция для обращения по урл и скачивания картинки
    r = requests.get(url, stream=True)  # передаем урл , указываем потоковое скачивание
    return r  # возвращаем результат


def get_name(url):  # ф-ция для переименования картинок
    name = url.split('/')[-1]  # разделяем урл по символу "/" и берем последную часть из списка по индексу(-1)
    return name  # возвращаем результат


def save_image(name, file_object):  # ф-ция сохранения файла принимаем имя и объект requests
    with open(name, 'bw') as f:  # открываем файл бинарной записью с именем name
        for chunk in file_object.iter_content(8192):  # записываем  в цикле картинку по частям объемом 8192
            f.write(chunk)  # записываем части в файл


def main():  # основная ф-ция
    print("""
    1 - 3D
    2 - Абстракция
    3 - Аниме
    4 - Арт
    5 - Вектор
    6 - Города
    7 - Еда
    8 - Животные
    9 - Космос
    10 - Любовь
    11 - Макро
    12 - Машины
    13 - Минимализм
    14 - Мотоциклы
    15 - Музыка
    16 - Праздники
    17 - Природа
    18 - Разное
    19 - Слова
    20 - Смайлы
    21 - Спорт
    22 - Текстуры
    23 - Темные
    24 - Технологии
    25 - Фэнтези
    26 - Цветы
    27 - Черный
    28 - Все
    """)
    theme = {1: 'catalog/3d',
             2: 'catalog/abstract',
             3: 'catalog/anime',
             4: 'catalog/art',
             5: 'catalog/vector',
             6: 'catalog/city',
             7: 'catalog/food',
             8: 'catalog/animals',
             9: 'catalog/space',
             10: 'catalog/love',
             11: 'catalog/macro',
             12: 'catalog/cars',
             13: 'catalog/minimalism',
             14: 'catalog/motorcycles',
             15: 'catalog/music',
             16: 'catalog/holidays',
             17: 'catalog/nature',
             18: 'catalog/other',
             19: 'catalog/words',
             20: 'catalog/smilies',
             21: 'catalog/sport',
             22: 'catalog/textures',
             23: 'catalog/dark',
             24: 'catalog/hi-tech',
             26: 'catalog/flowers',
             25: 'catalog/fantasy',
             27: 'catalog/black',
             28: 'all'}
    words = theme[int(input('Выберите номер нужной темы картинок >>> '))]
    how_pages = int(input('Введите количество страниц для скачивания(1 стр.- 15 картинок) >>>'))
    one_url = 'https://wallpaperscraft.ru/'  # целевой адрес
    page_num = 0  # начальное значение количества страниц

    while page_num != how_pages:  # цикл пока значение не равно n  продолжать работу
        url_gen = one_url + words + '/page' + str(page_num)  # собираем адрес последнее значение номер страницы
        print('Скачиваю %s страницу...' % (page_num + 1))
        for url in get_page(get_response(url_gen)):  # коротко - для каждой url в urls (get_page() -> urls)
            save_image(get_name(url), get_file(url))  # запускаем ф-цию сохранения принимающей 2 другие ф-ции
        page_num += 1  # счетчик значений страниц


if __name__ == '__main__':  # точка входа
    main()
