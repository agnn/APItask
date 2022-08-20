import mysql.connector as conn
from logging_class import lg
from flask import Flask, request, jsonify

app = Flask(__name__)

mydb = conn.connect(host = "localhost", user = "root", passwd = "Failsafeauto#1")
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS dbAPItask")
query = "CREATE TABLE IF NOT EXISTS dbAPItask.details(student_id int primary key not null,student_name varchar(80) ,student_email_id varchar(80) ,student_DOB varchar(10),student_gender varchar(10))"
cursor.execute(query)

@app.route('/insert-sql',methods=['GET' , 'POST'])
def insert_values():
    'function to record in to database'
    lg.info("function call successful")
    if (request.method=='POST'):
        a = request.json['value0']
        b = request.json['value1']
        c = request.json['value2']
        d = request.json['value3']
        f = request.json['value4']
        lg.info(f"record inserted {a},{b},{c},{d},{f})")
        try:
            query = f"INSERT INTO dbAPItask.details values('{a}','{b}','{c}','{d}','{f}')"
            lg.info(f"record entered successfully '{a}','{b}','{c}','{d}','{f}'")
            cursor.execute(query)
            mydb.commit()

        except Exception as e:
              lg.error(e)
    return jsonify(str(f"record inserted successfully {a},{b},{c},{d},{f}"))

@app.route('/update-sql',methods=['GET' , 'POST'])
def update_values():
    'to update existing values'

    lg.info("function call successful")
    if (request.method=='POST'):
        a = request.json['value0']
        b = request.json['value1']
        c = request.json['value2']
        d = request.json['value3']
        f = request.json['value4']
        lg.info(a,b,c,d,f)
        try:
            query = f"UPDATE dbAPItask.details SET student_name = '{b}' ,student_email_id = '{c}' ,student_DOB = '{d}' ,student_gender= '{f}' WHERE student_id = {a}"
            lg.info(f"record updated successfully for {a}, with, {b},{c},{d},{f}")
            cursor.execute(query)
            mydb.commit()

        except Exception as e:
              lg.error(e)
    return jsonify(str(f"record updated successfully for,{a},with,{b},{c},{d},{f}"))


@app.route('/del-sql',methods=['GET','Post'])
def delete_values():

    lg.info("function call successful")
    if (request.method=='POST'):
        a = request.json['value0']

        try :
            query = f"DELETE from dbAPItask.details WHERE student_id ={a}"
            cursor.execute(query)
            mydb.commit()
            lg.info(f"record deleted for student_id {a}")
            return jsonify(str(f"record deleted with student_id {a}"))
        except Exception as e:
            lg.error(e)


@app.route('/view-sql',methods=['GET','Post'])
def view_values():

    lg.info("function call successful")
    if (request.method=='POST'):
        a = request.json['value0']

        try :
            query = f"SELECT * from dbAPItask.details WHERE student_id ={a}"
            cursor.execute(query)
            r = cursor.fetchall()
            lg.info(f"record -  {r}")
            return jsonify(r)
        except Exception as e:
            lg.error(e)


if __name__=='__main__':
    app.run()


