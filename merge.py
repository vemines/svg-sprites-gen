import os
import re

# Input folder
input_folder = 'input'
# Sprite file need merge
sprite_file = 'merge/sprite.svg'
# Id prefix of symbol in sprites (prefix+name)
id_prefix = ''

def extract_symbol_ids(sprite_file):
    """Extracts all symbol IDs from the existing sprite file."""
    with open(sprite_file, 'r') as file:
        content = file.read()
    return re.findall(r'<symbol id="([^"]+)"', content)

def create_svg_sprite(input_directory, sprite_file, id_prefix):
    # Extract existing symbol IDs from the sprite file
    existing_ids = extract_symbol_ids(sprite_file)
    print(existing_ids)

    # Read the existing sprite content
    with open(sprite_file, 'r') as file:
        sprite_content = file.read()

    # Iterate over all SVG files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.svg'):
            symbol_id = f"{id_prefix}{os.path.splitext(filename)[0]}"
            if symbol_id not in existing_ids:
                with open(os.path.join(input_directory, filename), 'r') as file:
                    content = file.read()
                    # Extract the content between <svg> and </svg>
                    start = content.find('<svg')
                    end = content.find('</svg>') + len('</svg>')
                    symbol_content = content[start:end]
                    # Replace <svg> with <symbol> and add an id with prefix
                    symbol_content = symbol_content.replace('<svg', f'<symbol id="{symbol_id}"')
                    symbol_content = symbol_content.replace('</svg>', '</symbol>')
                    # Add the symbol content to the sprite
                    sprite_content = sprite_content.replace('</svg>', symbol_content + '\n</svg>')

    # Write the updated sprite content back to the sprite file
    with open(sprite_file, 'w') as output:
        output.write(sprite_content)

# Example usage
create_svg_sprite(input_folder, sprite_file, id_prefix)