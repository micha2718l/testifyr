from bs4 import BeautifulSoup

from testifyr import (
    Problem,
    MultipleChoiceProblem,
    WorkProblem,
    Choice,
    Question,
    Bonus,
    Information,
)


def test_Problem():
    statement = "This is a base problem"
    p = Problem(statement=statement)
    soup = BeautifulSoup(p.html(), "html.parser")
    assert soup.div["class"] == ["problem"]
    assert p.show() == None


def test_MultipleChoiceProblem():
    statement = "This is a multiple choice problem"
    choices = [
        Choice("First option", correct=True),
        Choice("Second option", correct=False),
        Choice("Third option", correct=False),
    ]
    p = MultipleChoiceProblem(statement=statement, choices=choices)
    soup = BeautifulSoup(p.html(number=1), "html.parser")
    assert soup.div.p.div.text.strip() == "Problem #1 (3 points)"
    assert p.show() == None


def test_WorkProblem():
    statement = "This is a work problem"
    questions = [
        Question("First question", answer="Answer to first question", points=2),
        Question("Second question", answer="Answer to second question", points=5),
    ]
    p = WorkProblem(statement=statement, questions=questions)
    soup = BeautifulSoup(p.html(number=1), "html.parser")
    assert soup.div.p.div.text.strip() == "Problem #1 (7 points)"
    assert p.show() == None
