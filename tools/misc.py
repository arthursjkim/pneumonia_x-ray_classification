import os
import sys


def count_files(paths):
    total = 0
    for path in paths:
        print(os.path.basename(path).upper())
        print('-' * 25)
        subtotal = 0
        for dirname in os.listdir(path):
            dirtotal = len(os.listdir(os.path.join(path, dirname)))
            subtotal += dirtotal
            print(f'\t{dirname}: {dirtotal}')
        print(f'\n\tSUBTOTAL: {subtotal}')
        total += subtotal
    print('-' * 25)
    print(f'TOTAL: {total}')
