from flask import Flask
from flask import render_template
from flask import request,redirect,url_for,Response
import os 
app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        user=request.form["srn"]
        password=request.form["pass"]
        emailid=request.form["email"]
        return redirect(url_for("users",usr=user,pw=password,ei=emailid))
    else:
        return render_template("Register.html")

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

#@app.route('/shutdown', methods=['GET','POST'])
#def shutdown():
#    shutdown_server()
#    return 'Thank you for entering your response'

@app.route('/<usr>/<pw>/<ei>', methods=['GET'])
def users(usr,pw,ei):
    file_object = open('currentuserdetails.txt', 'a')
    file_object2 = open('userdetailscomplete.txt', 'a')
    file_object. truncate(0)
    file_object.write(usr)
    file_object.write('\n')
    file_object.write(pw)
    file_object.write('\n')
    file_object.write(ei)
    file_object.write('\n')
    file_object2.write(usr)
    file_object2.write('\n')
    file_object2.write(pw)
    file_object2.write('\n')
    file_object2.write(ei)
    file_object2.write('\n')
    file_object.close()
    file_object2.close()
    shutdown_server()
    return render_template("ThankYou.html")

if __name__=="__main__":
    app.run(debug=False)

os.system('cmd /k "python snip.py"')
