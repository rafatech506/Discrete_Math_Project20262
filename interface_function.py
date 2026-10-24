"""Author: Oscar Vargas Pabon
Blueprint/interface for the project.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
class Valuation:
	def __init__(self,variable_equiv:dict,unary_equiv:dict,binary_equiv):
		self.variable=variable_equiv
		self.unary=unary_equiv
		self.binary=binary_equiv
class Formula(ABC):
	@abstractmethod
	def __str__(self)->str:
		#str(v) = v
		#str(∘φ) = ∘ + "(" + str(φ) + ")"
		#str(φ□β) = "(" + str(φ) + ")" + □ + "(" + str(β) + ")"
		pass
	@abstractmethod
	def eval(self,val:Valuation):
		#Evaluates the formula given the mappings in 'val'
		pass
	@abstractmethod
	def count(self)->dict[str,int]:
		#Counts the amount of variables, unary operators and binary operators
		## the answer 'ans' is organized as:
		##        * ans['var']:amount of variables
		##        * ans['uni']:amount of unary operators
		##        * ans['bin']:amount of binary operators
		pass
def expression_tree(cad:str)->Formula:
	# receives a correct formula. ej:
	#  (x)+(y) ; w ; code((A)multiply(B))
	# and builds the corresponding expression tree 
	pass