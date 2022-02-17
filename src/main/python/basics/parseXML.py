"""Calculate the number of attributes XML has."""
import xml.etree.ElementTree as etree


def get_attr_number(node):
    total = 0
    for elem in node.iter():
        total += len(elem.items())
    return total


maxdepth = 0


def depth(elem, level):
    global maxdepth
    if level == maxdepth:
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)


xml = "<feed xml:lang='en'><title>HackerRank</title><subtitle lang='en'>Programming challenges</subtitle><link " \
      "rel='alternate' type='text/html' href='http://hackerrank.com/'/><updated>2013-12-25T12:00:00</updated></feed> "
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
print(get_attr_number(root))

depth(tree.getroot(), -1)
print(maxdepth)
