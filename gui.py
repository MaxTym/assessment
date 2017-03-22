from tkinter import *
import json

with open('ca.json') as f:
    results = json.loads(f.read())
    cities = [i["name"] for i in results]
    cities = list(set(cities))
    cities.sort()

def option_changed(*args):
    with open('ca.json') as f:
        results = json.loads(f.read())
        for i in results:
            if i["name"] == variable.get():
                county.set(i["county_name"])
                latitude.set(i["primary_latitude"])
                longtitude.set(i["primary_longitude"])

master = Tk()
master.title("City Selector")

mainframe = Frame(master)
mainframe.grid(column=0,row=0)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 10, padx = 10)

variable = StringVar(master)
variable.set(cities[0])
variable.trace("w", option_changed)

w = OptionMenu(master, variable, *cities)
w.pack()

Label(mainframe, text="County").grid(row = 2, column = 1)
Label(mainframe, text="Latitude").grid(row = 3, column = 1)
Label(mainframe, text="Longtitude").grid(row = 4, column = 1)
county = StringVar()
latitude = StringVar()
longtitude = StringVar()
county_ent = Entry(mainframe, text=county, width = 15).grid(column = 2, row = 2)
latitude_ent = Entry(mainframe, text=latitude, width = 15).grid(column = 2, row = 3)
longtitude_ent = Entry(mainframe, text=longtitude, width = 15).grid(column = 2, row = 4)
mainloop()
