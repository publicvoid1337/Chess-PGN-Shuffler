import random as rnd
from tkinter import messagebox as mb
import chess.pgn as pgn
import os


FILENAMES = None
MERGE_FILES = None
FILE_OVERWRITE = None
HEADER_OVERWRITE = None


def wrapper():
    __shuffle()
    mb.showinfo('Complete', 'Games shuffled!')

def __shuffle():
    allGames = []
    
    for file in FILENAMES:
        currFile = open(file, encoding='latin-1')
        
        games = []
        game = pgn.read_game(currFile)
        while game is not None:
            games.append(game)
            game = pgn.read_game(currFile)
        
        rnd.shuffle(games)
        allGames.append(games)
    print(HEADER_OVERWRITE)
    
    if MERGE_FILES:
        allGamesMerged = sum(allGames)
        newFile = open(f'{os.path.dirname(FILENAMES[0])}merged{os.path.splitext(FILENAMES[0])[1]}', 'w', encoding='utf-8')        
        exporter = pgn.FileExporter(newFile)
        for game in allGamesMerged:
            if HEADER_OVERWRITE:
                for header in game.headers:
                    game.headers[header] = '?'
            game.accept(exporter)
        return

    if FILE_OVERWRITE:
        for i, games in enumerate(allGames):
            newFile = open(FILENAMES[i], 'w', encoding='utf-8')
            exporter = pgn.FileExporter(newFile)
            for game in games:
                if HEADER_OVERWRITE:
                    for header in game.headers:
                        game.headers[header] = '?'
                game.accept(exporter)
        return
    else:
        for i, games in enumerate(allGames):
            newFile = open(f'{os.path.splitext(FILENAMES[i])[0]}_shuffled{os.path.splitext(FILENAMES[i])[1]}', 'w', encoding='utf-8')
            exporter = pgn.FileExporter(newFile)
            for game in games:
                if HEADER_OVERWRITE:
                    for header in game.headers:
                        game.headers[header] = '?'
                game.accept(exporter)
        return

def __overwrite_header(header):
    pass #TODO