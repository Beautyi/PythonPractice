def make_album(singer, album):
    song = {'first': singer, 'last': album}
    return song


song_1 = make_album('Tim', 'aaa')
print(song_1)


def make_album(singer, album, number=' '):
    song = {'first': singer, 'last': album}
    if number:
        song['number'] = number
    return song


song_1 = make_album('Tim', 'aaa', number = 6)
print(song_1)