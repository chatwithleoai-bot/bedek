import re
# image -> (standard, part or None, section or None)
IMG={}
def parse(fn):
    b=fn.split('/')[-1].rsplit('.',1)[0]
    m=re.search(r'(1205|1555|1752|4068|5044|1918)',b)
    if not m: return None
    num=m.group(1); rest=b[m.end():]
    pm=re.match(r'_(\d)(?=_|$)',rest); part=pm.group(1) if pm else None
    if pm: rest=rest[pm.end():]
    sm=re.search(r'(?:sec_?)?((?:\d_){1,4}\d)',rest)
    sec=sm.group(1).replace('_','.') if sm else None
    return num,part,sec
def keep(f):
    img=f.get('std_image')
    if not img: return True
    p=parse(img)
    if not p: return False
    num,part,sec=p
    std=(f.get('std') or '')+' '+(f.get('name') or '')
    if num not in std: return False
    if part and not re.search(num+r'\s*(?:חלק\s*|\.)'+part,std): return False
    if sec and sec not in std: return False
    return True
