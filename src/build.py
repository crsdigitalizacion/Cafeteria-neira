# Genera la web con los recursos como archivos aparte (el móvil solo descarga su vídeo).
import json,glob,re,os,shutil,sys
OUT=sys.argv[1] if len(sys.argv)>1 else '..'                 # carpeta de la web
HTML=sys.argv[2] if len(sys.argv)>2 else '../index.html'
t=open('plantilla.html').read(); d=json.load(open('logo-paths.json'))
def tube(path,o,g): return f'<g class="tube" data-o="{o}" data-g="{g}"><g class="glow" filter="url(#blur)"><path d="{path}"/></g><g class="core"><path d="{path}"/></g></g>'
def miny(p): return min(float(m[1]) for m in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',p))
hair=sorted(d['hair'],key=miny); line=sorted(d['line'],key=miny)
neon='<g class="hair">'+''.join(tube(p,i,'hair') for i,p in enumerate(hair))+'</g><g class="line">'+''.join(tube(p,len(hair)+i,'line') for i,p in enumerate(line))+'</g>'
A=os.path.join(OUT,'a'); shutil.rmtree(A,ignore_errors=True); os.makedirs(A+'/img')
fr=[];fm=[]
for f in sorted(glob.glob('frames/f*.webp')): shutil.copy(f,A); fr.append('a/'+os.path.basename(f))
for f in sorted(glob.glob('framesm/m*.webp')): shutil.copy(f,A); fm.append('a/'+os.path.basename(f))
out=t.replace('{{NEON}}',neon).replace('{{VB}}',d['vb']).replace('{{FRAMESM}}',json.dumps(fm)).replace('{{FRAMES}}',json.dumps(fr))
for n in ['parrillada','huevos','tabla','hamburguesa','estofado','ensalada']:
    shutil.copy(f'img/{n}-v2.jpg',f'{A}/img/{n}.jpg'); out=out.replace('{{%s}}'%n,f'a/img/{n}.jpg')
for n in ['logo','logo-m','fachada-wide']:
    shutil.copy(f'img/{n}.jpg',f'{A}/img/{n}.jpg'); out=out.replace('{{%s}}'%n,f'a/img/{n}.jpg')
assert '{{' not in out, re.findall(r'\{\{[\w-]+\}\}',out)
HEAD=open('head.html').read() if os.path.exists('head.html') else ''
if HEAD: out=HEAD+out.replace('<title>Neira Se Enciende</title>','')+'\n</body>\n</html>\n'
open(HTML,'w').write(out)
tot=sum(os.path.getsize(p) for p in glob.glob(A+'/**/*',recursive=True) if os.path.isfile(p))
print('html',os.path.getsize(HTML)//1024,'KB · recursos',tot//1024,'KB ·',len(fr),'+',len(fm),'fotogramas')
