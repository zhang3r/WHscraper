"""scraper for hacker news who's hiring post"""
from urllib.request import urlopen
import unicodedata
import codecs
import re

def scraper(url):

    website = [line.decode('utf-8').strip() for line in urlopen(url)]
    # or_array = []
    # and_array = []
    # if or_arr is not None:
    #   or_array+=or_arr
    # if and_arr is not None:
    #   and_array+=and_arr
    i = 0
    lang_filters = []
    ca = re.compile(' ca,')
    ca1 = re.compile('san francisco')
    ca6 = re.compile('los angeles')
    ca2 = re.compile('mountain view')
    ca3 = re.compile('san mateo')
    ca4 = re.compile('sunnyvale')
    ca5 = re.compile(' ca ')
    ca7 = re.compile('santa monica')
    california = re.compile('california')
    python = re.compile('python')
    java = re.compile('java ')
    lang_filters.append(python)
    lang_filters.append(java)
    locale_filters = []
    locale_filters.append(california)
    locale_filters.append(ca)
    locale_filters.append(ca1)
    locale_filters.append(ca2)
    locale_filters.append(ca3)
    locale_filters.append(ca4)
    locale_filters.append(ca5)
    locale_filters.append(ca6)
    locale_filters.append(ca7)

    with codecs.open('sanfran.html', 'w+', encoding='utf8') as f:
        for line in website:
            line_lowercase = line.lower()
            lan_filters = []
            loc_filters = []

            for filt in lang_filters:
                match = re.search(filt, line_lowercase)
                if match:
                    lan_filters.append(True)
            for filt in locale_filters:
                match = re.search(filt, line_lowercase)
                if match:
                    loc_filters.append(True)

            if any(loc_filters):
                #any(loc_filters) or any(lan_filters):
                if i:
                    f.write("<ul style='background-color:lightcoral'>")
                else:
                    f.write("<ul style='background-color: lightsteelblue'>")
                f.write(line_lowercase)
                f.write("</ul>")
                f.write("<hr>")
                i += 1
                i &= 1
    f.close()
    print("done :D")





def main():

    # flags = raw_input()
    url = "https://news.ycombinator.com/item?id=11012044"
    scraper(url)

if __name__ == '__main__':
    main()
