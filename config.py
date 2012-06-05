# config file

# which url to use
#search_url = "http://www.google.com/search?q={0}"
search_url = "http://www.bing.com/search?q={0}&setmkt=en-ww"

# delay between requests
delay = 0.1

# regex for number of results
#count_regex = "(\d[,\d]*) results" # google 
count_regex = "of (\d[\d\.,]*) results" # bing

# string to test for "no match" responses
no_match = "did not match any documents" 

# the keyword to search for
# add quotes if necessary
keyword = '"my iq is {0}"'

# the range to insert into the keyword
search_range = range(70, 170, 1)

# scale for y-axis ("linear" or "log") 
y_scale = "log"

