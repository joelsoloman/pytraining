from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import Developer, Skill
from .views import level

class DeveloperModelTests(TestCase):

    def test_200_index(self):
        
        url = reverse('ninja:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_200_details(self):

        dev = Developer(name='Joe', experience=5, country='IND')
        dev.save()
        url = reverse('ninja:details', args=(dev.id,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_404_details(self):

        url = reverse('ninja:details', args=(1,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_all_dev(self):
        
        dev = Developer(name='Joe', experience=5, country='IND')
        dev.save()
        dev_list = Developer.objects.all()
        assert len(dev_list) == 1


class SkillModelTests(TestCase):

    def test_create_skill(self):
        dev = Developer(name='Joe', experience=5, country='IND')
        dev.save()
        skill = dev.skill_set.create(name='Java', level=1)
        assert skill.name == 'Java'

    def test_skill_of_dev(self):
        dev = Developer(name='Joe', experience=5, country='IND')
        dev.save()
        dev.skill_set.create(name='Java', level=1)
        dev.skill_set.create(name='Python', level=1)
        dev_skill_list = dev.skill_set.all()
        assert len(dev_skill_list) == 2

    def test_level_up_details(self):
        dev = Developer(name='Joe', experience=5, country='IND')
        dev.save()
        dev.skill_set.create(name='Java', level=1)
        dev.skill_set.create(name='Python', level=1)
        select = dev.skill_set.get(pk=1)
        select.level += 1
        select.save()
        skill = dev.skill_set.all() 
        assert skill[0].level == 2