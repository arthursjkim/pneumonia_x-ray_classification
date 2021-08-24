import os
import sys


def count_files(paths):
    """Iterate through list of paths and display class distributions for image filesystem, returns counts dict"""
    total = 0
    counts = {}

    # Iterate through paths (i.e., train, val, and test)
    for path in paths:
        print(os.path.basename(path).upper())
        print('-' * 25)

        # Initialize running count for subset and count files
        subtotal = 0
        for dirname in os.listdir(path):
            key = os.path.basename(path) + '_' + dirname.lower()
            dirtotal = len(os.listdir(os.path.join(path, dirname)))

            # Add subdirectory totals to subset total and counts to dict
            subtotal += dirtotal
            counts[key] = dirtotal
            print(f'\t{dirname}: {dirtotal}')
        print(f'\n\tSUBTOTAL: {subtotal}')
        total += subtotal

    # Display running total
    print('-' * 25)
    print(f'TOTAL: {total} files')
    return counts


if __name__ == '__main__':
    TRAIN_PATH = 'data/split/train'
    VAL_PATH = 'data/split/val'
    TEST_PATH = 'data/split/test'
    os.chdir('..')
    print(count_files([TRAIN_PATH, VAL_PATH, TEST_PATH]))