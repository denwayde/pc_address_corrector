import sqlite3

connection = sqlite3.connect('data.db')


def delete_or_insert_data(delete_or_insert_query, tup=()):
    global connection
    cur = connection.cursor()
    cur.execute(delete_or_insert_query, tup)
    connection.commit()
    #connection.close()

def select_data(selection_query, tup=()):
    global connection
    cur = connection.cursor()
    cur.execute(selection_query, tup)
    return cur.fetchall()
    #connection.close()

#print(select_data('SELECT DISTINCT row FROM seats WHERE taken = ? and place = ?', (0, "Партер", )))