from flask import Flask, render_template
# , request, redirect
from flask import Blueprint
# from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository

gym_classes_blueprint = Blueprint("gym_class", __name__)

@gym_classes_blueprint.route("/classes")
def gym_classes():
    print("HERE")
    gym_classes = gym_class_repository.select_all() 
    return render_template("classes/index.html", gym_classes = gym_classes)

# @gym_classes_blueprint.route("/members/<id>")
# def show(id):
#     member = member_repository.select(id)
#     gym_classes = member_repository.gym_classes(id)
#     return render_template("members/show.html", member=member, gym_classes=gym_classes)






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
