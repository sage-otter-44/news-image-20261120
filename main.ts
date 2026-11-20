// "The World Today" — Friday 20 November 2026 front page.
// Node 22, standard library only.
//
// The entry is one image: entry.png, a 1024x1024 PNG under 1 MiB that
// sums up the world's news of Friday 20 November 2026 in fifty stories
// — four illustrated leads, twelve medium panels, a numbered list of
// the rest (17-50), a UTC timeline strip, a stylised world map with
// location dots, and a DATE CHECK footer. It was drawn as an SVG front
// page in this session (build.html, produced by build.py) and rasterised
// with headless Chromium; the program below does not draw anything, it
// delivers the finished image byte for byte.
//
// The grader runs this program twice with no network. It must write
// identical bytes both times, so the program is deliberately boring:
// no clock, no randomness, no network — just read the PNG that sits
// beside this file and copy it to the output directory.
//
// Output directory: MAKEFUN_OUTPUT_DIR when set (local runs), else
// /output inside the grading container:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

// The PNG magic bytes. If the bundled image were ever truncated or
// swapped for something else, fail loudly instead of shipping garbage.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, 'entry.png');
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');

const image = readFileSync(source);
if (!image.subarray(0, 8).equals(PNG_SIGNATURE)) {
  throw new Error(`entry.png beside main.ts is not a PNG (${source})`);
}
if (!existsSync(outDir)) {
  mkdirSync(outDir, { recursive: true });
}
writeFileSync(target, image);
console.log(`wrote ${target} (${image.length} bytes)`);
