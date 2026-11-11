import json,glob,re,sys
p='findings_data.js'
s=open(p,encoding='utf8').read()
pre=s[:s.find('{')];post=s[s.rfind('}')+1:]
d=json.loads(s[s.find('{'):s.rfind('}')+1])
dele=json.load(open('rewrite/delete.json',encoding='utf8'))
rw={}
for f in sorted(glob.glob('rewrite/c*.json')): rw.update(json.load(open(f,encoding='utf8')))
n=0
for f in d['findings']:
    if f['id'] in rw:
        f['name'],f['rec']=rw[f['id']]; f['reworded']=True; n+=1
    for k in ('name','rec','std'):
        if f.get(k): f[k]=re.sub(r'[ \t]{2,}',' ',f[k]).strip()
before=len(d['findings'])
d['findings']=[f for f in d['findings'] if f['id'] not in dele]
open(p,'w',encoding='utf8').write(pre+json.dumps(d,ensure_ascii=False,indent=2)+post)
print('reworded',n,'deleted',before-len(d['findings']),'total',len(d['findings']))
