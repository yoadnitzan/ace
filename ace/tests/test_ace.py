'''
Created on Sep 21, 2014

@author: nick
'''
import unittest
import random

import numpy
import pylab

from ace import ace

class TestAce(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sample_problem(self):
        N = 100
        ace_solver = ace.ACESolver()

        x = [numpy.array([random.random() * 2.0 - 1 for i in range(N)])
             for _i in range(5)]
        y = numpy.log(4.0 + numpy.sin(4 * x[0]) + numpy.abs(x[1]) + x[2] ** 2 +
                     x[3] ** 3 + x[4] + 0.1 * numpy.random.standard_normal(N))

        pylab.figure()
        for i in range(5):
            pylab.subplot(2, 3, i + 1)
            pylab.plot(x[i], y, '.', label='xi'.format(i))
        pylab.show()

        ace_solver._x = x
        ace_solver._y = y
        ace_solver.solve()
        pylab.figure()
        for i in range(5):
            pylab.subplot(2, 3, i + 1)
            pylab.plot(x[i], ace_solver._x_transforms[i], '.', label='Phi {0}'.format(i))
        pylab.subplot(2, 3, 6)
        pylab.plot(y, ace_solver._y_transform, '.', label='Theta')
        pylab.legend()
        pylab.show()



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()