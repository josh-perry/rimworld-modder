import os
import argparse
import re


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

about_template = '''<?xml version="1.0" encoding="utf-8"?>
<ModMetaData>
    <name>{Name}</name>
    <author>{Author}</author>
    <url>{Url}</url>
    <targetVersion>{Version}</targetVersion>
    <description>{Description}</description>
</ModMetaData>'''


def create_dirs(mods_path, mod_name):
    mod_dir = os.path.join(mods_path, mod_name)

    # Mods/Mod
    os.mkdir(mod_dir)

    # Mods/Mod/Subdirs
    for d in directories:
        os.mkdir(os.path.join(mod_dir, d))

    with open(os.path.join(mod_dir, "About/About.xml"), 'w') as f:
        data = {"Name": mod_name,
                "Author": "",
                "Url": "",
                "Version": get_version(mods_path),
                "Description": ""}

        about_xml_content = about_template.format(**data)
        f.write(about_xml_content)


def get_version(mods_path):
    rimworld_dir = os.path.join(mods_path, "..")

    try:
        with open(os.path.join(rimworld_dir, "Version.txt")) as f:
            # version = f.read().replace("\n", "")
            # return version.strip()

            contents = f.read()
            m = re.search(r'\d+\.\d+\.\d+', contents)
            return m.group(0)
    except Exception as ex:
        print(ex)
        return ""


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
