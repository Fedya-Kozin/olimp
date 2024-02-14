import csv
d=dict()
with open('songs.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    dict_artists=[]
    for row in reader:
        for i in dict_artists:
            if row['artist_name'] not in i[0]:
                dict_artists.append([row['artist_name'],0])


    print(dict_artists)