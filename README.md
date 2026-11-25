# HEIMTEXTIL 2027 · Lucky Textile Mills – 3D Bedding Collection
Mobile-first, open-source product site: 6 beds, each rotatable in 3D with 5 layers that unstack left-to-right. Hall 9.0 · Stand B-37 · Jan 12–15, 2027.

## Publish on GitHub Pages
1. Create a public repo (e.g. `heimtextil-2027`) and upload everything in this folder.
2. Settings → Pages → Deploy from branch `main` / root. Your URL: `https://<username>.github.io/heimtextil-2027/`
3. Regenerate the QR codes with your real URL (they currently hold a placeholder):
   `pip install opencv-python numpy && python make_qr.py https://<username>.github.io/heimtextil-2027/`
4. Print `qr/*.png` (2000 px+) or `qr/*.svg` (vector). `collection` = whole site; each bed has its own QR (`/#bed-id`).

## Edit content
All product data is in `data/products.json`; images in `assets/<bed-id>/` (`hero.jpg`, `l1–l5.jpg` swatch textures).
Local preview: `python -m http.server` then open http://localhost:8000
