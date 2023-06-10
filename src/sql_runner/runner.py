def run_sql(database_name: str, type, args, TABLES: dict, bptrees: list, dic_bptree_tablename_to_index: dict, con_where
):
    from sql_type import SQLType
    from sql_runner.create_table import create_table
    from sql_runner.insert_into import insert_into
    from sql_runner.delete_from import delete_from
    from sql_runner.drop_table import drop_table
    from sql_runner.my_select import my_select

    if type == SQLType.CREATE:
        table_name, attributes, primary_key = args
        df = create_table(
            database_name=database_name,
            table_name=table_name,
            attributes=attributes,
            primary_key=primary_key,
            TABLES=TABLES, bptrees=bptrees,
            dic_bptree_tablename_to_index=dic_bptree_tablename_to_index
        )
    elif type == SQLType.INSERT:
        table_name, attributes, values = args
        df = insert_into(
            database_name=database_name,
            table_name=table_name,
            attributes=attributes,
            values=values,
            TABLES=TABLES, bptrees=bptrees,
            dic_bptree_tablename_to_index=dic_bptree_tablename_to_index
        )
    elif type == SQLType.DELETE:
        table_name, conditions = args
        df = delete_from(
            database_name=database_name, table_name=table_name, conditions=conditions
        )
    elif type == SQLType.DROP:
        table_name = args
        df = drop_table(database_name=database_name, table_name=table_name)
    elif type == SQLType.SELECT:
        table_name, attributes, conditions, mode = args
        df = my_select(
            con_where = con_where,
            TABLES=TABLES, bptrees=bptrees,
            dic_bptree_tablename_to_index=dic_bptree_tablename_to_index,
            database_name=database_name,
            table_name=table_name,
            attributes=attributes,
            conditions=conditions,
            mode=mode
        )
    else:
        raise ValueError("Invalid SQL type.")
    return df
