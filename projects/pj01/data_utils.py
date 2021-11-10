"""Some helpful utility functions for working with CSV files. This file for PJ01."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
   
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when you're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] with all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        n_values = []
        i = 0
        while i < n:
            value_of_n = column_table[column][i]
            n_values.append(value_of_n)
            i += 1
        result[column] = n_values
    return result


def select(original_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for name in names:
        result[name] = original_table[name]
    return result


def isolate(value: str, section: str, only: dict[str, list[str]]) -> list[str]:
    """Return a list containing only the value indicated."""
    value_only: list[str] = []
    i: int = 0
    while i < len(only[section]):
        if only[section][i] == value:
            value_only.append(only[section][i])
        i += 1
    return value_only


def count(tally: list[str]) -> float:
    result: float = 0.0
    result = len(tally)
    return result