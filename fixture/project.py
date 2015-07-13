# -*- coding: utf-8 -*-

from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_proj_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")

    def setvalue(self, value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(value).click()
            wd.find_element_by_name(value).clear()
            wd.find_element_by_name(value).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.setvalue("name", project.name)
        self.setvalue("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        if not wd.current_url.endswith("/manage_proj_page.php"):
            self.return_to_project_page()
        self.project_cache = None

    def return_to_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_manage_proj_page()
            self.project_cache = []
            for i in wd.find_elements_by_css_selector('a[href^="manage_proj_edit_page.php?project_id="]'):
                # id =
                name = i.text
                # description =
                self.project_cache.append(Project(name = name))
        return list(self.project_cache)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_manage_proj_page()
        wd.find_element_by_link_text("%s" % name).click()
        # wd.find_element_by_css_selector('a[href="manage_proj_edit_page.php?project_id=%s"]' % id).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        if not wd.current_url.endswith("/manage_proj_page.php"):
            self.return_to_project_page()
        self.project_cache = None