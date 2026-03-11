#!/usr/bin/env python3
"""
JE Labs Deck Setup Script
=========================
This script prepares your slide HTML files for the web presentation.

Usage:
  1. Place all your slide HTML files in a folder called 'raw_slides/'
     in the same directory as this script.
  2. Name them in order: slide_cover.html, slide_toc.html, slide_who_we_are.html, etc.
     OR just number them: 01.html, 02.html, ..., 17.html
  3. Run: python3 setup.py
  4. The 'dist/' folder will contain your deployment-ready website.

The script will:
  - Copy slides to dist/slides/ as slide-0.html through slide-16.html
  - Inject keyboard navigation support into each slide
  - Generate the presentation shell (index.html)
"""

import os, sys, shutil, glob, re

TOTAL_SLIDES = 17
DIST_DIR = "dist"
SLIDES_DIR = os.path.join(DIST_DIR, "slides")

KEY_INJECT = '''<script>
document.addEventListener("keydown",function(e){
  if(e.key==="ArrowRight"||e.key==="ArrowDown"||e.key===" "){
    e.preventDefault();window.parent.postMessage("next","*");
  } else if(e.key==="ArrowLeft"||e.key==="ArrowUp"){
    e.preventDefault();window.parent.postMessage("prev","*");
  }
});
</script>'''

def find_slide_files(src_dir):
    """Find and sort HTML files from source directory."""
    patterns = ['*.html', '*.htm']
    files = []
    for p in patterns:
        files.extend(glob.glob(os.path.join(src_dir, p)))
    
    # Sort: try numeric sorting first
    def sort_key(f):
        name = os.path.basename(f)
        nums = re.findall(r'\d+', name)
        return int(nums[0]) if nums else name
    
    files.sort(key=sort_key)
    return files

def inject_keyboard_support(html_content):
    """Inject keyboard event forwarding for iframe communication."""
    if '</body>' in html_content:
        return html_content.replace('</body>', KEY_INJECT + '\n</body>')
    return html_content + KEY_INJECT

def generate_index_html():
    """Generate the main presentation shell."""
    slide_frames = []
    for i in range(TOTAL_SLIDES):
        active = ' active' if i == 0 else ''
        slide_frames.append(f'    <div class="slide{active}" id="slide-{i}">\n'
                          f'      <iframe src="slides/slide-{i}.html" frameborder="0" scrolling="no"\n'
                          f'              style="width:1280px;height:720px;border:none;pointer-events:auto;display:block;"></iframe>\n'
                          f'    </div>')

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>JE Labs — Strategic Growth Partner for Frontier Tech Builders</title>
<meta name="description" content="JE Labs: Integrated Growth Command Center for AI, Web3, and frontier tech ventures."/>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⚡</text></svg>"/>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet"/>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100%;height:100%;background:#000;overflow:hidden;font-family:'Noto Sans KR',sans-serif}}

#vp{{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:#000;padding-bottom:56px}}
#wr{{width:1280px;height:720px;position:relative;transform-origin:center center}}

.slide{{
  position:absolute;inset:0;width:1280px;height:720px;
  opacity:0;pointer-events:none;
  transition:opacity 0.5s ease,transform 0.5s ease;
  transform:scale(0.96);overflow:hidden;background:#000;
}}
.slide.active{{opacity:1;pointer-events:auto;transform:scale(1);z-index:10}}

#pb{{position:fixed;top:0;left:0;right:0;height:3px;background:#111;z-index:9999}}
#pf{{height:100%;background:#00F5B8;transition:width 0.4s ease;box-shadow:0 0 8px rgba(0,245,184,0.5)}}

