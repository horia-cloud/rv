#!flask/bin/python
from flask import Flask, jsonify, request, abort
from datetime import datetime, timedelta, date

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': 'John',
        'birthday': '2018-10-10', 
    },
    {
        'id': 2,
        'name': 'test',
        'birthday': '2015-01-01', 
    }
]

@app.route('/hello/<name_get>', methods=['GET','PUT'])
def hello_name(name_get):
   if request.method=='PUT':
    nume = search(name_get,tasks)
    req_data = request.get_json(force=True)
    result = req_data['message']
    print result
    try:
            datetime.strptime(result, '%Y-%m-%d')
    except ValueError:
            return "Incorrect data format, should be YYYY-MM-DD"
    if len(nume) == 0:
     task = {
        'id': tasks[-1]['id'] + 1,
        'name': name_get,
        'birthday': result
     }
     tasks.append(task)
     return ('', 204) 
    else:
        name_index = next((index for (index, d) in enumerate(tasks) if d["name"] == name_get), None)
        tasks[name_index]['birthday'] = 'result'
       # return 'Hello %s! Your birthday is in x days' %name_get
        return ('', 204)

   elif request.method=='GET':
    for nume2 in tasks:
        if nume2['name'] == name_get:
          s = days_until(nume2['birthday'])
          print s
          a = ''
          if s==5:
             a="Hello %s! your birthday is in %s days"  %(nume2['name'], s)
          elif s==0:
             a="Hello %s! Happy birthday!" %nume2['name']
          return jsonify({'message': a}), 200
    
def search(name, people):
    return [element for element in people if element['name'] == name]

def days_until(d1):
    today = datetime.now().strftime('%Y-%m-%d')
    date_format = "%Y-%m-%d"
    a = datetime.strptime(d1, date_format)
    b = datetime.strptime(today, date_format)
    delta = abs(b - a)
    return delta.days

if __name__ == '__main__':
    app.run('0.0.0.0',80)
