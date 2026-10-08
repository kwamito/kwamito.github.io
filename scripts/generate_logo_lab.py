"""Generate ten editable, animated SVG identity studies for Nana Kwame."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public" / "logo-lab"
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

INK = "#18352d"
GREEN = "#238463"
MINT = "#a9dfc3"
GOLD = "#c49a53"


def svg(slug, title, category, artwork, width=680, height=400, css=""):
    base_css = f"""
      .ink{{fill:{INK}}}.green{{fill:{GREEN}}}.mint{{fill:{MINT}}}.gold{{fill:{GOLD}}}
      .stroke-ink{{stroke:{INK}}}.stroke-green{{stroke:{GREEN}}}.stroke-gold{{stroke:{GOLD}}}
      .move,.draw,.spin,.pulse{{transform-box:fill-box;transform-origin:center;transition:transform .65s cubic-bezier(.2,.8,.2,1),opacity .45s ease,stroke-dashoffset 1s ease}}
      svg:hover .move{{transform:translateY(-7px)}}
      svg:hover .spin{{transform:rotate(24deg)}}
      svg:hover .pulse{{transform:scale(1.12)}}
      svg:hover .draw{{stroke-dashoffset:0!important}}
      @media (prefers-reduced-motion:reduce){{.move,.draw,.spin,.pulse{{transition:none!important}}}}
      {css}
    """
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{slug}-title {slug}-desc">
<title id="{slug}-title">{title}</title><desc id="{slug}-desc">Interactive {category} logo concept for Nana Kwame. Hover to see subtle motion.</desc>
<style>{base_css}</style>
{artwork}
</svg>'''
    (ASSETS / f"{slug}.svg").write_text(content)
    return dict(slug=slug, title=title, category=category, svg=content)


logos = []

# Initials: each has a different construction, not merely a font swap.
logos.append(svg("nk-01-signal", "Signal", "initials", f'''
<g class="move" fill="none" stroke="{INK}" stroke-width="24" stroke-linecap="square" stroke-linejoin="miter">
 <path d="M178 282V118L289 282V118"/><path d="M365 118V282M476 118L365 211L484 282"/>
</g>
<path class="draw" d="M210 96H302V157" fill="none" stroke="{GREEN}" stroke-width="8" stroke-dasharray="154" stroke-dashoffset="154"/>
<circle class="green pulse" cx="302" cy="96" r="12"/><circle class="green pulse" cx="502" cy="282" r="11"/>
'''))

logos.append(svg("nk-02-orbit", "Orbit", "initials", f'''
<circle cx="340" cy="200" r="130" fill="none" stroke="{MINT}" stroke-width="2"/>
<path class="spin" d="M340 70A130 130 0 0 1 463 159" fill="none" stroke="{GREEN}" stroke-width="12" stroke-linecap="round"/>
<text x="340" y="237" text-anchor="middle" class="ink" font-family="Georgia,serif" font-size="111" font-weight="700" letter-spacing="-15">NK</text>
<circle class="gold pulse" cx="467" cy="159" r="10"/><path d="M262 283H418" stroke="{GREEN}" stroke-width="3"/>
'''))

logos.append(svg("nk-03-stack", "Stack", "initials", f'''
<g class="move"><rect x="182" y="89" width="316" height="222" rx="24" fill="{INK}"/>
<path d="M222 264V137L314 264V137" fill="none" stroke="#f2f6ef" stroke-width="21" stroke-linejoin="round"/>
<path d="M370 137V264M460 137L370 211L465 264" fill="none" stroke="{MINT}" stroke-width="21" stroke-linejoin="round"/>
<path d="M182 272H498" stroke="{GREEN}" stroke-width="10"/></g>
'''))

logos.append(svg("nk-04-ligature", "Ligature", "initials", f'''
<g fill="none" stroke="{INK}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round" class="move">
<path d="M161 288V112L286 288V112"/><path d="M286 205H371M371 112V288M371 208L490 112M371 208L490 288"/>
</g><path class="draw" d="M160 318H494" stroke="{GOLD}" stroke-width="5" stroke-dasharray="334" stroke-dashoffset="334"/>
<circle class="gold pulse" cx="286" cy="112" r="9"/>
'''))

logos.append(svg("nk-05-facet", "Facet", "initials", f'''
<path class="spin" d="M340 55L485 200L340 345L195 200Z" fill="none" stroke="{GREEN}" stroke-width="5"/>
<path d="M246 259V141L315 259V141" fill="none" stroke="{INK}" stroke-width="17" stroke-linejoin="bevel"/>
<path d="M369 141V259M443 141L369 207L446 259" fill="none" stroke="{INK}" stroke-width="17" stroke-linejoin="bevel"/>
<path d="M340 55L383 98" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/><circle class="gold pulse" cx="340" cy="55" r="8"/>
'''))

# Full-name signatures are composed to work as horizontal marks.
logos.append(svg("name-01-editorial", "Editorial", "full name", f'''
<text x="340" y="203" text-anchor="middle" class="ink move" font-family="Georgia,serif" font-size="82" font-weight="700" letter-spacing="-5">Nana Kwame</text>
<path class="draw" d="M115 230H565" fill="none" stroke="{GREEN}" stroke-width="4" stroke-dasharray="450" stroke-dashoffset="450"/>
<text x="340" y="269" text-anchor="middle" class="green" font-family="Arial,sans-serif" font-size="16" letter-spacing="9">ENGINEER · MAKER</text>
'''))

logos.append(svg("name-02-terminal", "Terminal", "full name", f'''
<rect x="83" y="105" width="514" height="190" rx="18" fill="none" stroke="{INK}" stroke-width="4"/>
<circle class="green pulse" cx="119" cy="137" r="7"/><circle cx="143" cy="137" r="7" fill="{MINT}"/>
<path d="M83 162H597" stroke="{INK}" stroke-width="3"/>
<text x="116" y="237" class="green" font-family="Menlo,monospace" font-size="54" font-weight="700">&gt;</text>
<text x="161" y="237" class="ink move" font-family="Menlo,monospace" font-size="46" font-weight="700" letter-spacing="-3">nana_kwame</text>
<rect class="pulse" x="510" y="246" width="28" height="5" fill="{GREEN}"/>
'''))

logos.append(svg("name-03-axis", "Axis", "full name", f'''
<path d="M122 98V304" stroke="{GREEN}" stroke-width="7"/>
<text x="150" y="184" class="ink move" font-family="Arial,sans-serif" font-size="83" font-weight="800" letter-spacing="-7">NANA</text>
<text x="150" y="271" class="ink move" font-family="Arial,sans-serif" font-size="83" font-weight="800" letter-spacing="-7">KWAME</text>
<path class="draw" d="M475 112L557 112L557 194" fill="none" stroke="{GOLD}" stroke-width="5" stroke-dasharray="164" stroke-dashoffset="164"/>
'''))

logos.append(svg("name-04-keystone", "Keystone", "full name", f'''
<path class="spin" d="M142 143L198 200L142 257L86 200Z" fill="{INK}"/>
<path d="M117 226V175L141 226V175M160 175V226M181 175L160 203L182 226" fill="none" stroke="{MINT}" stroke-width="5"/>
<text x="225" y="202" class="ink move" font-family="Georgia,serif" font-size="58" font-weight="700" letter-spacing="-3">Nana Kwame</text>
<text x="229" y="239" class="green" font-family="Arial,sans-serif" font-size="14" letter-spacing="5">BUILT WITH INTENT</text>
'''))

logos.append(svg("name-05-current", "Current", "full name", f'''
<text x="340" y="212" text-anchor="middle" class="ink move" font-family="Arial,sans-serif" font-size="78" font-weight="300" letter-spacing="-5">nana<tspan font-weight="700">kwame</tspan></text>
<path class="draw" d="M123 251H557" stroke="{GREEN}" stroke-width="5" stroke-dasharray="434" stroke-dashoffset="434"/>
<circle class="gold pulse" cx="558" cy="251" r="9"/>
<text x="340" y="292" text-anchor="middle" class="green" font-family="Arial,sans-serif" font-size="14" letter-spacing="7">DESIGN · SYSTEMS · CODE</text>
'''))

cards = "\n".join(f'''<article class="card" data-type="{item['category']}">
  <button class="art" type="button" aria-label="Enlarge {item['title']} logo" data-open="{item['slug']}">{item['svg']}</button>
  <div class="card-bottom"><div><span class="index">{i:02d} / {item['category'].upper()}</span><h3>{item['title']}</h3></div>
  <div class="actions"><a href="/logo-lab/assets/{item['slug']}.svg" download aria-label="Download {item['title']} SVG">SVG ↓</a><a href="/logo-lab/assets/{item['slug']}.png" download aria-label="Download {item['title']} PNG">PNG ↓</a></div></div>
</article>''' for i, item in enumerate(logos, 1))

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Nana Kwame — Logo Lab</title>
<style>
:root{{--bg:#f2f4ef;--surface:#fff;--text:#18352d;--muted:#658075;--line:#dce5dd}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--text);font-family:Arial,sans-serif}}
button,a{{font:inherit}}button{{cursor:pointer}}a{{color:inherit;text-decoration:none}}
.wrap{{max-width:1460px;margin:auto;padding:0 34px}}header{{display:flex;justify-content:space-between;align-items:center;padding-top:32px;padding-bottom:32px;border-bottom:1px solid var(--line)}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800;letter-spacing:-.03em}}.brandmark{{display:grid;place-items:center;width:36px;height:36px;background:#18352d;color:#b0e4c7;border-radius:11px;font-size:14px;letter-spacing:-.08em}}
.back{{font-size:13px;color:var(--muted)}}.back:hover{{color:var(--text)}}main{{padding-bottom:85px}}.hero{{padding-top:62px;padding-bottom:38px;display:flex;align-items:end;justify-content:space-between;gap:25px}}
.eyebrow,.index{{font-size:11px;font-weight:700;letter-spacing:.16em;color:#238463}}h1{{font-size:clamp(48px,7vw,100px);line-height:.92;letter-spacing:-.075em;margin:18px 0 20px;font-weight:700}}.lede{{max-width:510px;color:#5a7065;font-size:17px;line-height:1.55;margin:0}}
.hero-note{{font-size:12px;line-height:1.65;color:#6e8479;max-width:230px;text-align:right}}.toolbar{{position:sticky;top:0;z-index:4;background:color-mix(in srgb,var(--bg) 94%,transparent);backdrop-filter:blur(18px);display:flex;justify-content:space-between;gap:18px;padding:20px 0;border-bottom:1px solid var(--line);flex-wrap:wrap}}
.filters,.controls{{display:flex;align-items:center;gap:8px;flex-wrap:wrap}}.chip{{background:transparent;border:1px solid var(--line);border-radius:100px;padding:9px 17px;color:var(--muted);font-size:12px;font-weight:700}}.chip.active{{background:#18352d;color:#fff;border-color:#18352d}}.controls label{{font-size:12px;color:var(--muted);margin-right:5px}}.swatch{{width:25px;height:25px;border-radius:50%;border:2px solid var(--bg);outline:1px solid var(--line);padding:0}}.swatch.active{{outline:2px solid #238463}}.swatch[data-surface=light]{{background:#fff}}.swatch[data-surface=dark]{{background:#10231d}}.swatch[data-surface=paper]{{background:#ebddc4}}.motion{{margin-left:15px}}
.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;padding-top:26px}}.card{{background:var(--surface);border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:0 8px 28px #17352708}}.card[hidden]{{display:none}}.art{{display:block;width:100%;height:310px;border:0;background:var(--art-bg,#fff);padding:16px;transition:background .3s}}.art svg{{width:100%;height:100%;display:block;transition:transform .5s cubic-bezier(.2,.8,.2,1)}}.art:hover svg{{transform:scale(1.045)}}.card-bottom{{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:20px 23px;border-top:1px solid var(--line)}}h3{{font-size:21px;letter-spacing:-.04em;margin:5px 0 0}}.actions{{display:flex;gap:8px}}.actions a,.actions button{{border:1px solid var(--line);border-radius:8px;background:transparent;padding:9px 11px;font-size:11px;font-weight:700;white-space:nowrap}}.actions a:hover,.actions button:hover{{border-color:#238463;color:#238463}}.pause .art svg *{{transition:none!important;animation:none!important}}
body[data-surface=dark] .art svg .ink,body[data-surface=dark] .dialog-art svg .ink{{fill:#ecf5ef}}body[data-surface=dark] .art svg .stroke-ink,body[data-surface=dark] .dialog-art svg .stroke-ink{{stroke:#ecf5ef}}body[data-surface=dark] .art svg path[stroke="#18352d"],body[data-surface=dark] .dialog-art svg path[stroke="#18352d"]{{stroke:#ecf5ef}}body[data-surface=dark] .art svg rect[stroke="#18352d"],body[data-surface=dark] .dialog-art svg rect[stroke="#18352d"]{{stroke:#ecf5ef}}
body[data-surface=dark] .art svg .green,body[data-surface=dark] .dialog-art svg .green{{fill:#9ddfbd}}body[data-surface=dark] .art svg path[fill="#18352d"],body[data-surface=dark] .dialog-art svg path[fill="#18352d"]{{fill:#238463}}
footer{{padding:30px 0 55px;color:var(--muted);font-size:12px;border-top:1px solid var(--line)}}dialog{{border:0;border-radius:22px;padding:0;box-shadow:0 25px 100px #0a201766;max-width:min(900px,92vw);width:100%;overflow:hidden}}dialog::backdrop{{background:#0a1e19ae;backdrop-filter:blur(5px)}}.dialog-head{{display:flex;justify-content:space-between;align-items:center;padding:15px 20px;border-bottom:1px solid #e0e8e1}}.dialog-head button{{border:0;background:none;font-size:24px;line-height:1}}.dialog-art{{height:min(60vh,520px);display:grid;place-items:center;background:var(--art-bg,#fff)}}.dialog-art svg{{width:100%;height:100%}}
@media(max-width:760px){{.wrap{{padding:0 18px}}.hero{{padding-top:42px;display:block}}.hero-note{{text-align:left;margin-top:26px}}.grid{{grid-template-columns:1fr;gap:15px}}.art{{height:250px}}.toolbar{{position:static}}.controls{{width:100%}}.card-bottom{{padding:17px}}.actions a,.actions button{{padding:8px}}}}
</style></head><body><header class="wrap"><a class="brand" href="/"><span class="brandmark">NK</span>Nana Kwame</a><a class="back" href="/">↖ Back to portfolio</a></header>
<main class="wrap"><section class="hero"><div><div class="eyebrow">IDENTITY EXPLORATIONS / 2026</div><h1>Logo<br><em style="font-family:Georgia,serif;font-weight:400">lab.</em></h1><p class="lede">Ten directions for Nana Kwame. Explore five monograms and five full-name marks, then take the editable vectors into Inkscape.</p></div><p class="hero-note">Hover to see each mark respond.<br>Tap a concept for a larger view.<br>Download SVG or transparent PNG.</p></section>
<div class="toolbar"><div class="filters" role="group" aria-label="Filter logos"><button class="chip active" data-filter="all" aria-pressed="true">All 10</button><button class="chip" data-filter="initials" aria-pressed="false">NK initials</button><button class="chip" data-filter="full name" aria-pressed="false">Full name</button></div><div class="controls"><label>Preview on</label><button class="swatch active" data-surface="light" title="White background" aria-label="White background" aria-pressed="true"></button><button class="swatch" data-surface="dark" title="Dark background" aria-label="Dark background" aria-pressed="false"></button><button class="swatch" data-surface="paper" title="Warm paper background" aria-label="Warm paper background" aria-pressed="false"></button><button class="chip motion" id="motion" aria-pressed="false">Pause motion</button></div></div>
<section class="grid" aria-label="Logo concepts">{cards}</section></main><footer class="wrap">Designed for Nana Kwame · Editable SVG files · Hover motion respects reduced-motion settings</footer>
<dialog id="zoom"><div class="dialog-head"><strong id="zoom-title"></strong><button id="close" aria-label="Close preview">×</button></div><div class="dialog-art" id="zoom-art"></div></dialog>
<script>
const root=document.documentElement, dialog=document.querySelector('#zoom');
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{{
 document.querySelectorAll('[data-filter]').forEach(b=>{{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',b===button)}});
 document.querySelectorAll('.card').forEach(card=>card.hidden=button.dataset.filter!=='all'&&card.dataset.type!==button.dataset.filter);
}}));
document.querySelectorAll('[data-surface]').forEach(button=>button.addEventListener('click',()=>{{
 const colors={{light:'#fff',dark:'#10231d',paper:'#ebddc4'}};root.style.setProperty('--art-bg',colors[button.dataset.surface]);document.body.dataset.surface=button.dataset.surface;
 document.querySelectorAll('[data-surface]').forEach(b=>{{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',b===button)}});
}}));
document.querySelector('#motion').addEventListener('click',e=>{{const on=document.body.classList.toggle('pause');e.currentTarget.textContent=on?'Play motion':'Pause motion';e.currentTarget.setAttribute('aria-pressed',on)}});
document.querySelectorAll('[data-open]').forEach(button=>button.addEventListener('click',()=>{{document.querySelector('#zoom-title').textContent=button.closest('.card').querySelector('h3').textContent;document.querySelector('#zoom-art').replaceChildren(button.querySelector('svg').cloneNode(true));dialog.showModal()}}));
document.querySelector('#close').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{{if(e.target===dialog)dialog.close()}});
</script></body></html>'''

PAGE = Path(__file__).resolve().parents[1] / "src" / "logo-lab-gallery.html"
PAGE.write_text(html)
old_page = ROOT / "index.html"
if old_page.exists():
    old_page.unlink()
print(f"Generated {len(logos)} SVGs and {PAGE}")
