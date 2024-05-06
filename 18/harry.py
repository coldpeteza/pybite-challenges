import os
import string
import urllib.request
from collections import Counter
import re

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    c = Counter()
    stop_words = []
    string.punctuation
    pattern = re.compile(r'[\-0-9\,\.\"\'\!\?\;]+')
    with open(stopwords_file, 'r') as sw:
        for line in sw:
            words = line.split()
            for word in words:
                lowered_stop_word = word.lower()
                stop_words.append(lowered_stop_word.strip())

    with open(harry_text, 'r') as f:
        for line in f:
            for word in line.split():
                replacement = re.sub(pattern, '', word)
                lower_word = replacement.lower()
                if lower_word not in stop_words:
                    if lower_word:
                        c[lower_word] += 1

    return c.most_common()[0]
