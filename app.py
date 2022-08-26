# importing required libraries
from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json

# instant of app 
app = Flask(__name__)


# connecting to MySQL engine and accessing database
app.config["MYSQL_HOST"]='localhost'
app.config["MYSQL_USER"]='rohit'
app.config["MYSQL_PASSWORD"]=''
app.config["MYSQL_DB"]='college'

mysql = MySQL(app)
app.secret_key = "this is a secret key"

# available domain
@app.route("/")
def availabledomain():
    return  render_template("index.html")

# login landing page
@app.route("/login")
def login():
    return  render_template("login.html")

# ADMIN landing page route
@app.route("/admin", methods=['GET'])
def admin():
    return render_template("admin.html")
    
# STUDNET landing page route
@app.route("/student", methods=['GET'])
def student():
    return render_template("student.html")
    
# FACULTY landing page route
@app.route("/faculty", methods=['GET'])
def faculty():
    return render_template("faculty.html")
    
# administrative tasks for student
@app.route("/managestudent")
def managestudent():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM first_year WHERE status=0 ORDER BY roll_no ASC;")
    student = cursor.fetchall()
    #student = json.dumps(student)
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM first_year WHERE status=1;")
    dstudent = cursor.fetchall()
    
    return render_template("managestudent.html", student=student, dstudent=dstudent)
    
# administrative tasks for faculty
@app.route("/managefaculty")
def managefaculty():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from faculty")
    faculty = cursor.fetchall()
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM faculty WHERE status=1;")
    dfaculty = cursor.fetchall()
    
    return render_template("managefaculty.html", faculty=faculty, dfaculty=dfaculty)
    
# administrative tasks for course
@app.route("/managecourse")
def managecourse():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from course")
    course = cursor.fetchall()
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM course WHERE status=1;")
    dcourse = cursor.fetchall()
    
    return render_template("managecourse.html", course=course, dcourse=dcourse)


def create():
    cursor = mysql.connection.cursor()
    cursor.execute(" ") # IINSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
    database = cursor.fetchall()
    return database
  
@app.route("/update")  
def update():
    #cursor = mysql.connection.cursor()
    #cursor.execute(" ")# UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
    #cursor.commit()
    cursor = mysql.connection.cursor()
    cursor.execute("select * from course")
    course = cursor.fetchall()
    return render_template("update.html", course=course)

# ADMIN DELETE SECTION START HERE 
@app.route("/delete/<student_id>")  
def delete(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE first_year SET status=1 WHERE student_id={student_id};") 
    mysql.connection.commit()
    return f"deleted succefully : {student_id} " 
  
  
#@app.route("/deletedstudent")

    #student = json.dumps(student)
    
 # ADMIN READMIT SECTION START HERE 
@app.route("/readmit/<student_id>")
def readmitstudent(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE first_year SET status=0 WHERE student_id={student_id};")
    mysql.connection.commit() 
    return "STUDENT READMITED SUCCEFULLY"
 
@app.route("/readmit/<faculty_id>")  
def hirefaculty(faculty_id):
    cursor = mysql.connection.cursor()
    cursor.execute(f"UPDATE faculty SET status=0 WHERE faculty_id={faculty_id};")
    mysql.connection.commit() 
    return "FACULTY REHIRED SUCCEFULLY" 
  
@app.route("/retake/<course_id>") 
def recourse(course_id):
    cursor = mysql.connection.cursor()
    mysql.execute("UPDATE course SET status=0 WHERE course_id={course_id};") 
    mysql.connection.commit()
    return "FACULTY REHIRED SUCCEFULLY"
  
  
  
  
  
  
  
  
       
# calling the function for starting app
if __name__ == '__main__':
   app.run
       
