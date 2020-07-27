from flask import Flask, request, jsonify
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user= request.json['username']
        password = request.json['password']

        if user.isalpha()!=True:
            data={"status":203,"msg":"Failure: only characters allowed in username"}
        else:
            if len(password)<6:
                data={"status":201,"msg":"Failure: password should be of length 6"}
            else:
                if password.isalnum()== True and password.isalpha()==True:
                    data={"status":202,"msg":"Failure: password to have 1 character and 1 number"}
                elif password.isalnum()== True and password.isalpha()==False:
                    data={"status":200,"msg":"Success"}
        return jsonify(data)

    else:
        return "<h1>Hello</h1>"    

        
