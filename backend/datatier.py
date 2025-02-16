#
# datatier.py
#
# Executes SQL queries against the given database.
#

# runs a sql SELECT statement and returns a row
def select_one_row(dbConn, sql, parameters=None):
    if (parameters == None):
        parameters = []

    dbCursor = dbConn.cursor()
    try:
        dbCursor.execute(sql, parameters)
        row = dbCursor.fetchone()

        if row == None:
            row = '()'
        return row
    except Exception as err:
        print("select_one_row failed:", err)
        return None
    finally:
        dbConn.close()

# runs a sql SELECT statement and returns all rows
def select_n_rows(dbConn, sql, parameters=None): 
    if (parameters == None):
       parameters = []

    dbCursor = dbConn.cursor()

    try:
       dbCursor.execute(sql, parameters)
       rows = dbCursor.fetchall()
       return rows
    except Exception as err:
       print("select_n_rows failed:", err)
       return []
    finally:
       dbCursor.close()

# runs update, delete, insert commands
def perform_action(dbConn, sql, parameters=None):
    if (parameters == None):
        parameters = []

    dbCursor = dbConn.cursor()

    try:
        dbCursor.execute(sql, parameters)
        dbConn.commit()
        return dbCursor.rowcount
    except Exception as err:
        # print("perform_action failed:", err)
        print("perform_action failed:", err)
        return -1 
    finally:
        dbCursor.close()


