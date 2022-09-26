import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import GymClass
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
from datetime import date, datetime
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

    members_of_this_class = gym_class_repository.members(id)
    all_members = member_repository.select_all()

    all_members_not_in_this_class = [x for x in all_members if x not in members_of_this_class]
    #  THIS LINE IS CURRENTLY NOT WORKING....



    # members_of_this_class_set = set(members_of_this_class) 
    # all_members_not_in_this_class = [x for x in all_members if x not in members_of_this_class_set]

    # all_members_not_in_this_class = all_members
    # for member_in_class in members_of_this_class:
    #     if all_members.count(member_in_class):
    #         all_members_not_in_this_class.remove(member_in_class)


    # print("members of this class")
    # for member in members_of_this_class:
    #     print(member.first_name)
    
    # print("")
    # print("all members ")
    # for member in all_members:
    #     print(member.first_name)

    # print("")
    # print("all members not in this class")
    # for member in all_members_not_in_this_class:
    #     print(member.first_name)

    return render_template("classes/show.html", gym_class=gym_class, all_members_not_in_this_class=all_members_not_in_this_class, members_of_this_class=members_of_this_class)

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
    # pdb.set_trace()
    # Get all gym_classes
    gym_classes = gym_class_repository.select_all() 
    # organise this list into ALL the classes since some are repeating and will occur more than once
    gym_classes_calendar = []

    for gym_class in gym_classes:
        # class_date = start date from repo
        current_class_date = gym_class.date_start
        todays_date = datetime.now()
        # check we aren't already after the start date
        if current_class_date >= todays_date:
            # 	while class_date < end date
            if gym_class.repeating=="None":
                gym_classes_calendar.append(gym_class)
            else:
                while current_class_date < gym_class.end_date: 
                    
                    gym_class_to_append = {'name' : gym_class.name, 
                                            'date_start' : current_class_date,
                                            'repeating' : gym_class.repeating, 
                                            'end_date' : gym_class.end_date, 
                                            'id' : gym_class.id
                                            }
                    gym_classes_calendar.append(gym_class_to_append)

                    # If class repeats monthly
                    if gym_class.repeating == "Monthly":
                        current_class_date = current_class_date + relativedelta(months=1)
                        gym_class.date_start = current_class_date
                        print("monthly trying to set date start to " + str(current_class_date))
                    elif gym_class.repeating == "Weekly":
                        current_class_date = current_class_date + relativedelta(weeks=1)
                        gym_class.date_start = current_class_date
                        # print("weekly trying to set date start to " + str(current_class_date))
                        # print(gym_class.date_start)
                    #  THIS ISN"T QUITE working, the gym_class is being handed over with only it's original start
                    
                    # print("hi")
                    # # print(gym_classes_calendar[0].__dict__)
                    # for gym in gym_classes_calendar:
                    #     print(gym.__dict__)

        

    return render_template("classes/calendar.html", gym_classes_calendar = gym_classes_calendar)





