def drop_table(database_name: str, table_name: str | list[str]):
    import os

    from sql_runner.delete_from import delete_from

    if isinstance(table_name, str):
        if table_name == "__META":
            raise ValueError("Cannot delete meta data.")
        path = os.path.join(database_name, table_name + ".csv")
        os.remove(path=path)
        delete_from(
            database_name=database_name,
            table_name="__META",
            conditions=("TABLE_NAME", lambda x: x == table_name),
        )
    else:
        for t in table_name:
            drop_table(database_name=database_name, table_name=t)
