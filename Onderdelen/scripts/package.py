from pathlib import Path
import zipfile, subprocess, sys
root=Path(__file__).resolve().parents[2]
output=Path(sys.argv[1])
tracked=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
 for name in tracked:
  if not name or name.startswith('.'):continue
  source=root/name
  if not source.is_file():continue
  target=name if name.startswith(('Onderdelen/','Schrijftafel/')) or name=='▶ Begin hier.html' else 'Onderdelen/Documentatie/'+name
  archive.write(source,'schrijftafel/'+target)
with zipfile.ZipFile(output) as archive:
 assert archive.testzip() is None
 assert {n.split('/')[1] for n in archive.namelist()}=={'▶ Begin hier.html','Onderdelen','Schrijftafel'}
print(output)
