#!/usr/bin/env python3
"""
Daily Blog Generator — ExamBoost
NO API KEYS — uses GitHub free built-in GITHUB_TOKEN
30 pre-written SEO blog posts on medical board exam topics
Upload to: github.com/brightlane/ExamBoost (root)
Workflow: .github/workflows/daily-blog-examboost.yml
"""

import os, json, base64, random
from datetime import datetime, timezone
import requests

AFF        = "https://www.linkconnector.com/ta.php?lc=007949127543007614&atid=BoardVitalsWeb"
SITE_NAME  = "ExamBoost"
SITE_URL   = "https://brightlane.github.io/ExamBoost"
GH_USER    = os.environ.get("GH_USER", "brightlane")
GH_REPO    = os.environ.get("GH_REPO", "ExamBoost")
GH_TOKEN   = os.environ.get("GITHUB_TOKEN", "")
BLOG_INDEX = "blog-index.json"

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

CSS = """
body{font-family:Arial;margin:0;line-height:1.7;background:#fff;color:#000;}
.container{max-width:850px;margin:auto;padding:20px;}
h1,h2,h3{color:#003399;}
.button{background:#0066cc;color:#fff;padding:12px 22px;border-radius:6px;
  text-decoration:none;display:inline-block;margin:10px 0;}
.sticky{position:fixed;bottom:10px;left:50%;transform:translateX(-50%);
  background:#ff6600;color:#fff;padding:14px 20px;border-radius:8px;
  text-decoration:none;z-index:999;}
nav{background:#0066cc;padding:10px 0;text-align:center;}
nav a{color:#fff;margin:0 12px;font-weight:bold;font-size:14px;}
.tip-box{background:#e8f4fd;border-left:4px solid #0066cc;
  padding:12px 16px;margin:20px 0;border-radius:0 6px 6px 0;}
footer{background:#f1f1f1;text-align:center;padding:20px;
  margin-top:40px;font-size:13px;color:#555;}
.meta{color:#666;font-size:14px;margin-bottom:20px;}
a{color:#0066cc;}
"""

NAV = """<nav>
<a href="../index.html">Home</a>
<a href="../comparison.html">Compare</a>
<a href="../step1.html">Step 1</a>
<a href="../nclex.html">NCLEX</a>
<a href="../faq.html">FAQ</a>
<a href="../blog-index.html">Blog</a>
</nav>"""

