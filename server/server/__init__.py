from bottle import route, request, run, template, error, abort, static_file
import os, string, pprint

def find_file(type, name):
  """searches file within directory by name, ignoring extension"""
  dir = 'files/' + type
  options = []
  if os.path.isdir(dir):
    for root, dirs, files in os.walk(dir):
      for f in files:
        if f[0] == '.':
          options.append(f)
        else:
          splitName = string.split(f, '.')
          filename = splitName[0]
          if filename.lower() == name.lower():
            return [options, dir, f]
  return False

@route('/<type>/<name>')
def render(type, name):
  lookup = find_file(type, name)

  if lookup:
    options, dir, filename = lookup
    download = False
    if request.query_string == 'download' or request.query_string == 'dl':
      # todo: use options for download file name
      download = True
    return static_file(filename, dir, mimetype='text/plain', download=download)
  else:
    abort(404, 'File not found')

run(host='localhost', port=8080)