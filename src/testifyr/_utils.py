from pathlib import Path
from IPython.display import Markdown, display

__all__ = ["_styled_print"]

# style_string = ""
testify_dir = Path(__file__).parent
p = testify_dir / Path("testify") / Path("testifyr.css")
with open(p, "r") as f:
    style_string = "<style>" + f.read() + "</style>"


def _styled_print(string: str):
    display(Markdown(style_string + string))


def _pluralize(n: int, singular: str, plural: str | None = None):
    plural = plural or singular + "s"
    return f"{n} {singular if n == 1 else plural}"


class Element:

    def html(self, answers=False):
        return ""

    def show(self, answers=False):
        display(Markdown(style_string + self.html(answers=answers)))
