// Render build.html into entry.png with headless Chromium.
//
// Usage: node render.mjs
// Reads build.html from this folder and writes entry.png (1024x1024)
// next to it. No npm packages are needed: this script drives the
// Chromium binary from the Playwright browser cache directly
// (~/.cache/ms-playwright), so it works with a bare Node install.
// The page is a local file, so nothing here touches the network.

import { execFile } from "node:child_process";
import { existsSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { promisify } from "node:util";

const run = promisify(execFile);

const folder = dirname(fileURLToPath(import.meta.url));
const pageUrl = pathToFileURL(join(folder, "build.html")).href;
const outPath = join(folder, "entry.png");

// Prefer the full Chromium build; fall back to the headless shell.
const candidates = [
  join(
    homedir(),
    ".cache/ms-playwright/chromium-1255/chrome-linux64/chrome",
  ),
  join(
    homedir(),
    ".cache/ms-playwright/chromium_headless_shell-1255/"
      + "chrome-headless-shell-linux64/chrome-headless-shell",
  ),
];

const browser = candidates.find((path) => existsSync(path));
if (!browser) {
  throw new Error(
    "no Chromium binary found under ~/.cache/ms-playwright; "
      + "install the Playwright browsers first",
  );
}

await run(browser, [
  "--headless",
  "--disable-gpu",
  "--no-sandbox",
  "--hide-scrollbars",
  "--force-device-scale-factor=1",
  "--window-size=1024,1024",
  "--virtual-time-budget=2000",
  `--screenshot=${outPath}`,
  pageUrl,
]);

console.log(`wrote ${outPath} (via ${browser})`);
