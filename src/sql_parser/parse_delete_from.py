def parse_delete_from(sql: str) -> tuple:
    from sql_parser.parse_conditions import parse_conditions

    sql = sql[6:-1]
    sql = sql.strip()[4:]
    if "where" in sql:
        table_name, conditions = sql.split("where")
        table_name = table_name.strip()
        conditions = conditions.strip()
        return table_name, parse_conditions(conditions)
    else:
        table_name = sql.strip()
        return table_name, None
