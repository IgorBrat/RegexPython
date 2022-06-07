import re
import zipfile
import io


class FileManager:
    """Class that works with files"""

    @staticmethod
    def print_edu_bug(location: str):
        """Prints all string that match regex from txt"""
        regex = r'bugs.*\.edu.*menu.*'
        count = 0
        with open(location) as file:
            lines = file.readlines()
            for line in lines:
                find_regex = re.search(regex, line)
                if find_regex is not None:
                    print(find_regex.group())
                    count += 1
        print(f"Count of matches: {count}")

    @staticmethod
    def manage_zip(location: str, filename: str):
        """Prints all string that match regex from txt in zip"""
        regex = r'bugs.*\.edu.*menu.*'
        count = 0
        with zipfile.ZipFile(location) as zf:
            with io.TextIOWrapper(zf.open(filename), encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    find_regex = re.search(regex, line)
                    if find_regex is not None:
                        print(find_regex.group())
                        count += 1
            print(f"Count of matches: {count}")
