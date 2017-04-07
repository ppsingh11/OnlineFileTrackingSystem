#!/usr/bin/python

import cgi, cgitb ,os,webbrowser
import mysql.connector as mariadb
form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"

print '<html>'
print '<head>'
print '<link rel="stylesheet" type="text/css" href="login.css">'

print '</head>'
print '<body>'

u_name=form.getvalue('uname')
paswd=form.getvalue('psw')

mariadb_connection = mariadb.connect(user='pps', password='pps', database='student')

cursor = mariadb_connection.cursor(buffered=True)
cursor.execute("select Password from user_entry where ID='{0}'".format(u_name))
passwd=cursor.fetchone()[0]
passwd=str(passwd)
if passwd==paswd:
	print '<form action="http://localhost/update.cgi" method ="post">'
	print '<input type="text" placeholder="Enter file id" name="file_id" required>'
	print '<input type="submit" value="Update existing"></a>'
	print '<input type="hidden" name ="post" value=%s>'%(u_name)
	print '</form>'
	print '<br>'
	print '<form action="http://localhost/login.cgi">'
	print '<input type="submit" value="Add New Entry"></button></a>'
	print '</form>'
	
	
else :
  	print "Wrong Credentials"

print '</body>'
print '</html>'


