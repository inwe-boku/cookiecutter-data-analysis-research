import re


def format_latex_command(key, value, unit=None):
    # test if key contains invalid characters for a latex command:
    if not re.match(r"^[a-zA-Z]+$", key):
        raise ValueError(f"Invalid key '{key}': not a valid latex command name")

# Unfortunately, curly braces are used as place holders by cookiecutter (uses jinja templates)
# https://cookiecutter.readthedocs.io/en/stable/troubleshooting.html#i-m-having-trouble-generating-jinja-templates-from-jinja-templates
{% raw %}
    if unit is not None:
        value = f"\\qty{{{value}}}{{{unit}}}"

    return f"\\newcommand{{\\{key}}}{{{value}}}"
{% endraw %}


def write_result_values(result_values, filename):
    """Write the result values to a latex header file creating new Latex command for each value.

    Parameters
    ----------
    result_values : dict
        Results to be written to the Latex header file: keys of the dictionary are the names of the
        latex commands the values are either a single value or a tuple containing the value and the
        unit.
    filename : str
        The name of the Latex header file to write the result values to.

    """
    result_values_flat = [
        (key, *value) if isinstance(value, tuple) else (key, value)
        for key, value in result_values.items()
    ]
    latex_commands = [format_latex_command(*params) for params in result_values_flat]

    with open(filename, "w") as f:
        f.write("\n".join(latex_commands) + "\n")