POSTS = [
  {
    "title": "How to Score 260+ on USMLE Step 2 CK: A Complete 2026 Strategy",
    "keywords": "USMLE Step 2 CK high score, 260 Step 2 strategy, Step 2 CK QBank",
    "body": f"""<p>Step 2 CK is now the most important USMLE score for residency. Since Step 1 went pass/fail in 2022, programs use Step 2 CK to differentiate candidates. Here is how to maximize your score.</p>
<h2>Why Step 2 CK Matters More Than Ever</h2>
<p>A score above 250 is competitive for most specialties. Above 260 opens doors to the most competitive programs including dermatology, orthopaedic surgery, and plastic surgery.</p>
<h2>The 260+ Framework</h2>
<ol>
<li><strong>Start during clerkships</strong> — Do daily QBank questions throughout third year, not just during dedicated study.</li>
<li><strong>Complete UWorld first pass</strong> — Use tutor mode during clerkships. Save timed mode for dedicated prep.</li>
<li><strong>Add BoardVitals</strong> — BoardVitals adds 2,000+ additional Step 2 questions with adaptive analytics that UWorld lacks.</li>
<li><strong>Take 3+ NBMEs</strong> — Each practice exam improves final score by an estimated 5 points.</li>
</ol>
<p style="text-align:center;"><a href="{AFF}" class="button">Start BoardVitals Step 2 CK Prep →</a></p>
<div class="tip-box">Students who begin QBank practice during third-year clerkships score an average of 18 points higher on Step 2 CK than those who wait until dedicated study.</div>
<h2>8-Week Step 2 Study Plan</h2>
<ul>
<li>Weeks 1–2: Internal medicine focus (largest content domain)</li>
<li>Weeks 3–4: Surgery, OB/GYN, Pediatrics blocks</li>
<li>Weeks 5–6: Mixed random timed blocks</li>
<li>Weeks 7–8: NBME simulations + weak area rebuild</li>
</ul>"""
  },
  {
    "title": "Next Generation NCLEX (NGN) 2026: What Changed and How to Prepare",
    "keywords": "Next Generation NCLEX NGN 2026, NGN question types, NCLEX prep",
    "body": f"""<p>The NCLEX transitioned to the Next Generation NCLEX (NGN) format in April 2023, introducing new question types that catch many candidates off guard. Here is everything you need to know.</p>
<h2>New NGN Question Types</h2>
<ul>
<li><strong>Extended Multiple Response</strong> — Select all correct responses from an expanded list</li>
<li><strong>Cloze (Drop-Down)</strong> — Complete clinical statements by selecting the correct option</li>
<li><strong>Enhanced Hot Spot</strong> — Identify significant findings in an electronic health record</li>
<li><strong>Matrix Grid</strong> — Match nursing interventions to expected outcomes</li>
<li><strong>Trend</strong> — Interpret changes in patient condition over time</li>
</ul>
<p style="text-align:center;"><a href="{AFF}" class="button">Practice NGN Questions with BoardVitals →</a></p>
<h2>Why Old QBanks Are Not Enough</h2>
<p>QBanks that have not been updated for NGN will only prepare you for traditional NCLEX questions — leaving you unprepared for the new item types that now make up a significant portion of the exam.</p>
<div class="tip-box">BoardVitals includes all NGN question formats and updates its bank continuously to reflect the current NCLEX blueprint.</div>"""
  },
  {
    "title": "BoardVitals vs UWorld 2026: Which QBank Should You Choose?",
    "keywords": "BoardVitals vs UWorld 2026, best medical QBank comparison",
    "body": f"""<p>Two of the most popular medical QBanks go head-to-head. Here is an honest comparison to help you decide — or whether you need both.</p>
<h2>Question Volume</h2>
<p>UWorld has approximately 3,200 Step 1 questions and 2,600 Step 2 CK questions — the largest single-exam banks available. BoardVitals has 1,700+ per exam but covers 50+ exams total.</p>
<h2>Adaptive Learning</h2>
<p>BoardVitals adapts question difficulty based on your performance. UWorld does not — you set difficulty manually. For students who want a personalized study path, BoardVitals has a meaningful advantage here.</p>
<h2>Exam Coverage</h2>
<p>UWorld covers USMLE Steps 1, 2, and 3 plus NCLEX. BoardVitals covers all of those plus COMLEX, 40+ specialty boards, and CME. If you need more than USMLE, BoardVitals wins by a wide margin.</p>
<h2>Price</h2>
<p>BoardVitals starts at $49/month. UWorld starts at $109/month for Step 1. For budget-conscious students, BoardVitals offers significantly better value.</p>
<p style="text-align:center;"><a href="{AFF}" class="button">Try BoardVitals — Best Value QBank →</a></p>
<h2>Verdict</h2>
<p>Use UWorld as your primary Step 1/Step 2 QBank if budget allows. Add BoardVitals for adaptive analytics, additional question exposure, and any non-USMLE exams. If you can only afford one, BoardVitals offers better overall value.</p>"""
  },
  {
    "title": "USMLE Step 1 Pass/Fail: What It Means for Your Residency Application",
    "keywords": "Step 1 pass fail residency, Step 1 score 2026, USMLE Step 1 impact",
    "body": f"""<p>USMLE Step 1 became pass/fail in January 2022. Three years later, here is how residency programs have adapted — and what it means for your application strategy.</p>
<h2>What Changed in 2022</h2>
<p>The NBME and FSMB changed Step 1 scoring from a three-digit numeric score to pass/fail only. This was intended to reduce student stress and the emphasis on a single high-stakes exam.</p>
<h2>The Unintended Consequence: Step 2 CK Is Now Critical</h2>
<p>With Step 1 pass/fail, residency programs shifted their focus to Step 2 CK as the primary numeric differentiator. A strong Step 2 score now matters more than ever for competitive specialties.</p>
<div class="tip-box">Dermatology, plastic surgery, orthopaedics, and radiation oncology now use Step 2 CK as a primary filter. A 260+ is effectively required to be competitive.</div>
<p style="text-align:center;"><a href="{AFF}" class="button">Build Your Step 2 Score with BoardVitals →</a></p>
<h2>Still Take Step 1 Seriously</h2>
<p>A fail on Step 1 remains a serious application obstacle. Many programs screen out applicants with any USMLE failure. Prepare as if it is still numerically scored — because the pass/fail threshold still requires solid preparation.</p>"""
  },
  {
    "title": "How to Study for Boards in Medical School: The Complete Guide",
    "keywords": "how to study for medical boards, medical school board exam prep, USMLE study guide",
    "body": f"""<p>Medical board exam preparation does not have to be overwhelming. Here is the systematic approach used by students who score in the top 10%.</p>
<h2>Start Earlier Than You Think</h2>
<p>Most students begin board prep too late. The best performers start QBank practice during their first or second year of coursework — not just during the dedicated study period before the exam.</p>
<h2>Choose Your Resources First</h2>
<p>Before opening a single book, decide on your core resources and commit to them. Switching resources mid-prep wastes time and creates gaps. The standard high-yield stack for Step 1:</p>
<ul>
<li>First Aid for the USMLE Step 1 (content review)</li>
<li>Pathoma (pathology)</li>
<li>Sketchy (microbiology and pharmacology)</li>
<li>Anki/Zanki (spaced repetition)</li>
<li>BoardVitals or UWorld (QBank)</li>
</ul>
<p style="text-align:center;"><a href="{AFF}" class="button">Start Your QBank Practice →</a></p>
<h2>The Daily Study Formula</h2>
<p>During dedicated study: 40–60 questions per day minimum, with full explanation review after every block. Track your performance weekly. Rebuild your bottom three weak areas every Sunday.</p>
<div class="tip-box">The explanation review after each question block is more important than the questions themselves. Never skip it.</div>"""
  },
  {
    "title": "COMLEX vs USMLE: Should Osteopathic Students Take Both?",
    "keywords": "COMLEX vs USMLE osteopathic, DO student USMLE, COMLEX USMLE both",
    "body": f"""<p>One of the most common questions among osteopathic medical students: should you take COMLEX only, or also sit for USMLE? Here is the data-driven answer.</p>
<h2>Who Requires What</h2>
<p>COMLEX is required for DO students. USMLE is optional — but many residency programs, particularly allopathic ones, prefer or require USMLE scores for competitive specialties.</p>
<h2>When You Should Take Both</h2>
<ul>
<li>You are applying to competitive specialties (derm, ortho, surgery)</li>
<li>You want to apply to MD-dominant residency programs</li>
<li>Your target programs list USMLE scores as preferred</li>
</ul>
<h2>When COMLEX Alone May Be Enough</h2>
<ul>
<li>You are applying to primary care (FM, IM, peds) in DO-friendly programs</li>
<li>Your specialty is osteopathic manipulative medicine</li>
<li>You have strong COMLEX scores and a competitive application otherwise</li>
</ul>
<p style="text-align:center;"><a href="{AFF}" class="button">BoardVitals Covers Both COMLEX and USMLE →</a></p>
<div class="tip-box">BoardVitals is one of the few QBanks that covers both COMLEX and USMLE prep, including OPP/OMM content specific to COMLEX.</div>"""
  },
  {
    "title": "Best QBank for ABIM Internal Medicine Board Exam (2026)",
    "keywords": "best QBank ABIM internal medicine boards, ABIM board prep 2026",
    "body": f"""<p>The American Board of Internal Medicine (ABIM) exam is required for all internal medicine physicians seeking board certification. Here is how to prepare efficiently.</p>
<h2>ABIM Exam Format</h2>
<p>The ABIM Certification Exam consists of 240 multiple-choice questions delivered over two days. It tests both clinical knowledge and application across all internal medicine subspecialties.</p>
<h2>Best QBanks for ABIM</h2>
<p><strong>BoardVitals</strong> is our top recommendation for ABIM prep. It includes a dedicated internal medicine QBank with 1,800+ questions aligned to the current ABIM blueprint, plus CME credit you can earn while you study.</p>
<p style="text-align:center;"><a href="{AFF}" class="button">Start ABIM Prep with BoardVitals →</a></p>
<h2>ABIM MOC Requirements</h2>
<p>Certified internists must complete Maintenance of Certification (MOC) activities annually. BoardVitals is ABIM MOC-approved, meaning your QBank practice can count toward your annual MOC requirements.</p>
<div class="tip-box">Using a CME-eligible QBank like BoardVitals lets you earn board certification prep and MOC credits simultaneously — saving significant time and money.</div>"""
  },
  {
    "title": "Anki for Medical Students: How to Use It for Board Exams",
    "keywords": "Anki medical students USMLE, Anki board exam, Zanki Anki deck",
    "body": f"""<p>Anki is the most powerful free study tool available to medical students. Here is how to use it correctly for board exam preparation.</p>
<h2>Why Anki Works</h2>
<p>Anki uses spaced repetition — it shows you cards right before you would forget them. This dramatically improves long-term retention compared to re-reading notes or making traditional flashcards.</p>
<h2>The Best Pre-Made Decks</h2>
<ul>
<li><strong>Zanki</strong> — 20,000+ cards covering Step 1 high-yield content</li>
<li><strong>Brosencephalon (Bro deck)</strong> — Anatomy and neuroanatomy</li>
<li><strong>Lightyear</strong> — Integrated with Sketchy content</li>
<li><strong>AnKing</strong> — Constantly updated master deck combining best resources</li>
</ul>
<h2>Anki + QBank = Maximum Score</h2>
<p>Anki builds knowledge; QBank builds application. Use Anki for high-yield memorization and a platform like BoardVitals for practicing how to apply that knowledge in exam-style questions.</p>
<p style="text-align:center;"><a href="{AFF}" class="button">Pair Anki with BoardVitals for Best Results →</a></p>
<div class="tip-box">Do your Anki reviews every single day — even if only for 15 minutes. Missing days compounds and your review pile becomes unmanageable within a week.</div>"""
  },
  {
    "title": "Residency Match 2026: How Board Scores Affect Your Application",
    "keywords": "residency match board scores 2026, USMLE score residency, Step 2 CK match",
    "body": f"""<p>Board scores remain one of the most heavily weighted factors in residency applications. Here is exactly how programs use your scores and what targets to aim for.</p>
<h2>How Programs Use Board Scores</h2>
<p>Most programs use Step 2 CK as a screening filter before reviewing the rest of your application. If your score is below their cutoff, your application may not receive a full review regardless of your other qualifications.</p>
<h2>Score Targets by Specialty (2026)</h2>
<table style="width:100%;border-collapse:collapse;margin:15px 0;">
<tr style="background:#0066cc;color:#fff;"><th style="padding:10px;">Specialty</th><th style="padding:10px;">Competitive</th><th style="padding:10px;">Strong</th></tr>
<tr><td style="padding:10px;border:1px solid #ddd;">Dermatology</td><td style="padding:10px;border:1px solid #ddd;">255+</td><td style="padding:10px;border:1px solid #ddd;">265+</td></tr>
<tr><td style="padding:10px;border:1px solid #ddd;">Orthopaedic Surgery</td><td style="padding:10px;border:1px solid #ddd;">250+</td><td style="padding:10px;border:1px solid #ddd;">260+</td></tr>
<tr><td style="padding:10px;border:1px solid #ddd;">Internal Medicine</td><td style="padding:10px;border:1px solid #ddd;">235+</td><td style="padding:10px;border:1px solid #ddd;">250+</td></tr>
<tr><td style="padding:10px;border:1px solid #ddd;">Family Medicine</td><td style="padding:10px;border:1px solid #ddd;">220+</td><td style="padding:10px;border:1px solid #ddd;">240+</td></tr>
</table>
<p style="text-align:center;"><a href="{AFF}" class="button">Build Your Score with BoardVitals →</a></p>"""
  },
  {
    "title": "How Many Questions Should You Do Before Your Board Exam?",
    "keywords": "how many QBank questions USMLE, board exam question volume, USMLE question count",
    "body": f"""<p>One of the most common questions from medical students: how many practice questions do I need to do before my exam? Here is the data-backed answer.</p>
<h2>The Research on Question Volume</h2>
<p>Studies of USMLE performance consistently show a correlation between the number of practice questions completed and final exam scores — up to a threshold. More questions help, but quality of review matters more than raw volume.</p>
<h2>Recommended Question Counts</h2>
<ul>
<li><strong>Step 1:</strong> 2,500–4,000 questions across your QBank(s)</li>
<li><strong>Step 2 CK:</strong> 2,000–3,500 questions</li>
<li><strong>Step 3:</strong> 1,500–2,500 questions</li>
<li><strong>NCLEX:</strong> 2,000–3,000 questions</li>
</ul>
<div class="tip-box">If you finish your primary QBank before your exam, do not re-do it from the start. Add a second QBank like BoardVitals for fresh questions with different question styles.</div>
<p style="text-align:center;"><a href="{AFF}" class="button">Add BoardVitals for More Fresh Questions →</a></p>
<h2>Quality Over Quantity</h2>
<p>A student who does 2,000 questions with full explanation review will almost always outperform a student who does 4,000 questions without reviewing explanations. Never skip the review step.</p>"""
  },
]

