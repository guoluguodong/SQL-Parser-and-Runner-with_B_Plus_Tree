def parse_conditions(conditions: str) -> tuple:
    def parse_B(operator: str, B: str):
        if B.isnumeric():
            if "." in B:
                B = float(B)
            else:
                B = int(B)

        if operator == "!=":
            return lambda x: x != B
        elif operator == ">":
            return lambda x: x > B
        elif operator == "<":
            return lambda x: x < B
        elif operator == "=":
            return lambda x: x == B
        else:
            raise ValueError("Unsupported operator {}".format(operator))

    operators = ["!=", ">", "<", "="]
    for operator in operators:
        if conditions.count(operator) != 0:
            pos = conditions.index(operator)
            A = conditions[:pos].strip()
            B = conditions[pos + len(operator) :].strip()
            return (A, parse_B(operator=operator, B=B))
    else:
        raise ValueError("Invalid conditions {}".format(conditions))
