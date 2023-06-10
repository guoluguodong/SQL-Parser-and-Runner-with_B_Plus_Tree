from sql_runner.merge_join import JoinMode
import b_plus_tree


def my_select(
        TABLES: dict,
        bptrees: list,
        dic_bptree_tablename_to_index: dict,
        database_name: str,
        table_name: str | list[str],
        attributes: list[str],
        conditions: tuple | None = None,
        mode: JoinMode = JoinMode.inner_join,
        con_where=None
):
    import os
    import pandas as pd

    if len(table_name) == 1:
        table_name = table_name[0]
    if isinstance(table_name, str):
        if con_where == None or table_name not in TABLES or TABLES[table_name][0] != con_where[0]:
            path = os.path.join(database_name, table_name + ".csv")
            df = pd.read_csv(filepath_or_buffer=path, index_col=0)
            if "*" in attributes:
                attributes = df.columns.values
            if conditions is not None:
                attribute, p = conditions
                if attribute in df:
                    selected = df.loc[p(df[attribute]), attributes]
                else:
                    selected = df[attributes]
            else:
                selected = df[attributes]
            return selected
        else:
            selected = b_plus_tree.searchIndex(bptrees[dic_bptree_tablename_to_index[table_name]], con_where,
                                               con_where[0])
            return selected[0].value

    elif len(table_name) == 2:
        from sql_runner.merge_join import merge_join
        # from merge_join import merge_join

        left_path = os.path.join(database_name, table_name[0] + ".csv")
        left_df = pd.read_csv(filepath_or_buffer=left_path, index_col=0)
        right_path = os.path.join(database_name, table_name[1] + ".csv")
        right_df = pd.read_csv(filepath_or_buffer=right_path, index_col=0)

        left_attributes = []
        right_attributes = []
        join_attributes = []
        if "*" in attributes:
            attributes = []
            for attribute in left_df:
                attributes.append(attribute)
            for attribute in right_df:
                attributes.append(attribute)
            attributes = list(set(attributes))

        for attribute in attributes:
            if attribute in left_df and attribute in right_df:
                join_attributes.append(attribute)
            if attribute in left_df:
                left_attributes.append(attribute)
            if attribute in right_df:
                right_attributes.append(attribute)

        left_df = my_select(con_where = con_where,TABLES=TABLES, bptrees=bptrees,
            dic_bptree_tablename_to_index=dic_bptree_tablename_to_index,database_name=database_name, table_name=table_name[0], attributes=left_attributes,
                            conditions=conditions)
        right_df = my_select(con_where = con_where,TABLES=TABLES, bptrees=bptrees,
            dic_bptree_tablename_to_index=dic_bptree_tablename_to_index,database_name=database_name, table_name=table_name[1], attributes=right_attributes,
                             conditions=conditions)
        df = merge_join(left=left_df, right=right_df, attributes=join_attributes, mode=mode)
        return df
    else:
        raise ValueError("Unsupported.")
