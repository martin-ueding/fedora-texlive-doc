#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2015-2016 Martin Ueding <martin-ueding.de>

# Licensed under The MIT License

'''
Installs documentation packages for all installed TeXLive packages on Fedora
22.
'''

import argparse
import subprocess


def get_texlive_packages():
    '''
    Obtains all TeXLive packages that are installed on the system.

    http://unix.stackexchange.com/a/240826/8251
    '''
    command = ['rpm', '--qf', r'%{name}\n', '-qa', 'texlive-*']
    lines = subprocess.check_output(command).decode().strip().split('\n')
    return lines


def convert_to_doc(packages):
    '''
    Converts the list of packages into documentation packages.
    '''
    return [
        package + '-doc'
        for package in packages
        if not package.endswith('-doc')
    ]


def package_exists(package):
    '''
    Checks whether a given package exists.
    '''
    print('Checking', package)
    try:
        subprocess.check_output(['dnf', 'info', package])
    except subprocess.CalledProcessError:
        return False
    else:
        return True


def get_installable():
    packages = get_texlive_packages()
    print('Found {} texlive packages. Checking whether documentation is available …'.format(len(packages)))
    doc_packages = convert_to_doc(packages)

    return filter(package_exists, doc_packages)


def main():
    options = _parse_args()

    installable = get_installable()

    command = ['sudo', 'dnf', 'install'] + sorted(installable)
    print()
    print(' '.join(command))
    print()
    print('Press Enter key to execute that command')
    input()
    subprocess.call(command)


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
