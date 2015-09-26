# -*- coding: utf-8 -*-


class Awari(object):
    def solve(self, boxes_list):
        running = True
        solution = 'S'

        while running:
            print(boxes_list)

            nro_box = len(boxes_list)
            i = 0
            for rocks in boxes_list[::-1]:
                if nro_box == rocks:
                    i = rocks
                    boxes_list[nro_box - 1] = 0
                    break
                nro_box -= 1
            else:
                if sum(boxes_list) == 0:
                    solution = 'S'
                else:
                    solution = 'N'
                break

            boxes_remaining = boxes_list[:i - 1]
            boxes_remaining_len = len(boxes_remaining)
            for nro_box, rocks in enumerate(boxes_remaining, 1):
                if rocks != 0 and nro_box > rocks and i > 0:
                    boxes_list[nro_box - 1] += 1
                    i -= 1
                    boxes_remaining_len -= 1

            if boxes_remaining_len == len(boxes_remaining):
                break

        return solution
