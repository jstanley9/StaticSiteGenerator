import os

from generatepage import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # print(f'==> picking up index.md files in dir tree {dir_path_content}')
    # print(f'==> deliver index.html file to dir {dest_dir_path}')

    for node in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, node)
        if os.path.isfile(path):
            # print(f'==> FILE: {path}')
            if path.endswith('.md'):
                generate_page(path, template_path, dest_dir_path, basepath)
        elif os.path.isdir(path):
            # print(f'==> DIRECTORY: {path}')
            generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, node), basepath)
        else:
            print(f'==> UNKNOWN: {path}')

def main():
    generate_pages_recursive('./content', 'template.html', './public')

if __name__ == '__main__':
    main()    