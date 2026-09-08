def read_json(file_path: str, mode: str = "r"):
	import json

	"""
	Reads a JSON file and returns its content as a Python object.

	Args:
		file_path (str): The path to the JSON file.
		mode (str): The mode in which to open the file.
	"""
	with open(file_path, mode) as file:
		data = json.load(file)
	return data


def read_csv(file_path: str, mode: str = "r"):
	"""
	Reads a CSV file and returns its content as a list of dictionaries.

	Args:
		file_path (str): The path to the CSV file.
		mode (str): The mode in which to open the file.
	"""
	import csv

	with open(file_path, mode) as file:
		reader = csv.DictReader(file)
		data = [row for row in reader]
	return data


def csv_to_dataframe(file_path: str, schema: dict | None = None):
	"""
	Reads a CSV file and returns its content as a pandas DataFrame.

	Args:
		file_path (str): The path to the CSV file.
		schema (dict | None): Optional column name to polars dtype mapping.
	"""
	import polars as pl

	df = pl.read_csv(file_path, schema=schema)
	return df
