# -*- coding: utf-8 -*-

from solution import BaileReconciliacion


class TestBaileReconciliacion(object):
    @classmethod
    def setup_class(cls):
        cls.baile_reconciliacion = BaileReconciliacion()

    def test_results(self):
        assert self.baile_reconciliacion.solve(20) == 5
        assert self.baile_reconciliacion.solve(1) == 1
        assert self.baile_reconciliacion.solve(9747) == 57
