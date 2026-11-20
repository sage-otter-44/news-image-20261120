#!/usr/bin/env python3
"""Build build.html — the 1024x1024 SVG front page for news-image-20261120.

Every story below was verified firsthand as having happened or first been
reported on FRIDAY 20 November 2026 (AP, Reuters, Al Jazeera, Axios, NYT,
NPR, NDTV, LA Times, Seoul Economic Daily, BBC Sport, ESPNcricinfo,
Rio Times, UPI, Africanews, ReliefWeb, Yahoo Finance).

Layout: masthead + UTC timeline strip + 4 illustrated lead panels (2x2)
+ 12 medium panels (4x3) + stylised world map + numbered list 17-50 +
DATE CHECK footer. Run: python3 build.py  (writes build.html next door)
"""
import html

W, H = 1024, 1024
INK = "#141414"
RED = "#a31621"
GREY = "#333333"
MUTED = "#666666"
SERIF = "Georgia, 'Noto Serif', serif"
SANS = "Arial, 'Noto Sans', sans-serif"


def esc(s):
    return html.escape(s, quote=False)


def text(x, y, s, size, family=SANS, weight="normal", fill=INK,
         anchor="start", style="", spacing=None):
    a = f' x="{x}" y="{y}" font-family="{family}" font-size="{size}"'
    if weight != "normal":
        a += f' font-weight="{weight}"'
    if fill != INK:
        a += f' fill="{fill}"'
    if anchor != "start":
        a += f' text-anchor="{anchor}"'
    if style:
        a += f' font-style="{style}"'
    if spacing:
        a += f' letter-spacing="{spacing}"'
    return f'<text{a}>{esc(s)}</text>'


def line(x1, y1, x2, y2, w=1.5, color=INK):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{w}"/>')


def rect(x, y, w, h, fill, stroke=None, sw=1.5):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{sw}"'
    return s + '/>'


# ---------------------------------------------------------------- stories
# leads: (kicker, headline lines, deck lines, art key)
LEADS = [
    ("WAR \u00b7 KYIV \u00b7 UKRAINE",
     ["RUSSIA\u2019S BARRAGE", "HITS KYIV BRIDGES"],
     ["Eight killed as missiles and drones",
      "strike bridges over the Dnipro and",
      "knock out power. \u2014 Al Jazeera / Reuters"],
     "bridge"),
    ("DIPLOMACY \u00b7 LONDON \u00b7 A DECADE ON",
     ["UK AND EU AGREE", "RELATIONS RESET"],
     ["A decade after Brexit, London and",
      "Brussels agree steps towards closer",
      "alignment. \u2014 AP / Al Jazeera"],
     "flags"),
    ("MARKETS \u00b7 ARTIFICIAL INTELLIGENCE",
     ["ANTHROPIC SHARES", "SLUMP 11% ON DAY TWO"],
     ["A day after the biggest IPO on record,",
      "Claude\u2019s maker slides as AI fever",
      "fades. \u2014 Axios / Reuters"],
     "slump"),
    ("US \u00b7 WHITE HOUSE \u00b7 DATA CENTRES",
     ["TRUMP THREATENS", "DATA-CENTRE TAX"],
     ["US firms building data centres abroad",
      "face a \u2018tremendous tax\u2019, he tells a",
      "news conference. \u2014 Axios / NYT"],
     "server"),
]

