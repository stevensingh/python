# Generate L2 Vni to vlan mapping variables
vlan = input("Input vlan id: ")
vlan = int(vlan)
l2_vni_id = (vlan + 10000)
vlan = (str(vlan))
l2_vni_id = (str(vlan))
vrf = input("input tenant vrf: ")
addr = input("L3 gateway address: ")
mask = input("input subnet mask: ")
mcast_grp = input("input mcast group mapping: ")

print("{ vlan_id: " + vlan + "," + " vni_id: " + l2_vni_id + ", " + "addr: " + addr + "," + " mask: " + mask + "," + " mcast_grp: " + mcast_grp + "," + " vrf:" + vrf + " }")


