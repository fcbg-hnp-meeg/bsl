import os
import sys
import glob

from pathlib import Path
from importlib import import_module

import neurodecode


def main():
    """Entrypoint for nd <command> usage."""
    neurodecode_root = Path(__file__).parent.parent
    valid_commands = sorted(
        glob.glob(str(neurodecode_root/'commands'/'nd_*.py')))
    valid_commands = [file.split(os.path.sep)[-1][3:-3]
                      for file in valid_commands]

    def print_help():
        print("Usage : NeuroDecode command options\n")
        print("Accepted commands:\n")
        for command in valid_commands:
            print("\t- %s" % command)
        print('\nExample : nd stream_player StreamPlayer "path to .fif file"')
        print("\nGetting help example : nd stream_recorder -h")

    if len(sys.argv) == 1 or "help" in sys.argv[1] or "-h" in sys.argv[1]:
        print_help()
    elif sys.argv[1] == "--version":
        print("NeuroDecode %s" % neurodecode.__version__)
    elif sys.argv[1] not in valid_commands:
        print('Invalid command: "%s"\n' % sys.argv[1])
        print_help()
    else:
        cmd = sys.argv[1]
        cmd = import_module('.nd_%s' % (cmd,), 'neurodecode.commands')
        sys.argv = sys.argv[1:]
        cmd.run()