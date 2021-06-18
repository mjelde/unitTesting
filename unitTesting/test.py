import unittest
from lock  import lock
from user  import user
from scan import scan

class TestLock(unittest.TestCase):
    def setUp(self):
        self.LK=lock(123, 40, 1)
    def test_lockid(self):
       self.assertEqual(self.LK.getLockId(), 123)

class Testusername(unittest.TestCase):
    def setUp(self):
         self.name=user('PASS', 1 , 'valid')

    def test_username(self):
         self.assertEqual(self.name.getUserName(),'PASS')

class TestScan(unittest.TestCase):
    def setUp(self):
         self.lock=scan(1, 2)

    def test_scan(self):
         self.assertEqual(self.lock.getLock(), 1)
    def test_card(self):
         self.assertEqual(self.lock.getCard(), 2)