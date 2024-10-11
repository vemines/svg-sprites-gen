# SVG Sprite Generator

This project provides tools to generate and merge SVG sprite files from individual SVG icons. It includes two main scripts: `merge.py` and `sprite.py`.

## Overview

- **`sprite.py`**: Creates a new SVG sprite file from all SVG files in a specified input folder.
- **`merge.py`**: Merges new SVG symbols from a specified input folder into an existing SVG sprite file, ensuring no duplicate symbols are added.

## Prerequisites

- Python 3.x
- Required Python packages: `os`, `re`

## Setup

1. Clone the repository or download the scripts.
2. Ensure you have Python 3.x installed on your system.
3. Place your SVG files in the `input` folder.

## Usage

### `sprite.py`

This script generates a new SVG sprite file from all SVG files in the input folder.

- **Input Folder**: `input` (contains individual SVG files)
- **Output File**: `sprite.svg` (newly created sprite file)
- **ID Prefix**: `prefix_` (prefix for symbol IDs)

#### How to Run

```bash
py sprite.py
```

- The script will read all SVG files from the `input` folder.
- It will generate a new `sprite.svg` file containing all symbols with the specified ID prefix.

### `merge.py`

This script merges new SVG symbols into an existing sprite file.

- **Input Folder**: `input` (contains individual SVG files)
- **Target File**: `merge/sprite.svg` (existing sprite file to be updated)
- **ID Prefix**: `prefix_` (prefix for symbol IDs)

#### How to Run

```bash
py merge.py
```

- The script will read SVG files from the `input` folder.
- It will add new 'symbol' to `sprite_file` if they do not already exist.

## Notes

- Ensure that the `input` folder contains only valid SVG files.
- The `merge.py` script will not overwrite existing symbols in the target file.
- You can customize the `id_prefix` in both scripts to suit your naming conventions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
