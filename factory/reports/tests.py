from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Report, ProblemReported, ProblemCategory
from products.models import Product
from areas.models import ProductionLine

class ReportModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product', short_code='TP')
        self.production_line = ProductionLine.objects.create(name='Test Line', team_leader=self.user)
        self.report = Report.objects.create(
            day='2023-01-01',
            start_hour=8,
            end_hour=16,
            user=self.user,
            product=self.product,
            plan=100,
            execution=80,
            production_line=self.production_line
        )

    def test_report_creation(self):
        self.assertTrue(isinstance(self.report, Report))
        self.assertEqual(self.report.__str__(), f"Report for Test Product by testuser (08:00-16:00)")

    def test_report_get_efficiency(self):
        self.assertEqual(self.report.get_efficiency(), 80.0)

    def test_report_get_duration(self):
        self.assertEqual(self.report.get_duration(), 8)

class ReportViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_report_list_view(self):
        response = self.client.get(reverse('reports:report-list'))
        self.assertEqual(response.status_code, 200)

    def test_report_create_view(self):
        response = self.client.get(reverse('reports:report-create'))
        self.assertEqual(response.status_code, 200)

class ProblemReportedModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product', short_code='TP')
        self.production_line = ProductionLine.objects.create(name='Test Line', team_leader=self.user)
        self.report = Report.objects.create(
            day='2023-01-01',
            start_hour=8,
            end_hour=16,
            user=self.user,
            product=self.product,
            plan=100,
            execution=80,
            production_line=self.production_line
        )
        self.category = ProblemCategory.objects.create(name='Test Category')
        self.problem = ProblemReported.objects.create(
            category=self.category,
            description='Test Problem',
            breakdown=5,
            user=self.user,
            report=self.report
        )

    def test_problem_creation(self):
        self.assertTrue(isinstance(self.problem, ProblemReported))
        self.assertEqual(self.problem.__str__(), "Test Category: Test Problem...")

    def test_problem_id_generation(self):
        self.assertIsNotNone(self.problem.problem_id)
        self.assertEqual(len(self.problem.problem_id), 12)