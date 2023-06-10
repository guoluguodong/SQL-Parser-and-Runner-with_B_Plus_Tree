def create_table(
    database_name: str, table_name: str, attributes: list[str], primary_key: str, TABLES: dict, bptrees: list, dic_bptree_tablename_to_index: dict
):
    import os
    import pandas as pd

    from sql_runner.my_select import my_select
    from sql_runner.insert_into import insert_into
    import b_plus_tree
    if primary_key not in attributes:
        raise ValueError("No attribute named {}.".format(primary_key))
    if not my_select(
        TABLES=TABLES, bptrees=bptrees,
        dic_bptree_tablename_to_index=dic_bptree_tablename_to_index,
        database_name=database_name,
        table_name="__META",
        attributes=["TABLE_NAME"],
        conditions=("TABLE_NAME", lambda x: x == table_name),
    ).empty:
        raise ValueError("Table {} existed.".format(table_name))
    insert_into(
        database_name=database_name,
        table_name="__META",
        attributes=["TABLE_NAME", "ATTRIBUTES", "PRIMARY_KEY"],
        values=[table_name, ",".join(attributes), primary_key],
        TABLES=TABLES, bptrees=bptrees,
        dic_bptree_tablename_to_index=dic_bptree_tablename_to_index
    )

    path = os.path.join(database_name, table_name + ".csv")
    df = pd.DataFrame(columns=attributes)
    df.to_csv(path_or_buf=path)
    # 创建B+树索引，以第一列创建
    TABLES[table_name] = attributes
    bptree = b_plus_tree.Bptree(4, 4)
    bptrees.append(bptree)
    dic_bptree_tablename_to_index[table_name] = len(bptrees) - 1
    return df
