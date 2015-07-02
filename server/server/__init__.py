from bottle import route, request, run, template, error, abort, static_file
import os, string, pprint

def find_file(type, name):
  """searches file within directory by name, ignoring extension and case"""
  dir = 'files/' + type
  options = []
  # todo: sanitize type and name
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

@route('/<type>/<name>')
def render(type, name):
  lookup = find_file(type, name)

  if lookup:
    options, dir, filename = lookup
    download = False
    # todo: make dl flag more concise
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

run(host='localhost', port=8080)