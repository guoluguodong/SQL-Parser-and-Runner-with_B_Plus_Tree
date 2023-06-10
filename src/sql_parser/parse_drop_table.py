def parse_drop_table(sql: str) -> list[str]:
    sql = sql[4:-1]
    sql = sql.strip()[5:]
    tables = sql.split(",")
    tables = [table.strip() for table in tables]
    return tables
