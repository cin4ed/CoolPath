"""CoolPath.

Usage:
  coolpath list
  coolpath add <path>...
  coolpath remove <path>...
  coolpath (-h | --help)
  coolpath --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
import os

PATH = os.environ.get('PATH')

def showPath():
  print(PATH)

def add(path):
  print('add executed, {0} added to the path'.format(path))

def remove(path):
  print('remove executed, {0} removed from path'.format(path))

if __name__ == '__main__':
  arguments = docopt(__doc__, version='CoolPath v1.0')

  if arguments['list']:
    showPath()
  elif arguments['add']:
    add(arguments['<path>'])
  elif arguments['remove']:
    remove(arguments['<path>'])

  # for debugging
  # print(arguments)