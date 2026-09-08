import math
from datetime import datetime


def ask_positive_float(prompt: str, required=True):
	"""
	Request a positive number.

	Args:
			prompt (str): Text to display on the input message.
			required (boolean): The input is mandatory or not.
	"""
	while True:
		raw_value = input(prompt).strip()

		# User leaves the input empty
		if not raw_value:
			if required:
				print("This field is mandatory. Please enter a positive number.")
				continue

			# Optional field: confirm action
			while True:
				confirm = (
					input(
						"No value provided. Do you want to leave this field empty? (yes/no): "
					)
					.strip()
					.lower()
				)

				if confirm in ("yes", "y"):
					return None

				if confirm in ("no", "n"):
					break  # Request the value again

				print("Please answer yes or no.")

			continue

		# Try to parse string to floar
		try:
			value = float(raw_value)
		except ValueError:
			print("Invalid input. Please enter a valid number.")
			continue

		# Validate that is greater than 0
		if not math.isfinite(value) or value <= 0:
			print("The value must be a positive number greater than 0.")
			continue

		return value


def ask_date(prompt: str, required: True):
	"""
	Request a positive number.

	Args:
			prompt (str): Text to display on the input message.
			required (boolean): The input is mandatory or not.
	"""
	pass


def ask_datetime(prompt: str, required: True):
	"""
	Request a positive number.

	Args:
			prompt (str): Text to display on the input message.
			required (boolean): The input is mandatory or not.
	"""
	pass
