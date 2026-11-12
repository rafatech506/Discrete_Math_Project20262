import sys
from helpers import Blank_Spaces

if hasattr(sys.stdin, 'reconfigure'):
    try:
        sys.stdin.reconfigure(encoding='utf-8')
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class Formula:
    """
    Clase abstracta base para representar una fórmula lógica.
    El uso de 'pass' se limita estrictamente a los métodos abstractos.
    """
    def __str__(self) -> str:
        pass

    def eval(self, valuation) -> any:
        pass

    def count(self) -> dict:
        pass


class Variable(Formula):
    """
    Nodo hoja que representa una variable dentro de la fórmula.
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        res = self.name
        return res

    def eval(self, valuation):
        # AQUI ESTA LA CORRECCION: Se usa 'variable' en singular
        if hasattr(valuation, 'variable'):
            res = valuation.variable[self.name]
        elif hasattr(valuation, 'get'):
            res = valuation[self.name]
        else:
            res = valuation.variable[self.name]
        return res

    def count(self) -> dict:
        res = {'var': 1, 'uni': 0, 'bin': 0}
        return res


class UnaryFormula(Formula):
    """
    Nodo que representa una fórmula con operador unario: op(child)
    """
    def __init__(self, op: str, child: Formula):
        self.op = op
        self.child = child

    def __str__(self) -> str:
        res = self.op + "(" + str(self.child) + ")"
        return res

    def eval(self, valuation):
        if hasattr(valuation, 'unary'):
            func = valuation.unary[self.op]
        elif hasattr(valuation, 'get'):
            func = valuation[self.op]
        else:
            func = valuation.unary[self.op]
        res = func(self.child.eval(valuation))
        return res

    def count(self) -> dict:
        c = self.child.count()
        res = {
            'var': c['var'],
            'uni': c['uni'] + 1,
            'bin': c['bin']
        }
        return res


class BinaryFormula(Formula):
    """
    Nodo que representa una fórmula con operador binario: (left)op(right)
    """
    def __init__(self, left: Formula, op: str, right: Formula):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self) -> str:
        res = "(" + str(self.left) + ")" + self.op + "(" + str(self.right) + ")"
        return res

    def eval(self, valuation):
        if hasattr(valuation, 'binary'):
            func = valuation.binary[self.op]
        elif hasattr(valuation, 'get'):
            func = valuation[self.op]
        else:
            func = valuation.binary[self.op]
        res = func(self.left.eval(valuation), self.right.eval(valuation))
        return res

    def count(self) -> dict:
        l = self.left.count()
        r = self.right.count()
        res = {
            'var': l['var'] + r['var'],
            'uni': l['uni'] + r['uni'],
            'bin': l['bin'] + r['bin'] + 1
        }
        return res


def parse_clean_formula(s: str) -> Formula:
    """
    Parsea recursivamente una cadena sin espacios para construir el árbol.
    """
    res = None
    if s[0] == '(':
        count_paren = 0
        match_idx = -1
        
        for idx in range(len(s)):
            if match_idx == -1:
                if s[idx] == '(':
                    count_paren = count_paren + 1
                elif s[idx] == ')':
                    count_paren = count_paren - 1
                    if count_paren == 0:
                        match_idx = idx

        next_open = -1
        for idx2 in range(match_idx + 1, len(s)):
            if next_open == -1:
                if s[idx2] == '(':
                    next_open = idx2

        left_str = s[1:match_idx]
        op = s[match_idx + 1:next_open]
        right_str = s[next_open + 1:-1]

        left_formula = parse_clean_formula(left_str)
        right_formula = parse_clean_formula(right_str)
        res = BinaryFormula(left_formula, op, right_formula)

    else:
        first_open = -1
        for idx3 in range(len(s)):
            if first_open == -1:
                if s[idx3] == '(':
                    first_open = idx3

        if first_open == -1:
            res = Variable(s)
        else:
            op = s[0:first_open]
            inner_str = s[first_open + 1:-1]
            inner_formula = parse_clean_formula(inner_str)
            res = UnaryFormula(op, inner_formula)

    return res


def expression_tree(s: str) -> Formula:
    """
    Función principal requerida por la interfaz.
    """
    cleaned = ""
    for char in s:
        is_blank = False
        for blank in Blank_Spaces:
            if char == blank:
                is_blank = True

        if not is_blank:
            cleaned = cleaned + char

    res = parse_clean_formula(cleaned)
    return res

