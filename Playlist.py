"""Create a Playlist class that holds a list of songs.
Implement the __len__ method so that len(obj) returns the number of songs."""


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)


new_playlist = Playlist()
new_playlist.add_song(input())
new_playlist.add_song(input())
new_playlist.add_song(input())
print(len(new_playlist))
