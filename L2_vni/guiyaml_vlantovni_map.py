#!/usr/bin/env python3

from collections import OrderedDict
import os
import signal
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import yaml

root = tk.Tk()
root.geometry("600x350")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)

#mapping from key name to label text
elements = OrderedDict([('vlan_id', 'Vlan Id'), ('vrf', 'VRF Instance'), ('addr', 'L3 gateway address'), ('mask', 'Subnet mask CIDR'), ('mcast_grp', 'Mcast address mapping')])


def sigint_handler(signum, frame):
    exitbox = tk.messagebox.askquestion('Exit?', 'Are you sure you want to exit?', icon='warning')
    if exitbox == 'yes':
        root.destroy()


def getInput():
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Select filename to save as', filetypes=(('yamlfiles', '*.yaml'), ('all files', '*.*')))

    data = {}

    for elem in entries:
        entry = entries[elem]
        data[elem] = entry.get()
        if elem == 'vlan_id':
            data['l2_vni_id'] = data[elem] + '10'

    with open(filename, 'w') as yamlfile:
        yaml.dump(data, yamlfile)


rectangle_topleft = tk.Label(root, text="Singh Swan Song: ", bg="black", fg="white")
rectangle_topleft.grid(column=0, row=0, ipadx=30, ipady=30, sticky="EW")
rectangle_topright = tk.Label(root, text="L2vni Configuration Generator: ", bg="black", fg="white")
rectangle_topright.grid(column=1, row=0, ipadx=30, ipady=30, sticky="EW")

rectangles = []
entries = OrderedDict()
for i, elem in enumerate(elements):
    bgcolour = "green" if i%2 == 0 else "red"
    rect = tk.Label(root, text=elements[elem] + ':', bg=bgcolour, fg="white")
    rect.grid(column=0, row=i+1, ipadx=10, ipady=10, sticky="EW")
    rectangles.append(rect)
    entry = tk.Entry(root)
    entry.grid(column=1, row=i+1, ipadx=10, ipady=10, sticky="EW")
    entries[elem] = entry


button = tk.Button(root, text="submit", command=getInput)
button.grid(column=0, row=6, ipadx=10, ipady=10, sticky="EW")

#setup a sig handler for ctrl-c
signal.signal(signal.SIGINT, sigint_handler)

root.mainloop()
