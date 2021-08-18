import unittest
from app import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News('ABC NEws', 'https://abcnews.go.com', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', 'us', 'general', 'abc-news')

def test_instance(self):
    '''
    '''
    self.assertTrue(isinstance(self.new_source, News))

def test_to_check_instance_variables(self):
            
    self.assertEquals(self.new_source.name, 'ABC News')
    self.assertEquals(self.new_source.url, 'https://abcnews.go.com')
    self.assertEquals(self.new_source.description, 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
    self.assertEquals(self.new_source.country, 'us')
    self.assertEquals(self.new_source.category, 'general')
    self.assertEquals(self.new_source.id, 'abc-news')

if __name__ == '__main__':
    unittest.main()