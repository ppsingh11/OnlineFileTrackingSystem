#!/usr/bin/python

import cgi, cgitb 
import mysql.connector as mariadb
form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"

print '<html>'
print '<head>'
print '<link rel="stylesheet" type="text/css" href="login.css">'
print '''<script>
function myFunction() {
    window.print();
}
</script>'''
print '</head>'
print '<body>'

f_type=form.getvalue('f_type')
name=form.getvalue('Name')
id=form.getvalue('Id')
branch=form.getvalue('branch')
semester=form.getvalue('sem')
email=form.getvalue('Email')
contact=form.getvalue('Mob')

mariadb_connection = mariadb.connect(user='pps', password='pps', database='student')

cursor = mariadb_connection.cursor(buffered=True)
if f_type=='Medical':
		F_ID='ML'+id
		
		cursor.execute("insert into Medical(ID) values('{0}')".format(F_ID))
elif f_type=='Leave':
		F_ID='LE'+id
		
		cursor.execute("insert into Leave_app(ID) values('{0}')".format(F_ID))
elif f_type=='Project':
		F_ID='PT'+id
		
		cursor.execute("insert into Project_file(ID) values('{0}')".format(F_ID))
elif f_type=='Railways':
		F_ID='RS'+id

		cursor.execute("insert into Railway_conces(ID) values('{0}')".format(F_ID))


cursor.execute("insert into Registartion_detail values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(F_ID,name,id,branch,semester,email,contact))

mariadb_connection.commit()

print '<h1><center>Your details has been saved successfully</center></h1>'
print '<center> <h3>'
print "File_ID :    ",F_ID
print '<br>'
print '<br>'
print '<br>'
print "File type :    ",f_type 
print '<br>'
print '<br>'
print '<br>'
print "File_Name :    ",name 
print '<br>'
print '<br>'
print '<br>'
print "Your Id :    ",id 
print '<br>'
print '<br>'
print '<br>'

print '<button onclick="myFunction()">Print this page</button>'
print '</h3></center>'
print '</body>'
print '</html>'


