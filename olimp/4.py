import csv


def artist():
    '''
    Функция создаёт два текстовых документа russian_artists.txt и foreign_artists.txt,
    в которых содержаться имена исполнителей на русском языке и иностранном языке соответственно.
    Для этого функция проверяет есть ли имя артиста уже в файле, если нет, то добавляет его в текстовый  документ и увеличивает количество исполнителей на 1.
    :return: Количество российских и иностранных исполнителей
    '''
    kirl = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    with open('songs.csv', 'r', encoding='utf-8') as f:
        russian_artists = open('russian_artists.txt', 'w', encoding='utf-8')
        foreign_artists = open('foreign_artists.txt', 'w', encoding='utf-8')
        reader = csv.DictReader(f, delimiter=';')
        artist = set()
        russian_artists_sum = 0
        foreign_artists_sum = 0
        for row in reader:
            if row['artist_name'] not in artist:
                simbol_name = [str(i) for i in row['artist_name'] if i in kirl]
                if len(simbol_name) > 0:
                    russian_artists.write(row['artist_name'] + '\n')
                    russian_artists_sum += 1
                else:
                    foreign_artists.write(row['artist_name'] + '\n')
                    foreign_artists_sum += 1
                artist.add(row['artist_name'])
            else:
                continue
        print(f'Количество российских исполнителей: {russian_artists_sum}')
        print(f'Количество иностранных исполнителей: {foreign_artists_sum}')


artist()
