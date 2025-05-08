import tkinter as tk
import datetime as dt
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tktimepicker import AnalogPicker, AnalogThemes, constants

root = tk.Tk()
root.title("On Demand to Transcription")



#########
#
#   Up to generating DateTime that matches the GUI at start of app
#   setup a date time and use current day/month/year but set time
#   to 00:59 as that's what the GUI shows
#
#########


# Create a DateTime instance.
#selectedDateTime = dt.datetime()

def minutesToSeconds(minutes):
    # Returns an integer
    if minutes == "":
        minutes = 0
    return int(minutes) * 60

def genURL():
    currentDT = set_datetime(cal,tp)
    
    baseURL = "https://rrr.org.au/"
    lengthOption = "&l="
    dtStrFormat = '%Y%m%d%H%M%S'
    dateTimeStr = currentDT.strftime(dtStrFormat)    
    newVar = baseURL + dateTimeStr + lengthOption + \
             str(minutesToSeconds(lengthVar.get()))
    urlVar.set(newVar)

def copyToClipboard():
    genURL()
    root.clipboard_clear()
    root.clipboard_append(urlVar.get())

def convert12to24(hour, am_pm):
    if am_pm == 'AM' and hour == 12:
        hour = 0
        return hour
    if am_pm == 'PM':
        if hour == 12:
            return hour
        hour = int(hour) + 12
    return hour

def print_datetime(selectedDateTime):
    dtFormatString = '%Y-%m-%d-%H-%M-%S'
    print(selectedDateTime.strftime(dtFormatString))

def set_datetime(cal, tp):
    #unpacking time tuple
    hour, minute, am_pm = tp.time()

    hour = convert12to24(hour, am_pm)
    tpTime = dt.time(hour=hour, minute=minute)
    calDate = cal.selection_get()
    selectedDateTime = dt.datetime.combine(calDate, tpTime)

    print_datetime(selectedDateTime)
    return selectedDateTime
    
# Setup Frames
topFrame = ttk.Frame(root)
topFrame['padding'] = 5

selectorsFrame = ttk.Frame(root)
selectorsFrame['padding'] = 5

urlFrame = ttk.Frame(root)
urlFrame['padding'] = 5

titleLabel = ttk.Label(topFrame)
titleLabel['text'] = "On Demand to Transcription helper"

# Create selectors frame widgets

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

generateBtn = ttk.Button(
    urlFrame,
    text='Generate',
    command=genURL
)

copyBtn = ttk.Button(
    urlFrame,
    text='Copy',
    command=copyToClipboard
)

# Setup calendar widget
cal = Calendar(selectorsFrame,
               font="Arial 14",
               selectmode = 'day',
               locale = 'en_AU',
               date_pattern = 'dd/mm/y'
               )

# Setup time picker widget
tp = AnalogPicker(selectorsFrame, type=constants.HOURS12)
tp_theme = AnalogThemes(tp)
tp_theme.setDracula()
			
# Arrange frames
topFrame.grid(column=0,row=0)
selectorsFrame.grid(column=0,row=1)
urlFrame.grid(column=0,row=2)

## Arrange widgets
# Arrange top widgets
titleLabel.grid(column=0,row=0)

# Arrange selector widgets
cal.grid(column=0, row=0, sticky='e', padx=2, pady=2)
tp.grid(column=1, row=0, sticky='e', padx=2, pady=2)

lengthLabel.grid(column=0, row=2, sticky='e', padx=2, pady=2)
lengthEntry.grid(column=1, row=2, sticky='w', padx=2, pady=2)

# Arrange URL widgets
generateBtn.grid(column=0, row=0)
copyBtn.grid(column=1, row=0)
urlEntry.grid(column=0, row=1, columnspan=2)

# Set initial DateTime
#selectedDateTime = set_datetime(cal, tp)


root.mainloop()
