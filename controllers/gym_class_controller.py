from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

gym_classes_blueprint = Blueprint("gym_class", __name__)

@gym_classes_blueprint.route("/classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all() 
    return render_template("classes/index.html", gym_classes = gym_classes)

@gym_classes_blueprint.route("/classes/<id>")
def show(id):
    # we want to get the class details and all the members of that class
    gym_class = gym_class_repository.select(id)

    members = gym_class_repository.members(id)
    #  this line was members = member_repository.gym_classes(id)

    all_members = member_repository.select_all()
    return render_template("classes/show.html", gym_class=gym_class, members=members, all_members=all_members)

@gym_classes_blueprint.route("/classes/new")
def new_gym_class():
    return render_template("classes/add.html")



# CREATE
# POST '/classes'
@gym_classes_blueprint.route("/classes",  methods=['POST'])
def create_gym_class():
    name = request.form['name']
    
    gym_class = GymClass(name)
    gym_class_repository.save(gym_class)
    return redirect('/classes')