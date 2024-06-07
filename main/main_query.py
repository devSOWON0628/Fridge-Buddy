import sqlite3
con = sqlite3.connect('./db.sqlite3', check_same_thread=False)
con.row_factory = sqlite3.Row
cur = con.cursor()

def insertIngredient(name, amount, amountUnit):
    return cur.execute('INSERT INTO ingredient (name, amount, amountUnit) VALUES (?, ?, ?);', (name, amount, amountUnit))

def selectAllIngredients():
    cur.execute("SELECT * FROM main_ingredient;")
    rows = cur.fetchall()
    rowarray_list = []
    for row in rows:
        d = dict(zip(row.keys(), row))   # a dict with column names as keys
        rowarray_list.append(d)
    return rowarray_list

def updateIngredient(data):
    cur.execute('UPDATE main_ingredient SET name= "%s", amount= %s, unit= %s WHERE id= %s' % (data['name'], data['amount'], data['unit'], data['id']))
    con.commit()
    
def createIngredient(data):
    cur.execute('INSERT INTO main_ingredient (name, amount, unit, user_id, imgUrl) VALUES (?, ?, ?, ?, ?);', (data['name'], data['amount'], data['unit'], 1, data['imgUrl']))
    con.commit()
    
def deleteIngredient(ingredientId):
    cur.execute('DELETE FROM main_ingredient WHERE id = ?;', (ingredientId, ))
    con.commit()
