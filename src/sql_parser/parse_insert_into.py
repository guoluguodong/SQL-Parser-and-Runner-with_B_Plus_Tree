def parse_insert_into(sql: str) -> tuple:
    sql = sql[6:-1]
    sql = sql.strip()[4:]
    table_name, attributes, values = sql.split("(")
    table_name = table_name.strip()
    attributes, _ = attributes.split(")")
    attributes = attributes.split(",")
    attributes = [attribute.strip() for attribute in attributes]
    values, _ = values.split(")")
    values = values.split(",")
    values = [value.strip() for value in values]
    return table_name, attributes, values
