<p align="center">
	<img src="./asset/logo.png" alt="Logo" width="200" height="25">
</p>

<h1 align="center">Character Crisis</h1>

<p align="center">
	<strong>Generate ASCII art & text images!</strong>
</p>

## 🚀 Overview

Welcome to **Character Crisis**! This program allows you to create ASCII art for an input text string, using a given charmap. The program also stores the text as an image.

> [!NOTE]
> The logo for the program was created using the program itself.

## 🎨 Features

- **Dynamic loading of charmaps**: The program can load any charmap from a file, allowing for custom charmaps, of different row sizes.
- **Efficient storing of charmaps**: The program has 4 columns per row, so that each character can be represented by 1 hex digit for it's ASCII art charmap character.
- **Storing text images**: The program displays the ASCII art in the terminal, but also stores a BMP image of the text in the ASCII art font.

## 📦 TODO

- [ ] Use different base number system like base64 instead of hex (base 16) to store more columns per row because 4 is asymmetric and not very efficient.
	- 5 columns per row would look nice and symmetric. 5x5 is also square (the 4x4 does not look good because it has so few grid cells).
- [ ] Add functionality for escape characters such as `\t` and `\n`.
- [ ] Add more characters to the charmaps (rather than A-Z, make it !-~).
- [ ] Add charmaps and functionality for segment displays (7 segment, 14 segment, etc.).

## 🛠️ Installation

To get started with the program, follow the steps below:

1. **Clone the repository**
```sh
git clone https://github.com/321BadgerCode/character_crisis.git
cd ./character_crisis/
```

## 📈 Usage

To use the program, follow the instructions below:

1. **Run the program**
```sh
# python ./load_charmap.py ./charmap4x4.txt 4 | python ./main.py "hello world"
python ./load_charmap.py ./charmap4x5.txt | python ./main.py "hello world"
```

## 📜 License

[LICENSE](./LICENSE)