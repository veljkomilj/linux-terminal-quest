#!/usr/bin/env python

from distutils.core import setup
import os


# gets all directories from a directory
def recursively_get_dirs(package_name, start_dir):
    start_path = os.path.join(package_name, start_dir)
    paths = []

    for root, dir, files in os.walk(start_path):
        for f in files:
            file_path = os.path.join(root, f)

            # If this is package data for linux_story
            if package_name:
                file_path = file_path.replace(package_name + "/", "")

            paths.append(file_path)

    return paths


file_system = recursively_get_dirs("linux_story", "file_system")
data = recursively_get_dirs("linux_story", "data")
animation = recursively_get_dirs("linux_story", "animation")
challenges = recursively_get_dirs("linux_story", "challenges")
gtk3 = recursively_get_dirs("linux_story", "gtk3")
terminals = recursively_get_dirs("linux_story", "terminals")
media = recursively_get_dirs("", "media")

setup(name='Linux Story',
      version='1.2',
      description='Story to teach people basic Linux commands',
      author='Team Kano',
      author_email='dev@kano.me',
      url='https://github.com/KanoComputing/linux-tutorial',
      packages=['linux_story'],
      package_dir={'linux_story': 'linux_story'},
      scripts=['bin/linux-story', 'bin/linux-story-gui'],
      package_data={'linux_story': file_system + data + animation + challenges + gtk3 +
                    terminals},
      data_files=[('/usr/share/linux-story/media/', media),
                  ('/usr/share/kano-applications/', "icon/linux-story.app"),
                  ('/usr/share/icons/Kano/66x66/apps/', 'icon/linux-story.png')]
      )
