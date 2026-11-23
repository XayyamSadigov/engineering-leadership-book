// Print helper for tools/build_ebooks.py. Uses the puppeteer that @mermaid-js/mermaid-cli installs.
//
//   node print.cjs pdf   book.html  out.pdf    # 6 x 9 in PDF with outline and clickable links
//   node print.cjs cover cover.html out.png    # 1600 x 2400 EPUB cover image
//
// NODE_PATH must point at the node_modules that contains puppeteer.
const path = require("path");
const puppeteer = require("puppeteer");

async function main() {
  const [mode, src, out] = process.argv.slice(2);
  const browser = await puppeteer.launch({
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--allow-file-access-from-files"],
  });
  try {
    const page = await browser.newPage();
    if (mode === "cover") {
      await page.setViewport({ width: 800, height: 1200, deviceScaleFactor: 2 });
      await page.goto("file://" + path.resolve(src), { waitUntil: "load" });
      await page.evaluate(() => document.fonts.ready);
      await page.screenshot({ path: out, type: "png" });
    } else if (mode === "pdf") {
      // Lay out at the text-block width (6 in page minus 1.2 in margins = 4.8 in = 461 px) and
      // report anything wider: Chromium silently shrinks the whole book when one element overflows.
      await page.setViewport({ width: 461, height: 800 });
      await page.emulateMediaType("print");
      await page.goto("file://" + path.resolve(src), { waitUntil: "load", timeout: 0 });
      await page.evaluate(() => document.fonts.ready);
      const wide = await page.evaluate(() =>
        [...document.querySelectorAll("body *")]
          .filter((el) => el.getBoundingClientRect().right > 466 && el.children.length < 3)
          .slice(0, 10)
          .map((el) => el.tagName + ": " + (el.textContent || "").trim().slice(0, 70)));
      if (wide.length) {
        console.warn("WARNING: elements wider than the page; the PDF will be scaled down:\n  " + wide.join("\n  "));
      }
      await page.pdf({
        path: out,
        preferCSSPageSize: true,
        printBackground: true,
        outline: true,
        tagged: true,
        timeout: 0,
      });
    } else {
      throw new Error("unknown mode " + mode);
    }
  } finally {
    await browser.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
