def insert_into(
    database_name: str, table_name: str, attributes: list[str], values: list,TABLES: dict, bptrees: list, dic_bptree_tablename_to_index: dict
):
    import os
    import pandas as pd

    from sql_runner.my_select import my_select
    import b_plus_tree

    selected = my_select(
        TABLES=TABLES, bptrees=bptrees,
        dic_bptree_tablename_to_index=dic_bptree_tablename_to_index,
        database_name=database_name,
        table_name="__META",
        attributes=["PRIMARY_KEY"],
        conditions=("TABLE_NAME", lambda x: x == table_name),
    )
    if selected.empty:
        raise ValueError("No table named {}".format(table_name))
    primary_key = selected["PRIMARY_KEY"].values[0]
    if primary_key not in attributes:
        raise ValueError("Cannot insert without primary key {}.".format(primary_key))
    primary_key_value = values[attributes.index(primary_key)]
    if not my_select(
        TABLES=TABLES, bptrees=bptrees,
        dic_bptree_tablename_to_index=dic_bptree_tablename_to_index,
        database_name=database_name,
        table_name=table_name,
        attributes=[primary_key],
        conditions=(primary_key, lambda x: x == primary_key_value),
    ).empty:
        raise ValueError("Primary key {} existed.".format(primary_key_value))
    inserted = dict()
    for attribute, value in zip(attributes, values):
        inserted[attribute] = value
    df = pd.DataFrame(data=inserted, columns=attributes, index=[primary_key_value])

    path = os.path.join(database_name, table_name + ".csv")
    old = pd.read_csv(filepath_or_buffer=path, index_col=0)
    new = pd.concat(objs=[old, df])
    new.to_csv(path_or_buf=path)
    # 添加记录到B+树
    if table_name != "__META" :
        bptrees[dic_bptree_tablename_to_index[table_name]].insert(b_plus_tree.KeyValue(values[0], values))
    return new
