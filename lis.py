import functools

class Expression():
    def __init__(self, func, args):
        self.func = func
        self.args = args
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return "({} {})".format(self.func, self.args)


fn_table = {
    "=": lambda *x: functools.reduce(lambda a, b: a == b, x),
    "+": lambda *x: sum(x),
    "-": lambda *x: functools.reduce(lambda a, b: a - b, x),
    "*": lambda *x: functools.reduce(lambda a, b: a * b, x),
    "/": lambda *x: functools.reduce(lambda a, b: a / b, x),
    ">": lambda *x: max(x),
    "<": lambda *x: min(x),
    "//": lambda *x: functools.reduce(lambda a, b: a // b, x),
    "println": lambda x: print(x),
}


def tokenize(code):
    return code.replace("(", " ( ").replace(")", " ) ").split()


def express(expr):
    func = None
    args = []
    while expr[0] != ")":
        if expr[0] == "(":
            expr.pop(0)
            expr.insert(0, express(expr))
        else:
            if not func:
                func = expr.pop(0)
            else:
                args.append(expr.pop(0))
    if not args:
        return func
    else:
        expression = Expression(func, args)
        return expression


def read(code):
    tokens = tokenize(code)
    return express(tokens)


def eval(expr):
    if type(expr) == Expression:
        func = expr.func
        args = [eval(x) for x in expr.args]
        return fn_table[func](*args)
    else:
        try:
            return int(expr)
        except ValueError:
            return str(expr)


if __name__ == "__main__":
    while True:
        code = input("> ")
        print(eval(read(code)))