from sql_runner.merge_join import JoinMode


def parse_select(sql: str) -> tuple:
    from sql_parser.parse_conditions import parse_conditions

    sql = sql[6:-1]
    if sql.find("where") != -1:
        sql, conditions = sql.split("where")
        conditions = conditions.strip()
        conditions = parse_conditions(conditions=conditions)
    else:
        conditions = None
    attributes, tables = sql.strip().split("from")
    attributes = attributes.strip().split(",")

    mode = JoinMode.inner_join
    if "left outer join" in tables:
        tables = tables.split("left outer join")
        mode = JoinMode.left_outer_join
    elif "right outer join" in tables:
        tables = tables.split("right outer join")
        mode = JoinMode.right_outer_join
    elif "outer join" in tables:
        tables = tables.split("outer join")
        mode = JoinMode.full_outer_join
    else:
        tables = tables.split("join")
    tables = [table.strip() for table in tables]
    attributes = [attribute.strip() for attribute in attributes]
    tables = [table.strip() for table in tables]
    return tables, attributes, conditions, mode
