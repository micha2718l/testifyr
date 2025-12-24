from flask import Flask, render_template, request
from testifyr.elements import *
from testifyr.stuff import Value
from testifyr._utils import style_string

app = Flask(__name__)


def create_mc(mass_truck, mass_bug):
    statement = f"A truck with mass {mass_truck} collides with a bug with mass {mass_bug}. How does the magnitude of the bug's force on the truck compare to the magnitude of the truck's force on the bug?"

    choices = [
        Choice(
            "The bug's force on the truck is greater than the truck's force on the bug."
        ),
        Choice(
            "The truck's force on the bug is greater than the bug's force on the truck."
        ),
        Choice("The two forces are equal in magnitude.", True),
        Choice("It is impossible to determine without more information."),
    ]

    return MultipleChoiceProblem(statement=statement, choices=choices)


@app.route("/")
def index():
    return render_template("index.jinja.html")


@app.route("/clicked", methods=["POST"])
def clicked():
    f = request.form
    mass_truck = Value(float(f["mass_truck"]), "kg")
    mass_bug = Value(float(f["mass_bug"]), "kg")
    mc = create_mc(mass_truck, mass_bug)
    return render_template("mc.jinja.html", mc=mc)


if __name__ == "__main__":
    app.run(
        port=1337,
        debug=True,
        extra_files=["templates/index.jinja.html", "templates/mc.jinja.html"],
    )
