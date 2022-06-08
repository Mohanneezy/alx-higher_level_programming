#!/usr/bin/python3
# 3-common_elements.py


def common_elements(set_1, set_2):
    for i in set_1:
        if i in set_2:
            return set_1[i]
