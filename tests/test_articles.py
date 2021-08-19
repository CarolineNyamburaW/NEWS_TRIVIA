import unittest
from app.models import Articles

class test_articles(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Articles class
  '''
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_article= Articles("2021-08-18T17:00:00Z",' ""https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/b64f24febe8559c507071c6b8c420e80.jpg','This Mexican Butterwort Plant Can Help Solve Your Gnat Problem','Gnats and other small flies are annoying to get rid of. A small number of them is bad enough, but an infestation can mean a lot more effort. There are several remedies weve covered before, like apple… [+2452 chars]','Aisha Jordan',' ""https://lifehacker.com/this-mexican-butterwort-plant-can-help-solve-your-gnat-1847498754')

    def test_instance(self):
      self.assertTrue(isinstance(self.new_article, Articles))
