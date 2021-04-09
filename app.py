from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/count")
def count():
    t = int(open("/var/count/count.txt", "r").read().strip())
    t += 1
    s = str(t)
    open("/var/count/count.txt", "w").write(s + "\n")
    return s


@app.route("/peek")
def peek():
    return open("/var/count/count.txt", "r").read().strip() + "\n"
