from classes.guest import Guest
from classes.song import Song


class Room:
    def __init__(self, room_name, capcity, entry_fee):
        self.room = room_name
        self.songs = []
        self.guests = []
        self.capcity = capcity
        self.entry_fee = entry_fee
        self.room_money = 0

    def check_in_guest(self, guest):
        if self.is_room_full():
            return "Sorry this room is full, please try another"
        elif guest.wallet < self.entry_fee:
            return "Sorry, you don't have enough money"
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)

    def is_room_full(self):
        if len(self.guests) >= self.capcity:
            return "Sorry this room is full"
        return False

    def guest_favourite_song(self, guest):
        for song in self.songs:
            if song == guest.fav_song:
                return "Whoo!"

    def add_money_to_room(self):
        self.room_money += self.entry_fee

    def request_a_song(self):
        artist = input("Please enter an Artist: ")
        song = input("Please enter a Song: ")
        requested_song = Song(song, artist)
        self.add_song_to_room(requested_song)