#nav{{
  position:fixed;bottom:0;left:0;right:0;height:56px;
  background:rgba(0,0,0,0.92);backdrop-filter:blur(12px);
  border-top:1px solid #222;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 20px;z-index:9999;
}}
.nb{{
  background:none;border:1px solid #333;color:#888;
  padding:8px 14px;cursor:pointer;font-size:12px;
  font-family:monospace;letter-spacing:0.06em;
  transition:all 0.2s;border-radius:4px;white-space:nowrap;
}}
.nb:hover{{border-color:#00F5B8;color:#00F5B8}}
.nb:disabled{{opacity:0.25;cursor:default}}
.nb:disabled:hover{{border-color:#333;color:#555}}

#ct{{color:#666;font-family:monospace;font-size:13px;letter-spacing:0.1em;min-width:70px;text-align:center}}
#ct span{{color:#00F5B8}}

#dt{{display:flex;gap:5px;align-items:center}}
.dot{{width:7px;height:7px;border-radius:50%;background:#333;cursor:pointer;transition:all 0.25s;border:none;padding:0}}
.dot.on{{background:#00F5B8;box-shadow:0 0 6px rgba(0,245,184,0.6);transform:scale(1.4)}}
.dot:hover{{background:#555}}

#fs{{
  background:none;border:1px solid #333;color:#666;
  width:34px;height:34px;display:flex;align-items:center;justify-content:center;
  cursor:pointer;border-radius:4px;transition:all 0.2s;font-size:13px;
}}
#fs:hover{{border-color:#00F5B8;color:#00F5B8}}

#hi{{
  position:fixed;bottom:66px;left:50%;transform:translateX(-50%);
  color:#444;font-size:11px;font-family:monospace;letter-spacing:0.1em;
  z-index:9999;animation:fo 5s forwards;pointer-events:none;
}}
@keyframes fo{{0%,60%{{opacity:1}}100%{{opacity:0}}}}
@media(max-width:700px){{#dt{{display:none}}.nb{{padding:6px 10px;font-size:11px}}}}
</style>
</head>
<body>
<div id="pb"><div id="pf" style="width:0%"></div></div>
<div id="vp"><div id="wr">
{chr(10).join(slide_frames)}
</div></div>
<div id="nav">
  <button class="nb" id="pv" disabled><i class="fa-solid fa-arrow-left"></i> PREV</button>
  <div id="dt"></div>
  <div id="ct"><span>1</span> / {TOTAL_SLIDES}</div>
  <button class="nb" id="nx">NEXT <i class="fa-solid fa-arrow-right"></i></button>
  <button id="fs" title="Fullscreen (F)"><i class="fa-solid fa-expand"></i></button>
</div>
<div id="hi">← ARROW KEYS / SWIPE / CLICK EDGES →</div>
<script>
const T={TOTAL_SLIDES};let c=0;
function go(n){{if(n<0||n>=T||n===c)return;document.querySelectorAll('.slide')[c].classList.remove('active');document.querySelectorAll('.slide')[n].classList.add('active');c=n;ui()}}
function ui(){{
  document.getElementById('ct').innerHTML='<span>'+(c+1)+'</span> / '+T;
  document.getElementById('pf').style.width=(c/(T-1)*100)+'%';
  document.getElementById('pv').disabled=c===0;
  document.getElementById('nx').disabled=c===T-1;
  document.querySelectorAll('.dot').forEach((d,i)=>d.classList.toggle('on',i===c));
}}
// Dots
(function(){{const el=document.getElementById('dt');for(let i=0;i<T;i++){{const d=document.createElement('button');d.className='dot'+(i===0?' on':'');d.onclick=()=>go(i);el.appendChild(d)}}}})();
// Buttons
document.getElementById('pv').onclick=()=>go(c-1);
document.getElementById('nx').onclick=()=>go(c+1);
// Keyboard
document.addEventListener('keydown',e=>{{
  if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key===' '){{e.preventDefault();go(c+1)}}
  else if(e.key==='ArrowLeft'||e.key==='ArrowUp'){{e.preventDefault();go(c-1)}}
  else if(e.key==='Home')go(0);else if(e.key==='End')go(T-1);
  else if(e.key==='f'||e.key==='F')tf();
}});
// Iframe keyboard forwarding
window.addEventListener('message',function(e){{if(e.data==='next')go(c+1);else if(e.data==='prev')go(c-1)}});
// Touch
let tx=0;
document.addEventListener('touchstart',e=>{{tx=e.touches[0].clientX}});
document.addEventListener('touchend',e=>{{const d=e.changedTouches[0].clientX-tx;if(Math.abs(d)>50){{d<0?go(c+1):go(c-1)}}}});
// Click edges
document.getElementById('vp').addEventListener('click',e=>{{if(e.target.closest('#nav')||e.target.closest('button'))return;const x=e.clientX;if(x<window.innerWidth*0.25)go(c-1);else if(x>window.innerWidth*0.75)go(c+1)}});
// Scale
function sc(){{const vw=window.innerWidth,vh=window.innerHeight-56;document.getElementById('wr').style.transform='scale('+Math.min(vw/1280,vh/720,2)+')'}}
window.addEventListener('resize',sc);sc();
// Fullscreen
function tf(){{if(!document.fullscreenElement)document.documentElement.requestFullscreen().catch(()=>{{}});else document.exitFullscreen()}}
document.getElementById('fs').onclick=tf;
ui();
</script>
</body>
</html>'''


def main():
    src_dir = "raw_slides"
    
    if not os.path.isdir(src_dir):
        print(f"❌ '{src_dir}/' directory not found.")
        print(f"   Create it and place your 17 slide HTML files inside.")
        print(f"   Then run this script again.")
        sys.exit(1)
    
    files = find_slide_files(src_dir)
    
    if len(files) != TOTAL_SLIDES:
        print(f"⚠️  Found {len(files)} HTML files, expected {TOTAL_SLIDES}.")
        if len(files) == 0:
            print(f"   Place your slide HTML files in '{src_dir}/'")
            sys.exit(1)
        print(f"   Proceeding with {len(files)} slides...")
    
    # Create dist structure
    os.makedirs(SLIDES_DIR, exist_ok=True)
    
    # Process slides
    for i, filepath in enumerate(files[:TOTAL_SLIDES]):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = inject_keyboard_support(content)
        
        dest = os.path.join(SLIDES_DIR, f"slide-{i}.html")
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ {os.path.basename(filepath)} → slide-{i}.html")
    
    # Generate index.html
    actual_total = min(len(files), TOTAL_SLIDES)
    global TOTAL_SLIDES
    TOTAL_SLIDES = actual_total
    
    index_content = generate_index_html()
    index_path = os.path.join(DIST_DIR, "index.html")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"\n🎉 Done! Your presentation is ready in '{DIST_DIR}/'")
    print(f"   Open '{DIST_DIR}/index.html' in a browser to preview.")
    print(f"\n📦 To deploy:")
    print(f"   • Netlify: drag & drop the '{DIST_DIR}/' folder at app.netlify.com/drop")
    print(f"   • Vercel: npx vercel {DIST_DIR}/")
    print(f"   • GitHub Pages: push '{DIST_DIR}/' contents to a repo, enable Pages")


if __name__ == '__main__':
    main()
