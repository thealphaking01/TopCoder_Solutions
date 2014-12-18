# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BuyingTshirts:
    def meet(self, t, q, p):
	i=0
	j=0
	r=0
	for k in range(len(p)):
		i+=p[k]
		j+=q[k]
		if(i>=t and j>=t):
			r+=1
			i-=t
			j-=t
		if(i>=t): i-=t
		if(j>=t): j-=t
	return r