# medium: (kicker, headline lines, deck lines, icon key)
MEDIUM = [
    ("MARKETS \u00b7 WALL STREET",
     ["WALL ST FALLS 2%", "VIX JUMPS TO 28"],
     ["S&P 500 \u22122.02% as Fed hike fears",
      "grow. \u2014 Reuters"],
     "chart"),
    ("MARKETS \u00b7 SEOUL \u00b7 TOKYO",
     ["KOSPI PLUNGES 4.8%", "SIDECAR TRIPS"],
     ["Samsung, SK hynix slide; SoftBank",
      "\u221214% in Tokyo. \u2014 SED / AJ Bell"],
     "chartdown"),
    ("WEATHER \u00b7 INDIA \u00b7 ODISHA",
     ["CYCLONE AKVAN", "WEAKENS OFF ODISHA"],
     ["300,000 evacuated; heavy rain in",
      "three states. \u2014 NDTV"],
     "storm"),
    ("MIDDLE EAST \u00b7 YEMEN",
     ["SAUDIS STRIKE HOUTHIS", "5 DRONES DOWNED"],
     ["Coalition hits Hodeidah and Sanaa;",
      "missile intercepted. \u2014 AP \u00b7 CLAIM"],
     "flame"),
    ("JUSTICE \u00b7 MYANMAR",
     ["MYANMAR REJECTS", "ICJ GENOCIDE RULING"],
     ["Naypyidaw calls Thursday\u2019s verdict",
      "\u2018unfair\u2019. \u2014 Africanews"],
     "scales"),
    ("DIPLOMACY \u00b7 SEOUL",
     ["NO KIM MEETING", "AS TRUMP LEAVES ASIA"],
     ["Seoul urges renewed US\u2013North Korea",
      "dialogue. \u2014 UPI"],
     "phone"),
    ("LATIN AMERICA \u00b7 BOGOT\u00c1",
     ["COLOMBIA PROTESTS", "TAX AND US TROOPS"],
     ["Thousands march against tax plans",
      "and US military role. \u2014 Al Jazeera"],
     "placard"),
    ("AFRICA \u00b7 LILONGWE",
     ["MALAWI FUEL CRISIS", "CAUSES CHAOS"],
     ["Shortages paralyse motorists and",
      "businesses. \u2014 Al Jazeera"],
     "pump"),
    ("US \u00b7 LOS ANGELES",
     ["LA QUAKE 4.2", "RATTLES WIDE AREA"],
     ["Temblor centred near Commerce",
      "at 3:25 a.m. \u2014 LA Times"],
     "crack"),
    ("US \u00b7 CINCINNATI",
     ["FIONA THE HIPPO", "DIES AFTER EATING HAT"],
     ["Beloved zoo hippo dies days after",
      "swallowing a visitor\u2019s hat. \u2014 AP"],
     "hippo"),
    ("ECONOMY \u00b7 US",
     ["CONSUMER MOOD", "SURGES AFTER MIDTERMS"],
     ["Sentiment jumps; inflation, not jobs,",
      "blamed for hardship. \u2014 Axios"],
     "smile"),
    ("SCIENCE \u00b7 SPACE",
     ["DYING STAR SWALLOWS", "ITS COMPANION"],
     ["A puffy star, 7\u00d7 the sun\u2019s mass,",
      "swallows its companion. \u2014 Reuters"],
     "star"),
]

