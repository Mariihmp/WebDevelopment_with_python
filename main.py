from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
# @app.route('/handle_data',methods=['POST'])
# def handle_data():
#     name = request.form['name']
#     email = request.form['email']
#     password = request.form['password']

@app.route("/login",methods=["POST"])
def receive_data():
    name = request.form['username']
    email = request.form['email']
    password = request.form['password']
    return f"<h1>Name: {name}</h1>" \
           f"<h1> Email:{email}</h1>" \
           f"<h1>Password:{password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)