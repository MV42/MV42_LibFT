import os
import sys
import argparse
import datetime


USER = "MV42"  # À modifier selon l'utilisateur souhaité
USE_DATE_FIXED = True  # Mettre True pour utiliser DATE_FIXED, False pour auto
DATE_FIXED = "2024/12/21 21:42:42"  # Mettre la date fixe ici au format "YYYY/MM/DD HH:MM:SS"

HEADER_WIDTH = 80

def pad_line(left, center, right):
    # left: début de ligne, center: champ à centrer, right: fin de ligne
    left_len = len(left)
    right_len = len(right)
    center_len = len(center)
    spaces = HEADER_WIDTH - left_len - center_len - right_len
    return f"{left}{center}{' ' * spaces}{right}"

def make_header(filename, user, created, updated):
    lines = [
        "/* ************************************************************************** */",
        "/*                                                                            */",
        "/*                                                        :::      ::::::::   */",
        pad_line("/*   ", f"{filename}",                        ":+:      :+:    :+:   */"),
        "/*                                                    +:+ +:+         +:+     */",
        pad_line("/*   By: ", f"{user}",                  "  +#+  +:+       +#+        */"),
        "/*                                                +#+#+#+#+#+   +#+           */",
        pad_line("/*   Created: ", f"{created} by {user}",   "  #+#    #+#             */"),
        pad_line("/*   Updated: ", f"{updated} by {user}",   " ###   ########.fr       */"),
        "/*                                                                            */",
        "/* ************************************************************************** */",
        "",
        "",
    ]
    return "\n".join(lines)

def get_file_dates(filepath):
    stat = os.stat(filepath)
    created = datetime.datetime.fromtimestamp(stat.st_ctime).strftime("%Y/%m/%d %H:%M:%S")
    updated = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%Y/%m/%d %H:%M:%S")
    return created, updated

def remove_existing_header(content):
    # Remove header if it starts with /* ************************************************************************** */
    if content.startswith("/* ************************************************************************** */"):
        # Find the second occurrence of /* ************************************************************************** */
        idx = content.find("/* ************************************************************************** */", 1)
        if idx != -1:
            # Move past the end of second header
            end = content.find("*/", idx)
            if end != -1:
                return content[end+2:].lstrip("\n")
        else:
            # Only one header, remove it
            end = content.find("*/")
            if end != -1:
                return content[end+2:].lstrip("\n")
    return content

def process_file(filepath, user):
    filename = os.path.basename(filepath)
    if USE_DATE_FIXED and DATE_FIXED:
        created = updated = DATE_FIXED
    else:
        created, updated = get_file_dates(filepath)
    header = make_header(filename, user, created, updated)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    content = remove_existing_header(content)
    new_content = header + content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

def find_files(dirs):
    files = []
    for d in dirs:
        for root, _, filenames in os.walk(d):
            for name in filenames:
                if name.endswith(".c") or name.endswith(".h"):
                    files.append(os.path.join(root, name))
    return files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Insère ou remplace le header dans les fichiers .c et .h")
    parser.add_argument("folders", nargs="+", help="Dossiers à traiter")
    args = parser.parse_args()

    files = find_files(args.folders)
    for f in files:
        process_file(f, USER)
    print(f"Header inséré/remplacé dans {len(files)} fichiers.")
    