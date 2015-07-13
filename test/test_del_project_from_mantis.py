# -*- coding: utf-8 -*-

from model.project import Project
import random
import string

def test_del_project_from_mantis(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    if len(app.project.get_project_list()) == 0:
        project = Project(name=random_string("name", 10), description=random_string("description", 30))
        app.project.create(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.key) == sorted(new_projects, key=Project.key)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])