def create_database(database_name: str) -> None:
    import os

    if not os.path.exists(database_name):
        os.mkdir(path=database_name)



