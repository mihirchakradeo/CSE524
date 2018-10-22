import pandas as pd
import re
import sys
import glob

p = re.compile(r'SYNOPSIS')

def build_dict(a):
    # d = {}
    # for i in a:
    #     d[i.strip()] = []
    # return d
    d = set()
    for i in a:
    	d.add(i.strip())
    return d

def build_dictionaries(filename):

	with open(filename) as f:
		lines = f.read().splitlines()
		for i in range(len(lines)):
		    if p.findall(lines[i].strip()):
		        break

        while True:
            if lines[i+1] != "":
                i += 1
                break
            i += 1

	synopsis = lines[i].strip()

	temp = synopsis.split("->")
	ip = temp[0]
	op = "".join(temp[1:])
	ip = ip.strip()
	op = op.strip()
	ip = ip.split(",")
	op = op.split(",")

	inputs = build_dict(ip)
	outputs = build_dict(op)
	# print inputs
	# print outputs
	sets = inputs.union(outputs)
	return sets

def get_unique_vars():
	unique_vars = set()

	for file in glob.glob("operations/*.txt"):
		# print file
		sets = build_dictionaries(file)
		unique_vars = unique_vars.union(sets)
	# print len(unique_vars)
	# print unique_vars
	unique_vars = list(unique_vars)
	unique_vars.sort()
	with open('unique_vars.txt', 'w') as f:

		for var in unique_vars:
			s = var+"\n"
			f.write(s)


if __name__ == '__main__':
	# build_dictionaries(sys.argv[1])
	get_unique_vars()