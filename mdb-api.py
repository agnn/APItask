import pymongo
from logging_class import lg
from flask import Flask, request, jsonify

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://achowdh:failsafe@agnik0.mmtem.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client['apitask']
collection = database["details"]

@app.route('/insert-mongo',methods=['GET' , 'POST'])
def insert_values_mdb():
    'insert values to mongo database'
    lg.info('function call successful')

    if (request.method == 'POST'):
        a = request.json['value0']
        b = request.json['value1']
        c = request.json['value2']
        d = request.json['value3']
        f = request.json['value4']
        lg.info(f"record is {a},{b},{c},{d},{f}")
    try:
        data = {"student_id":a,
                 "student_name":b,
                 "student_email":c,
                 "student_DOB":d,
                 "student_gender":f}

        collection.insert_one(data)
        lg.info("record updated %s",data)

    except Exception as e:
        lg.error(e)

    return(jsonify(str(data)))

@app.route('/update-mdb',methods=['GET' , 'POST'])

def update_values_mdb():
    'to update values'

    lg.info("function call successful")
    if (request.method=='POST'):
        a = request.json['value0']
        b = request.json['value1']
        c = request.json['value2']
        d = request.json['value3']
        f = request.json['value4']
        lg.info(a,b,c,d,f)

        try:

            collection.update_one({"student_id":a},{'$set':{
                     "student_name":b,
                     "student_email":c,
                     "student_DOB":d,
                     "student_gender":f}
            })
            lg.info("record updated successfully")
        except Exception as e:
            lg.error(e)

    return jsonify(str("record updated successfully"))

@app.route('/del-mdb',methods=['GET','Post'])
def delete_values_mdb():

    lg.info("function call successful")
    if (request.method=='POST'):
        a = request.json['value0']

        try:
            collection.delete_one({'student_id': a})
            lg.info("record deleted with id : %s",a)
        except Exception as e:
            lg.error(e)

    return jsonify(f"record deleted successfully with id {a}")

@app.route('/view-mdb',methods=['GET','Post'])
def view_values_mdb():

    lg.info("function call successful")
    if (request.method=='POST'):
        a = request.json['value0']

        try:
            record = collection.find({'student_id': a})
            lg.info("record with id : %s",a)
            for i in record:
                lg.info(i)
        except Exception as e:
            lg.error(e)

    return jsonify(f"record details with id {a} is {i}")

if __name__=='__main__':
    app.run()

