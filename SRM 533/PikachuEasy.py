# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class PikachuEasy:
    def check(self, word):
        i=0
        l=len(word)
        i+=word.count("pi")*2
        i+=word.count("ka")*2
        i+=word.count("chu")*3
        if(i!=l): return "NO"
        return "YES"
