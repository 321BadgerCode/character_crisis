import sys
from PIL import Image

def get_charmap(string):
	char_map = {}
	lines = string.split("\n")
	for line in lines:
		if line:
			char, hex_value = line.split(": ")
			char_map[char] = int(hex_value, 16)
	return char_map

char_map = get_charmap(sys.stdin.read())

def get_ascii_art(string, rows=5):
	out = [''] * len(string)
	count = 0
	for char in string:
		if char == ' ':
			out[count] += "    \n" * rows
			count += 1
			continue
		for row in range(rows):
			if char in char_map:
				hex_value = char_map[char]
				invert = 4 * (rows - 1)
				binary_row = (hex_value >> (invert - (row * 4))) & 0xF
				out[count] += format(binary_row, '04b').replace('0', ' ').replace('1', '#') + '\n'
			else:
				out += '\t'
		out[count] = out[count][:-1]
		count += 1
	print(out)
	return out

def print_bitmap(bitmap):
	for row in range(rows):
		for char in bitmap:
			print(char.split('\n')[row], end=' ')
		print()

def save_bitmap(bitmap, filename):
	width = len(bitmap) * 5
	height = 5
	image = Image.new('1', (width, height), 1)
	for x in range(len(bitmap)):
		for y in range(height):
			row = bitmap[x].split('\n')[y]
			for i in range(4):
				if row[i] == '#':
					image.putpixel((i + (x * 5), y), 0)
	image.save(filename)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		input_string = sys.argv[1].upper()
		rows = 5
		if len(sys.argv) > 2:
			rows = int(sys.argv[2])
		print_bitmap(get_ascii_art(input_string, rows))
		save_bitmap(get_ascii_art(input_string, rows), f"{input_string}.bmp")
	else:
		print(get_ascii_art("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
		print("Please provide a string as a command line argument.")
		print(f"Usage: {sys.argv[0]} <string> [rows=5]")
		print("\tSet rows to another value if you're charmap is not 5 rows.")