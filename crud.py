#!C:\wamp64\www\CGI\venv\Scripts\python.exe

import cgi
import cgitb
import MySQLdb

cgitb.enable()

def connect_db():
    return MySQLdb.connect(host="localhost", user="root", password="", db="test")

def create_user(cursor, username, password):
    sql = "INSERT INTO user (`username`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, (username, password))

def read_user(cursor, username):
    sql = "SELECT * FROM user WHERE username = %s"
    cursor.execute(sql, (username,))
    return cursor.fetchall()

def update_user(cursor, old_username, new_username, new_password):
    sql = "UPDATE user SET username = %s, password = %s WHERE username = %s"
    cursor.execute(sql, (new_username, new_password, old_username))

def delete_user(cursor, username):
    sql = "DELETE FROM user WHERE username = %s"
    cursor.execute(sql, (username,))

print("Content-type:text/html")
print()

try:
    form = cgi.FieldStorage()
    myDb = connect_db()
    myCursor = myDb.cursor()

    action = form.getvalue('action')

    if action == 'Create':
        username = form.getvalue('username')
        password = form.getvalue('password')
        create_user(myCursor, username, password)
        myDb.commit()
        print(f"<p>User {username} created successfully!</p>")

    elif action == 'Read':
        username = form.getvalue('username')
        user_data = read_user(myCursor, username)
        if user_data:
            for row in user_data:
                print(f"<p>Username: {row[0]}, Password: {row[1]}</p>")
        else:
            print("<p>No user found.</p>")

    elif action == 'Update':
        old_username = form.getvalue('old_username')
        new_username = form.getvalue('new_username')
        new_password = form.getvalue('new_password')
        update_user(myCursor, old_username, new_username, new_password)
        myDb.commit()
        print(f"<p>User {old_username} updated successfully!</p>")

    elif action == 'Delete':
        username = form.getvalue('username')
        delete_user(myCursor, username)
        myDb.commit()
        print(f"<p>User {username} deleted successfully!</p>")

except Exception as e:
    print(f"<p>Error: {e}</p>")
finally:
    myDb.close()
