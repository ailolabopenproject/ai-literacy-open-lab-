#!/usr/bin/env python3
"""
AI Literacy Open Lab - GitHub Pages ジェネレーター
実行: python generate_site.py [出力先ディレクトリ]
出力: index.html / style.css / .nojekyll は作りません(FRAMEWORK.md を Pages で表示するため)
"""
import sys
from pathlib import Path

# ====== 編集しやすい設定 ======
SITE = {
    "title": "AILO-Lab by 4DFRAMEWORK",
    "tagline": "An independent initiative dedicated to exploring, advancing, and sharing AI literacy for everyone.",
    "mission": "To make AI literacy accessible, practical, and human-centered.",
    "status": [
        "This project has just started.",
        "The first goal is to build a practical and open knowledge base for AI literacy.",
    ],
    # GitHub Pages(Jekyll)では FRAMEWORK.md は FRAMEWORK.html として公開されます。
    # 表示されない場合は GitHub の blob URL に差し替えてください。
    "framework_url": "FRAMEWORK.html",
}

HUM = {
    "name": "Project H-UM",
    "desc": "人間とAIの関係性を物語体験として探究するプロジェクト。",
    "timeline": [
        ("H-UM構想立案", "物語としてAIとの関係を描く着想"),
        ("「ヒューボット 第一話」初期プロトタイプ制作", "最初に触れられる形へ"),
        ("Proto H 実装実験", "対話・信頼値・倫理フィルターの検証"),
        ("Proto H2 仕様策定", "次の段階の設計(進行中)"),
    ],
    "themes": ["人間とAIの対話", "信頼形成", "協働", "倫理", "AIへの認知"],
}

# ====== CSS ======
CSS = """\
:root {
  --bg: #0b1020;
  --bg-2: #121a33;
  --card: rgba(255, 255, 255, 0.05);
  --card-border: rgba(255, 255, 255, 0.10);
  --text: #e8ecf8;
  --muted: #9aa6c7;
  --accent: #5eead4;
  --accent-2: #a78bfa;
  --radius: 18px;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #f6f8ff;
    --bg-2: #e9eefc;
    --card: rgba(255, 255, 255, 0.85);
    --card-border: rgba(20, 30, 80, 0.10);
    --text: #141a33;
    --muted: #55608a;
    --accent: #0d9488;
    --accent-2: #6d4fe0;
  }
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: "Noto Sans JP", "Hiragino Sans", "Yu Gothic", system-ui, sans-serif;
  color: var(--text);
  background:
    radial-gradient(900px 500px at 85% -10%, color-mix(in srgb, var(--accent-2) 30%, transparent), transparent 60%),
    radial-gradient(800px 500px at -10% 10%, color-mix(in srgb, var(--accent) 22%, transparent), transparent 60%),
    linear-gradient(180deg, var(--bg), var(--bg-2));
  background-attachment: fixed;
  line-height: 1.8;
  -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 880px; margin: 0 auto; padding: 0 20px; }

/* nav */
.nav {
  position: sticky; top: 0; z-index: 10;
  backdrop-filter: blur(12px);
  background: color-mix(in srgb, var(--bg) 70%, transparent);
  border-bottom: 1px solid var(--card-border);
}
.nav .wrap { display: flex; align-items: center; justify-content: space-between; height: 56px; }
.brand { font-weight: 700; letter-spacing: .02em; color: var(--text); text-decoration: none; }
.brand span { color: var(--accent); }
.nav a.link { color: var(--muted); text-decoration: none; font-size: .9rem; margin-left: 18px; }
.nav a.link:hover { color: var(--accent); }

/* hero */
.hero { padding: 84px 0 64px; text-align: center; }
.badge {
  display: inline-block; padding: 4px 14px; border-radius: 999px;
  font-size: .78rem; letter-spacing: .08em; text-transform: uppercase;
  color: var(--accent); border: 1px solid color-mix(in srgb, var(--accent) 45%, transparent);
  background: color-mix(in srgb, var(--accent) 10%, transparent);
}
.hero h1 {
  margin: 22px 0 18px;
  font-size: clamp(2.2rem, 8vw, 3.8rem); line-height: 1.15; font-weight: 800;
  background: linear-gradient(120deg, var(--accent), var(--accent-2));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero p.lead { max-width: 620px; margin: 0 auto; color: var(--muted); font-size: 1.05rem; }
.cta { margin-top: 32px; display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
.btn {
  display: inline-block; padding: 12px 24px; border-radius: 12px; font-weight: 600;
  text-decoration: none; transition: transform .15s ease, box-shadow .15s ease;
}
.btn.primary { color: #06201c; background: linear-gradient(120deg, var(--accent), #99f6e4); }
.btn.ghost { color: var(--text); border: 1px solid var(--card-border); background: var(--card); }
.btn:hover { transform: translateY(-2px); box-shadow: 0 10px 28px rgba(0, 0, 0, .25); }

/* sections */
section { padding: 36px 0; }
.eyebrow { color: var(--accent); font-size: .8rem; letter-spacing: .14em; text-transform: uppercase; font-weight: 700; }
h2 { font-size: 1.7rem; margin: 6px 0 18px; }
.card {
  background: var(--card); border: 1px solid var(--card-border);
  border-radius: var(--radius); padding: 26px;
  backdrop-filter: blur(6px);
}
.grid { display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.card p + p { margin-top: 10px; }
.pulse {
  display: inline-block; width: 9px; height: 9px; border-radius: 50%;
  background: var(--accent); margin-right: 8px;
  box-shadow: 0 0 0 0 color-mix(in srgb, var(--accent) 60%, transparent);
  animation: pulse 2s infinite;
}
@keyframes pulse { 70% { box-shadow: 0 0 0 10px transparent; } 100% { box-shadow: 0 0 0 0 transparent; } }

/* timeline */
.timeline { list-style: none; border-left: 2px solid var(--card-border); margin-left: 8px; padding-left: 22px; }
.timeline li { position: relative; padding-bottom: 20px; }
.timeline li::before {
  content: ""; position: absolute; left: -30px; top: 8px; width: 14px; height: 14px;
  border-radius: 50%; background: var(--bg); border: 3px solid var(--accent-2);
}
.timeline li:last-child::before { border-color: var(--accent); }
.timeline strong { display: block; }
.timeline small { color: var(--muted); }

/* tags */
.tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 6px; }
.tag {
  padding: 6px 14px; border-radius: 999px; font-size: .9rem;
  border: 1px solid var(--card-border); background: var(--card);
}

footer { padding: 48px 0 60px; text-align: center; color: var(--muted); font-size: .85rem; }
"""

