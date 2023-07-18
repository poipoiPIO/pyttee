
import html_to_json
from pyttee import TemplateStrBuilder
import pytest


def tags_test(html: str, template: list):
    builder = TemplateStrBuilder()

    template_html = builder(template)
    print(template_html)
    base_json = html_to_json.convert(html)
    template_json = html_to_json.convert(template_html)
    return base_json == template_json


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


def test_multiple_tags():
    html_str = "<h1><i>Hello <b>world!</b></i><i>Meow</i></h1>"
    template = \
        ["h1",
         ["i", "Hello ", ["b", "world!"]],
         ["i", "Meow"]]
    test = tags_test(html_str, template)
    assert test


def test_properties():
    html_str = "<h1 color='red'>owo</h1>"
    template = \
        ["h1", {"color": "red"}, "owo"]
    test = tags_test(html_str, template)
    assert test
