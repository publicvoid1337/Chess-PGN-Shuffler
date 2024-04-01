from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import shuffler

#------------------------  Logic  ------------------------
def get_file_name():
    # Reset preferences
    shuffler.MERGE_FILES = False
    shuffler.FILE_OVERWRITE = False
    mergeFilesPreference.set(False)
    fileOverwritePreference.set(False)
    
    # Open filedialog
    shuffler.FILENAMES = fd.askopenfilenames()
    
    match len(shuffler.FILENAMES):
        case 0:
            # Disable all buttons and throw warning
            mb.showwarning('Warning', 'Please select one or more Files')
            mergeFilesPreferenceButton.configure(state='disabled')
            fileOverwritePreferenceButton.configure(state='disabled')
            scriptStartButton.configure(state='disabled')
        case 1:
            # Disable merge button (because there is only one file) and enable overwrite button
            mergeFilesPreferenceButton.configure(state='disabled')
            fileOverwritePreferenceButton.configure(state='normal', text='Overwrite original File')
            scriptStartButton.configure(state='normal')
        case _:
            # Enable all buttons
            mergeFilesPreferenceButton.configure(state='normal')
            fileOverwritePreferenceButton.configure(state='normal', text='Overwrite original Files')
            scriptStartButton.configure(state='normal')

     
def merge_files_preference_changed():
    shuffler.MERGE_FILES = mergeFilesPreference.get()
    
    # File overwrite and merging are mutually exclusive
    if shuffler.MERGE_FILES:
        fileOverwritePreferenceButton.configure(state='disabled')
    else:
        fileOverwritePreferenceButton.configure(state='normal')


def overwrite_files_preference_changed():
    shuffler.FILE_OVERWRITE = fileOverwritePreference.get()
    
    # File overwrite and merging are mutually exclusive
    if shuffler.FILE_OVERWRITE:
        mergeFilesPreferenceButton.configure(state='disabled')
    elif not shuffler.FILE_OVERWRITE and len(shuffler.FILENAMES) > 1:
        mergeFilesPreferenceButton.configure(state='normal')
        
#------------------------  Logic  ------------------------


#---------------------  UI-Elements  ---------------------
window = Tk()

fileSelecter = Button(window, text='Select PGN Files', fg='black', command=get_file_name)
fileSelecter.place(x=80, y=20)

mergeFilesPreference = BooleanVar()
mergeFilesPreferenceButton = Checkbutton(window, text='Merge Files', variable=mergeFilesPreference, state='disabled', command=merge_files_preference_changed)
mergeFilesPreferenceButton.place(x=60, y=65)

fileOverwritePreference = BooleanVar()
fileOverwritePreferenceButton = Checkbutton(window, text='Overwrite original File(s)', variable=fileOverwritePreference, state='disabled', command=overwrite_files_preference_changed)
fileOverwritePreferenceButton.place(x=60, y=95)

scriptStartButton = Button(window, text='Shuffle!', fg='black', height= 2, width=24, state='disabled')
scriptStartButton.place(x=40, y=130)
scriptStartButton.bind('<Button-1>', shuffler.shuffle)

window.title('PGN Shuffler')
window.geometry('300x200+10+20')
window.mainloop()
#---------------------  UI-Elements  ---------------------