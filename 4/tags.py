import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    data = ET.fromstring(content)
    # feed contiains datashape ['rss']['channel']['item']
    items = data.findall('.//channel/item')
    pybites_tags = []
    for item in items:
        categories = item.findall('category')
        for category in categories:
            pybites_tags.append(category.text)

    return Counter(pybites_tags).most_common(n)
