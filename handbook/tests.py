from django.test import TestCase
from django.urls import reverse


class SalaryCalculatorTests(TestCase):
    def test_calculates_salary_from_label_and_questions(self):
        response = self.client.post(
            reverse("salary_calculator"),
            {
                "lesson_label": "高中解題教室",
                "duration_minutes": "30",
                "question_count": "5",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "總薪資")
        self.assertContains(response, "300")
