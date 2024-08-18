import sys
import re

def load_charmap(file_path,rows=5):
	char_map = {}
	with open(file_path, 'r') as file:
		for line in file:
			if re.match(r'^\s*$', line):
				continue
			elif re.match(r'^[A-Z0-9]', line):
				char = line.strip()
				bitmap = []
				for _ in range(rows):
					bitmap.append(file.readline().strip())
				char_map[char] = bitmap
	return char_map

def print_charmap(char_map):
	for char, bitmap in char_map.items():
		hex_value = 0
		for row in bitmap:
			hex_value = (hex_value << 4) | int(row, 2)
		print(f"{char}: 0x{hex(hex_value)[2:]}")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		file_path = sys.argv[1]
		rows = 5
		if len(sys.argv) > 2:
			rows = int(sys.argv[2])
		char_map = load_charmap(file_path, rows)
		print_charmap(char_map)
	else:
		print("Please provide a file path as a command line argument.")
		print(f"Usage: python {sys.argv[0]} <file_path> [rows=5]")
		print("\tIf you use a different amount of rows, you will need to specify the rows attribute")