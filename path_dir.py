import os
from pathlib import Path

import config
import projekt_tests


def project():
    return Path(projekt_tests.__file__).parent.parent

def screenshots(file):
    return str(project().joinpath(f'screenshots/{file}'))


def screenshots_dir():
    return str(project().joinpath(f'screenshots/'))


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


def reports():
    return str(project().joinpath(f'reports/'))


def log():
    return str(project().joinpath(f'log/'))


def upload_users_csv(file):
    return str(project().joinpath(f'resources/upload_files/users_csv/{file}'))


def upload_dxbt(file=None):
    if file:
        return str(project().joinpath(f'resources/upload_files/dxbt/{file}'))
    else:
        return str(project().joinpath(f'resources/upload_files/dxbt/'))


#########   bvbei_deuev_mva_a1   ############################

def execute():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/execute/'))


def execute_rueckmeldung():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/execute_rueckmeldung/'))


def templates():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/templates/'))


def templates_a1a():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/templates/A1A/'))


def testcases():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/testcases/'))


# temp


def temp_dir():
    return str(project().joinpath(
        f'resources/bvbei_deuev_mva_a1/temp/'))


def working():
    return str(project().joinpath(
        f'resources/bvbei_deuev_mva_a1/temp/working/'))  # <!-- temporary working directory for creating data -->


def clear():
    return str(project().joinpath(
        f'resources/bvbei_deuev_mva_a1/temp/clear/'))  # <!-- if clear directory is not given, the clear files won't be saved -->


# output
def output():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/output/'))


def rueckmeldungen():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/output/rueckmeldungen/'))


def rueckmeldungen_file(file):
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/output/rueckmeldungen/{file}'))


def rueckmeldungen_ag():
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/output/rueckmeldungen_ag/'))


def quittung():
    return str(
        project().joinpath(
            f'resources/bvbei_deuev_mva_a1/output/quittung/'))  # QuittierungsAntwort: str = 'Upload/Quittung'


def quittung_antwort():
    return str(
        project().joinpath(
            f'resources/bvbei_deuev_mva_a1/output/quittung/QuittungAntwort.xml'))


def log(file):
    return str(project().joinpath(f'resources/bvbei_deuev_mva_a1/output/log/{file}'))  # Log


def execute_testcases(dir):
    return str(project().joinpath(f'resources/exec/testcases/{dir}/'))


def decryption():
    return str(project().joinpath(f'resources/decryption/'))


def config_dasbv(file):
    return str(project().joinpath(f'projekt_tests/help/mod_testdata_creator/{file}'))  # Log


def health_center():
    return str(project().joinpath(f'win32_health_center_5_1_0_2/'))


def make_order_file():
    return str(project().joinpath(f'win32_health_center_5_1_0_2/makeOrderFile.exe'))


def make_order_directory():
    return str(project().joinpath('win32_health_center_5_1_0_2'))


def xmlvalidator_directory():
    return str(project().joinpath('projekt_tests/help/mod_testdata_creator/xmlValidator'))


def xmlvalidator_Qt5Core_dll():
    return str(project().joinpath('projekt_tests/help/mod_testdata_creator/xmlValidator/Qt5Core.dll'))
