
from pyttee import TemplateStrBuilder 


def my_first_template(name: str):
    # Define a template using function
    return ["body",
            ["h1",  # Do whatever you want with your
                    # template described as datastructure!
                f"Hello {name}!"],
            ["h1",  # Add some selectors using dicts
                {"style": "color:aliceBlue"},
                "Hello world!"],
            ["i", 
                ["h1", "sugoooi~"]]]


if __name__ == "__main__":
    template = my_first_template("World")
    builder = TemplateStrBuilder()
    html = builder(template)
    print(html)
