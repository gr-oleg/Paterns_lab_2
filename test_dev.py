import datetime
import uuid
from unittest import TestCase
from main import QualityAssurance, AssignManagement, Employee, Project, ProjectManager


class TestAssignmentManager(TestCase):
    def test_link(self):
        p1 = AssignManagement()
        tempid = uuid.uuid4()
        project1 = "title"


class TestQualityAssurance(TestCase):
    def test_ask_sick_leave(self):
        QA = QualityAssurance
        employee = Employee("test")
        project = Project("test")
        PM = ProjectManager("test")
        AM = AssignManagement()
