from pathlib import Path
import Vars as vars
import Classes as classes

project = 'Nuka2'
file_name = 'mixt'

my_project = classes.Project(project)


if __name__ == "__main__":
    my_project.create_project()