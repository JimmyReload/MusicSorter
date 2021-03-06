#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Does what it says on the tin...
'''

from MP3MusicSorter import MP3MusicSorter
from MP3Logger import MP3Logger
import sys
import os
import ConfigParser

this_script = os.path.basename(__file__)
name = "MP3MusicSorter"
license_message = '''

  Created by jchapman on 1 September 2013.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

'''
help_message = '''

USAGE

  %s show_duplicates  - Will print out a list of Artists and Track Titles 
                            that have more than 1 file associated with it.
  %s pretend          - Won't actually do anything, just a pretend run.
  %s sort_and_rename  - This will cause files to be sorted and renamed.
  %s update_tags      - Try and upgrade existing tags to ID3 version 2.4
                            (not sure that this actually does anything!)
  
''' % (this_script, this_script, this_script, this_script)

configFile = "%s.cfg" % (name)
if not os.path.exists(configFile):
    print("Can't find %s." % (configFile))
    sys.exit(1)

config = ConfigParser.ConfigParser()
config.read(configFile)
myos = config.get('MP3Tagger', 'os')
current_mp3_dir = config.get('MP3Tagger', 'current_mp3_dir')
sorted_mp3_dir = config.get('MP3Tagger', 'sorted_mp3_dir')
mp3_sort_format = config.get('MP3Tagger', 'mp3_sort_format')

MP3MusicSorter_logger = MP3Logger(name, "debug", "%s.log" % (name))


if __name__ == '__main__':
    print(license_message)
    arg = "None"
    sorter = MP3MusicSorter(myos, sorted_mp3_dir, logger=MP3MusicSorter_logger)
    try:
        arg = sys.argv[1]
    except:
        print(help_message)
        MP3MusicSorter_logger.closeLog()
    if arg == "pretend":
        try:
            sorter.iterateThroughFolder(current_mp3_dir, action="pretend")
        except KeyboardInterrupt:
            print("CTRL+C caught... Stopped!")
            MP3MusicSorter_logger.closeLog()
    elif arg == "sort_and_rename":
        try:
            sorter.iterateThroughFolder(current_mp3_dir, action="restructure")
        except KeyboardInterrupt:
            print("CTRL+C caught... Stopped!")
            MP3MusicSorter_logger.closeLog()
    elif arg == "show_duplicates":
        try:
            sorter.iterateThroughFolder(current_mp3_dir, action="getDuplicates")
        except KeyboardInterrupt:
            print("CTRL+C caught... Stopped!")
            MP3MusicSorter_logger.closeLog()
    elif arg == "update_tags":
        try:
            sorter.iterateThroughFolder(current_mp3_dir, action="upgradeTags")
        except KeyboardInterrupt:
            print("CTRL+C caught... Stopped!")
            MP3MusicSorter_logger.closeLog()
    else:
        print(help_message)
    MP3MusicSorter_logger.closeLog()
    
    
    
    
    
    
    
    
    