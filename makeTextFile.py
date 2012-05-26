#!/usr/bin/env python

'makeTextFile.py --- create text file'

import os
ls = os.linesep

fname = 'D:/textFile.txt'

# get filename
while True:
	if os.path.exists(fname):
		print("ERROR: ", "%s already exists" % fname)
		exit()
	else:
		break

# get file content (text) lines
all = []
print("\n Enter lines ('.' by itself to quit).\n")

# loop until user terminate input
while True:
	entry = input('> ')
	if entry == '.':
		break
	else:
		all.append(entry)

# write lines to file with proper line-ending
fileObject = open(fname, 'w')
fileObject.writelines(['%s%s' % (x, ls) for x in all])
fileObject.close()

print('DONE')