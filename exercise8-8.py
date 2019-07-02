#8-8 User album: Start with your program from exercise8-7. Write a while loop that allows users to enter an album's artist and title.
#Once you have that information. call make_album() with the user's input and print the dictionary that's created.
#Be sure to include a quit value in the while loop.

def make_album(name, title, tracks=''):
    """Display album name, artist and number of tracks"""
    album = {'artist_name': name.title(), 'album_title': title.title(), 'tracks_number': tracks}
    return album

while True:
    title = input("Enter an album title: \n(type 'q' to quit the program) ")
    if title == 'q':
        break
    artist = input("Enter the artist's name of the album; \n(type 'q' to quit the program) ")
    if artist == 'q':
        break
    user_album = make_album(artist, title)
    print(user_album)
