# -*- coding: utf-8 -*-
# $Id$
import unittest
import doctest

from zope.testing import doctestunit
from zope.component import testing, eventtesting

from Testing import ZopeTestCase as ztc

from collective.plonefinder.tests import base

def test_suite():
    return unittest.TestSuite([

        ztc.ZopeDocFileSuite(
            'README.txt', package='collective.plonefinder',
            test_class=base.FunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