# list 17-50: (headline, source) — keep each line short
LIST = [
    ("Pentagon: Ukraine deep strikes \u201ccounterproductive\u201d", "NPR"),
    ("Senate votes on data-centre permitting bill", "AP"),
    ("DOJ drops Alaska Senate challenge", "AP"),
    ("Oil up Friday, set for weekly fall", "Reuters"),
    ("EU aviation emissions plan faces Mideast pushback", "Reuters"),
    ("German youth protest military expansion", "Al Jazeera"),
    ("COP31 activists protest fossil-fuel failure", "Africanews"),
    ("Somali protesters back UAE envoy expulsion", "Africanews"),
    ("Tunisian activist Bensedrine jailed 5 years", "Africanews"),
    ("1 in 4 children lived in conflict zones in 2025", "Save the Children"),
    ("US protesters demand human control over AI", "Africanews"),
    ("Iraq deal: Kataib Hezbollah to pull out in a month", "AP"),
    ("Nvidia signals caution on China", "Yahoo Finance"),
    ("Hyundai unveils new Avante at LA Auto Show", "SED"),
    ("Russell Brand prison message stays on YouTube", "Yahoo"),
    ("Lindsay Clancy to face retrial next year", "Yahoo"),
    ("Gaza children swim in the sea", "AP"),
    ("Bhutan\u2019s wood-painting tradition", "Africanews"),
    ("Japan\u2019s rabbit island\u2019s dark secret", "Africanews"),
    ("Barnsley 1\u20132 Sheffield Wednesday", "BBC Sport"),
    ("Southend 2\u20133 Boreham Wood", "BBC Sport"),
    ("Cliftonville 3\u20132 Glentoran", "BBC Sport"),
    ("SMAT: Saurashtra stay unbeaten; Unadkat 3\u201323", "ESPNcricinfo"),
    ("East Bengal 2\u20132 SC Delhi; Bengaluru 2\u20130 Mumbai City", "BBC Sport"),
    ("Shakhtar 1\u20131 Livyi Bereh", "BBC Sport"),
    ("Korea Cosmetics jumps 45% in two days", "SED"),
    ("STX names Jeon Jae-gon CEO", "SED"),
    ("3.2m in Guatemala face crisis hunger", "ReliefWeb"),
    ("Gold $3,722/oz, no haven bid", "Rio Times"),
    ("US 10-year yield 5.048%", "Rio Times"),
    ("Philadelphia Fed index 6.3 vs 20 expected", "Rio Times"),
    ("Brazil Selic on hold at 13.75%", "Rio Times"),
    ("Top traders buy SK hynix as it slides 6%", "SED"),
    ("Mideast oil exports dip as Iran hits tankers", "AP"),
]
assert len(LIST) == 34, len(LIST)

TIMELINE = [
    ("OVERNIGHT", "Russia\u2019s barrage hits Kyiv"),
    ("MORNING", "KOSPI plunges 4.8%"),
    ("MIDDAY", "UK and EU agree reset"),
    ("AFTERNOON", "Anthropic shares fall 11%"),
    ("EVENING", "Trump: data-centre tax"),
]

# ---------------------------------------------------------------- lead art
def art_bridge(x, y):
    """Dnipro bridge hit: deck, arch, explosion, smoke. 116x128 box."""
    s = []
    # river
    s.append(rect(x + 6, y + 96, 104, 16, "#7fa8c9", stroke=INK))
    # bridge deck + arch
    s.append(f'<path d="M{x+8},{y+88} Q{x+58},{y+30} {x+108},{y+88}" fill="none" stroke="{INK}" stroke-width="3"/>')
    s.append(line(x + 8, y + 88, x + 108, y + 88, 4))
    for cx in (x + 26, x + 58, x + 90):
        s.append(line(cx, y + 62, cx, y + 88, 2))
    # explosion on the deck
    s.append(f'<polygon points="{x+58},{y+52} {x+66},{y+66} {x+80},{y+62} {x+70},{y+74} {x+76},{y+86} {x+60},{y+82} {x+48},{y+90} {x+50},{y+76} {x+36},{y+74} {x+50},{y+66}" fill="#e8590c" stroke="#7f1d1d" stroke-width="1.5"/>')
    # smoke
    s.append(f'<circle cx="{x+52}" cy="{y+40}" r="8" fill="#9e9e9e"/><circle cx="{x+64}" cy="{y+30}" r="10" fill="#bdbdbd"/><circle cx="{x+76}" cy="{y+20}" r="7" fill="#e0e0e0"/>')
    # broken span
    s.append(line(x + 70, y + 88, x + 82, y + 96, 3, RED))
    s.append(text(x + 58, y + 126, "KYIV", 10, weight="bold", anchor="middle", fill=MUTED))
    return "".join(s)


