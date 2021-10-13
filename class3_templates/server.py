from bottle import route, run, template

@route("/")
def get_index():
    return ("home page!")


def get_hello():
    return ("hello!")

@route("/hello")
@route("/hello/<name>")
def get_hello(name="world"):
    return template("hello.tpl",name="Hashi",extra=None)

@route("/greet")
@route("/greet/<name>")
def get_greet(name="world"):
    return template("hello.tpl",name="Hashi",extra="Happy Birthday")


@route("/greeting/<names>")
def get_greeting(names="world"):
    names = names.split(',')
    return template("greetings.tpl",names=names)


run(host="localhost", port=8080)