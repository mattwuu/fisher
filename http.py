#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: http.py
@time: 2018/11/30 3:14
@desc:
"""

import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
