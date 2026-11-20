[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/sage-otter-44/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/sage-otter-44/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World Today — Friday 20 November 2026

One image that sums up the world's news of Friday 20 November 2026,
drawn as a newspaper front page. Fifty stories, across regions and fields,
all of which happened or were first reported on 20 November 2026: four
illustrated leads, twelve medium panels, a numbered list of the rest
(17–50), a UTC timeline strip across the top, a stylised world map with
location dots, and a DATE CHECK footer. Every story is labelled with its
source; one-sided accounts are marked CLAIM.

## The four leads

1. **Russia's barrage hits Kyiv bridges** — eight killed as missiles and
   drones strike bridges over the Dnipro and knock out power. —
   Al Jazeera / Reuters
2. **UK and EU agree relations reset** — a decade after Brexit, London and
   Brussels agree steps towards closer alignment. — AP / Al Jazeera
3. **Anthropic shares slump 11% on day two** — a day after the biggest IPO
   on record, Claude's maker slides as AI fever fades. — Axios / Reuters
4. **Trump threatens data-centre tax** — US firms building data centres
   abroad face a "tremendous tax", he tells a news conference. —
   Axios / NYT

## The twelve medium panels

5. **Wall St falls 2%, VIX jumps to 28** — S&P 500 −2.02% as Fed hike fears
   grow. — Reuters
6. **KOSPI plunges 4.8%, sidecar trips** — Samsung, SK hynix slide;
   SoftBank −14% in Tokyo. — Seoul Economic Daily / AJ Bell
7. **Cyclone Akvan weakens off Odisha** — 300,000 evacuated; heavy rain in
   three states. — NDTV
8. **Saudis strike Houthis, 5 drones downed** — coalition hits Hodeidah
   and Sanaa; missile intercepted. — AP · CLAIM
9. **Myanmar rejects ICJ genocide ruling** — Naypyidaw calls Thursday's
   verdict "unfair". — Africanews
10. **No Kim meeting as Trump leaves Asia** — Seoul urges renewed US–North
    Korea dialogue. — UPI
11. **Colombia protests tax and US troops** — thousands march against tax
    plans and US military role. — Al Jazeera
12. **Malawi fuel crisis causes chaos** — shortages paralyse motorists and
    businesses. — Al Jazeera
13. **LA quake 4.2 rattles wide area** — temblor centred near Commerce at
    3:25 a.m. — LA Times
14. **Fiona the hippo dies after eating hat** — beloved zoo hippo dies days
    after swallowing a visitor's hat. — AP
15. **Consumer mood surges after midterms** — sentiment jumps; inflation,
    not jobs, blamed for hardship. — Axios
16. **Dying star swallows its companion** — a puffy star, 7× the sun's
    mass, swallows its companion. — Reuters

## The rest of the day — 17 to 50

17. Pentagon: Ukraine deep strikes "counterproductive" — NPR
18. Senate votes on data-centre permitting bill — AP
19. DOJ drops Alaska Senate challenge — AP
20. Oil up Friday, set for weekly fall — Reuters
21. EU aviation emissions plan faces Mideast pushback — Reuters
22. German youth protest military expansion — Al Jazeera
23. COP31 activists protest fossil-fuel failure — Africanews
24. Somali protesters back UAE envoy expulsion — Africanews
25. Tunisian activist Bensedrine jailed 5 years — Africanews
26. 1 in 4 children lived in conflict zones in 2025 — Save the Children
27. US protesters demand human control over AI — Africanews
28. Iraq deal: Kataib Hezbollah to pull out in a month — AP
29. Nvidia signals caution on China — Yahoo Finance
30. Hyundai unveils new Avante at LA Auto Show — Seoul Economic Daily
31. Russell Brand prison message stays on YouTube — Yahoo
32. Lindsay Clancy to face retrial next year — Yahoo
33. Gaza children swim in the sea — AP
34. Bhutan's wood-painting tradition — Africanews
35. Japan's rabbit island's dark secret — Africanews
36. Barnsley 1–2 Sheffield Wednesday — BBC Sport
37. Southend 2–3 Boreham Wood — BBC Sport
38. Cliftonville 3–2 Glentoran — BBC Sport
39. SMAT: Saurashtra stay unbeaten; Unadkat 3–23 — ESPNcricinfo
40. East Bengal 2–2 SC Delhi; Bengaluru 2–0 Mumbai City — BBC Sport
41. Shakhtar 1–1 Livyi Bereh — BBC Sport
42. Korea Cosmetics jumps 45% in two days — Seoul Economic Daily
43. STX names Jeon Jae-gon CEO — Seoul Economic Daily
44. 3.2m in Guatemala face crisis hunger — ReliefWeb
45. Gold $3,722/oz, no haven bid — Rio Times
46. US 10-year yield 5.048% — Rio Times
47. Philadelphia Fed index 6.3 vs 20 expected — Rio Times
48. Brazil Selic on hold at 13.75% — Rio Times
49. Top traders buy SK hynix as it slides 6% — Seoul Economic Daily
50. Mideast oil exports dip as Iran hits tankers — AP

## Date check

Every story above happened or was first reported on Friday 20 November
2026. Excluded on purpose: Thursday's ICJ genocide ruling (only
Myanmar's rejection today counts), the Shenzhen peace declaration,
Anthropic's $83 IPO pricing and the GTA VI launch (all 19 Nov). No
future-dated event is featured. CLAIM marks a one-sided account.

## How the program works

The entry is the image: `entry.png` is a 1024×1024 PNG (333,324 bytes,
under the 1 MiB cap), drawn as an SVG front page (`build.html`, produced
by `build.py` in this session) and rasterised with headless Chromium
(`node render.mjs`). All visuals are original drawn art; no photographs
or copied artwork.

`main.ts` (Node 22, standard library only) is the courier: it reads the
PNG beside it, checks its PNG signature, and writes the exact same bytes
to the output directory — `MAKEFUN_OUTPUT_DIR` when set, otherwise
`/output`. No network, no clock, no randomness, so both grading runs
write byte-identical output (verified: two runs, same SHA-256).

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Rebuild the image from scratch with `python3 build.py && node render.mjs`.
