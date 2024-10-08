#Система управління музичною колекцією:
#Створіть клас "Пісня" з атрибутами: назва, виконавець, альбом, рік випуску, жанр, тривалість. 
# Розробіть клас "Плейлист", який містить список пісень та має назву. Потім створіть клас "МузичнаБібліотека", 
# який використовує словник для зберігання всіх пісень (ключ - унікальний ідентифікатор пісні) 
# та список для зберігання плейлистів.

class Song:
    def __init__(self, title,artist,  album, release_year, genre, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.release_year = release_year
        self.genre = genre
        self.duration = duration

    def __repr__(self):
        return f"'{self.title}' by {self.artist} from album '{self.album}' ({self.release_year}) [{self.genre}] - {self.duration} minutes"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs_list = []

    def add_song(self, song):
        self.songs_list.append(song)

    def remove_song(self, song_title):
        self.songs_list = [song for song in self.songs_list if song.title != song_title]

    def show_songs(self):
        return self.songs_list

    def __repr__(self):
        return f"Playlist '{self.name}' with {len(self.songs_list)} songs"


class MusicLibrary:
    def __init__(self):
        self.songs = {}
        self.playlists = []

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def show_playlists(self):
        return self.playlists


def menu():
    song1 = Song("Song 1", "Artist A", "Album X", 2020, "Pop", 3.5)
    song2 = Song("Song 2", "Artist B", "Album Y", 2019, "Rock", 4.0)
    song3 = Song("Song 3", "Artist C", "Album Z", 2021, "Jazz", 5.0)
    
    library = MusicLibrary()
    library.songs[1] = song1
    library.songs[2] = song2
    library.songs[3] = song3

    playlist = Playlist("Favorites")
    library.add_playlist(playlist)

    while True:
        print("\nMenu:")
        print("1. Show all songs")
        print("2. Show all playlists")
        print("3. Add a song to the playlist")
        print("4. Remove a song from the playlist")
        print("5. Show songs in the playlist")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            print("\nAll Songs in Library:")
            for song_id, song in library.songs.items():
                print(f"{song_id}. {song}")

        elif choice == '2':
            print("\nAll Playlists:")
            for playlist in library.show_playlists():
                print(playlist)

        elif choice == '3':
            song_id = int(input("Enter the ID of the song to add: "))
            song = library.songs.get(song_id)
            if song:
                playlist.add_song(song)
                print(f"Song '{song.title}' added to playlist '{playlist.name}' successfully!")
            else:
                print("Song not found.")

        elif choice == '4':
            song_title = input("Enter the title of the song to remove: ")
            playlist.remove_song(song_title)
            print(f"Song '{song_title}' removed from playlist '{playlist.name}' successfully!")

        elif choice == '5':
            print(f"\nSongs in Playlist '{playlist.name}':")
            for song in playlist.show_songs():
                print(f"  - {song}")

        elif choice == '6':
            break

        else:
            print("Invalid choice, please try again.")
menu()



