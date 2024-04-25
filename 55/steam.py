from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    return list(parse_feed(url=FEED_URL))


def parse_feed(url):
    rss_feed = feedparser.parse(FEED_URL)
    for game in rss_feed['entries']:
        title = game.title
        link = game.link
        yield Game(title, link)


if __name__ == '__main__':
    for g in get_games():
        print(g)
