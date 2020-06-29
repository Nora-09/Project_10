from flask import Flask , request, jsonify

app = Flask(__name__)

@app.route('/get_data_count' , methods = ['Get'])
def get_data_count():
    try:
        import psycopg2
        connection = psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', database='project_9')
        cursor = connection.cursor()
        label_name = int(input("label_name = "))
        count      = int(input("count      = "))
        q = 'SELECT count (*) FROM data_labeling WHERE classi_number = %s LIMIT %s;'
        cursor.execute(q, [label_name, count])
        print (q,label_name,count)
        connection.commit()
        r = cursor.fetchall()
        return jsonify(r)
    except:
        return "ERROR"


@app.route('/get_data' , methods = ['Get'])
def get_data():
    try:
        import psycopg2
        connection = psycopg2.connect(user='postgres', password='12345', host='localhost', port='5432', database='project_9')
        cursor = connection.cursor()
        count      = int(input("count      = "))
        sort_order = str(input("sort_order = "))
        w = 'SELECT data_input.text , data_labeling.classi_number FROM data_input JOIN data_labeling ON id = serial_number ORDER BY text_date %s LIMIT %s;'%(sort_order,count)
        cursor.execute(w, [])
        result = cursor.fetchall()
        print (result)
        return jsonify(result)
        cursor.close()
        connection.close()
    except:
        return "ERROR"

if __name__=='__main__':
    app.run(debug=True,port=3000)
