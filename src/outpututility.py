import os
import shutil
import sys

IMAGES_DIRECTORY = 'images'
TARGET_DIRECTORY = 'public'
TEMPLATE_DIRECTORY = 'static'

target_directory = os.path.abspath(f'./{TARGET_DIRECTORY}')

def init_public_space():
    static_path = os.path.abspath(f'./{TEMPLATE_DIRECTORY}')

    clear_directory(target_directory)
    copy_templates_to_target(static_path, target_directory)

def copy_templates_to_target(static_path, target_directory):
    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    for path in os.listdir(static_path):
        source_path = os.path.join(static_path, path)
        if os.path.isdir(source_path):
            copy_templates_to_target(source_path, os.path.join(target_directory, path))
        else:
            shutil.copy(source_path, target_directory)

def clear_directory(path):
    for name in os.listdir(path):
        file_title = os.path.join(path, name)
        if os.path.isdir(file_title):
            clear_directory(file_title)
            os.rmdir(file_title)
        else:
            os.remove(file_title)

def prepare_destination_directories(dest_path):
    start_index = 0
    if dest_path.startswith('.'):
        start_index = 1
        if dest_path.startswith('./'):
            start_index = 2
    path = dest_path[start_index:]
    #print(f'==> MakeDirs({path})')
    os.makedirs(path, exist_ok = True)

def write_html(dest_path, final_html):
    try:
        with open(dest_path, 'w') as html_file:
            html_file.write(final_html)
        return
    except FileNotFoundError:
        print("Error: The file or directory does not exist.")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    sys.exit(1)

# Primative logging
events_monitered = ('os.open', 'os.mkdir', 'os.remove', 'os.rmdir', 'os.chmod', 'os.rename' )
def audit_hook(event, args):
    if event in events_monitered:
        print(f'<*** monitered event: {event} :: arguments {args}')

# sys.addaudithook(audit_hook)    