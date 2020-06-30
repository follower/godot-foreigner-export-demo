#!/usr/bin/env python3

#
# Usage: GODOT_BINARY=/<path>/Godot-v3.2.1.app/Contents/MacOS/Godot ./tools/package-all-with-version.py
#

# Requires: `export_presets.cfg` to have at least one preset with valid export path.

# Produces: # TODO: List here...

# TODO: Add license etc.

# Note: Yes, this script will inevitably grow to the
#       point where it can send/receive email.

# TODO: Reimplement in GDScript? (I mean I *guess* I could've started with bash.)

import os
import glob
import subprocess
import configparser


class GodotExecutable:

    file_path = ""


    def __init__(self, executable_file_path):

        self.file_path = executable_file_path


    def show_version_test(self):

        return subprocess.run([self.file_path, "--version"])


    def _get_arguments_for_export(self, export_config):

        # TODO: Support headless & no-window.
        # TODO: Support release template.

        return [self.file_path, "--windowed", "--resolution", "160x160", "--export-debug", export_config.preset_name , export_config.output_file_path]


    def export_dry_run(self, export_config):

        # TODO: Handle mkdir so it's not created on dry_run.

        print(self._get_arguments_for_export(export_config))


    def export(self, export_config):

        subprocess.run(self._get_arguments_for_export(export_config))



class ExportConfig:

    def __init__(self):
        pass



def export_with_preset(export_config, godot_instance):

    # TODO: Make this a method of GodotExecutable?

    export_output_directory_no_bump = os.path.join(export_config.output_base_dir, export_config.platform.lower(), export_config.template,  "v%s" % (export_config.version))

    if os.path.exists(export_output_directory_no_bump):

        existing_bump_dirs = glob.glob("%s?" % export_output_directory_no_bump)

        if not existing_bump_dirs:
           export_config.revision_bump = "a" # TODO: Don't just overwrite if supplied?
        else:
           latest_revision_bump = sorted(existing_bump_dirs)[-1][-1]

           # TODO: Validate better...
           export_config.revision_bump = chr(ord(latest_revision_bump) + 1)

        if export_config.revision_bump == "z":
            raise NotImplementedError # TODO: Handle this situation.

    export_output_directory = "%s%s" % (export_output_directory_no_bump, export_config.revision_bump)

    os.makedirs(export_output_directory) # TODO: Don't error out if the directory exists but is empty to avoid wasting directories on failed exports?

    export_file_name = "{base_name}-{platform}-v{version}{revision_bump}.{extension}".format_map(export_config.__dict__) # TODO: Handle map properly.

    export_config.output_file_path = os.path.join(export_output_directory, export_file_name)


    print("")

    # godot_instance.export_dry_run(export_config)
    godot_instance.export(export_config)

    # TODO: Return (and collect) output file paths.

    print("")



if __name__=="__main__":

   godot_binary_file_path = os.getenv("GODOT_BINARY")
   if not godot_binary_file_path:
      print("Please set GODOT_BINARY environment variable to Godot binary file path.")
      raise SystemExit

   godot = GodotExecutable(godot_binary_file_path)

   print("")
   godot.show_version_test()
   print("")

   export_presets = configparser.ConfigParser()
   export_presets.read("export_presets.cfg")

   # TODO: Enable non --all option

   for section_name in export_presets.sections():

       section = export_presets[section_name]

       if "name" in section.keys():

          print()
          print(section["name"])

          export_preset_name = section["name"].strip('"')

          path_parts = section["export_path"].strip('"').rsplit("/", 3)

          export_output_base_dir = path_parts[0]
          export_platform = path_parts[1].capitalize()
          export_version = path_parts[2].lstrip("v") # TODO: Handle revision bump? Retrieve from elsewhere?

          filename_parts = path_parts[3].rsplit("-", 1)

          export_base_name = filename_parts[0]
          export_extension = filename_parts[-1].rsplit(".")[-1]


          export_config_for_preset = ExportConfig()

          # TODO: Set these properly?
          export_config_for_preset.preset_name = export_preset_name

          export_config_for_preset.output_base_dir = export_output_base_dir
          export_config_for_preset.platform = export_platform
          export_config_for_preset.version = export_version

          export_config_for_preset.base_name = export_base_name
          export_config_for_preset.extension = export_extension

          export_config_for_preset.project_name = export_base_name # TODO: Handle properly.
          export_config_for_preset.revision_bump = "" # TODO: Handle properly?

          export_config_for_preset.template = "release" # TODO: Handle properly.


          export_with_preset(export_config_for_preset, godot)

          # TODO: Add automatic archive creation where required.

          # TODO: Only export one Mac option and/or handle directory naming better.
          # TODO: Don't attempt DMG export on non-Mac.

          print()


   # TODO: Handle export_template.
   # TODO: Update presets file with new (base) version value in path?
   # TODO: Update all references to version in the presets file?

   #export_project_name = "ForeignerExportDemo"
   ##export_base_name = "ForeignerExportDemo"
   ##export_version="0.1.1"
   ##export_revision_bump = "f"
   #export_revision_bump = ""
   #export_template = "release" # "debug"
   ##export_extension = "exe" # or ...
   ##export_platform = "Win64" # or "Mac" or "Linux"

   # "exports/<platform>/v<version>[<bump>]/<ForeignerExportDemo>-<short_platform>-[<template>]-v<version>[<bump>].<ext>"

