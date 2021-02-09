#If you follow this command of enlightenment, your soul shall be cleansed.
#Run the following command.
#Make sure the enclosed secret.txt file is in the same folder as this script when you run it.
'''
riteofpassage.py 86753094205318008
'''

import sys
from itertools import cycle
noise = list(map(int, sys.argv[1]))
output = ""
for ch, key in zip(open("secret.txt", "r", encoding="utf-8").read(), cycle(noise)):
    output += chr(ord(ch)-key)

print(output)



