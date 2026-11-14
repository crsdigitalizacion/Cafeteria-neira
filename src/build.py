import json,base64,glob,re
HEAD='<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="description" content="Cafetería Neira, el bar de toda la vida de Lobete, en Logroño. Calamares, vermú de grifo, menú del día y reservas.">\n</head>\n<body>\n'
t=open('plantilla.html').read(); d=json.load(open('logo-paths.json'))
def tube(path,o,g): return f'<g class="tube" data-o="{o}" data-g="{g}"><g class="glow" filter="url(#blur)"><path d="{path}"/></g><g class="core"><path d="{path}"/></g></g>'
def miny(p): return min(float(m[1]) for m in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',p))
hair=sorted(d['hair'],key=miny); line=sorted(d['line'],key=miny)
neon='<g class="hair">'+''.join(tube(p,i,'hair') for i,p in enumerate(hair))+'</g><g class="line">'+''.join(tube(p,len(hair)+i,'line') for i,p in enumerate(line))+'</g>'
frames=['data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode() for f in sorted(glob.glob('frames/f*.webp'))]
out=t.replace('{{NEON}}',neon).replace('{{VB}}',d['vb']).replace('{{FRAMESM}}',json.dumps(['data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode() for f in sorted(glob.glob('framesm/m*.webp'))])).replace('{{FRAMES}}',json.dumps(frames))
for n in ['parrillada','huevos','tabla','hamburguesa','estofado','ensalada','logo','logo-m','fachada-wide']:
    out=out.replace('{{%s}}'%n,'data:image/jpeg;base64,'+base64.b64encode(open(f'img/{n}-v2.jpg' if n in ('parrillada','huevos','tabla','hamburguesa','estofado','ensalada') else f'img/{n}.jpg','rb').read()).decode())
assert '{{' not in out, re.findall(r'\{\{[\w-]+\}\}',out)
open('../index.html','w').write(HEAD+out+'\n</body>\n</html>\n')
print(len(out)//1024,'KB')
