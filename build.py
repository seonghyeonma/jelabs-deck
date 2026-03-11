#!/usr/bin/env python3
"""
Build script that creates the final index.html for JE Labs deck.
Each slide is an individual HTML file loaded via iframe.
"""
import os, json

TOTAL = 17
SLIDE_DIR = "slides"

# Generate the main index.html
def build():
    slide_frames = []
    for i in range(TOTAL):
        active = ' active' if i == 0 else ''
        slide_frames.append(f'''    <div class="slide{active}" id="slide-{i}">
      <iframe src="{SLIDE_DIR}/slide-{i}.html" frameborder="0" scrolling="no" 
              style="width:1280px;height:720px;border:none;pointer-events:auto;display:block;"></iframe>
    </div>''')

    dots_init = "createDots();"
    
    index_html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>JE Labs — Strategic Growth Partner for Frontier Tech Builders</title>
<meta name="description" content="JE Labs pitch deck: Integrated Growth Command Center for AI, Web3, and frontier tech ventures."/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet"/>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:100%;height:100%;background:#000;overflow:hidden;font-family:'Noto Sans KR',sans-serif}}

#deck-viewport{{
  position:fixed;inset:0;
  display:flex;align-items:center;justify-content:center;
  background:#000;
  padding-bottom:56px; /* nav bar */
}}

#slides-wrapper{{
  width:1280px;height:720px;
  position:relative;
  transform-origin:center center;
}}

.slide{{
  position:absolute;inset:0;
  width:1280px;height:720px;
  opacity:0;pointer-events:none;
  transition:opacity 0.45s ease,transform 0.45s ease;
  transform:scale(0.97);
  overflow:hidden;background:#000;
}}
.slide.active{{
  opacity:1;pointer-events:auto;
  transform:scale(1);z-index:10;
}}

/* Progress */
#progress-bg{{position:fixed;top:0;left:0;right:0;height:3px;background:#111;z-index:9999}}
#progress{{height:100%;background:#00F5B8;transition:width 0.4s ease;box-shadow:0 0 8px rgba(0,245,184,0.5)}}

/* Nav bar */
#nav{{
  position:fixed;bottom:0;left:0;right:0;height:56px;
  background:rgba(0,0,0,0.9);backdrop-filter:blur(12px);
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
.nb:disabled{{opacity:0.25;cursor:default;border-color:#333;color:#555}}
.nb:disabled:hover{{border-color:#333;color:#555}}

#counter{{color:#666;font-family:monospace;font-size:13px;letter-spacing:0.1em;min-width:70px;text-align:center}}
#counter span{{color:#00F5B8}}

#dots{{display:flex;gap:5px;align-items:center}}
.dot{{
  width:7px;height:7px;border-radius:50%;background:#333;
  cursor:pointer;transition:all 0.25s;border:none;padding:0;
}}
.dot.on{{background:#00F5B8;box-shadow:0 0 6px rgba(0,245,184,0.6);transform:scale(1.4)}}
.dot:hover{{background:#555}}

#fs{{
  background:none;border:1px solid #333;color:#666;
  width:34px;height:34px;display:flex;align-items:center;justify-content:center;
  cursor:pointer;border-radius:4px;transition:all 0.2s;font-size:13px;
}}
#fs:hover{{border-color:#00F5B8;color:#00F5B8}}

/* Keyboard shortcut hint */
#hint{{
  position:fixed;bottom:66px;left:50%;transform:translateX(-50%);
  color:#444;font-size:11px;font-family:monospace;letter-spacing:0.1em;
  z-index:9999;animation:fo 5s forwards;pointer-events:none;
}}
@keyframes fo{{0%,60%{{opacity:1}}100%{{opacity:0}}}}

/* Responsive: hide dots on very small screens */
@media(max-width:600px){{
  #dots{{display:none}}
  .nb{{padding:6px 10px;font-size:11px}}
}}
</style>
</head>
<body>

<div id="progress-bg"><div id="progress" style="width:0%"></div></div>

<div id="deck-viewport">
  <div id="slides-wrapper">
{chr(10).join(slide_frames)}
  </div>
</div>

<div id="nav">
  <button class="nb" id="pb" disabled><i class="fa-solid fa-arrow-left"></i> PREV</button>
  <div id="dots"></div>
  <div id="counter"><span>1</span> / {TOTAL}</div>
  <button class="nb" id="nb">NEXT <i class="fa-solid fa-arrow-right"></i></button>
  <button id="fs" title="Fullscreen (F)"><i class="fa-solid fa-expand"></i></button>
</div>

<div id="hint">← ARROW KEYS / SWIPE →</div>

<script>
const T={TOTAL};
let cur=0;

function go(n){{
  if(n<0||n>=T||n===cur)return;
  const sl=document.querySelectorAll('.slide');
  sl[cur].classList.remove('active');
  sl[n].classList.add('active');
  cur=n;ui();
}}

function ui(){{
  document.getElementById('counter').innerHTML='<span>'+(cur+1)+'</span> / '+T;
  document.getElementById('progress').style.width=(cur/(T-1)*100)+'%';
  document.getElementById('pb').disabled=cur===0;
  document.getElementById('nb').disabled=cur===T-1;
  document.querySelectorAll('.dot').forEach((d,i)=>d.classList.toggle('on',i===cur));
}}

// Dots
!function(){{
  const c=document.getElementById('dots');
  for(let i=0;i<T;i++){{
    const d=document.createElement('button');
    d.className='dot'+(i===0?' on':'');
    d.onclick=()=>go(i);
    c.appendChild(d);
  }}
}}();

// Buttons
document.getElementById('pb').onclick=()=>go(cur-1);
document.getElementById('nb').onclick=()=>go(cur+1);

// Keyboard
document.addEventListener('keydown',e=>{{
  if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key===' '){{e.preventDefault();go(cur+1)}}
  else if(e.key==='ArrowLeft'||e.key==='ArrowUp'){{e.preventDefault();go(cur-1)}}
  else if(e.key==='Home')go(0);
  else if(e.key==='End')go(T-1);
  else if(e.key==='f'||e.key==='F')tf();
}});

// Also listen for keyboard events from iframes
window.addEventListener('message',function(e){{
  if(e.data==='next')go(cur+1);
  else if(e.data==='prev')go(cur-1);
}});

// Touch
let tx=0;
document.addEventListener('touchstart',e=>{{tx=e.touches[0].clientX}});
document.addEventListener('touchend',e=>{{
  const d=e.changedTouches[0].clientX-tx;
  if(Math.abs(d)>50){{d<0?go(cur+1):go(cur-1)}}
}});

// Scale
function sc(){{
  const vw=window.innerWidth,vh=window.innerHeight-56;
  const s=Math.min(vw/1280,vh/720,2);
  document.getElementById('slides-wrapper').style.transform='scale('+s+')';
}}
window.addEventListener('resize',sc);sc();

// Fullscreen
function tf(){{
  if(!document.fullscreenElement)document.documentElement.requestFullscreen().catch(()=>{{}});
  else document.exitFullscreen();
}}
document.getElementById('fs').onclick=tf;

ui();
</script>
</body>
</html>'''

    with open('/home/claude/jelabs-deck/index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print("✅ index.html generated")

build()
