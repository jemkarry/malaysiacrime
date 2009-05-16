from django.test import TestCase


class MainTestCase(TestCase):
    """
    Test accessing and browsing crime reports.
    """
    fixtures = ['crimes', 'comments']

    def setUp(self):
        pass

    def test_get_index(self):
        """
        Test accessing index page.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main/index.html')

        self.assertEquals(len(response.context['crimes']), 3)
        self.assertEquals(response.context['crimes'][0].id, 1)
        self.assertEquals(response.context['crimes'][1].id, 2)
        self.assertEquals(response.context['crimes'][2].id, 3)

    def test_get_most_updated(self):
        """
        Test accessing most updated page.
        """
        response = self.client.get('/most/updated/')
        self.assertTemplateUsed(response, 'main/most_updated.html')

        self.assertEquals(len(response.context['crimes']), 3)
        self.assertEquals(response.context['crimes'][0].id, 3)
        self.assertEquals(response.context['crimes'][1].id, 2)
        self.assertEquals(response.context['crimes'][2].id, 1)

    def tearDown(self):
        pass
