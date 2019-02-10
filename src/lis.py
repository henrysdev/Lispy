
class Expression():
    def __init__(self, func, args):
        self.func = func
        self.args = args


def read(code):
    return code.replace("(", " ( ").replace(")", " ) ").split()


def eval(expr):
    func = None
    args = []
    while expr[0] != ")":
        if expr[0] == "(":
            expr.pop(0)
            expr.insert(0, eval(expr))
        else:
            if not func:
                func = expr.pop(0)
            else:
                args.append(expr.pop(0))
    print("func:", func, " args:", args)
    return Expression(func, args)


if __name__ == "__main__":
    while True:
        code = input("> ")
        eval(read(code))