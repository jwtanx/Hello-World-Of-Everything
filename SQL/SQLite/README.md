# Python SQLite3

## Merging databases

```py
def merge_databases(db1, db2):
    con3 = sqlite3.connect(db1)

    con3.execute("ATTACH '" + db2 +  "' as dba")

    con3.execute("BEGIN")
    for row in con3.execute("SELECT * FROM dba.sqlite_master WHERE type='table'"):
        combine = "INSERT OR IGNORE INTO "+ row[1] + " SELECT * FROM dba." + row[1]
        print(combine)
        con3.execute(combine)
    con3.commit()
    con3.execute("detach database dba")


def read_files(directory):
    fname = []
    for root,d_names,f_names in os.walk(directory):
        for f in f_names:
            c_name = os.path.join(root, f)
            filename, file_extension = os.path.splitext(c_name)
            if (file_extension == '.sqlitedb'):
                fname.append(c_name)

    return fname

def batch_merge(directory):
    db_files = read_files(directory)
    for db_file in db_files[1:]:
        merge_databases(db_files[0], db_file)

if __name__ == '__main__':
    batch_merge('/directory/to/database/files')
```

## Getting the list of tables
```py
import sqlite3
connection = sqlite3.connect("test.db")
query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor = connection.execute(query)
tables = [fetch[0] for fetch in cursor.fetchall()]
```

## Getting the list of columns
Reference: https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite
```py
import sqlite3

connection = sqlite3.connect("test.db")
table_name = "test"
query = f"SELECT * FROM {table_name}"
cursor = connection.execute(query)
cols = list(map(lambda x: x[0], cursor.description))
cols = [description[0] for description in cursor.description]
```