def art_flags(x, y):
    """Union Jack and EU flag on poles over a table. 116x128 box."""
    s = []
    s.append(f'<ellipse cx="{x+58}" cy="{y+104}" rx="52" ry="10" fill="#8a6d3b" stroke="#5a4a28" stroke-width="2"/>')
    s.append(f'<rect x="{x+52}" y="{y+104}" width="12" height="18" fill="#5a4a28"/>')
    # UK flag pole (left) and EU flag pole (right)
    for px in (x + 22, x + 78):
        s.append(f'<line x1="{px}" y1="{y+18}" x2="{px}" y2="{y+104}" stroke="#5a4a28" stroke-width="3"/>')
    # Union Jack (simplified): blue, white diagonals, red cross
    s.append(rect(x + 22, y + 18, 32, 20, "#012169", stroke=INK))
    s.append(f'<line x1="{x+22}" y1="{y+18}" x2="{x+54}" y2="{y+38}" stroke="#fff" stroke-width="4"/>')
    s.append(f'<line x1="{x+54}" y1="{y+18}" x2="{x+22}" y2="{y+38}" stroke="#fff" stroke-width="4"/>')
    s.append(f'<line x1="{x+38}" y1="{y+18}" x2="{x+38}" y2="{y+38}" stroke="#fff" stroke-width="6"/>')
    s.append(f'<line x1="{x+22}" y1="{y+28}" x2="{x+54}" y2="{y+28}" stroke="#fff" stroke-width="6"/>')
    s.append(f'<line x1="{x+38}" y1="{y+18}" x2="{x+38}" y2="{y+38}" stroke="{RED}" stroke-width="3"/>')
    s.append(f'<line x1="{x+22}" y1="{y+28}" x2="{x+54}" y2="{y+28}" stroke="{RED}" stroke-width="3"/>')
    # EU flag: blue with a ring of gold stars
    s.append(rect(x + 78, y + 18, 32, 20, "#003399", stroke=INK))
    import math
    for k in range(12):
        a = 2 * math.pi * k / 12 - math.pi / 2
        sx = x + 94 + 9 * math.cos(a)
        sy = y + 28 + 7 * math.sin(a)
        s.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="1.3" fill="#ffcc00"/>')
    # two heads shaking hands at the table
    for cx in (x + 38, x + 78):
        s.append(f'<circle cx="{cx}" cy="{y+92}" r="9" fill="#e8c39e" stroke="{INK}" stroke-width="1.5"/>')
    s.append(f'<circle cx="{x+58}" cy="{y+96}" r="5" fill="#f2c14e" stroke="{INK}" stroke-width="1.5"/>')
    return "".join(s)


def art_slump(x, y):
    """Falling chart + bell + ANT ticker. 116x128 box."""
    s = []
    s.append(rect(x + 6, y + 52, 104, 60, "#fbeeee", stroke=INK))
    s.append(f'<path d="M{x+14},{y+60} L{x+38},{y+72} L{x+54},{y+68} L{x+80},{y+92} L{x+102},{y+104}" fill="none" stroke="{RED}" stroke-width="3"/>')
    s.append(f'<polygon points="{x+102},{y+104} {x+90},{y+104} {x+98},{y+92}" fill="{RED}"/>')
    # bell
    s.append(f'<path d="M{x+44},{y+40} Q{x+44},{y+18} {x+58},{y+18} Q{x+72},{y+18} {x+72},{y+40} L{x+76},{y+44} L{x+40},{y+44} Z" fill="#f2c14e" stroke="{INK}" stroke-width="1.5"/>')
    s.append(f'<circle cx="{x+58}" cy="{y+48}" r="3" fill="{INK}"/>')
    s.append(text(x + 14, y + 106, "ANT \u221211%", 13, weight="bold", fill=RED))
    return "".join(s)


