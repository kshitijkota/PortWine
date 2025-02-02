from flask import Flask, send_from_directory
from multiprocessing import Process

# Create the Flask applications
app1 = Flask(__name__, static_folder="public")
app2 = Flask(__name__)
app3 = Flask(__name__)
app4 = Flask(__name__)

# Define the ports
port1 = 8000
port2 = 5001
port3 = 8080
port4 = 4000


# Routes for app1
@app1.route("/")
def index():
    return send_from_directory(app1.static_folder, "index.html")


@app1.route("/flag")
def flag1():
    return "Your close :("


# Routes for app2
@app2.route("/")
def app2_root():
    return "Welcome to port 5001"


@app2.route("/flag")
def flag2():
    return "https://drive.google.com/file/d/1B5Kb8pxdLbvifabABUuflqGCgMz3ldHC/view?usp=sharing"


# Routes for app3
@app3.route("/")
def app3_root():
    return "Welcome to port 8080"


@app3.route("/flag")
def flag3():
    return "Flag4_Txt_Op3n#"


# Routes for app4
@app4.route("/")
def app4_root():
    return "Welcome to port 4000"


@app4.route("/flag")
def flag4():
    return "Your close :("


# Functions to run each app
def run_app1():
    app1.run(port=port1)


def run_app2():
    app2.run(port=port2)


def run_app3():
    app3.run(port=port3)


def run_app4():
    app4.run(port=port4)


if __name__ == "__main__":
    # Create and start processes for each app
    p1 = Process(target=run_app1)
    p2 = Process(target=run_app2)
    p3 = Process(target=run_app3)
    p4 = Process(target=run_app4)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Optional: Join processes to keep the main thread alive
    p1.join()
    p2.join()
    p3.join()
    p4.join()
