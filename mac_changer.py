#!/usr/bin/env python

# Media Access Control (MAC) address changer.
# This program prompts the user for a new MAC address and what interface to assign it to.
# This helps maintain anonymity and allows impersonation.

# subprocess is a module that allows CLI interaction from the script.

import subprocess
from random import seed
from random import randint

seed

mac_array = ["10"]  # MAC addresses must start with an even number.

for _ in range(5):
    mac_element = str(randint(10, 99))
    mac_array.append(mac_element)


interface = input("interface > ")
new_MAC_address = ":".join(mac_array)

print("[+] Changing MAC address for " + interface + " to " + new_MAC_address)

subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_MAC_address, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
