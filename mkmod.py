import os
import argparse

directories = ["About",
               "Assemblies",
               "Defs",
               "Languages",
               "Languages/English",
               "Languages/English/Strings",
               "Languages/English/Strings/NameBanks",
               "Sounds",
               "Source",
               "Textures"]


def create_dirs(mods_path, mod_name):
    mod_dir = os.path.join(mods_path, mod_name)

    # Mods/Mod
    os.mkdir(mod_dir)

    # Mods/Mod/Subdirs
    for d in directories:
        os.mkdir(os.path.join(mod_dir, d))

    open(os.path.join(mod_dir, "About/About.xml"), 'a').close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mods_path", help="The Rimworld mods directory.")
    parser.add_argument("mod_name", help="Name to give the new mod.")
    args = parser.parse_args()

    mods_path = args.mods_path
    mod_name = args.mod_name

    create_dirs(mods_path, mod_name)

if __name__ == '__main__':
    main()
