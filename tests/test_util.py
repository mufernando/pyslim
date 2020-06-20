"""
Test cases for utility functions.
"""
from __future__ import print_function
from __future__ import division

import tests
import unittest
import numpy as np

import pyslim

class TestUniqueLabelsByGroup(unittest.TestCase):

    def verify_unique_labels_by_group(self, group, label, minlength):
        x = pyslim.util.unique_labels_by_group(group, label, minlength)
        self.assertGreaterEqual(len(x), minlength)
        for g in range(len(x)):
            if g != -1:
                u = set(label[group == g])
                self.assertEqual(len(u) == 1, x[g])

    def test_all_same(self):
        n = 10
        group = np.repeat(1, 10)
        label = np.arange(10)
        self.verify_unique_labels_by_group(group, label, 1)
        x = pyslim.util.unique_labels_by_group(group, label, 1)
        self.assertEqual(len(x), 2)
        self.assertEqual(x[0], False)
        self.assertEqual(x[1], False)
        label = np.repeat(5, 10)
        self.verify_unique_labels_by_group(group, label, 1)
        x = pyslim.util.unique_labels_by_group(group, label, 1)
        self.assertEqual(len(x), 2)
        self.assertEqual(x[0], False)
        self.assertEqual(x[1], True)

    def test_all_unique(self):
        ng = 10
        group = np.arange(ng)
        label = np.arange(ng)
        self.verify_unique_labels_by_group(group, label, ng)
        x = pyslim.util.unique_labels_by_group(group, label, ng)
        self.assertTrue(np.all(x))
        group = np.append(group, [-1, -1, -1])
        label = np.append(label, [0, 1, 2])
        self.verify_unique_labels_by_group(group, label, ng)
        x = pyslim.util.unique_labels_by_group(group, label, ng)
        self.assertTrue(np.all(x))

    def test_unique_labels_by_group(self):
        for ng in 3 * np.arange(2, 15):
            for n in (10, 100):
                for nl in (2, ng):
                    for minl in (-5, 10000000):
                        group = np.random.choice(np.arange(ng) - 1, size=n)
                        label = minl + np.random.choice(np.arange(nl), size=n)
                        self.verify_unique_labels_by_group(group, label, ng)


