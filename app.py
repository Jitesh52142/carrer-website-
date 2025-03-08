from flask import Flask,render_template,jsonify

app = Flask(__name__)## that show how the perticular scricpt is invoked 

JOBS = [
    {
        'id' : 1,
        'title': 'data scientist',
        'location': 'banglaru , india',
        'salary':'Rs. 100000'

    },

     {
        'id' : 2,
        'title': 'Data scientist',
        'location': 'mumbi , india',
        'salary':'Rs. 500000'

    },

     {
        'id' : 3,
        'title': 'Data Enginear',
        'location': 'indore , india',
        'salary':'Rs. 200000'

    },

     {
        'id' : 4,
        'title': 'enginear',
        'location': 'banglaru , india',
        'salary':'Rs. 500000'

    },

     {
        'id' : 5,
        'title': 'backend developer',
        'location': 'Bangladesh , india',
        'salary':'Rs. 1000000'

    },

     {
        'id' : 7,
        'title': 'arrospcace enginear',
        'location': 'chenai , india',
        'salary':'Rs. 10000000'

    }


]


@app.route("/")#they make and sattle the path of the link of the app after domain name.register the rpute to the application

def helloworld():
    return render_template('home.html',
                           jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS) 

if __name__ =="__main__":
    app.run(host="0.0.0.0",debug = True)

