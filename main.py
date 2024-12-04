#! /usr/bin/env python3 

import sys
from controllers.gui.app import run_gui
from controllers.cli.commands import run_cli

def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        run_cli()   
    else:
        run_gui()

main()