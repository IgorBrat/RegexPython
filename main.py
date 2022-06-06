import os

from regex_log.file_manager import FileManager


def main():
    file_name = "con228.bugs.799464655"
    location = os.path.abspath(file_name)
    FileManager.print_edu_bug(location=location)


if __name__ == "__main__":
    main()
