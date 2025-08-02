import os
import sys
from outpututility import prepare_destination_directories, write_html
from markdown import markdown_to_html_node
from texttohtmlnode import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    markdown_text = get_file_content(from_path)
    parent_node = markdown_to_html_node(markdown_text)
    html = parent_node.to_html()
    title = extract_title(from_path)

    template_html = get_file_content(template_path)
    final_html = fill_in_html_template(template_html, title, html, basepath)
    #print(final_html)

    prepare_destination_directories(dest_path)

    file_name, _ = os.path.splitext(os.path.basename(from_path))
    file_path = os.path.join(dest_path, f'{file_name}.html')
    write_html(file_path, final_html)

    #print('Fini')

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

def fill_in_html_template(template_html, title, html, basepath):
    return template_html.replace('{{ Title }}', title). \
                         replace('{{ Content }}', html). \
                         replace('href="/', f'href="{basepath}'). \
                         replace('src="/', f'src="{basepath}')