from pathlib import Path

rootdir=Path('destination')

for path in rootdir.glob('*.txt'):
  with open(path, 'wb') as file:
    file.write(b'')
  path.unlink()