from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


@app.route('/')
def index():
   return redirect('/dojos')
    


@app.route('/dojos/')
def user_page():
  dojos_lists = Dojo.get_all()
  return render_template('/create_dojo.html', dojos = dojos_lists)



@app.route('/ninjas')
def new_page():
    return render_template("create_ninja.html")



@app.route('/dojos/',methods=['POST'])
def create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos/')


@app.route('/ninjas/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_ninjas.html",ninjas=Ninja.get_one(data))


@app.route('/dojos/update',methods=['POST'])
def new_dojos():
    return render_template("create_dojos.html")



@app.route('/dojos/1')
def show_dojos():
    return render_template('show_ninjas.html')



#@app.route('/dojos/edit/<int:id>')
#def edit(id):
 #   data ={ 
  #      "id":id
   #}
    #return render_template("edit_dojo.html",dojo=Dojo.get_one(data))



#@app.route('/dojos/show/<int:id>')
#def show(id):
 #   data ={ 
  #      "id":id
   # }
    #return render_template("show_dojos.html",dojo=Dojo.get_one(data))


#@app.route('/dojos/update',methods=['POST'])
#def update():
 #   Dojo.update(request.form)
  #  return redirect('/dojos')


#@app.route('/dojos/destroy/<int:id>')
#def destroy(id):
 #   data ={
  #      'id': id
    #}
   # Dojo.destroy(data)
    #return redirect('/dojos')