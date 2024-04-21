import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color_name = color
        self.rgb = COLOR_NAMES.get(color.upper(), None)

    @classmethod
    def hex2rgb(cls, hex):
        """Class method that converts a hex value into an rgb one"""
        return int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16)

    @classmethod
    def rgb2hex(cls, rgb):
        if len(rgb) != 3:
            raise ValueError
        for color in rgb:
            if not (0 <= color <= 255):
                raise ValueError
        """Class method that converts an rgb value into a hex one"""
        return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}('{self.color_name}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return f"{self.rgb}" if self.rgb else 'Unknown'
