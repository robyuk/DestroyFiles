from pathlib import Path

rootdir=Path('destination')

for path in rootdir.glob('*.txt'):
  with open(path, 'wb') as file:
    file.write(b'') # Not sure this destroys a file
  path.unlink()