def art_server(x, y):
    """Server rack + TAX stamp. 116x128 box."""
    s = []
    # rack
    s.append(rect(x + 18, y + 14, 60, 96, "#37474f", stroke=INK, sw=2))
    for i in range(4):
        yy = y + 22 + i * 22
        s.append(rect(x + 24, y + 22 + i * 22, 48, 14, "#90a4ae", stroke=INK))
        s.append(f'<circle cx="{x+30}" cy="{yy+7}" r="2" fill="#69f0ae"/>')
        s.append(f'<circle cx="{x+38}" cy="{yy+7}" r="2" fill="#ffd43b"/>')
        s.append(line(x + 46, yy + 4, x + 66, yy + 4, 1.5, "#546e7a"))
        s.append(line(x + 46, yy + 10, x + 66, yy + 10, 1.5, "#546e7a"))
    # TAX stamp, rotated
    s.append(f'<g transform="rotate(-14 {x+84} {y+96})">')
    s.append(rect(x + 58, y + 84, 52, 24, "#ffffff", stroke=RED, sw=2.5))
    s.append(text(x + 84, y + 101, "TAX", 15, weight="bold", anchor="middle", fill=RED))
    s.append('</g>')
    # cable
    s.append(f'<path d="M{x+78},{y+110} Q{x+96},{y+118} {x+108},{y+104}" fill="none" stroke="{INK}" stroke-width="2"/>')
    return "".join(s)


ART = {"bridge": art_bridge, "flags": art_flags,
       "slump": art_slump, "server": art_server}


