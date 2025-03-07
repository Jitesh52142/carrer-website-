from flask import Flask 

app = Flask(__name__)## that show how the perticular scricpt is invoked 


@app.route("/")#they make and sattle the path of the link of the app after domain name.register the rpute to the application

def helloworld():
    return "hellow world"

if __name__ =="__main__":
    app.run(host="0.0.0.0",debug = True)

    