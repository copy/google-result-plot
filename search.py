from urllib import FancyURLopener
import re
import time
import sys
from config import *


class GoogleOpener(FancyURLopener):
	# useragent
	version = "Mozilla"

def getCountByKeyword(keyword):
	opener = GoogleOpener()
	handle = opener.open(search_url.format(keyword))
	match = None
	line = True
	while not match and line:
		line = handle.readline()
		match = re.search(count_regex, line)

		if no_match in line:
			break

	handle.close()

	if not match:
		return 0

	count = match.group(1).replace(",", "").replace(".", "")

	return int(count)

print "Keyword: " + keyword
print "This will take ~%.0f seconds" % (len(search_range) * delay)

results = []

for i in search_range:
	count = getCountByKeyword(keyword.format(i))
	results.append(count)
	print "{:>6,}  |".format(i), 
	print "{:>15,}".format(count)
	time.sleep(delay)


import pylab

pylab.plot(search_range, results)
pylab.xlabel(keyword)

pylab.gca().set_yscale(y_scale)

pylab.show()

