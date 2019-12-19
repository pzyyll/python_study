# -*- coding:utf-8 -*-

import functools
import types

class Decorator(object):
	def __init__(self, func):
		functools.update_wrapper(self, func)
		self.func = func

	def __call__(self, instance, *args, **kwargs):
		print('@call Decorator', self, args, kwargs)
		return self.func(instance, *args, **kwargs)

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			return types.MethodType(self, instance)


class FuncObj(object):
	def __call__(self, *args, **kwargs):
		print('@FuncObj', self, args, kwargs)


class TObj(object):
	fObj = FuncObj()

	@Decorator
	def P(self, *args, **kwargs):
		print ('@p, ', self, args, kwargs)


def tFunc(self, *args, **kwargs):
	print('@tFunc', self, args, kwargs)


def testFunc1():
	t0 = TObj()

	t0.P(1,2,3)

	t0.fObj(1,2,3)

	t0.tFunc = tFunc
	t0.tFunc(1,2,3)

	t0.tFuncBound = types.MethodType(tFunc, t0)
	t0.tFuncBound(1,2,3)

if __name__ == '__main__':
    testFunc1()