def icon(key, x, y):
    """Tiny 26x26 motif for a medium panel, top-right."""
    if key == "chart":
        return (f'<path d="M{x+3},{y+22} L{x+10},{y+14} L{x+15},{y+17} L{x+23},{y+5}" fill="none" stroke="{RED}" stroke-width="2.5"/>'
                f'<polygon points="{x+23},{y+5} {x+17},{y+5} {x+21},{y+11}" fill="{RED}"/>'
                f'<line x1="{x+3}" y1="{y+23}" x2="{x+23}" y2="{y+23}" stroke="{INK}" stroke-width="1.5"/>')
    if key == "chartdown":
        return (f'<path d="M{x+3},{y+5} L{x+10},{y+13} L{x+15},{y+10} L{x+23},{y+22}" fill="none" stroke="{RED}" stroke-width="2.5"/>'
                f'<polygon points="{x+23},{y+22} {x+17},{y+22} {x+21},{y+16}" fill="{RED}"/>'
                f'<line x1="{x+3}" y1="{y+23}" x2="{x+23}" y2="{y+23}" stroke="{INK}" stroke-width="1.5"/>')
    if key == "storm":
        return (f'<ellipse cx="{x+13}" cy="{y+11}" rx="10" ry="7" fill="#90a4ae" stroke="{INK}" stroke-width="1.5"/>'
                f'<polygon points="{x+11},{y+17} {x+16},{y+17} {x+12},{y+23} {x+17},{y+23}" fill="#ffd43b" stroke="{INK}" stroke-width="1"/>')
    if key == "flame":
        return (f'<path d="M{x+13},{y+2} Q{x+22},{y+12} {x+20},{y+18} Q{x+18},{y+24} {x+13},{y+24} Q{x+8},{y+24} {x+6},{y+18} Q{x+4},{y+12} {x+13},{y+2} Z" fill="#e8590c" stroke="#7f1d1d" stroke-width="1.5"/>'
                f'<path d="M{x+13},{y+12} Q{x+17},{y+16} {x+13},{y+20} Q{x+9},{y+20} {x+13},{y+12} Z" fill="#ffd43b"/>')
    if key == "scales":
        return (f'<line x1="{x+13}" y1="{y+4}" x2="{x+13}" y2="{y+22}" stroke="{INK}" stroke-width="2"/>'
                f'<line x1="{x+5}" y1="{y+7}" x2="{x+21}" y2="{y+7}" stroke="{INK}" stroke-width="2"/>'
                f'<path d="M{x+5},{y+7} L{x+2},{y+14} L{x+8},{y+14} Z" fill="#f2c14e" stroke="{INK}" stroke-width="1"/>'
                f'<path d="M{x+21},{y+7} L{x+18},{y+14} L{x+24},{y+14} Z" fill="#f2c14e" stroke="{INK}" stroke-width="1"/>'
                f'<line x1="{x+8}" y1="{y+22}" x2="{x+18}" y2="{y+22}" stroke="{INK}" stroke-width="2"/>')
    if key == "phone":
        return (f'<rect x="{x+7}" y="{y+2}" width="12" height="22" rx="2" fill="#e8e0cc" stroke="{INK}" stroke-width="1.5"/>'
                f'<rect x="{x+9}" y="{y+5}" width="8" height="13" fill="#bcd3e6"/>'
                f'<circle cx="{x+13}" cy="{y+21}" r="1.5" fill="{INK}"/>')
    if key == "placard":
        return (f'<line x1="{x+13}" y1="{y+10}" x2="{x+13}" y2="{y+24}" stroke="{INK}" stroke-width="2"/>'
                f'<rect x="{x+4}" y="{y+2}" width="18" height="10" fill="#fff" stroke="{INK}" stroke-width="1.5"/>'
                f'<line x1="{x+7}" y1="{y+6}" x2="{x+19}" y2="{y+6}" stroke="{RED}" stroke-width="1.5"/>'
                f'<line x1="{x+7}" y1="{y+9}" x2="{x+15}" y2="{y+9}" stroke="{INK}" stroke-width="1"/>')
    if key == "pump":
        return (f'<rect x="{x+5}" y="{y+3}" width="12" height="18" rx="2" fill="#e8e0cc" stroke="{INK}" stroke-width="1.5"/>'
                f'<rect x="{x+8}" y="{y+6}" width="6" height="6" fill="#fff" stroke="{INK}" stroke-width="1"/>'
                f'<path d="M{x+17},{y+8} L{x+22},{y+8} L{x+22},{y+18}" fill="none" stroke="{INK}" stroke-width="1.5"/>'
                f'<line x1="{x+5}" y1="{y+21}" x2="{x+21}" y2="{y+21}" stroke="{INK}" stroke-width="1.5"/>')
    if key == "crack":
        return (f'<polygon points="{x+4},{y+3} {x+10},{y+9} {x+6},{y+13} {x+13},{y+18} {x+9},{y+23} {x+20},{y+22} {x+23},{y+15} {x+16},{y+12} {x+19},{y+6}" fill="#b0bec5" stroke="{INK}" stroke-width="1.5"/>')
    if key == "hippo":
        return (f'<ellipse cx="{x+13}" cy="{y+16}" rx="10" ry="7" fill="#90a4ae" stroke="{INK}" stroke-width="1.5"/>'
                f'<circle cx="{x+20}" cy="{y+11}" r="4" fill="#90a4ae" stroke="{INK}" stroke-width="1.5"/>'
                f'<circle cx="{x+7}" cy="{y+10}" r="2" fill="#90a4ae" stroke="{INK}" stroke-width="1"/>'
                f'<circle cx="{x+21}" cy="{y+10}" r="1" fill="{INK}"/>')
    if key == "smile":
        return (f'<circle cx="{x+13}" cy="{y+13}" r="10" fill="#ffd43b" stroke="{INK}" stroke-width="1.5"/>'
                f'<circle cx="{x+9}" cy="{y+11}" r="1.5" fill="{INK}"/><circle cx="{x+17}" cy="{y+11}" r="1.5" fill="{INK}"/>'
                f'<path d="M{x+8},{y+15} Q{x+13},{y+20} {x+18},{y+15}" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    if key == "star":
        return (f'<polygon points="{x+13},{y+2} {x+16},{y+10} {x+24},{y+10} {x+18},{y+15} {x+20},{y+23} {x+13},{y+18} {x+6},{y+23} {x+8},{y+15} {x+2},{y+10} {x+10},{y+10}" fill="#ffd43b" stroke="{INK}" stroke-width="1"/>'
                f'<circle cx="{x+20}" cy="{y+5}" r="2" fill="#fff" stroke="{INK}" stroke-width="1"/>')
    return ""


# ---------------------------------------------------------------- map
CONTINENTS = [
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-55, 52), (-60, 45), (-75, 35), (-80, 25), (-97, 26), (-105, 20), (-115, 30), (-125, 40), (-145, 60)],
    [(-80, 10), (-60, 10), (-50, 0), (-35, -8), (-40, -20), (-50, -30), (-60, -40), (-70, -55), (-75, -40), (-80, -20)],
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (30, 31), (35, 28), (43, 12), (48, 10), (40, -5), (35, -18), (25, -33), (15, -35), (10, -15), (5, 5), (-8, 5)],
    [(-10, 36), (-9, 43), (-2, 48), (0, 50), (5, 53), (8, 57), (18, 56), (21, 55), (24, 58), (28, 60), (25, 65), (18, 66), (12, 70), (5, 60), (-5, 58), (-10, 50)],
    [(30, 62), (40, 68), (60, 70), (80, 73), (100, 77), (120, 73), (140, 72), (160, 70), (178, 66), (170, 60), (162, 56), (158, 50), (142, 45), (140, 38), (135, 35), (127, 33), (122, 30), (120, 25), (110, 20), (105, 10), (100, 8), (95, 15), (90, 22), (80, 15), (75, 10), (70, 20), (60, 25), (50, 28), (45, 30), (35, 36), (30, 42)],
    [(113, -22), (122, -14), (132, -12), (142, -11), (150, -20), (153, -27), (150, -37), (140, -38), (130, -32), (120, -34), (113, -30)],
]
# (lon, lat, label, dx, dy)
DOTS = [
    (30.5, 50.4, "KYIV", 4, -6),
    (-0.1, 51.5, "LONDON", -52, -4),
    (-74.0, 40.7, "NEW YORK", -58, -4),
    (46.7, 24.6, "RIYADH", 4, 10),
    (85.8, 20.3, "ODISHA", -6, 12),
    (127.0, 37.5, "SEOUL", -30, -4),
    (-74.0, 4.7, "BOGOT\u00c1", -44, 12),
    (33.8, -13.9, "LILONGWE", 4, 4),
]


