#!C:\wamp64\www\CGI\venv\Scripts\python.exe

import cgi
import cgitb
import MySQLdb

cgitb.enable()
try:
    myDb = MySQLdb.connect(host="localhost",user="root",password="",db="test")
    myCursor = myDb.cursor()

    form = cgi.FieldStorage()
    username = form.getvalue('username')
    password = form.getvalue('password')
    email = form.getvalue("email")

    sql = "INSERT INTO user (`username`, `password`) VALUES(%s,%s)"
    myCursor.execute(sql,(username,password))
    myDb.commit()
    print("Content-type:text/html")
    print()
    print(f'''<!DOCTYPE html>
                <html lang='en'>
                    <head>
                        <meta charset='UTF-8'>
                        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                        <title>Welcome</title>
                    </head>
                    <body>
                        <center>
                            <h1>Welcome, {username}!</h1>
                            <p>Your Registration was successful! check verification sent on {email}</p>
                            <p style='color:blue;'>Continue With registration</p>
                        </center>
                    </body>
                </html>''')
except Exception as e:
    print(e)
finally:
    myDb.close()

