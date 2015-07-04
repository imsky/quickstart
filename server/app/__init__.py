from bottle import route, request, run, error, abort, static_file
from bottle import template, jinja2_view
import os, string, pprint

def find_file(type, name):
  """ searches file within directory by name, ignoring extension and case """
  assert type.isalpha() and name.isalpha()
  type = type.lower()
  name = name.lower()
  dir = 'files/' + type
  options = []
  if os.path.isdir(dir):
    for root, dirs, files in os.walk(dir):
      for f in files:
        if f[0] == '.':
          options.append(f[1:])
        else:
          split = string.split(f, '.')
          filename = split[0]
          if filename.lower() == name.lower():
            return [options, dir, f]
  return False

def list_files(type):
  """ lists file within directory, ignoring extension and case """
  assert type.isalpha()
  type = type.lower()
  dir = 'files/' + type
  if os.path.isdir(dir):
    files = []
    for root, dirs, _files in os.walk(dir):
      for f in _files:
        if f[0] != '.':
          split = string.split(f, '.')
          files.append(split[0].lower())
    files.sort()
    return files
  return False

def list_types():
  """ lists types (directories), ignoring case and symlinks """
  types = []
  for root, dirs, files in os.walk('files'):
    for d in dirs:
      if os.path.islink('files/' + d) is False:
        types.append(d)
  types.sort()
  return types

@error(404)
@jinja2_view('404')
def error404(error):
  return dict()

@route('/static/<filepath:path>')
def serve_static(filepath):
  return static_file(filepath, root='./static')

@route('/')
@jinja2_view('home')
def get_home():
  return dict(types=list_types())

@route('/<type:re:[a-zA-Z]+/?>')
@jinja2_view('listing')
def get_type(type):
  type = type.replace('/', '')
  files = list_files(type)

  if files:
    return dict(type=type, files=files)
  else:
    abort(404, 'Category not found')

@route('/<type:re:[a-zA-Z]+>/<name:re:[a-zA-Z]+>')
def get_file(type, name):
  lookup = find_file(type, name)

  if lookup:
    options, dir, filename = lookup
    download = False
    # todo: make dl flag logic more concise
    if request.query_string == 'download' or request.query_string == 'dl':
      split = string.split(filename, '.')
      download = True

      if 'no-dot' in options:
        # name.ext -> ext
        download = split[1]
      elif 'no-name' in options:
        # name.ext -> .ext
        download = '.' + split[1]

    return static_file(filename, dir, mimetype='text/plain', download=download)
  else:
    abort(404, 'File not found')

def start():
  run()
