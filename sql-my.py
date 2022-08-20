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
    record = []
    if (request.method=='POST'):

        for i in range(0, 5):
            record.append(request.json[f'value{i}'])
        lg.info(f"record",record)
        try:
            query = f"INSERT INTO dbAPItask.details values('{record[0]}','{record[1]}','{record[2]}','{record[3]}','{record[4]}')"
            lg.info(f"record entered successfully")
            cursor.execute(query)
            mydb.commit()

        except Exception as e:
              lg.error(e)
    return jsonify(str(f"record inserted successfully {record}"))

@app.route('/update-sql',methods=['GET' , 'POST'])
def update_values():
    'to update existing values'
    record = []
    lg.info("function call successful")
    if (request.method=='POST'):

        for i in range(0, 5):
            record.append(request.json[f'value{i}'])
        lg.info(f"record {record}")
        try:
            #this query will execute with assumption that all keys passed are in order as actual table.
            query = f"UPDATE dbAPItask.details SET student_name = '{record[1]}' ,student_email_id = '{record[2]}' ,student_DOB = '{record[3]}' ,student_gender= '{record[4]}' WHERE student_id = {record[0]}"
            cursor.execute(query)
            mydb.commit()
            lg.info(f"record updated successfully for {record[0]}, with, {record[1]},{record[2]},{record[3]},{record[4]}")

        except Exception as e:
              lg.error(e)
    return jsonify(str(f"record updated successfully for {record[0]}, with, {record[1]},{record[2]},{record[3]},{record[4]}"))


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
            record = cursor.fetchall()
            lg.info(f"record -  {record}")
            return jsonify(record)
        except Exception as e:
            lg.error(e)


if __name__=='__main__':
    app.run()


