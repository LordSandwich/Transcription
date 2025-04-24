import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("On Demand to Transcription")

def minutesToSeconds(minutes):
    # Returns an integer
    if minutes == "":
        minutes = 0
    return int(minutes) * 60

def genURL():
    baseURL = "https://rrr.org.au/"
    lengthOption = "&l="
    dateTime = yearVar.get() + monthVar.get() + dayVar.get() + \
               hourVar.get() + minuteVar.get() + secondVar.get()
    newVar = baseURL + dateTime + lengthOption + \
             str(minutesToSeconds(lengthVar.get()))
    urlVar.set(newVar)

def copyToClipboard():
    root.clipboard_clear()
    root.clipboard_append(urlVar.get())
    #root.update()

topFrame = ttk.Frame(root)
topFrame['padding'] = 5

selectorsFrame = ttk.Frame(root)
selectorsFrame['padding'] = 5

urlFrame = ttk.Frame(root)
urlFrame['padding'] = 5

titleLabel = ttk.Label(topFrame)
titleLabel['text'] = "On Demand to Transcription helper"

# Create selectors frame widgets
yearLabel = ttk.Label(selectorsFrame)
yearLabel['text'] = "Year:"

yearVar = tk.StringVar(value='2025')
yearEntry = ttk.Entry(selectorsFrame)
yearEntry['textvariable'] = yearVar
yearEntry['width'] = 8


monthLabel = ttk.Label(selectorsFrame)
monthLabel['text'] = "Month:"

monthVar = tk.StringVar()
monthEntry = ttk.Entry(selectorsFrame)
monthEntry['textvariable'] = monthVar
monthEntry['width'] = 8

dayLabel = ttk.Label(selectorsFrame)
dayLabel['text'] = "Day:"

dayVar = tk.StringVar()
dayEntry = ttk.Entry(selectorsFrame)
dayEntry['textvariable'] = dayVar
dayEntry['width'] = 8

hourLabel = ttk.Label(selectorsFrame)
hourLabel['text'] = "Hour:"

hourVar = tk.StringVar()
hourEntry = ttk.Entry(selectorsFrame)
hourEntry['textvariable'] = hourVar
hourEntry['width'] = 8

minuteLabel = ttk.Label(selectorsFrame)
minuteLabel['text'] = "Minute:"

minuteVar = tk.StringVar()
minuteEntry = ttk.Entry(selectorsFrame)
minuteEntry['textvariable'] = minuteVar
minuteEntry['width'] = 8

secondLabel = ttk.Label(selectorsFrame)
secondLabel['text'] = "Second:"

secondVar = tk.StringVar()
secondEntry = ttk.Entry(selectorsFrame)
secondEntry['textvariable'] = secondVar
secondEntry['width'] = 8

lengthLabel = ttk.Label(selectorsFrame)
lengthLabel['text'] = "Length (in minutes):"

lengthVar = tk.StringVar()
lengthEntry = ttk.Entry(selectorsFrame)
lengthEntry['textvariable'] = lengthVar
lengthEntry['width'] = 8

# Create URL frame widgets
urlVar = tk.StringVar()
urlEntry = ttk.Entry(urlFrame)
urlEntry['textvariable'] = urlVar
urlEntry['width'] = 55
urlVar.set("https://rrr.org.au/20250423111500&l=300")

generateBtn = ttk.Button(urlFrame, text='Generate', command=genURL)
copyBtn = ttk.Button(
    urlFrame,
    text='Copy',
    command=copyToClipboard
)

# Arrange frames
topFrame.grid(column=0,row=0)
selectorsFrame.grid(column=0,row=1)
urlFrame.grid(column=0,row=2)

# Arrange widgets
# Arrange top widgets
titleLabel.grid(column=0,row=0)

# Arrange selector widgets
yearLabel.grid(column=0, row=0, sticky='e', padx=2, pady=2)
yearEntry.grid(column=1, row=0, sticky='w', padx=2, pady=2)
monthLabel.grid(column=0, row=1, sticky='e', padx=2, pady=2)
monthEntry.grid(column=1, row=1, sticky='w', padx=2, pady=2)
dayLabel.grid(column=0, row=2, sticky='e', padx=2, pady=2)
dayEntry.grid(column=1, row=2, sticky='w', padx=2, pady=2)
hourLabel.grid(column=2, row=0, sticky='e', padx=2, pady=2)
hourEntry.grid(column=3, row=0, sticky='w', padx=2, pady=2)
minuteLabel.grid(column=2, row=1, sticky='e', padx=2, pady=2)
minuteEntry.grid(column=3, row=1, sticky='w', padx=2, pady=2)
secondLabel.grid(column=2, row=2, sticky='e', padx=2, pady=2)
secondEntry.grid(column=3, row=2, sticky='w', padx=2, pady=2)
lengthLabel.grid(column=1, row=3, columnspan=2, sticky='e', padx=2, pady=2)
lengthEntry.grid(column=3, row=3, sticky='w', padx=2, pady=2)

# Arrange URL widgets
generateBtn.grid(column=0, row=0)
copyBtn.grid(column=1, row=0)
urlEntry.grid(column=0, row=1, columnspan=2)

root.mainloop()
