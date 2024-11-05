from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

current_dir = Path(__file__).parent
template_path = current_dir / "templates"
if not template_path.exists():
    raise ValueError(f"Could not find templates directory at {template_path}. ")
env = Environment(
    loader=FileSystemLoader(template_path),
    autoescape=select_autoescape(["html", "xml"]),
)


def space_html(space=None, answers=False, answer="", figure=None):
    out = f"""<div class="fig_space_container">
    <div
                    class="spaceBox"
                    style="height: calc(1em * {space or 0}); display: {"default" if space else "none"}; background-color: {'lightgreen' if answers else 'white'}"
                >

{answer if answers else ""}

</div>"""
    if figure:
        out += f"""<div class="img_container"><img src='data:image/png;base64, {figure.decode('utf-8')}' style="height: calc(1em * {space or 0})"/></div>"""
    return out + "</div>"
