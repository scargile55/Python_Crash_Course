def make_album(artist, title, songs=None):
    album = {
    'Artist': artist,
    'Title': title
    }

    if songs:
        album['Songs'] = songs

    return album

while True:
    artist = input("Enter an artist (or quit): ")

    if artist == 'quit':
        break
    title = input("Enter an album title: ")
    print(make_album(artist, title))