import os
import sys
import pickle


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
            dirtotal = len(os.listdir(os.path.join(path, dirname)))

            # Add subdirectory totals to subset total and counts to dict
            subtotal += dirtotal
            print(f'\t{dirname}: {dirtotal}')
        print(f'\n\tSUBTOTAL: {subtotal}')
        total += subtotal
        counts[os.path.basename(path)] = subtotal

    # Display running total
    print('-' * 25)
    print(f'TOTAL: {total} files')
    return counts


def pickle_history(model, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(model.history, f)


def unpickle_history(filepath):
    with open(filepath, 'rb') as f:
        history = pickle.load(f)
    return history


if __name__ == '__main__':
    TRAIN_PATH = 'data/split/train'
    VAL_PATH = 'data/split/val'
    TEST_PATH = 'data/split/test'
    os.chdir('..')
    print(count_files([TRAIN_PATH, VAL_PATH, TEST_PATH]))
