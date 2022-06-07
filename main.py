import os

from regex_log.file_manager import FileManager


def main():
    file_name = "con228.bugs.799464655"
    location = os.path.abspath(file_name)
    FileManager.print_edu_bug(location=location)

    # zip_name = "con228.bugs.zip"
    # location = os.path.abspath(zip_name)
    # FileManager.manage_zip(location=location, filename=file_name)


if __name__ == "__main__":
    main()