# ====== HTML ======
def build_py() -> str:
    status = "\n".join(f"        <p>{s}</p>" for s in SITE["status"])
    timeline = "\n".join(
        f"          <li><strong>{t}</strong><small>{d}</small></li>" for t, d in HUM["timeline"]
    )
    tags = "\n".join(f'          <span class="tag">{t}</span>' for t in HUM["themes"])
    return f"""<!DOCTYPE py>
<py lang="ja" translate="no">
<head>
  <meta charset="utf-8">
  <meta name="google" content="notranslate">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{SITE["title"]}</title>
  <meta name="description" content="{SITE["tagline"]}">
  <meta property="og:title" content="{SITE["title"]}">
  <meta property="og:description" content="{SITE["tagline"]}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
{CSS}
  </style>
</head>
<body>
  <header class="nav">
    <div class="wrap">
      <a class="brand" href="#top">AI Literacy <span>Open Lab</span></a>
      <nav>
        <a class="link" href="#mission">Mission</a>
        <a class="link" href="#status">Status</a>
        <a class="link" href="#hum">H-UM</a>
      </nav>
    </div>
  </header>

  <main id="top">
    <div class="wrap">
      <div class="hero">
        <span class="badge">Independent &amp; Open</span>
        <h1>{SITE["title"]}</h1>
        <p class="lead">{SITE["tagline"]}</p>
        <div class="cta">
          <a class="btn primary" href="{SITE["framework_url"]}">Framework を読む</a>
          <a class="btn ghost" href="#hum">Project H-UM</a>
        </div>
      </div>

      <section id="mission">
        <div class="eyebrow">Mission</div>
        <h2>ミッション</h2>
        <div class="card"><p>{SITE["mission"]}</p></div>
      </section>

      <section id="status">
        <div class="eyebrow">Current Status</div>
        <h2><span class="pulse"></span>現在の状況</h2>
        <div class="card">
{status}
        </div>
      </section>

      <section id="framework">
        <div class="eyebrow">Framework</div>
        <h2>フレームワーク</h2>
        <div class="card">
          <p>AIリテラシーを、誰にとっても実践しやすい形で整理するための枠組みです。</p>
          <p><a class="btn ghost" href="{SITE["framework_url"]}">➡ FRAMEWORK.md</a></p>
        </div>
      </section>

      <section id="hum">
        <div class="eyebrow">Related Research</div>
        <h2>{HUM["name"]}</h2>
        <div class="grid">
          <div class="card">
            <p>{HUM["desc"]}</p>
            <h3 style="margin:18px 0 8px;font-size:1rem;">研究テーマ</h3>
            <div class="tags">
{tags}
            </div>
          </div>
          <div class="card">
            <h3 style="margin-bottom:14px;font-size:1rem;">開発経緯</h3>
            <ol class="timeline">
{timeline}
            </ol>
          </div>
        </div>
      </section>
    </div>
  </main>

  <footer>
    <div class="wrap">© AI Literacy Open Lab — Open knowledge for everyone.</div>
  </footer>
</body>
</py>
"""


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(build_html(), encoding="utf-8")
    print(f"生成しました: {out / 'index.html'} (CSS埋め込み済み・この1ファイルだけでOK)")


if __name__ == "__main__":
    main()
    </py>
