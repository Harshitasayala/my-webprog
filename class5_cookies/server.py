from bottle import route, run, template, default_app, get, post, request, debug


@get("/")
def get_index():
    return ("home page!")


@get("/hello")
@get("/hello/<name>")
def get_hello(name="world"):
    return template("hello.tpl",name="Hashi",extra=None)

@get("/greet")
@get("/greet/<name>")
def get_greet(name="world"):
    return template("hello.tpl",name="Hashi",extra="Happy Birthday")


@get("/greeting/<names>")
def get_greeting(names="world"):
    names = names.split(',')
    return template("greetings.tpl",names=names)

@get("/login")
def get_login():
    return template("login.tpl",message="")

@post("/login")
def post_login():
    username=request.forms['username']
    password=request.forms['password']
    if password!="magic":
        return template("login",message="Bad Password")
    return template("hello.tpl",name=username + "!!!!",extra="Happy Birthday")

debug(True)
run(host="localhost", port=8080)