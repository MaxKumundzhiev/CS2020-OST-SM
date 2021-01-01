# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

from abc import ABC


class Factory(ABC):
    def read_data(self):
        """read any data"""
        pass

    def write_data(self):
        """"write data"""
        pass


class Transformer(Factory):
    def _extract_features(self):
        pass

    def _transform_features(self):
        pass

    def _select_features(self):
        pass


class Visualiser(Factory):
    def plot_importance(self):
        """"visualise features importance"""

