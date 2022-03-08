from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
        {
            "Contact": u"9987644456",
            "Name": u"Raju",
            "done": False,
            "id": 1
        },
        {
            "Contact": u"9876543222",
            "Name": u"Rahul",
            "done": False,
            "id": 2
        }
    ]


@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

contact = {
    'id': tasks[-1]['id'] +1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact', ""),
    'done': False
}

tasks.append(contact)
def get_task():
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })