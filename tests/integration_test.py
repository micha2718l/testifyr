from testifyr import (
    Problem,
    MultipleChoiceProblem,
    WorkProblem,
    Choice,
    Question,
    Bonus,
    Information,
)

# pytest hates things called Test
from testifyr import Test as Tesst


def test_Test():
    problems = [
        Information("This is information"),
        Problem("This is a base problem"),
        MultipleChoiceProblem(
            statement="This is a multiple choice problem",
            choices=[
                Choice("First option", correct=True),
                Choice("Second option", correct=False),
                Choice("Third option", correct=False),
            ],
        ),
        WorkProblem(
            statement="This is a work problem",
            questions=[
                Question("First question", answer="Answer to first question", points=2),
                Question(
                    "Second question", answer="Answer to second question", points=5
                ),
            ],
        ),
    ]
    bonuses = [
        Bonus("This is a bonus", points=3, answer="Bonus answer"),
        Bonus("This is another bonus", points=5, answer="Another bonus answer"),
    ]
    infos = [Information("This is information")]
    t = Tesst(problems=problems + infos + bonuses)
    assert t.total_points() == {"total": 11, "bonus": 8}
