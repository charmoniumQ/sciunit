from __future__ import absolute_import

from nose.tools import *

import testit


class TestShow(testit.LocalCase):
    def test_all(self):
        with assert_raises(SystemExit) as r:
            testit.sciunit('show', '-x')
            assert_equals(r.error_code, 2)

        with assert_raises(SystemExit) as r:
            testit.sciunit('show')
            assert_equals(r.error_code, 1)

        testit.sciunit('create', 'ok')

        with assert_raises(SystemExit) as r:
            testit.sciunit('show')
            assert_equals(r.error_code, 1)

        testit.sciunit('exec', 'pwd')
        assert_is_none(testit.sciunit('show'))

        testit.sciunit('exec', 'true')
        assert_is_none(testit.sciunit('show', 'e1'))

        with assert_raises(SystemExit) as r:
            testit.sciunit('show', 'e1', 'e2')
            assert_equals(r.error_code, 2)

        testit.sciunit('rm', 'e1')
        assert_is_none(testit.sciunit('show', 'e2'))

        with assert_raises(SystemExit) as r:
            testit.sciunit('show', 'e1')
            assert_equals(r.error_code, 1)

        testit.sciunit('rm', 'e2')

        with assert_raises(SystemExit) as r:
            testit.sciunit('show')
            assert_equals(r.error_code, 1)