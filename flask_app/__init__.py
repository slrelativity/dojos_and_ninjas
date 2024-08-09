from flask import Flask # type: ignore

app=Flask(__name__)
app.secret_key = "dan"

database = "dojos_and_ninjas"