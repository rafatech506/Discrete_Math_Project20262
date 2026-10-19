"""Author: Oscar Vargas Pabon
These are mainly constants and the code/decode of sets
"""
Blank_Spaces=[' ','	']
Names_Set_Universe=["hola",2,"lalalalala",354,23234.435,"https://www.youtube.com/watch?v=JsFnhaBXKIQ",333,(23,54,5)]
Set_Universe=set(Names_Set_Universe)
def code_set(X:set)->str:
	aux=lambda ind:0 if ind<0 else (int(Names_Set_Universe[ind]in X)<<ind)|aux(ind-1)
	return aux(len(Names_Set_Universe)-1)
def decode_set(X:int)->str:
	aux=lambda ind:set()if ind<0 else (aux(ind-1) if (X>>ind&1)==0 else {Names_Set_Universe[ind]}|aux(ind-1))
	return aux(len(Names_Set_Universe)-1)
The_spaces={
	"propositional_logic":(
		["p","q","r","s","t"],
		{'¬':lambda x:not x},
		{'∧':lambda x,y:x and y,
		 '∧':lambda x,y:x or  y,
		 '→':lambda x,y:(not x) or y,
		 '↔':lambda x,y:x==y,
		'⊕':lambda x,y:x!=y }
		),
	"set_operators":(
		["X","Y","Z","W"],
		{"C":lambda x:Set_Universe.difference(x)},
		{"∪":lambda x,y:x|y,"∩":lambda x,y:x&y,
		"-":lambda x,y:x.difference(y)}
		),
	"arithmetic":(
		["x","y","z","w"],
		{'-':lambda x:-x},
		{'+':lambda x,y:x+y,'*':lambda x,y:x*y,'-':lambda x,y:x-y}
		),
}