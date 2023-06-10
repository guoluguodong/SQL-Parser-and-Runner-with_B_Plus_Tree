def parse_create_table(sql: str) -> tuple:
    sql = sql[6:-1]
    sql = sql.strip()[5:]
    pos = sql.find("(")
    table_name, others = sql[:pos], sql[pos + 1 :]
    table_name = table_name.strip()
    attributes, primary_key = others.split("primary")
    attributes = attributes.split(",")[:-1]
    attributes = [attribute.split()[0] for attribute in attributes]
    primary_key = primary_key.strip()[3:].strip()[1:-1].strip()[:-1].strip()
    return table_name, attributes, primary_key
