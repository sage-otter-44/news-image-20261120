#!/usr/bin/env python3
"""Build the front page for THE WORLD TODAY - Friday 20 November 2026.

Reads nothing but the story list baked into this file (taken from the
entry README) and writes build.html: a 1024x1024 newspaper front page
with a UTC timeline strip, four illustrated leads, twelve medium panels,
a numbered list of stories 17-50, a stylised world map and a DATE CHECK
footer. Run with: python3 build.py
"""

import html

PAGE_W = 1024

# ---------------------------------------------------------------- stories

TIMELINE = [
    ("OVERNIGHT", "Russia's barrage hits Kyiv"),
    ("MORNING", "KOSPI plunges 4.8%"),
    ("MIDDAY", "UK and EU agree reset"),
    ("AFTERNOON", "Anthropic shares fall 11%"),
    ("EVENING", "Trump: data-centre tax"),
]

# Each lead: kicker, headline, body (with source), art key.
LEADS = [
    (
        "WAR \u00b7 KYIV \u00b7 UKRAINE",
        "RUSSIA'S BARRAGE HITS KYIV BRIDGES",
        "Eight killed as missiles and drones strike bridges over the "
        "Dnipro and knock out power. \u2014 Al Jazeera / Reuters",
        "bridge",
    ),
    (
        "DIPLOMACY \u00b7 LONDON \u00b7 A DECADE ON",
        "UK AND EU AGREE RELATIONS RESET",
        "A decade after Brexit, London and Brussels agree steps towards "
        "closer alignment. \u2014 AP / Al Jazeera",
        "flags",
    ),
    (
        "MARKETS \u00b7 ARTIFICIAL INTELLIGENCE",
        "ANTHROPIC SHARES SLUMP 11% ON DAY TWO",
        "A day after the biggest IPO on record, Claude's maker slides as "
        "AI fever fades. \u2014 Axios / Reuters",
        "bell",
    ),
    (
        "US \u00b7 WHITE HOUSE \u00b7 DATA CENTRES",
        "TRUMP THREATENS DATA-CENTRE TAX",
        "US firms building data centres abroad face a \u2018tremendous "
        "tax\u2019, he tells a news conference. \u2014 Axios / NYT",
        "servers",
    ),
]

# Each medium panel: kicker, headline, body (with source).
MEDIUMS = [
    (
        "MARKETS \u00b7 WALL STREET",
        "WALL ST FALLS 2% VIX JUMPS TO 28",
        "S&P 500 \u22122.02% as Fed hike fears grow. \u2014 Reuters",
    ),
    (
        "MARKETS \u00b7 SEOUL \u00b7 TOKYO",
        "KOSPI PLUNGES 4.8%, SIDECAR TRIPS",
        "Samsung, SK hynix slide; SoftBank \u221214% in Tokyo. "
        "\u2014 Seoul Economic Daily / AJ Bell",
    ),
    (
        "WEATHER \u00b7 INDIA \u00b7 ODISHA",
        "CYCLONE AKVAN WEAKENS OFF ODISHA",
        "300,000 evacuated; heavy rain in three states. \u2014 NDTV",
    ),
    (
        "MIDDLE EAST \u00b7 YEMEN",
        "SAUDIS STRIKE HOUTHIS 5 DRONES DOWNED",
        "Coalition hits Hodeidah and Sanaa; missile intercepted. "
        "\u2014 AP \u00b7 CLAIM",
    ),
    (
        "JUSTICE \u00b7 MYANMAR",
        "MYANMAR REJECTS ICJ GENOCIDE RULING",
        "Naypyidaw calls Thursday's verdict \u2018unfair\u2019. "
        "\u2014 Africanews",
    ),
    (
        "DIPLOMACY \u00b7 SEOUL",
        "NO KIM MEETING AS TRUMP LEAVES ASIA",
        "Seoul urges renewed US\u2013North Korea dialogue. \u2014 UPI",
    ),
    (
        "LATIN AMERICA \u00b7 BOGOT\u00c1",
        "COLOMBIA PROTESTS TAX AND US TROOPS",
        "Thousands march against tax plans and US military role. "
        "\u2014 Al Jazeera",
    ),
    (
        "AFRICA \u00b7 LILONGWE",
        "MALAWI FUEL CRISIS CAUSES CHAOS",
        "Shortages paralyse motorists and businesses. \u2014 Al Jazeera",
    ),
    (
        "US \u00b7 LOS ANGELES",
        "LA QUAKE 4.2 RATTLES WIDE AREA",
        "Temblor centred near Commerce at 3:25 a.m. \u2014 LA Times",
    ),
    (
        "US \u00b7 CINCINNATI",
        "FIONA THE HIPPO DIES AFTER EATING HAT",
        "Beloved zoo hippo dies days after swallowing a visitor's hat. "
        "\u2014 AP",
    ),
    (
        "ECONOMY \u00b7 US",
        "CONSUMER MOOD SURGES AFTER MIDTERMS",
        "Sentiment jumps; inflation, not jobs, blamed for hardship. "
        "\u2014 Axios",
    ),
    (
        "SCIENCE \u00b7 SPACE",
        "DYING STAR SWALLOWS ITS COMPANION",
        "A puffy star, 7\u00d7 the sun's mass, swallows its companion. "
        "\u2014 Reuters",
    ),
]

