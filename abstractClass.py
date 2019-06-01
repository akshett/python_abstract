#!/usr/bin/python3

# Creeating an abstract class in python

from abc import ABC, abstractmethod

class Language(ABC):
    self.region_list = ['']

    @abstractmethod
    def get_region(self):
        pass
