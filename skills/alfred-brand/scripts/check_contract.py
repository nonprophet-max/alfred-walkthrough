"""Validate the Alfred skill's portable type/spacing contract. No third-party packages."""
from pathlib import Path
import argparse,json,re,sys
sys.dont_write_bytecode=True
from build_tokens import generate
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=['hero','heading','section','component-title','lead','body','body-small','label','control','input','caption','amount']
def validate(t):
 errors=[]
 for key in ['typography','spacing','web']:
  if key not in t:errors.append(f'Missing {key} contract')
 if errors:return errors
 for name in REQUIRED:
  role=t['typography'].get(name)
  if role is None:errors.append(f'Missing type role: {name}');continue
  for key in ['font','sizePx','weight','lineHeight','trackingEm']:
   if key not in role:errors.append(f'Missing {name}.{key}')
  if role.get('font')=='display' and role.get('weight')!=400:errors.append(f'{name}: Archivo Black must be 400')
  if role.get('lineHeight',0)<=0:errors.append(f'{name}: invalid leading')
 for name in ['body','control','input']:
  role=t['typography'].get(name,{})
  if role.get('sizePx',0)<16:errors.append(f'{name}: reading/control text must be at least16px')
  if role.get('trackingEm')!=0:errors.append(f'{name}: use zero tracking')
 if t['web'].get('controlMinPx',0)<44:errors.append('Touch target must be at least44px')
 if t['spacing'].get('unitPx')!=4:errors.append('Spacing base must be4px')
 for key,value in t['spacing'].get('steps',{}).items():
  if int(key)*4!=value:errors.append(f'Invalid spacing step {key}')
 for name,face in t.get('font',{}).items():
  p=ROOT/'assets'/face.get('file','missing')
  if not p.is_file():errors.append(f'Missing bundled font: {name}')
  if name=='display' and face.get('declaredWeight')!='400':errors.append('Archivo @font-face must declare400')
 return errors
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--tokens',type=Path);args=parser.parse_args()
 t=json.loads((args.tokens or ROOT/'assets/tokens.json').read_text());errors=validate(t)
 if not args.tokens and not errors:
  for name,expected in generate().items():
   if (ROOT/'assets'/name).read_text()!=expected:errors.append('Generated CSS drift: '+name)
  for p in [ROOT/'SKILL.md',*sorted((ROOT/'references').glob('*.md'))]:
   for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
    if '://' in link or link.startswith(('#','mailto:')):continue
    target=(p.parent/link.split('#')[0]).resolve()
    if not target.exists():errors.append(f'Broken portable reference in {p.name}: {link}')
  if '--font-sans: var(--font-sans)' in (ROOT/'assets/shadcn-v4.css').read_text():errors.append('Circular font variable')
 print(json.dumps({'valid':not errors,'roles':len(t.get('typography',{})),'errors':errors},indent=2))
 sys.exit(1 if errors else 0)
