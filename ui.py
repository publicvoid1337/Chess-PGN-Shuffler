from tkinter import *
from tkinter import filedialog as fd
import shuffler

#------------------------  Logic  ------------------------
def get_file_name(event):
    shuffler.FILENAME = fd.askopenfilename()
    
def overwrite_preference(event):
    shuffler.FILE_OVERWRITE = not preference.get()
#------------------------  Logic  ------------------------


#---------------------  UI-Elements  ---------------------
window = Tk()

fileSelecter = Button(window, text='Select a PGN File', fg='black')
fileSelecter.place(x=80, y=20)
fileSelecter.bind('<Button-1>', get_file_name)
fileSelecter.bind('<Button-2>', get_file_name)

preference = BooleanVar()
fileOverwritePreference = Checkbutton(window, text = 'Overwrite original File', variable=preference)
fileOverwritePreference.place(x=60, y=95)
fileOverwritePreference.bind('<Button-1>', overwrite_preference)
fileOverwritePreference.bind('<Button-2>', overwrite_preference)

scriptStart = Button(window, text='Shuffle!', fg='black', height= 2, width=24)
scriptStart.place(x=40, y=130)
scriptStart.bind('<Button-1>', shuffler.shuffle)
scriptStart.bind('<Button-2>', shuffler.shuffle)

window.title('PGN Shuffler')
window.geometry('300x200+10+20')
window.mainloop()
#---------------------  UI-Elements  ---------------------