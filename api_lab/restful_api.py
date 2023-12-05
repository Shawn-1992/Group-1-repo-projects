from flask import Flask, request
app = Flask(__name__)

nc_college_database = {
    "NCSU": {"name": "North Carolina State University", "abbreviation": "NCSU", "year Founded": 1887, "nickname": "Wolfpack"},
    "UNC": {"name": "University of North Carolina Chapel Hill", "abbreviation": "UNC", "year Founded": 1789, "nickname": "Tar heels"},
    "DUKE": {"name": "Duke University", "abbreviation": "DUKE", "year Founded": 1838, "nickname": "Blue Devils"},
    "ECU": {"name": "East Carolina University", "abbreviation": "ECU", "year Founded": 1907, "nickname": "Pirates"},
    "WF": {"name": "Wake Forest University", "abbreviation": "WF", "year Founded": 1834, "nickname": "Demon Deacons"},
}


@app.get('/colleges')
def list_colleges():
    return {"Colleges": list(nc_college_database.values())}


@app.route('/colleges/<college_name>', methods=['GET', 'PUT', 'DELETE'])
def college_route(college_name):
    if request.method == "GET":
        return get_college(college_name)
    elif request.method == "PUT":
        return update_college(college_name, request.get_json(force=True))
    elif request.method == "DELETE":
        return delete_college(college_name)


@app.route('/colleges', methods=['GET', 'POST'])
def colleges_route():
    if request.method == 'GET':
        return list_colleges()
    elif request.method == 'POST':
        return add_college(request.get_json(force=True))


def add_college(new_college):
    college_name = new_college['abbreviation']
    nc_college_database[college_name] = new_college
    return new_college


def get_college(college_name):
    return nc_college_database[college_name]


def update_college(college_name, new_college_info):
    college_getting_update = nc_college_database[college_name]
    college_getting_update.update(new_college_info)
    return college_getting_update


def delete_college(college_name):
    deleting_college = nc_college_database[college_name]
    del nc_college_database[college_name]
    return deleting_college


if __name__ == '__main__':
    app.run()
