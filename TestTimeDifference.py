import unittest

import TimeUtil


class TestTimeDifference(unittest.TestCase):

    def testStartEnd(self):
        self.assertEqual(TimeUtil.getDifference("20:00", "18:00"), 120.0)

    def testStartEndInPast(self):
        self.assertEqual(TimeUtil.getDifference("18:00", "20:00"), -120.0)

    def testStartEndSmallerAmount(self):
        self.assertEqual(TimeUtil.getDifference("19:00", "18:25"), 35.0)

    def testStartEndSame(self):
        self.assertEqual(TimeUtil.getDifference("19:00", "19:00"), 0.0)

if __name__ == '__main__':
    unittest.main()