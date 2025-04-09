import os
from pathlib import Path

import config
import projekt_tests


def project():
    return Path(projekt_tests.__file__).parent.parent

def screenshots(file=None):
    if file:
        return str(project().joinpath(f'resources/screenshots/{file}'))
    else:
        return str(project().joinpath(f'resources/screenshots/'))



def reports():
    return str(project().joinpath(f'reports/'))


def upload(file=None):
    if file:
        return str(project().joinpath(f'resources/upload_files/{file}'))
    else:
        return str(project().joinpath(f'resources/upload_files/'))


def download(file=None):
    if file:
        return str(project().joinpath(f'resources/download_files/{file}'))
    else:
        return str(project().joinpath(f'resources/download_files/'))


def testdata(dir, file):
    return str(project().joinpath(f'resources/testdata/{dir}/{file}'))


def testdata_dir():
    return str(project().joinpath(f'resources/testdata/'))


def xsd_file(file):
    return str(project().joinpath(f'resources/xsd/{file}'))


def driver(file):
    path = str(project().joinpath(f'resources/drivers/{file}'))
    if not os.path.exists(path):
        if config.settings.browser_name == 'chrome':
            path = str(project().joinpath(f'driver/win32/{file}'))
        elif config.settings.browser_name == 'firefox':
            path = str(project().joinpath(f'driver/win64/{file}'))
        elif config.settings.browser_name == 'edge':
            path = str(project().joinpath(f'driver/win32/{file}'))
    return path





def log():
    return str(project().joinpath(f'log/'))


def upload_users_csv(file):
    return str(project().joinpath(f'resources/upload_files/users_csv/{file}'))


def upload_dxbt(file=None):
    if file:
        return str(project().joinpath(f'resources/upload_files/dxbt/{file}'))
    else:
        return str(project().joinpath(f'resources/upload_files/dxbt/'))


