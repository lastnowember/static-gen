from pathlib import Path
import Vars as vars


def create_folder(project_name, project_folder=False, name='', path=''):

    separator = vars.separator

    if project_folder:
        full_path = vars.projects_folder + project_name
    else:
        full_path = vars.projects_folder + project_name + separator + path + separator + name
        print(full_path)
    try:
        Path(full_path).mkdir(parents=True, exist_ok=False)
    except:
        print('Папка уже существует')


class File:
    def __init__(self, name):
        self.name = name

    def create_file(self, project_name, ext, path=''):
        full_path = vars.projects_folder + project_name + vars.separator + self.name + ext
        file = open(full_path, 'w+')
        file.write('hello')
        file.close()


class Project:
    def __init__(self, name):
        self.name = name

    def create_project(self):
        create_folder(self.name, True)
        create_folder(self.name, False, 'tmp')
        create_folder(self.name, False, 'next', 'tmp')


if __name__ == "__main__":
    pass
