"""Generate QR codes (PNG 2000px+ and SVG): one master + one per bed.
Usage: python make_qr.py https://YOUR-USERNAME.github.io/heimtextil-2027/
Needs: pip install opencv-python numpy"""
import sys, json, math, cv2, numpy as np
BASE = (sys.argv[1] if len(sys.argv) > 1 else 'https://YOUR-USERNAME.github.io/heimtextil-2027/').rstrip('/') + '/'
def matrix(text):
    p = cv2.QRCodeEncoder_Params(); p.correction_level = cv2.QRCodeEncoder_CORRECT_LEVEL_H
    im = cv2.QRCodeEncoder.create(p).encode(text)
    d = im < 128; ys, xs = np.where(d); d = d[ys.min():ys.max()+1, xs.min():xs.max()+1]
    run = int(np.argmin(d[0]))            # first light pixel = width of 7-module finder
    m = run // 7
    return d[m//2::m, m//2::m]
def save(name, text):
    M = matrix(text); n = len(M); q = 4; s = math.ceil(2000 / (n + 2*q))
    full = np.ones((n+2*q, n+2*q), np.uint8)*255; full[q:q+n, q:q+n] = np.where(M, 0, 255)
    cv2.imwrite(f'qr/{name}.png', np.kron(full, np.ones((s, s), np.uint8)))
    rects = ''.join(f'M{x+q} {y+q}h1v1h-1z' for y in range(n) for x in range(n) if M[y, x])
    open(f'qr/{name}.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n+2*q} {n+2*q}" shape-rendering="crispEdges"><rect width="100%" height="100%" fill="#fff"/><path d="{rects}" fill="#000"/></svg>')
    ok = cv2.QRCodeDetector().detectAndDecode(cv2.imread(f'qr/{name}.png'))[0] == text
    print(('OK  ' if ok else 'FAIL'), name, text)
save('collection', BASE)
for b in json.load(open('data/products.json'))['beds']: save(b['id'], BASE + '#' + b['id'])
