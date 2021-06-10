"""
This was the homework for session 3.
"""

import os
import argparse

parser = argparse.ArgumentParser("This script parses amber mdout files to extract the total energy")
parser.add_argument("filepath", help = "The filepath to the file to be analyzed.")

args = parser.parse_args()

filename = args.filepath
f = open(filename,'r')
data = f.readlines()
f.close()

# Put in file called 03_Prod.mdout and get out a file called 03_Prod_Etot.txt

output_filename = os.path.basename(filename)
output_filename = output_filename.split(".")[0]
output_filename = F"{output_filename}_Etot.txt"

print(F"Writing output to {output_filename}")

f_write = open(output_filename,'w')
energies = []

for line in data:
    if 'Etot' in line:
        split_line = line.split()
        energies.append(float(split_line[2]))
        f_write.write(F'{split_line[2]} \n')
f_write.close()

