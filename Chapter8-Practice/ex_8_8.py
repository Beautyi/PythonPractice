def make_album(singer, album):
    song = {'first': singer, 'last': album}
    return song


while True:
    print("\nPlease tell me the information of the album: ")
    print("(enter 'q' at any time to quit)")
    singer_1 = input("singer")
    if singer_1 == "q":
        break
    album_1 = input("album")
    if album_1 == "q":
        break
    make_album_1 = (singer_1, album_1)
    print(make_album_1)
