# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class LittleElephantAndBooks:
	def getNumber(self,pages,number):
		p=sorted(pages)
		s=0
		for i in range(number-1):
			s+=p[i]
		s+=p[number]
		return s

