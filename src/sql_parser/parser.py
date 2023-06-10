def parse_sql(sql: str):
    from sql_parser.parse_create_table import parse_create_table
    from sql_parser.parse_delete_from import parse_delete_from
    from sql_parser.parse_drop_table import parse_drop_table
    from sql_parser.parse_insert_into import parse_insert_into
    from sql_parser.parse_select import parse_select
    from sql_type import SQLType

    sql = sql.strip()
    if sql.startswith("select"):
        return SQLType.SELECT, parse_select(sql=sql)
    elif sql.startswith("delete"):
        return SQLType.DELETE, parse_delete_from(sql)
    elif sql.startswith("drop"):
        return SQLType.DROP, parse_drop_table(sql)
    elif sql.startswith("create"):
        return SQLType.CREATE, parse_create_table(sql)
    elif sql.startswith("insert"):
        return SQLType.INSERT, parse_insert_into(sql)
    else:
        raise ValueError("Invalid SQL type.")
