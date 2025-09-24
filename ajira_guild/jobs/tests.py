from django.test import TestCase
from django.urls import reverse
from .models import Job, JobCategory
from accounts.models import User

class JobTests(TestCase):
    def setUp(self):
        self.employer = User.objects.create_user(username='emp', password='pass', role='employer')
        self.cat = JobCategory.objects.create(name='IT', slug='it')
        self.job = Job.objects.create(title='Developer', employer=self.employer, category=self.cat)

    def test_job_list_view(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Developer')
