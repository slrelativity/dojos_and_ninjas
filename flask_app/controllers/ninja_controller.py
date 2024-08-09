from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.ninja_model import Ninja




#@app.route('/ninjas/')
#def user_page():
#    ninja_list = Ninja.get_all()
#    return render_template("ninjas.html", ninjas = ninja_list)



#@app.route('/ninjas/')
#def new_page1():
 #   return render_template('create_ninjas.html')



@app.route('/ninjas/create',methods=['POST'])
def create1():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/ninjas')



@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",ninja=Ninja.get_one(data))



@app.route('/user/show/<int:id>')
def show1(id):
    data ={ 
        "id":id
    }
    return render_template("show_ninja.html",user=Ninja.get_one(data))


@app.route('/user/update',methods=['POST'])
def update():
    Ninja.update(request.form)
    return redirect('/ninjas')


@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Ninja.destroy(data)
    return redirect('/Ninjas')