from model.project import Project
import random

def test_delete_project(app):

    app.go_to_control_page()
    if len(app.project.get_project_list()) ==0:
        app.project.create(Project().random())
    old_projects = app.soap.get_project_list("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_by_id(project.id)
    new_projects = app.soap.get_project_list("administrator", "root")
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
