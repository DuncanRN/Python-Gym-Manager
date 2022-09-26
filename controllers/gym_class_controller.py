import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
from datetime import date
from dateutil.relativedelta import relativedelta # using this to add a month onto a date

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

    all_members = member_repository.select_all()
    return render_template("classes/show.html", gym_class=gym_class, members=members, all_members=all_members)

@gym_classes_blueprint.route("/classes/new")
def new_gym_class():

    # get current year to help with default end date in this upcoming form

    current_year = date.today().year

    return render_template("classes/add.html", current_year=current_year)


# CREATE
# POST '/classes'
@gym_classes_blueprint.route("/classes",  methods=['POST'])
def create_gym_class():
    name = request.form['name']
    date_start = request.form['date_start']
    repeating = request.form['repeating']
    end_date = request.form['end_date']
    gym_class = GymClass(name, date_start, repeating, end_date)
    gym_class_repository.save(gym_class)
    return redirect('/classes')




@gym_classes_blueprint.route("/classes/<id>/edit")
def edit_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template("classes/edit.html", gym_class=gym_class)

# UPDATE
# PUT (although really POST) /members/{{member.id}}/edit

@gym_classes_blueprint.route("/classes/<id>/update", methods=['POST'])
def update_class(id):
    # pdb.set_trace()
    name = request.form['name']
    date_start = request.form['date_start']
    repeating = request.form['repeating']
    end_date = request.form['end_date']
    gym_class_to_update = GymClass(name, date_start, repeating, end_date, id)
    gym_class_repository.update(gym_class_to_update)
    return redirect ('/classes/' + id)



@gym_classes_blueprint.route("/classes/calendar")
def calendar():
    # Get all gym_classes
    gym_classes = gym_class_repository.select_all() 
    # organise this list into ALL the classes since some are repeating and will occur more than once
    gym_classes_calendar = []

    for gym_class in gym_classes:
        # class_date = start date from repo
        current_class_date = gym_class.date_start
        # 	while class_date < end date
        if gym_class.repeating=="None":
            gym_classes_calendar.append(gym_class)
        else:
            while current_class_date < gym_class.end_date: 
                gym_classes_calendar.append(gym_class)
                # If class repeats monthly
                if gym_class.repeating == "Monthly":
                    current_class_date = current_class_date + relativedelta(months=1)
                elif gym_class.repeating == "Weekly":
                    current_class_date = current_class_date + relativedelta(weeks=1)
                

        
    return render_template("classes/calendar.html", gym_classes_calendar = gym_classes_calendar)
    
                    # date_after_month = datetime.today()
                    # print('Today: ',datetime.today().strftime('%d/%m/%Y'))
                    # print('After Month:', date_after_month.strftime('%d/%m/%Y'))

            # 		    add a month to the class_date
            #       if class repeates weekly
            #           add a week to the class_date
            # 		append that in class output

# If weekly
# 	add week to class date
# 		while class_…..