# Stories 17-50: (number, one-liner with source).
REST = [
    (17, "Pentagon: Ukraine deep strikes \u201ccounterproductive\u201d \u2014 NPR"),
    (18, "Senate votes on data-centre permitting bill \u2014 AP"),
    (19, "DOJ drops Alaska Senate challenge \u2014 AP"),
    (20, "Oil up Friday, set for weekly fall \u2014 Reuters"),
    (21, "EU aviation emissions plan faces Mideast pushback \u2014 Reuters"),
    (22, "German youth protest military expansion \u2014 Al Jazeera"),
    (23, "COP31 activists protest fossil-fuel failure \u2014 Africanews"),
    (24, "Somali protesters back UAE envoy expulsion \u2014 Africanews"),
    (25, "Tunisian activist Bensedrine jailed 5 years \u2014 Africanews"),
    (26, "1 in 4 children lived in conflict zones in 2025 \u2014 Save the Children"),
    (27, "US protesters demand human control over AI \u2014 Africanews"),
    (28, "Iraq deal: Kataib Hezbollah to pull out in a month \u2014 AP"),
    (29, "Nvidia signals caution on China \u2014 Yahoo Finance"),
    (30, "Hyundai unveils new Avante at LA Auto Show \u2014 Seoul Economic Daily"),
    (31, "Russell Brand prison message stays on YouTube \u2014 Yahoo"),
    (32, "Lindsay Clancy to face retrial next year \u2014 Yahoo"),
    (33, "Gaza children swim in the sea \u2014 AP"),
    (34, "Bhutan's wood-painting tradition \u2014 Africanews"),
    (35, "Japan's rabbit island's dark secret \u2014 Africanews"),
    (36, "Barnsley 1\u20132 Sheffield Wednesday \u2014 BBC Sport"),
    (37, "Southend 2\u20133 Boreham Wood \u2014 BBC Sport"),
    (38, "Cliftonville 3\u20132 Glentoran \u2014 BBC Sport"),
    (39, "SMAT: Saurashtra stay unbeaten; Unadkat 3\u201323 \u2014 ESPNcricinfo"),
    (40, "East Bengal 2\u20132 SC Delhi; Bengaluru 2\u20130 Mumbai City \u2014 BBC Sport"),
    (41, "Shakhtar 1\u20131 Livyi Bereh \u2014 BBC Sport"),
    (42, "Korea Cosmetics jumps 45% in two days \u2014 Seoul Economic Daily"),
    (43, "STX names Jeon Jae-gon CEO \u2014 Seoul Economic Daily"),
    (44, "3.2m in Guatemala face crisis hunger \u2014 ReliefWeb"),
    (45, "Gold $3,722/oz, no haven bid \u2014 Rio Times"),
    (46, "US 10-year yield 5.048% \u2014 Rio Times"),
    (47, "Philadelphia Fed index 6.3 vs 20 expected \u2014 Rio Times"),
    (48, "Brazil Selic on hold at 13.75% \u2014 Rio Times"),
    (49, "Top traders buy SK hynix as it slides 6% \u2014 Seoul Economic Daily"),
    (50, "Mideast oil exports dip as Iran hits tankers \u2014 AP"),
]

DATE_CHECK = (
    "Every story above happened or was first reported on 20 November 2026. "
    "Excluded: Thursday's ICJ genocide ruling (only Myanmar's rejection today "
    "counts), the Shenzhen peace declaration, Anthropic's $83 IPO pricing and "
    "the GTA VI launch (all 19 Nov). No future-dated event is featured. "
    "CLAIM = one-sided account."
)