def map_svg(mx, my, mw, mh):
    """Stylised world map in box (mx,my,mw,mh). Equirectangular."""
    def px(lon, lat):
        return mx + (lon + 180) / 360 * mw, my + (75 - lat) / 130 * mh
    s = [rect(mx, my, mw, mh, "#bcd3e6", stroke=INK)]
    for poly in CONTINENTS:
        pts = " ".join(f"{px(lon, lat)[0]:.1f},{px(lon, lat)[1]:.1f}" for lon, lat in poly)
        s.append(f'<polygon points="{pts}" fill="#e8d9b0" stroke="#8a6d3b" stroke-width="1"/>')
    for lon, lat, label, dx, dy in DOTS:
        cx, cy = px(lon, lat)
        s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="3.5" fill="{RED}" stroke="#fff" stroke-width="1"/>')
        if label:
            s.append(text(cx + dx, cy + dy, label, 8.5, weight="bold", fill=INK))
    return "".join(s)


# ---------------------------------------------------------------- build
def build():
    p = []
    p.append(f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">')
    p.append(rect(0, 0, W, H, "#f6f1e7"))

    # ---- masthead
    p.append(line(28, 12, 996, 12, 2))
    p.append(text(512, 60, "THE WORLD TODAY", 44, SERIF, "bold", anchor="middle"))
    p.append(text(28, 94, "50 STORIES", 13, weight="bold", fill=RED, spacing="2"))
    p.append(text(512, 94, "FRIDAY \u00b7 20 NOVEMBER 2026", 24, weight="bold", fill=RED, anchor="middle", spacing="2"))
    p.append(text(996, 94, "SOURCES NAMED", 13, weight="bold", fill=RED, anchor="end", spacing="2"))
    p.append(line(28, 106, 996, 106, 4))
    p.append(line(28, 112, 996, 112, 1.5))

    # ---- UTC timeline strip
    p.append(text(28, 130, "THE DAY IN UTC", 12, weight="bold", fill=RED, spacing="1"))
    for i, (slot, head) in enumerate(TIMELINE):
        bx = 28 + i * 194
        p.append(rect(bx, 136, 188, 32, "#ffffff", stroke=INK, sw=1))
        p.append(text(bx + 6, 148, slot, 10, weight="bold", fill=RED))
        p.append(text(bx + 6, 162, head, 11))

    # ---- lead panels 2x2
    lead_y = [176, 328]
    lead_x = [28, 518]
    for idx, (kicker, heads, deck, artkey) in enumerate(LEADS):
        x = lead_x[idx % 2]
        y = lead_y[idx // 2]
        p.append(rect(x, y, 478, 146, "#fffdf5", stroke=INK, sw=1.5))
        p.append(text(x + 14, y + 20, kicker, 13, weight="bold", fill=RED, spacing="1"))
        for j, hl in enumerate(heads):
            p.append(text(x + 14, y + 50 + j * 30, hl, 24, SERIF, "bold"))
        for j, dl in enumerate(deck):
            p.append(text(x + 14, y + 102 + j * 16, dl, 13, fill=GREY))
        p.append(ART[artkey](x + 348, y + 8))

    # ---- medium panels 4x3
    med_y = [480, 576, 672]
    med_x = [28, 268, 508, 748]
    for idx, (kicker, heads, deck, ikey) in enumerate(MEDIUM):
        x = med_x[idx % 4]
        y = med_y[idx // 4]
        p.append(rect(x, y, 236, 92, "#fffdf5", stroke=INK, sw=1))
        p.append(text(x + 8, y + 15, kicker, 10, weight="bold", fill=RED, spacing="0.5"))
        p.append(icon(ikey, x + 202, y + 4))
        for j, hl in enumerate(heads):
            p.append(text(x + 8, y + 36 + j * 18, hl, 15, SERIF, "bold"))
        for j, dl in enumerate(deck):
            p.append(text(x + 8, y + 72 + j * 13, dl, 11, fill=GREY))

    # ---- map + numbered list
    p.append(line(28, 770, 996, 770, 1.5))
    p.append(text(28, 788, "WHERE IT HAPPENED", 12, weight="bold", fill=RED, spacing="1"))
    p.append(text(348, 788, "THE REST OF THE DAY \u2014 17 TO 50", 12, weight="bold", fill=RED, spacing="1"))
    p.append(map_svg(28, 794, 308, 156))
    p.append(text(182, 962, "Stylised map \u00b7 red dots mark story locations", 9, fill=MUTED, anchor="middle"))
    for col in range(2):
        cx = 348 + col * 328
        for row in range(17):
            n = 17 + col * 17 + row
            head, src = LIST[n - 17]
            y = 800 + row * 9.6
            p.append(text(cx, y, f"{n}. {head} \u2014 {src}", 10))

    # ---- DATE CHECK footer
    p.append(line(28, 970, 996, 970, 1.5))
    p.append(text(28, 988, "DATE CHECK", 13, weight="bold", fill=RED, spacing="1"))
    p.append(text(140, 988, "Every story above happened or was first reported on 20 November 2026.", 12.5))
    p.append(text(28, 1004, "Excluded: Thursday\u2019s ICJ genocide ruling (only Myanmar\u2019s rejection today counts), the Shenzhen peace declaration,", 12.5, fill=GREY))
    p.append(text(28, 1018, "Anthropic\u2019s $83 IPO pricing and the GTA VI launch (all 19 Nov). No future-dated event is featured. CLAIM = one-sided account.", 12.5, fill=GREY))

    p.append("</svg>")
    return "\n".join(p)


HTML = """<!doctype html>
<html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#f6f1e7}svg{display:block}</style></head>
<body>
""" + build() + """
</body></html>
"""

if __name__ == "__main__":
    with open("build.html", "w", encoding="utf-8") as f:
        f.write(HTML)
    print("wrote build.html", len(HTML), "bytes")
