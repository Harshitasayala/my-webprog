from bottle import route, run

@route("/")
def get_index():
    return ("home page!")


def get_hello():
    return ("hello!")

@route("/hello")
@route("/hello/<name>")
def get_hello(name="world"):
    return (f"hello, {name}!")

run(host="localhost", port=8080)