from pathlib import Path

import projekt_tests


def project():
    return Path(projekt_tests.__file__).parent.parent


def screenshots(file=None):
    if file:
        return str(project().joinpath(f'resources/screenshots/{file}'))
    else:
        return str(project().joinpath(f'resources/screenshots/'))


def screenshots_expected(file=None):
    if file:
        return str(project().joinpath(f'resources/screenshots/expected/{file}'))
    else:
        return str(project().joinpath(f'resources/screenshots/expected/'))


def reports():
    return str(project().joinpath(f'reports/'))
