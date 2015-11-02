"""scraper for hacker news who's hiring post"""
from urllib2 import urlopen
import unicodedata
import codecs

def scraper(url):
	website = [line.decode('utf-8').strip() for line in urlopen(url)]
	# or_array = []
	# and_array = []
	# if or_arr is not None:
	# 	or_array+=or_arr
	# if and_arr is not None:
	# 	and_array+=and_arr
	i =0;
	with codecs.open('sanfran.html', 'w+', encoding='utf8') as f:
		for line in website:
			line_lowercase = line.lower()

			if (' sf' in line_lowercase or 'sf ' in line_lowercase or 'san francisco' in line_lowercase or 'mountain view' in line_lowercase or 'sunnyvale' in line_lowercase  or 'CA ' in line_lowercase or ' CA' in line_lowercase) and ('python' in line_lowercase or 'java ' in line_lowercase or 'java,' in line_lowercase or 'java/' in line_lowercase or 'Django' in line_lowercase):
				if i:
					f.write("<ul style='background-color:lightcoral'>")
				else:
					f.write("<ul style='background-color: lightsteelblue'>")
				f.write(unicodedata.normalize('NFKD', line).encode('ascii','ignore'))
				f.write("</ul>")
				f.write("<hr>")
				i+=1
				i&=1
	f.close()
	print "done :D"




def main():
	# flags = raw_input()
	url = "https://news.ycombinator.com/item?id=10492086"
	scraper(url)
	

if __name__ == '__main__':
	main()