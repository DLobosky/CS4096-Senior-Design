from Tkinter import *
from ScrolledText import *
import ttk


def downloadFile(*args):
    try:
        value = fileName.get()
        Kb.set(value)
    except ValueError:
            pass
def showFileSize(*args):
    try:

    except ValueError:
            pass

root = Tk()
root.title("File Download from server")



mainframe = ttk.Frame(root, padding="3 3 12 12", width=20, height=20)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
textPad = ScrolledText(mainframe, width=50, height=10)
text = '''\
    FileName 1: Man who drive like hell
    FileName 2: Man who run in front of car
    FileName 3: Man who run behind car
    FileName 4: The Internet
    '''
textPad.insert('insert', text)
textPad.pack(fill='both', expand=True, padx=8, pady=8)

Kb = StringVar()
fileName = StringVar()

fileName_entry = ttk.Entry(mainframe, width=7, textvariable=fileName)
fileName_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=Kb).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Download", command=downloadFile).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="File Name").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="File size is:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Kb").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

fileName_entry.focus()
root.bind('<Return>', downloadFile)

root.mainloop()
