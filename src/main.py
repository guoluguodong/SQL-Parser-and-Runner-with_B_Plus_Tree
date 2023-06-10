from sql_parser.parser import parse_sql
from sql_runner.runner import run_sql
from sql_runner.create_database import create_database
from sql_runner.init_meta import init_meta
from sql_parser.parser_where import parser_where
database_name = input("Enter database name: ")
create_database(database_name=database_name)
init_meta(database_name=database_name)
TABLES = {}
bptrees = []
dic_bptree_tablename_to_index = {}

while True:
    sql = input("Enter SQL: ")
    con_where = parser_where(sql)
    type, args = parse_sql(sql=sql)
    print(type, args)
    df = run_sql(database_name=database_name, type=type, args=args, TABLES=TABLES, bptrees=bptrees,
                 dic_bptree_tablename_to_index=dic_bptree_tablename_to_index, con_where=con_where)
    print(df)
