#!/usr/bin/env python3

import argparse
from models.desktop_entry_config import DesktopEntry
from utils.desktop_entry_writer import Desktop_entry_writer

def generate_config_from_args(args) -> DesktopEntry:
    config = DesktopEntry(args.name, args.exec_path)
    
    config.set_name(args.name)
    config.set_exec_path(args.exec_path)
    
    if args.terminal:
        config.set_terminal(True)
    
    config.set_icon_path(args.icon_path if args.icon_path else None)
        
    return config

def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Create a .desktop file for an application.")

    parser.add_argument("name", help="Name of the application")
    parser.add_argument("exec_path", help="Path to the executable binary")
    parser.add_argument("-i", "--icon_path", help="Path to the icon file", default="/usr/share/icons/default_icon.png")
    parser.add_argument("-t", "--terminal", action="store_true", help="Run in a terminal")

    config = generate_config_from_args(parser.parse_args())
    writer = Desktop_entry_writer()
    writer.write(config)