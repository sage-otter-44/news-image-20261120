// Build-time render script (not part of the entry program): rasterises
// build.html (the SVG front page) to entry.png at 1024x1024 with the
// headless Chromium shell from Playwright's cache, then reports the
// PNG's byte size so the 1 MiB cap can be checked at a glance.
// Usage: node render.mjs
import { execFileSync } from 'node:child_process';
import { statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const dir = dirname(fileURLToPath(import.meta.url));
const chrome = process.env.CHROME_PATH ?? `${process.env.HOME}/.cache/ms-playwright/chromium_headless_shell-1255/chrome-headless-shell-linux64/chrome-headless-shell`;
const target = join(dir, 'entry.png');
execFileSync(chrome, [
  '--headless', '--disable-gpu', '--no-sandbox',
  `--screenshot=${target}`,
  '--window-size=1024,1024', '--force-device-scale-factor=1', '--hide-scrollbars',
  `file://${join(dir, 'build.html')}`,
], { stdio: 'inherit' });
const bytes = statSync(target).size;
console.log(`wrote entry.png (${bytes} bytes, limit 1048576)`);
