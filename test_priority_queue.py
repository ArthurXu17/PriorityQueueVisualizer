
import unittest
from parameterized import parameterized

from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    
    def setUp(self):
        self.pqueue = PriorityQueue(lambda x, y: x <= y)
    
    def test_empty_queue(self):
        self.assertEqual(self.pqueue.size(), 0)
    
    def test_queue_single_element(self):
        self.pqueue.insert(5)
        self.assertEqual(self.pqueue.size(), 1)
        self.assertEqual(self.pqueue.get_min(), 5)
        self.assertEqual(self.pqueue.size(), 1)
        self.assertEqual(self.pqueue.delete_min(), 5)
        self.assertEqual(self.pqueue.size(), 0)
        
    
    def test_two_queue_small_first(self):
        self.pqueue.insert(1)
        self.pqueue.insert(2)
        self.assertEqual(self.pqueue.get_min(), 1)
    
    def test_two_queue_large_first(self):
        self.pqueue.insert(2)
        self.pqueue.insert(1)
        self.assertEqual(self.pqueue.get_min(), 1)
    
    def test_insert_small_queue(self):
        self.pqueue.insert(3)
        self.assertEqual(self.pqueue.get_min(), 3)
        self.assertEqual(self.pqueue.size(), 1)
        self.pqueue.insert(2)
        self.assertEqual(self.pqueue.get_min(), 2)
        self.assertEqual(self.pqueue.size(), 2)
        self.pqueue.insert(1)
        self.assertEqual(self.pqueue.get_min(), 1)
        self.assertEqual(self.pqueue.size(), 3)
        self.pqueue.insert(0)
        self.assertEqual(self.pqueue.get_min(), 0)
        self.assertEqual(self.pqueue.size(), 4)
    
    @parameterized.expand([([2,3,1,4,5,6],), ([2,3,4,5,6,1],), ([6,2,4,3,1,5],)])
    def test_perms_of_6(self, perm):
        for n in perm:
            self.pqueue.insert(n)
        for i in range(1,7):
            self.assertEqual(self.pqueue.delete_min(), i)
            self.assertEqual(self.pqueue.size(), 6 - i)
    
    def test_large(self):
        k = 712
        for i in range(1000):
            self.pqueue.insert(k * 12894124 + 88487183)
            k = (401 * k + 417) % 1000
        self.assertEqual(self.pqueue.size(), 1000)
        for i in range(1000):
            self.assertEqual(self.pqueue.delete_min(), i * 12894124 + 88487183)