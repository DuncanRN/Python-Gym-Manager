from flask import Flask, render_template
# , request, redirect
from flask import Blueprint
# from models.gym_class import GymClass
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






# from flask import Flask, render_template
# # , request, redirect
# from flask import Blueprint
# # from models.gym_class import GymClass
# import repositories.gym_class_repository as gym_class_repository

# gym_class_blueprint = Blueprint("gym_class", __name__)

# @gym_class_blueprint.route("/classes")
# def gym_classes():
#     print("HERE")
#     gym_classes = gym_class_repository.select_all() 
#     return render_template("classes/index.html", classes = gym_classes)

# # @members_blueprint.route("/members/<id>")
# # def show(id):
# #     member = member_repository.select(id)
# #     gym_classes = member_repository.gym_classes(id)
# #     return render_template("members/show.html", member=member, gym_classes=gym_classes)
