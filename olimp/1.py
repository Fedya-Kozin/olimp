import csv

d1, m1, y1 = 12, 5, 2023


def res(d, m, y, d1, m1, y1):
    '''
    Функция считает разнуцу между двумя датами
    :param d: день 1 даты
    :param m: месяц 1 даты
    :param y: год 1 даты
    :param d1: день 2 даты
    :param m1: месяц 2 даты
    :param y1: год 2 даты
    :return: Разницу между днями в днях
    '''
    if y == y1:
        if m == m1:
            return abs(d - d1)
        else:
            return abs(m - m1) * 30 + abs(d - d1)
    else:
        return abs(m - m1) * 30 + abs(d - d1) + abs(y - y1) * 360 * 30


def break_streams():
    """
    Функция выводит в формате “<Название песни> - <артист> - <кол-во прослушиваний>” тех песен,
    которые были выпущены не позже 01.01.2002.
    Но также если количество песен оказалось 0, то счиитает количество песен по формуле,
    создаёт новый фал со всеми значениями.
    :return:
    """
    with open('songs_new.csv', 'w', encoding='utf-8', newline='') as file:
        with open('songs.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            w = csv.writer(file)
            w.writerow(['streams', 'artist_name', 'track_name', 'date'])
            for row in reader:
                name_art = row['artist_name']
                name_song = row['track_name']
                d, m, y = map(int, row['date'].split('.'))
                streams = row["\ufeffstreams"]
                if y < 2002:
                    print(f'{name_song} - {name_art} - {streams}')
                if streams == '0':
                    streams = abs((res(d, m, y, d1, m1, y1)) // (len(name_art) + len(name_song))) * 10000
                w.writerow([streams, row['artist_name'], row['track_name'], row['date']])


break_streams()
