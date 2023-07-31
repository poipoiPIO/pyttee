<h2 align="center">
Pyttee: Lispy DSL library for python html templates  
</h2>

![PyPI version](https://badge.fury.io/py/pyttee.svg)

## Example:
```python
import pyttee

def my_first_template(name: str):
	return ["h1", {"style": "color:blue"}, name]

template = my_first_template("Yummy name")
builder = pyttee.TemplateStrBuilder()
html = builder(template)
print(html)
```

You can find a more detailed example [here :3](https://github.com/poipoiPIO/pyttee/blob/master/example.py)

## Installation:
The package is now available on PyPi, which means it can be easily installed through any package manager:

### Using `pip`:
```bash
pip install pyttee
```
### Using `poetry`:
```bash
poetry add pyttee
```

## Base Library Reference:
### Basic template rules:
Basically, the template is the list of tags in sexp form. To create a simple template you need to write a list of values where the first element is the name of a tag and the second is the value of the tag:
> ["h1", "Hello world!"] -> `"<h1>Hello world</h1>"`

In the HTML language tags could also have attributes. Tag attributes in our DSL are represented as the dictionary, where the key is the name of an attribute and the value is the value itself, for example:
> ["i", {"style": "color:red"}, "Owo!"] -> `"<i color="red">Owo!</i>"`

For all of these, tags can represent arbitrary nesting of the tags, to reach that we could use list nesting, for example:
> ["i", ["b", ["tt", "meow"]]] -> `"<i><b><tt>meow</tt></b></i>"`

### Builders:
The builder is the entity that provides the interface of template building. Every builder of the library is inherited from the class Builder declares some abstract methods that every template should implement and provides a core compiler for Builders.

#### TemplateStrBuilder:
The basic builder that builds templates and returns HTML-string as the result of execution:

```python
from pyttee import TemplateStrBuilder

template = ["h1", "yummy!"]
builder = TemplateStrBuilder()
print(builder(template))  # -> `<h1>yummy!</h1>`
```
