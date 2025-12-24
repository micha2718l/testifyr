# app.py
from pprint import pprint as pp

from flask import Flask, render_template, request, jsonify
from dataclasses import asdict
from testifyr.elements import (
    Question,
    Choice,
    Problem,
    MultipleChoiceProblem,
    WorkProblem,
    Bonus,
    Information,
    Test,
)
from testifyr.stuff import Value, Unit
import base64

app = Flask(__name__)

# Store problems temporarily (in production, use a proper database)
current_test = {"problems": [MultipleChoiceProblem(statement="sample")], "metadata": {}}


@app.route("/")
def index():
    return render_template("index.html", mc=current_test["problems"][0])


@app.route("/dynamic-form", methods=["GET"])
def get_dynamic_form():
    problem_type = request.args.get("type")
    return render_template("partials/dynamic_form.html", problem_type=problem_type)


@app.route("/preview-problem", methods=["POST"])
def preview_problem():
    data = request.form
    pp(data)
    problem = create_problem_from_data(data)
    return render_template("partials/preview.html", problem=problem)


@app.route("/add-choice", methods=["GET"])
def add_choice():
    choice_num = int(request.args.get("next_num", 1))
    return render_template("partials/choice.html", choice_num=choice_num)


@app.route("/add-question", methods=["GET"])
def add_question():
    question_num = int(request.args.get("next_num", 1))
    return render_template("partials/question.html", question_num=question_num)


@app.route("/insert-value", methods=["POST"])
def insert_value():
    data = request.json
    value = Value(
        value=float(data["value"]),
        unit=data["unit"],
        sigfigs=int(data["sigfigs"]),
        pre_zeros=int(data["pre_zeros"]),
    )
    return jsonify({"formatted_value": str(value)})


@app.route("/add-problem", methods=["POST"])
def add_problem():
    data = request.form
    problem = create_problem_from_data(data)
    current_test["problems"].append(problem)
    return render_template(
        "partials/problem_list.html", problems=current_test["problems"]
    )


def create_problem_from_data(data):
    choices = []
    for i in range(int(data.get("choice_count", 0))):
        choice_text = data.get(f"choice_{i}")
        is_correct = data.get(f"correct_{i}") == "on"
        if choice_text:
            choices.append(Choice(statement=choice_text, correct=is_correct))

    return MultipleChoiceProblem(
        statement=data.get("statement"),
        points=int(data.get("points", 3)),
        choices=choices,
    )


if __name__ == "__main__":
    app.run(port=1337, debug=True)
