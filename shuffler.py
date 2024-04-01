import random as rnd
from tkinter import messagebox as mb
import chess.pgn as pgn
import os


FILENAME = ''
FILE_OVERWRITE = False

def shuffle(event):
    if not FILENAME:
        mb.showwarning('Error', 'No File selected') 
        return
    
    data = open(FILENAME, encoding='latin-1')
    
    games = []
    game = pgn.read_game(data)
    
    while game is not None:
        games.append(game)
        game = pgn.read_game(data)
    
    rnd.shuffle(games)
        
    if FILE_OVERWRITE:
        newFile = open(FILENAME, 'w', encoding='utf-8')
    else:
        newFile = open(f'{os.path.splitext(FILENAME)[0]}_shuffled{os.path.splitext(FILENAME)[1]}', 'w', encoding='utf-8')

    exporter = pgn.FileExporter(newFile)
    for game in games:
        game.accept(exporter)
  
    mb.showinfo('Complete', 'Games shuffled!')