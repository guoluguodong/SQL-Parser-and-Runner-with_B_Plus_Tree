from enum import Enum


class SQLType(Enum):
    SELECT = 0
    INSERT = 1
    DELETE = 2
    DROP = 3
    CREATE = 4
