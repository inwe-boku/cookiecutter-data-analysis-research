"""Write certain values of results to a LaTeX header file to create new LaTeX commands. Results are
meant to be loaded from output files produced in previous computation steps."""

from src.config import OUTPUT_DIR
from src.utils import create_folder
from src.result_values import write_result_values


def main():
    result_values = {}

    # XXX This is a dummy placeholder / example code. Replace it with real code.
    meaning_of_life = 42
    result_values["meaningoflife"] = f"{meaning_of_life:d}"

    # XXX This is a dummy placeholder / example code. Replace it with real code.
    #  - A unit can be passed as string as second parameter: the LaTeX package siunitx will be used
    #    to display the quantity.
    #  - Use .2f for rounding to two decimals.
    gravity_ms2 = 9.80665
    result_values["gravity"] = f"{gravity_ms2:.2f}", "m/s^2"

    latex_file_name = create_folder("result_values", prefix=OUTPUT_DIR) / "result_values.tex"

    write_result_values(result_values, latex_file_name)


if __name__ == "__main__":
    main()
