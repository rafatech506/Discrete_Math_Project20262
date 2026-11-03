""" Author: Oscar Vargas Pabon
A little helper to test your solution. Basically reads a file in the structure of
	/tests/ and verifies if it gives the same answer as my solution.
* Structure of files:

<name_space> ∈ {'propositional_logic', 'set_operators', 'arithmetic'}
<test_cases>
.... Several test cases


* For each test case we have
<formula>
<clean_formula>
<number of variables> <number of unary operators> <number of binary operators>
<evaluation of the formula>
<value of the 1th variable>  <value of the 2th variable> ... <value of the ith variable> ...

* Notice that <formula> may have 'blank spaces', which are the characters found
	in helpers.Blank_Spaces
  Under this idea <clean_formula> is the result after invoking str(.) over the 
  expression tree.
* Notice that for set operations I did some code/decode to allow easily the reading
	and writing through stdin/stdout.

"""
import sys
sys.setrecursionlimit(10**7)
from helpers import *
from interface_function import Valuation
import solution as sol

def main():
	name_space=sys.stdin.readline().strip()
	name_variables,unary_operators,binary_operators=The_spaces[name_space]
	var_am=len(name_variables)

	t=int(sys.stdin.readline().strip())
	for _  in range(t):
		raw_cad=sys.stdin.readline().strip()
		god_cad=sys.stdin.readline().strip()
		nvar,nuni,nbin=list(map(int,sys.stdin.readline().split()))
		god_ans=sys.stdin.readline().strip()
		raw_in=sys.stdin.readline().split()
		value_variables=[None for _ in range(var_am)]
		for i in range(var_am):
			if(name_space=="propositional_logic"):god_in=raw_in[i]=='True'
			elif(name_space=="set_operators"):god_in=decode_set(int(raw_in[i]))
			elif(name_space=="arithmetic"):god_in=int(raw_in[i])
			value_variables[i]=god_in

		the_formula=sol.expression_tree(raw_cad)
		assert(str(the_formula)==god_cad)
		nres=the_formula.count()
		assert(nres['var']==nvar and nres['uni']==nuni and nres['bin']==nbin)
		mvaluation=Valuation(
				{name_variables[i]:value_variables[i] for i in range(var_am)}
				,unary_operators,binary_operators
				)
		our_ans=the_formula.eval(mvaluation)
		if(name_space=="set_operators"):our_ans=code_set(our_ans)
		assert(str(our_ans)==god_ans)
if __name__=="__main__":
	main()
	pass