from pathlib import Path

from django.core.management.utils import get_random_secret_key


BASE_DIR = Path(__file__).resolve().parent
SETTINGS_DIR = Path.joinpath(BASE_DIR, 'backend_module', 'settings')


def create_django_project_secret_key():
    secret_key = get_random_secret_key()
    file_path = Path.joinpath(BASE_DIR, 'secret_key.txt')
    if file_path.exists():
        print('The secret key already exists. Skipping the process.')
    else:
        with open(file_path, 'w') as fp:
            fp.write(secret_key)
    return True


if __name__ == '__main__':
    assert BASE_DIR.match('**backend'), "The script should run in backend project directory."
    # Generate SECRET KEY for django
    create_django_project_secret_key()
