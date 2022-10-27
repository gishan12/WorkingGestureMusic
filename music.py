from IPython.display import Audio
from pretty_midi import PrettyMIDI
import music21
from musicalbeeps import Player, script
import os
from pygame import mixer
import time

class composition:
    def __init__(self, score_name: str = 'music', time_signature: str = '4/4', note_length: str = '1/4', tempo: int = 120, key: str = 'C', volume: float = 0.5) -> None:
        self.name = score_name
        self.time_signature = time_signature
        self.note_length = note_length
        self.key = key
        self.tempo = tempo
        self.player = Player(volume = volume, mute_output = True)
        self.duration = 60 / self.tempo
        self.notes = []

    def change_volume(self, volume: float = 0.5):
        self.player = Player(volume = volume)

    #def record_note(self, note: str, octave: int = 4):

    def play_note(self, note: str, octave: int = 4):
        if len(note) == 1:
            note = '{}{}'.format(note, octave)
        else:
            note = '{}{}{}'.format(note[0], octave, note[1])

        self.player.play_note(note, self.duration)
        self.notes.append(note)
        
    def play_full(self):
        for note in self.notes:
            self.player.play_note(note, self.duration)

    def export_full(self, style: str = 'txt'):
        if style == 'txt':
            with open('{}.txt'.format(self.name), 'a') as file:
                for note in self.notes:
                    file.write('{}:{}'.format(note, round(self.duration, 2)))
        else:
            pass


class score:
    def __init__(self, score_name: str = 'music', time_signature: str = '4/4', note_length: str = '1/4', tempo: int = 120, key: str = 'C', volume: float = 0.5) -> None:
        self.name = score_name
        self.time_signature = time_signature
        self.note_length = note_length
        self.key = key
        self.tempo = tempo
        self.duration = 0
        self.notes = []
        self.folder = os.path.join(os.getcwd(), 'Notes')
        self.new_note = None
        self.change = True
        mixer.init()

    '''
    def load_notes(self):
        notes = os.listdir(self.folder)
        for note in notes:
            file = os.path.join(self.folder, note)
            note_name = note.split('.')[0]
            self.player[note_name] = mixer.init()
    '''

    def read_input(self, note: str):
        if note != self.new_note:
            self.change = True
            self.new_note = note
        else:
            self.change = False


    def play(self):
        while True:
            if self.change == True:
                mixer.music.stop()
                mixer.music.load(os.path.join(self.folder,'{}.mp3'.format(self.new_note)))
                mixer.music.play()

            time.sleep(self.duration)

'''
comp = composition(volume = 0.5, tempo = 180)
script.player_loop('furelise.txt')
'''