from classes.song import Song


class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def wallet_reduced(self, room):
        self.wallet -= room.entry_fee
