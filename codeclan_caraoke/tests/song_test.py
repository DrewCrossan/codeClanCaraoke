import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Big Pimpin'", "JayZ")

    def test_create_song(self):
        self.assertEqual("Big Pimpin'", self.song.song)
        self.assertEqual("JayZ", self.song.artist)