# Map dots: (label, x, y) on a 330x190 canvas.
MAP_DOTS = [
    ("NEW YORK", 72, 68),
    ("LONDON", 163, 42),
    ("KYIV", 186, 52),
    ("SEOUL", 282, 72),
    ("RIYADH", 202, 96),
    ("ODISHA", 248, 100),
    ("BOGOT\u00c1", 92, 122),
    ("LILONGWE", 186, 142),
]


# ------------------------------------------------------------------ art

def art_bridge():
    """A bridge over a river with a burst above it."""
    return (
        '<svg width="118" height="92" viewBox="0 0 118 92">'
        '<rect x="6" y="66" width="106" height="18" fill="#7fa8c9"/>'
        '<path d="M10 66 Q59 22 108 66" fill="none" stroke="#3a3a3a" '
        'stroke-width="4"/>'
        '<line x1="30" y1="52" x2="30" y2="66" stroke="#3a3a3a" '
        'stroke-width="3"/><line x1="59" y1="40" x2="59" y2="66" '
        'stroke="#3a3a3a" stroke-width="3"/>'
        '<line x1="88" y1="52" x2="88" y2="66" stroke="#3a3a3a" '
        'stroke-width="3"/>'
        '<polygon points="59,6 66,20 80,14 68,26 78,34 62,32 58,46 52,32 '
        '38,36 50,26 40,16 54,20" fill="#e8590c"/>'
        '<circle cx="20" cy="14" r="7" fill="#c9c9c9"/>'
        '<circle cx="34" cy="9" r="5" fill="#c9c9c9"/>'
        '<text x="59" y="88" font-size="10" text-anchor="middle" '
        'fill="#333" font-family="Georgia,serif">KYIV</text></svg>'
    )


def art_flags():
    """Two small flags on poles above a round table."""
    return (
        '<svg width="118" height="92" viewBox="0 0 118 92">'
        '<ellipse cx="59" cy="78" rx="46" ry="9" fill="#8a6d3b"/>'
        '<line x1="34" y1="78" x2="34" y2="18" stroke="#3a3a3a" '
        'stroke-width="3"/><line x1="84" y1="78" x2="84" y2="18" '
        'stroke="#3a3a3a" stroke-width="3"/>'
        '<rect x="34" y="18" width="30" height="20" fill="#012169"/>'
        '<path d="M34 18 L64 38 M64 18 L34 38" stroke="#fff" '
        'stroke-width="3"/><path d="M34 18 L64 38 M64 18 L34 38" '
        'stroke="#c8102e" stroke-width="1.4"/>'
        '<rect x="84" y="18" width="30" height="20" fill="#003399"/>'
        '<circle cx="99" cy="28" r="7" fill="none" stroke="#ffcc00" '
        'stroke-width="1.6" stroke-dasharray="2 1.6"/>'
        '<circle cx="46" cy="66" r="8" fill="#e8c39a"/>'
        '<circle cx="74" cy="66" r="8" fill="#d9a066"/>'
        '<rect x="52" y="72" width="14" height="6" fill="#5a4632"/></svg>'
    )


def art_bell():
    """A bell over a falling chart line."""
    return (
        '<svg width="118" height="92" viewBox="0 0 118 92">'
        '<rect x="8" y="46" width="102" height="38" fill="#fdf6e3" '
        'stroke="#3a3a3a" stroke-width="1.5"/>'
        '<path d="M59 8 c-9 0 -13 8 -13 17 l-3 8 h32 l-3 -8 c0 -9 -4 -17 '
        '-13 -17z" fill="#f2c14e" stroke="#8a6d1a" stroke-width="1.5"/>'
        '<circle cx="59" cy="38" r="4" fill="#8a6d1a"/>'
        '<polyline points="16,52 40,58 62,64 84,70 102,72" fill="none" '
        'stroke="#c8102e" stroke-width="2.5"/>'
        '<polygon points="102,72 92,70 98,78" fill="#c8102e"/>'
        '<text x="59" y="80" font-size="11" font-weight="bold" '
        'text-anchor="middle" fill="#c8102e" '
        'font-family="Georgia,serif">ANT \u221211%</text></svg>'
    )


