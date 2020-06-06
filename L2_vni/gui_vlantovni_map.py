import tkinter as tk

root = tk.Tk()
root.geometry("600x350")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)

def getInput():
    vlan = entry1.get()
    vrf = entry2.get()
    addr = entry3.get()
    mask = entry4.get()
    mcast_grp = entry5.get()
    vlan = (str(vlan))
    l2_vni_id = (vlan + "10")

    output_string = "{ vlan_id: " + vlan + "," + " vni_id: " + l2_vni_id + ", " + "addr: " + addr + "," + " mask: " + mask + "," + " mcast_grp: " + mcast_grp + "," + " vrf:" + vrf + " }"
    output = tk.Label(root)
    output["text"]=output_string
    output.grid(column=1, row=6, ipadx=10, ipady=10, sticky="EW")

rectangle_topleft = tk.Label(root, text="Singh Swan Song: ", bg="black", fg="white")
rectangle_topleft.grid(column=0, row=0, ipadx=30, ipady=30, sticky="EW")
rectangle_topright = tk.Label(root, text="L2vni Configuration Genertor: ", bg="black", fg="white")
rectangle_topright.grid(column=1, row=0, ipadx=30, ipady=30, sticky="EW")
rectangle_1 = tk.Label(root, text="Vlan Id: ", bg="green", fg="white")
rectangle_1.grid(column=0, row=1, ipadx=10, ipady=10, sticky="EW")
rectangle_2 = tk.Label(root, text="VRF instance: ", bg="red", fg="white")
rectangle_2.grid(column=0, row=2, ipadx=10, ipady=10, sticky="EW")
rectangle_3 = tk.Label(root, text="L3 gateway address: ", bg="green", fg="white")
rectangle_3.grid(column=0, row=3, ipadx=10, ipady=10, sticky="EW")
rectangle_4 = tk.Label(root, text="Subnet mask CIDR: ", bg="red", fg="white")
rectangle_4.grid(column=0, row=4, ipadx=10, ipady=10, sticky="EW")
rectangle_5 = tk.Label(root, text="Mcast address mapping: ", bg="green", fg="white")
rectangle_5.grid(column=0, row=5, ipadx=10, ipady=10, sticky="EW")
entry1 = tk.Entry(root)
entry1.grid(column=1, row=1, ipadx=10, ipady=10, sticky="EW")
entry2 = tk.Entry(root)
entry2.grid(column=1, row=2, ipadx=10, ipady=10, sticky="EW")
entry3 = tk.Entry(root)
entry3.grid(column=1, row=3, ipadx=10, ipady=10, sticky="EW")
entry4 = tk.Entry(root)
entry4.grid(column=1, row=4, ipadx=10, ipady=10, sticky="EW")
entry5 = tk.Entry(root)
entry5.grid(column=1, row=5, ipadx=10, ipady=10, sticky="EW")
button = tk.Button(root, text="submit", command=getInput)
button.grid(column=0, row=6, ipadx=10, ipady=10, sticky="EW")

root.mainloop()