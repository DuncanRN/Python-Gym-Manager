from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all() 
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    gym_classes = member_repository.gym_classes(id)
    return render_template("members/show.html", member=member, gym_classes=gym_classes)

@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/add.html")

# CREATE
# POST '/members'
@members_blueprint.route("/members",  methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership = request.form['membership']
    active = request.form['active']

    member = Member(first_name, last_name, membership, active)
    member_repository.save(member)
    return redirect('/members')


@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member=member)


# UPDATE
# PUT (although really POST) /members/{{member.id}}/edit

@members_blueprint.route("/members/<id>/edit", methods=['POST'])
def update_member(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership = request.form['membership']
    active = request.form['active']
    
    # print("in update member")
    # print(active)
    # print("that was the active variable")

    member_to_update = Member(first_name, last_name, membership, active, id)
    member_repository.update(member_to_update)
    return redirect ('/members/' + id)
