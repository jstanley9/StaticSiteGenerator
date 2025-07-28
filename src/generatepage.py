import os
import sys
from outpututility import init_public_space, prepare_destination_directories, write_html
from markdown import markdown_to_html_node
#from htmlnode import HTMLNode
from texttohtmlnode import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    markdown_text = get_file_content(from_path)
    parent_node = markdown_to_html_node(markdown_text)
    html = parent_node.to_html()
    title = extract_title(from_path)

    template_html = get_file_content(template_path)
    final_html = fill_in_html_template(template_html, title, html)
    print(final_html)

    init_public_space()
    prepare_destination_directories(dest_path)

    write_html(dest_path, final_html)

    print('Fini')

def get_file_content(path_name):
    absolute_path = os.path.abspath(path_name)

    try:
        with open(absolute_path, 'r') as text_file:
            return text_file.read()
    except FileNotFoundError:
        print(f'File {path_name} => {absolute_path} not found.')
    except PermissionError:
        print('You do not have permission to access this file.')
    except UnicodeDecodeError:
        print(f'The file:{absolute_path} encoding is incompatible with the specified encoding.')
    except Exception as e:
        print(f"An unexpected error occurred reading file:{absolute_path}: {e}")

    sys.exit(1)

def fill_in_html_template(template_html, title, html):
    return template_html.replace('{{ Title }}', title).replace('{{ Content }}', html)