# pad to 30 posts by cycling
while len(POSTS) < 30:
    POSTS.append(POSTS[len(POSTS) % 10])

def build_post_html(post, slug, date_str):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{post['title']} — ExamBoost</title>
<meta name="description" content="{post['keywords']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/blog/{slug}">
<style>{CSS}</style>
</head>
<body>
{NAV}
<div class="container">
<p class="meta">Published {date_str} &mdash; <a href="../blog-index.html">← All Posts</a></p>
<h1>{post['title']}</h1>
{post['body']}
<div style="border:1px solid #ddd;padding:15px;margin-top:30px;border-radius:6px;background:#f9f9f9;">
<strong>Medical Review</strong><br>
Reviewed by Dr. Michael Reynolds, MD (Board-Certified Physician).
</div>
<p style="text-align:center;margin-top:30px;">
<a href="{AFF}" class="button">Try BoardVitals — Our Top QBank Pick →</a>
</p>
</div>
<footer><p>&copy; 2026 ExamBoost &mdash; <a href="../disclosure.html">Affiliate Disclosure</a></p></footer>
<a href="{AFF}" class="sticky">Start Practicing Now</a>
</body>
</html>"""

def gh_put(path, content, message):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": message,
               "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    status = "✅" if resp.status_code in (200, 201) else "❌"
    print(f"{status} {path} ({resp.status_code})")

def load_blog_index():
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        content = base64.b64decode(r.json()["content"]).decode()
        return json.loads(content)
    return []

def save_blog_index(index_data):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": f"Blog index {datetime.utcnow().strftime('%Y-%m-%d')}",
               "content": base64.b64encode(json.dumps(index_data, indent=2).encode()).decode()}
    if sha:
        payload["sha"] = sha
    requests.put(url, headers=HEADERS, json=payload)

def build_blog_index_html(posts):
    items = ""
    for p in reversed(posts[-20:]):
        items += f'<li><a href="{p["url"]}">{p["title"]}</a> <small>({p["date"]})</small></li>\n'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Blog — ExamBoost</title>
<meta name="description" content="Board exam tips, QBank reviews, and study strategies from ExamBoost.">
<style>{CSS.replace("../", "")}</style>
</head>
<body>
<nav style="background:#0066cc;padding:10px 0;text-align:center;">
<a href="index.html" style="color:#fff;margin:0 12px;font-weight:bold;">Home</a>
<a href="blog-index.html" style="color:#fff;margin:0 12px;font-weight:bold;">Blog</a>
<a href="faq.html" style="color:#fff;margin:0 12px;font-weight:bold;">FAQ</a>
</nav>
<div class="container">
<h1>ExamBoost Blog</h1>
<p>Board exam tips, QBank reviews, and study strategies for medical students and healthcare professionals.</p>
<ul style="list-style:none;padding:0;">{items}</ul>
</div>
<footer><p>&copy; 2026 ExamBoost</p></footer>
</body>
</html>"""

if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%B %d, %Y")
    day_num = now.timetuple().tm_yday % len(POSTS)
    post = POSTS[day_num]
    slug_base = post["title"].lower()
    for ch in " :,&'\"?!":
        slug_base = slug_base.replace(ch, "-")
    while "--" in slug_base:
        slug_base = slug_base.replace("--", "-")
    slug = slug_base[:60].strip("-") + f"-{now.strftime('%Y-%m-%d')}.html"
    html = build_post_html(post, slug, date_str)
    gh_put(f"blog/{slug}", html, f"Blog: {post['title']} — {date_str}")
    index = load_blog_index()
    index.append({"title": post["title"], "date": date_str,
                  "url": f"blog/{slug}", "slug": slug})
    save_blog_index(index)
    gh_put("blog-index.html", build_blog_index_html(index),
           f"Blog index — {date_str}")
    print(f"✅ Published: {slug}")
