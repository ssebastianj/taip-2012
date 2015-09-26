# -*- coding: utf-8 -*-

from solution import Awari


class TestAwari20(object):
    @classmethod
    def setup_class(cls):
        cls.awari = Awari()

    def test_solve(self):
        assert self.awari.solve([1, 2, 3]) == 'N'
        assert self.awari.solve([1, 1, 3, 0]) == 'S'
        assert self.awari.solve([0, 1, 3, 0, 2]) == 'N'
