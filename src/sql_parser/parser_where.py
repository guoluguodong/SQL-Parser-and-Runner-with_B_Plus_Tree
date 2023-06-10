def parser_where(sql: str) -> list[str]:
    if sql.find("where") != -1:
        result = [0, 0, 0]
        sql, conditions = sql.split("where")
        conditions = conditions.strip()
        conditions = conditions[:-1]
        if conditions.find('<=') != -1:
            result[1] = '<='
            conditions = conditions.replace("<=", ",")
        elif conditions.find('>=') != -1:
            result[1] = '>='
            conditions = conditions.replace(">=", ",")
        elif conditions.find('<') != -1:
            result[1] = '<'
            conditions = conditions.replace("<", ",")
        elif conditions.find('=') != -1:
            result[1] = '='
            conditions = conditions.replace("=", ",")
        elif conditions.find('>') != -1:
            result[1] = '>'
            conditions = conditions.replace(">", ",")
        conditions = conditions.split(",")
        result[0] = conditions[0].strip()
        result[2] = conditions[1].strip()
    else:
        result = None
    return result

