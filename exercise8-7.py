#8-7 Album: Write a function called make_album() that builds a dictionary describing a music album.
#The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
#Use the function to make three dictionaries representing different albums.
#Print each return value to show that the dictionaries are storing the album information correctly.
#Add an optional parameter to make_album() that allows to store the number of tracks on an album.
#If the calling line includes a value for the number of tracks add that value to the album's dictionary.
#Make at least one new function call that includes the number of tracks on an album.

def make_album(name, title, tracks=''):
    """Display album name, artist and number of tracks"""
    album = {'artist_name': name, 'album_title': title, 'tracks_number': tracks}
    return album

print(make_album('men i trust', 'show me how'))
print(make_album('daft punk', 'random access memories', 13))
print(make_album('death and vanilla', 'are you a dreamer?'))
print(make_album('potsu', 'just friends', 23))
