
from xmldiff import main, formatting
from pyttee import TemplateStrBuilder
import pytest


def tags_test(html: str, template: list):
    builder = TemplateStrBuilder()

    template_html = builder(template)

    diff = main.diff_texts(template_html, html)
    return not bool(diff)


@pytest.mark.parametrize(
    "excepted_html, template",
    [
        ("<h1>Hello world!</h1>", ["h1", "Hello world!"]),
        ("<b>owo</b>", ["b", "owo"]),
        ("<center>meow</center>", ["center", "meow"])
    ]
)
def test_plain_tags(excepted_html, template):
    html_str = excepted_html
    template = template
    test = tags_test(html_str, template)
    assert test


@pytest.mark.parametrize(
    "html_str, template",
    [
        ("<h1><i>Hello <b>world!</b></i></h1>", ["h1", ["i", "Hello ", ["b", "world!"]]]),
        ("<b>ow<i>o</i></b>", ["b", "ow", ["i", "o"]]),
        ("<body><center>meow</center></body>", ["body", ["center", "meow"]])
    ]
)
def test_nested_tags(html_str, template):
    test = tags_test(html_str, template)
    assert test


@pytest.mark.parametrize(
    "html_str, template",
    [
        ("<h1><i>Hello <b>world!</b></i><i>Meow</i></h1>",
         ["h1", ["i", "Hello ", ["b", "world!"]], ["i", "Meow"]]),
        ("<body><h1><i>Hello <b>world!</b></i><i>Meow</i></h1></body>",
         ["body", ["h1", ["i", "Hello ", ["b", "world!"]], ["i", "Meow"]]]),
        ("<body><center><div><i>m</i></div>eow</center></body>",
         ["body", ["center", ["div", ["i", "m"]], "eow"]])
    ]
)
def test_multiple_tags(html_str, template):
    test = tags_test(html_str, template)
    assert test


@pytest.mark.parametrize(
    "html_str, template",
    [
        ("<h1 color='red'>owo</h1>", ["h1", {"color": "red"}, "owo"]),
        ("<i color='red' width='12px' height='33px'>owo</i>",
         ["i", {"color": "red", "width": "12px", "height": "33px"}, "owo"]),
        ("<i height='33px'>ow<i color='red'>o</i></i>",
         ["i", {"height": "33px"}, "ow", ["i", {"color": "red"}, "o"]]),
    ]
)
def test_properties(html_str, template):
    test = tags_test(html_str, template)
    assert test
