import os
from pathlib import Path
from sys import platform

separator = '/'


current_folder = str(Path.cwd())

if platform != 'win32':
    pass
else:
    separator = '\\'

projects_folder = current_folder + separator + 'Projects' + separator
projects_temp = current_folder + separator + 'projects_temp' + separator

if __name__ == "__main__":
    pass