def art_servers():
    """A server rack with a tilted TAX stamp."""
    return (
        '<svg width="118" height="92" viewBox="0 0 118 92">'
        '<rect x="22" y="6" width="56" height="80" fill="#3a4452" '
        'stroke="#222" stroke-width="1.5"/>'
        '<rect x="28" y="12" width="44" height="14" fill="#5a6b7d"/>'
        '<rect x="28" y="32" width="44" height="14" fill="#5a6b7d"/>'
        '<rect x="28" y="52" width="44" height="14" fill="#5a6b7d"/>'
        '<circle cx="34" cy="19" r="2.4" fill="#7ee787"/>'
        '<circle cx="34" cy="39" r="2.4" fill="#f2c14e"/>'
        '<circle cx="34" cy="59" r="2.4" fill="#7ee787"/>'
        '<circle cx="34" cy="73" r="2.4" fill="#e8590c"/>'
        '<g transform="rotate(-14 88 66)">'
        '<rect x="66" y="56" width="46" height="20" fill="#fff" '
        'stroke="#c8102e" stroke-width="2.5"/>'
        '<text x="89" y="70" font-size="12" font-weight="bold" '
        'text-anchor="middle" fill="#c8102e" '
        'font-family="Georgia,serif">TAX</text></g></svg>'
    )


ART = {
    "bridge": art_bridge,
    "flags": art_flags,
    "bell": art_bell,
    "servers": art_servers,
}


def esc(text):
    return html.escape(text)


# -------------------------------------------------------------- sections

def timeline_html():
    cells = "".join(
        f'<div class="tl-cell"><div class="tl-tag">{esc(tag)}</div>'
        f'<div class="tl-text">{esc(text)}</div></div>'
        for tag, text in TIMELINE
    )
    return (
        '<div class="tl-label">THE DAY IN UTC</div>'
        f'<div class="timeline">{cells}</div>'
    )


def lead_html(kicker, headline, body, art_key):
    art = ART[art_key]()
    return (
        '<div class="lead">'
        f'<div class="kicker">{esc(kicker)}</div>'
        f'<div class="lead-art">{art}</div>'
        f'<div class="lead-head">{esc(headline)}</div>'
        f'<div class="lead-body">{esc(body)}</div>'
        "</div>"
    )


def medium_html(kicker, headline, body):
    return (
        '<div class="med">'
        f'<div class="kicker">{esc(kicker)}</div>'
        f'<div class="med-head">{esc(headline)}</div>'
        f'<div class="med-body">{esc(body)}</div>'
        "</div>"
    )


def map_svg():
    """Very stylised world map: rough continent blobs, red dots."""
    continents = [
        "M12 22 L92 16 L112 46 L96 82 L60 96 L30 76 L6 50 Z",          # N America
        "M86 106 L122 100 L136 130 L116 166 L96 150 Z",               # S America
        "M160 26 L200 20 L216 46 L190 62 L164 50 Z",                  # Europe
        "M164 76 L216 70 L236 102 L214 146 L184 150 L164 116 Z",      # Africa
        "M216 20 L320 16 L326 70 L290 96 L250 86 L230 56 L214 44 Z",   # Asia
        "M276 140 L316 134 L322 164 L286 170 Z",                     # Australia
    ]
    shapes = "".join(
        f'<path d="{d}" fill="#ecd9a4" stroke="#8a7a4a" stroke-width="1.2"/>'
        for d in continents
    )
    dots = ""
    for label, x, y in MAP_DOTS:
        dots += (
            f'<circle cx="{x}" cy="{y}" r="3.6" fill="#c8102e"/>'
            f'<text x="{x + 5}" y="{y + 3}" font-size="8.5" fill="#333" '
            f'font-family="Georgia,serif">{esc(label)}</text>'
        )
    return (
        '<svg width="330" height="190" viewBox="0 0 330 190">'
        '<rect x="0" y="0" width="330" height="190" fill="#cfe0ea"/>'
        f"{shapes}{dots}</svg>"
    )


def rest_list_html(items):
    rows = "".join(
        f'<div class="rest-row"><span class="rest-n">{n}.</span> '
        f"{esc(text)}</div>"
        for n, text in items
    )
    return f'<div class="rest-col">{rows}</div>'


