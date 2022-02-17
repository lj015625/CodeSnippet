"""
You are given an HTML code snippet of  lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])



html = '<head><title>HTML</title></head><object type="application/x-flash"data="your-file.swf"width="0" height="0"><!-- <param name="movie" value="your-file.swf" /> --><param name="quality" value="high"/></object>'
new = MyHTMLParser()
new.feed(html)
