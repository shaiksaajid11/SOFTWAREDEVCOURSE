from flask import Flask, redirect, url_for, render_template , request
app = Flask(__name__)


@app.route('/registration',methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
      data = request.form
      print("Email Id:"+data["email"])
      return render_template("registrationdata.html",registrationdata = data)
    else:
        return render_template("reg.html")

if __name__ == '__main__':
   app.run(debug = True)