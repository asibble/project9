#Q1: Music Playlist
import random, webbrowser, os, json


class Song:
    def __init__(self, title, artist, url):
        self.title = title
        self.artist = artist
        self.url = url
    def play(self):
        return webbrowser.open(self.url)

class Playlist:
    def __init__(self="", name="", songs={}):
        self.name = name
        self.songs = songs
        self.list=[]
        self.current_song=0
    def list_songs(self):
        for i in self.songs:
            self.list.append(i.title())
    def list_order(self):
        print("Playlist:")
        for i in range(len(self.list)):
            print(str(i+1)+". "+self.list[i])
        print("")
    def next_song(self):
        if self.current_song >=int(len(self.list)):
            self.current_song=0
        self.current_song +=1 
        return self.songs[self.list[(self.current_song-1)]]                
    def include(self, new_song):
        self.songs[new_song.title]=new_song
        self.list.append(new_song.title)
        print (new_song.title+" by " +new_song.artist+" added.")
    def import_list(self, songlist):
        for i in songlist:
            self.include(Song(i["title"], i["artist"], i["url"]))
    def shuffle(self):
        random.shuffle(self.list)
#Includes songs in different file
print("Which playlist would you like to play?")
playlists=[]
for file in os.listdir():
    if "json" in file:
        playlists.append(file)
for i in range(len(playlists)):
    print("  ", str(i+1)+".", playlists[i])
targetlist=playlists[int(input("> "))-1]
with open(targetlist) as fp:
    songs_list = json.load(fp)

playlist = Playlist()
playlist.import_list(songs_list)
playlist.include(Song('Bad Romance', 'Lady Gaga', 'https://youtu.be/qrO4YZeyl0I'))
playlist.include(Song('America', 'Simon and Garfunkel', 'https://youtu.be/Eo2ZsAOlvEM'))
playlist.include(Song('Mystery', 'Mysterious Artist', 'https://youtu.be/dQw4w9WgXcQ'))
playlist.shuffle()
#Added the method below to show the contents and order of the playlist
playlist.list_order()
playlist.shuffle()
playlist.list_order()
while True:
    song = playlist.next_song()
    print("Starting {} by {}...".format(song.title, song.artist))
    song.play()
    action = input("'q' to quit; 'new' to include another song; anything else for next song: ")
    if action == 'q':
        break
    #Adds new song in command line 
    elif action == 'new':
        print("")
        title=input("What is the name of the song? ")
        artist=input("What is the name of the artist? ")
        url=input("What is the url of the song? ")
        playlist.include(Song(title, artist, url))
        print("")
        playlist.list_order()
        continue
        