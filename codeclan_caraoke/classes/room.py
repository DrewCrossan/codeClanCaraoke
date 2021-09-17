from classes.guest import Guest

class Room:

    def __init__(self, room_name, capcity, entry_fee):
        self.room = room_name
        self.songs = []
        self.guests = []
        self.capcity = capcity
        self.entry_fee = entry_fee
        self.room_money = 0

    def check_in_guest(self, guest):
        if self.is_room_full() or guest.wallet < self.entry_fee:
            return "Sorry this room is full, please try another"
        self.guests.append(guest)
        # self.total()

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