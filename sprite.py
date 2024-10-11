import os

# Input folder
input_folder = 'input'
# Output file
output_file = 'sprite.svg'
# Id prefix of symbol in sprites (prefix+name)
id_prefix = ''

def create_svg_sprite(input_directory, output_file, id_prefix):
    # Start the SVG sprite file
    sprite_content = '<svg width="0" height="0" class="hidden">\n'

    # Iterate over all SVG files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.svg'):
            with open(os.path.join(input_directory, filename), 'r') as file:
                content = file.read()
                # Extract the content between <svg> and </svg>
                start = content.find('<svg')
                end = content.find('</svg>') + len('</svg>')
                symbol_content = content[start:end]
                # Replace <svg> with <symbol> and add an id with prefix
                symbol_content = symbol_content.replace('<svg', f'<symbol id="{id_prefix}{os.path.splitext(filename)[0]}"')
                symbol_content = symbol_content.replace('</svg>', '</symbol>')
                # Add the symbol content to the sprite
                sprite_content += symbol_content + '\n'

    # Close the SVG sprite file
    sprite_content += '</svg>'

    # Write the sprite content to the output file
    with open(output_file, 'w') as output:
        output.write(sprite_content)

create_svg_sprite(input_folder, output_file, id_prefix)