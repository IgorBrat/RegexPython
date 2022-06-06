import re
from typing import List


class FileManager:
    """Class that works with files"""
    @staticmethod
    def print_edu_bug(location: str):
        regex = r'bugs.*\.edu.*menu.*'
        with open(location) as file:
            lines = file.readlines()
            for line in lines:
                find_regex = re.search(regex, line)
                if find_regex is not None:
                    print(find_regex.group())
