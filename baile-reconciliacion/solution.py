# -*- coding: utf-8 -*-

from itertools import combinations_with_replacement


class BaileReconciliacion(object):
    def solve(self, numero_bailes):
        combinaciones_invitados = []
        combinaciones_invitados_append = combinaciones_invitados.append

        for invite in combinations_with_replacement(range(numero_bailes + 1), 3):
            nlogonia, cuadradonia, cubiconia = invite

            if cubiconia >= cuadradonia >= nlogonia:
                producto = cubiconia * cuadradonia + cubiconia * nlogonia + \
                    cuadradonia * nlogonia

                if producto == numero_bailes:
                    combinaciones_invitados_append(invite)

        return len(combinaciones_invitados)
