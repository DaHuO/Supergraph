import fnmatch
import importlib
import os
import time
import traceback

import main


def get_files():
    matches = []
    path = os.path.dirname(os.path.realpath(__file__))
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.in'):
            matches.append(os.path.join(root, filename))

    return matches

def tmp_file_name(file_name):
    return file_name[:-3] + ".tmp"


def out_file_name(file_name):
    return file_name[:-3] + ".out"


def run_file(file):
    print("Processing file \'%s\'... " % os.path.basename(file), end="")

    tmp_file = tmp_file_name(file)

    with open(file, "r") as input_file, open(tmp_file, "w") as out:
        try:
            main.process(input_file, out)
        except BaseException as e:
            if isinstance(e, KeyboardInterrupt):
                raise e
            else:
                traceback.print_exc()

    out_file = out_file_name(file)
    if os.path.exists(out_file):
        os.remove(out_file)
    os.rename(tmp_file, out_file)

    print("Finished!")


if __name__ == "__main__":
    main_last_time = os.path.getmtime(main.__file__)
    before = {}

    while 1:
        after = {f: os.path.getmtime(f) for f in get_files()}

        main_time = os.path.getmtime(main.__file__)
        if main_last_time < main_time:
            importlib.reload(main)
            files = list(after)
            print("\nMain file has changed...\n")
        else:
            files = [f for f in after.keys() if f not in before.keys() or before[f] < after[f]]

        for file in files:
            run_file(file)

        before = after
        main_last_time = main_time
        time.sleep(1)