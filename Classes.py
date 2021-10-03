from pathlib import Path
import Vars as vars
import shutil

separator = vars.separator


class File:
    def __init__(self, name):
        self.name = name

    def create_file(self, project_name, ext, path=''):
        full_path = vars.projects_folder + project_name + vars.separator + self.name + ext
        file = open(full_path, 'w+')
        file.write('hello')
        file.close()


class Folder:

    def __init__(self, name):
        self.name = name

    def create_folder(self, project_name, project_folder=False, name='', path=''):

        if project_folder:
            full_path = vars.projects_folder + project_name
        else:
            full_path = vars.projects_folder + project_name + separator + path + separator + name
            print(full_path)
        try:
            Path(full_path).mkdir(parents=True, exist_ok=False)
        except:
            print('Папка уже существует')

    def copy_folder(self, project_name, project_temp=False, dest_folder='', folder_name='', path=''):

        if project_temp:
            full_path = vars.projects_temp
            destination = vars.projects_folder + project_name + separator
        else:
            full_path = vars.projects_folder + project_name + separator + path + separator + folder_name
            destination = vars.projects_folder + project_name + separator + path + separator + dest_folder

        print(full_path)
        print(destination)

        if Path(full_path).exists():
            print("true")
            if Path(destination).exists():
                print("true")

                shutil.copytree(full_path, destination, dirs_exist_ok=True)
            else:
                print("Папки назначения не существует")
        else:
            print("Папки источника не существует")


class Project:
    def __init__(self, name):
        self.name = name

    def create_project(self):
        folders = Folder('project')
        #self.create_folder(self.name, True)
        folders.copy_folder(self.name, True)



if __name__ == "__main__":
    pass