# ------------------------------------------------------------------ page

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1024px; height: 1024px; background: #f7f1de;
  font-family: Georgia, 'Times New Roman', serif; color: #1a1a1a;
  padding: 10px 22px 8px 22px; overflow: hidden;
}
.masthead { text-align: center; }
.masthead h1 {
  font-size: 50px; letter-spacing: 3px; font-weight: 900; line-height: 1;
}
.dateline {
  color: #a41220; font-size: 22px; font-weight: 800;
  letter-spacing: 4px; margin-top: 4px;
}
.meta {
  display: flex; justify-content: space-between;
  color: #a41220; font-size: 13px; font-weight: 700;
  letter-spacing: 2px; margin-top: 4px;
}
.rule { border: none; border-top: 3px solid #1a1a1a; margin: 6px 0 8px 0; }
.tl-label {
  color: #a41220; font-size: 12px; font-weight: 800; letter-spacing: 2px;
}
.timeline {
  display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px;
  margin: 3px 0 9px 0;
}
.tl-cell {
  border: 1px solid #555; padding: 3px 7px 4px 7px; background: #fdfaf0;
  height: 40px; overflow: hidden;
}
.tl-tag { color: #a41220; font-size: 10px; font-weight: 800; letter-spacing: 1px; }
.tl-text { font-size: 12px; margin-top: 2px; }
.leads {
  display: grid; grid-template-columns: 1fr 1fr; gap: 0 22px;
}
.lead {
  border-top: 2px solid #1a1a1a; padding: 5px 2px 6px 2px;
  height: 132px; overflow: hidden; position: relative;
}
.kicker {
  color: #a41220; font-size: 11px; font-weight: 800; letter-spacing: 1px;
}
.lead-art { float: right; margin: 2px 0 0 8px; }
.lead-head { font-size: 22px; font-weight: 900; line-height: 1.08; margin-top: 3px; }
.lead-body { font-size: 12px; line-height: 1.32; margin-top: 4px; }
.mediums {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 0 14px;
  margin-top: 4px;
}
.med {
  border-top: 1.5px solid #1a1a1a; padding: 4px 1px 5px 1px;
  height: 84px; overflow: hidden;
}
.med-head { font-size: 13.5px; font-weight: 900; line-height: 1.12; margin-top: 2px; }
.med-body { font-size: 10px; line-height: 1.28; margin-top: 3px; }
.bottom { display: flex; gap: 16px; margin-top: 8px; }
.map-box { width: 330px; flex-shrink: 0; }
.map-title {
  color: #a41220; font-size: 12px; font-weight: 800; letter-spacing: 2px;
  margin-bottom: 3px;
}
.map-note { font-size: 9.5px; color: #555; margin-top: 2px; }
.rest-wrap { flex: 1; }
.rest-title {
  color: #a41220; font-size: 12px; font-weight: 800; letter-spacing: 1px;
  margin-bottom: 3px;
}
.rest-cols { display: flex; gap: 12px; }
.rest-col { flex: 1; }
.rest-row { font-size: 9.6px; line-height: 1.24; padding: 0.5px 0; }
.rest-n { font-weight: 800; }
.footer { border-top: 3px solid #1a1a1a; margin-top: 8px; padding-top: 5px; }
.footer .fc-tag {
  color: #a41220; font-size: 12px; font-weight: 900; letter-spacing: 1px;
}
.footer p { font-size: 11px; line-height: 1.35; margin-top: 2px; }
"""


def build_page():
    leads = "".join(
        lead_html(k, h, b, a) for k, h, b, a in LEADS
    )
    meds = "".join(
        medium_html(k, h, b) for k, h, b in MEDIUMS
    )
    first_half = REST[:17]
    second_half = REST[17:]
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>The World Today \u2014 Friday 20 November 2026</title>
<style>{CSS}</style></head>
<body>
<div class="masthead">
  <h1>THE WORLD TODAY</h1>
  <div class="dateline">FRIDAY \u00b7 20 NOVEMBER 2026</div>
</div>
<div class="meta"><span>50 STORIES</span><span>SOURCES NAMED</span></div>
<hr class="rule">
{timeline_html()}
<div class="leads">{leads}</div>
<div class="mediums">{meds}</div>
<div class="bottom">
  <div class="map-box">
    <div class="map-title">WHERE IT HAPPENED</div>
    {map_svg()}
    <div class="map-note">Stylised map \u2014 red dots mark story locations</div>
  </div>
  <div class="rest-wrap">
    <div class="rest-title">THE REST OF THE DAY \u2014 17 TO 50</div>
    <div class="rest-cols">
      {rest_list_html(first_half)}
      {rest_list_html(second_half)}
    </div>
  </div>
</div>
<div class="footer">
  <span class="fc-tag">DATE CHECK</span>
  <p>{esc(DATE_CHECK)}</p>
</div>
</body></html>
"""


def main():
    page = build_page()
    with open("build.html", "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"wrote build.html ({len(page.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
