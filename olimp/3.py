import csv


def finder35():
    '''
    Функция запрашивет имя артиста, если такой артист есть в таблице,
    то возращает название его песни, если же артиста нет в таблице,
    то функция возвращает “К сожалению, ничего не удалось найти”.
    Программа завершает своё действие если было получено 0.
    :return:
    '''
    i = input()
    with open('songs.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        track = ''
        if i == '0':
            return None
        else:
            for row in reader:
                if i == row['artist_name']:
                    track = f'У {row["artist_name"]} найдена песня: {row["track_name"]}'
            if track != '':
                print(track)
                finder35()
            else:
                print('К сожалению, ничего не удалось найти')
                finder35()


finder35()
