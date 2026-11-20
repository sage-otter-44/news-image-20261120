// The World Today — Friday 20 November 2026.
//
// This program is only a courier. The entry is the image that sits next
// to it, entry.png: a 1024x1024 front page summing up the world's news
// of Friday 20 November 2026 in fifty stories. The program reads that
// file, makes sure it really is a PNG, and copies its bytes unchanged
// into the output directory.
//
// The grader runs this program twice with no network access. The two
// runs must write identical bytes, so there is deliberately nothing
// clever here: no clock, no randomness, no network calls, no
// environment-dependent branches. Same input file, same output bytes.
//
// Output directory: the MAKEFUN_OUTPUT_DIR environment variable when it
// is set, otherwise /output (the grading container's output folder).
// Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Every PNG file starts with these eight magic bytes. If the bundled
// image was ever truncated or replaced, refuse loudly instead of
// handing the grader a broken file.
const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

const folder = dirname(fileURLToPath(import.meta.url));
const sourcePath = join(folder, "entry.png");
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const targetPath = join(outputDir, "entry.png");

const bytes = readFileSync(sourcePath);

for (let i = 0; i < PNG_MAGIC.length; i++) {
  if (bytes[i] !== PNG_MAGIC[i]) {
    throw new Error(
      `entry.png beside main.ts is not a PNG (checked ${sourcePath})`,
    );
  }
}

if (!existsSync(outputDir)) {
  mkdirSync(outputDir, { recursive: true });
}

writeFileSync(targetPath, bytes);
console.log(`wrote ${targetPath} (${bytes.length} bytes)`);
