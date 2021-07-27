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
from clint.textui import colored, puts, indent
import os

PATH = os.environ.get('PATH')

def showPath():
  index = 0
  pathList = PATH.split(':')
  for path in pathList:
    with indent(2, quote=colored.blue('> ')):
      puts(f'{colored.green(index)}: {path}')
    index += 1

def add(pathsToAdd):
  # Experimental
  newPATH = PATH
  for path in pathsToAdd:
    newPATH += f':{path}'
  os.environ['PATH'] = newPATH

def remove(path):
  pass

if __name__ == '__main__':
  arguments = docopt(__doc__, version='CoolPath v1.0')

  if arguments['list']:
    showPath()
  elif arguments['add']:
    add(arguments['<path>'])
  elif arguments['remove']:
    remove(arguments['<path>'])
  
  # print(arguments)