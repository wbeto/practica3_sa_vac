from config import app
#Module import
from logs.routes import user


from flask import render_template


#Register Blueprints
app.register_blueprint(user)


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

@app.route('/index.html', methods=['GET'])
def register():
    return render_template("index.html")

if __name__ ==  '__main__':
    app.run(debug=False, port=5000)