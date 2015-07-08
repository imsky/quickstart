from bottle import route, request, error, abort, static_file
from bottle import template, jinja2_view
import bottle, waitress, os, glob, string, pprint

cache = dict()

def find_file(type, name):
  """ searches file within directory by name, ignoring extension and case """
  assert type.isalpha() and name.replace('-', '').isalpha()
  type = type.lower()
  name = name.lower()
  dir = 'files/' + type

  if os.path.isdir(dir):
    options = [os.path.basename(f) for f in glob.glob(dir + '/.*')]
    files = [os.path.basename(f) for f in glob.glob(dir + '/' + name + '.*')]
    if len(files) >= 1:
      return [options, dir, files[0]]
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
@jinja2_view('404.html')
def error404(error):
  return dict()

@route('/static/<filepath:path>')
def serve_static(filepath):
  return static_file(filepath, root='./static')

@route('/')
@jinja2_view('home.html')
def get_home():
  if 'types' in cache:
    types = cache['types']
  else:
    types = list_types()
    cache['types'] = types
  return dict(types=types)

@route('/<type:re:[a-zA-Z]+/?>')
@jinja2_view('listing.html')
def get_type(type):
  type = type.replace('/', '')

  if 'files.' + type in cache:
    files = cache['files.' + type]
  else:
    files = list_files(type)
    cache['files.' + type] = files

  if files:
    return dict(type=type, files=files)
  else:
    abort(404, 'Category not found')

@route('/<type:re:[a-zA-Z]+>/<name:re:[a-zA-Z-]+>')
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

if __name__ == '__main__':
  waitress.serve(bottle.default_app())
else:
  waitress.serve(bottle.default_app(), unix_socket='/tmp/quickstart.sock')