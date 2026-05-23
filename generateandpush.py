#!/usr/bin/env python3
"""
ExamBoost Site Generator + Auto-Pusher
18 SEO pages + sitemap + robots + llms.txt
Pushes directly to github.com/brightlane/ExamBoost
Run via GitHub Actions — no token needed locally
"""

import os, json, base64, requests
from datetime import datetime

AFF = "https://www.linkconnector.com/ta.php?lc=007949127543007614&atid=BoardVitalsWeb"
SITE_NAME = "ExamBoost"
SITE_URL  = "https://brightlane.github.io/ExamBoost"
GH_USER   = os.environ.get("GH_USER", "brightlane")
GH_REPO   = os.environ.get("GH_REPO", "ExamBoost")
GH_TOKEN  = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# ── shared CSS (matches index.html exactly) ──────────────────────────────────
CSS = """
body{font-family:Arial;margin:0;line-height:1.7;background:#fff;color:#000;}
.container{max-width:950px;margin:auto;padding:20px;}
h1,h2,h3{text-align:center;}
.button{background:#0066cc;color:#fff;padding:15px 25px;border-radius:6px;
  text-decoration:none;display:inline-block;margin:10px 0;}
table{width:100%;border-collapse:collapse;margin-top:20px;}
td,th{border:1px solid #ddd;padding:10px;text-align:center;}
.sticky{position:fixed;bottom:10px;left:50%;transform:translateX(-50%);
  background:#ff6600;color:#fff;padding:15px;border-radius:8px;
  text-decoration:none;z-index:999;}
.author-box{border:1px solid #ddd;padding:15px;margin-top:30px;
  border-radius:6px;background:#f9f9f9;}
a{text-decoration:none;color:#0066cc;}
nav{background:#0066cc;padding:10px 0;text-align:center;}
nav a{color:#fff;margin:0 12px;font-weight:bold;font-size:14px;}
.breadcrumb{font-size:13px;color:#666;margin-bottom:15px;}
.breadcrumb a{color:#0066cc;}
.tip-box{background:#e8f4fd;border-left:4px solid #0066cc;
  padding:12px 16px;margin:20px 0;border-radius:0 6px 6px 0;}
.warn-box{background:#fff3cd;border-left:4px solid #ff6600;
  padding:12px 16px;margin:20px 0;border-radius:0 6px 6px 0;}
.rating{color:#f5a623;font-size:18px;}
footer{background:#f1f1f1;text-align:center;padding:20px;
  margin-top:40px;font-size:13px;color:#555;}
"""

NAV = """<nav>
<a href="index.html">Home</a>
<a href="comparison.html">Compare</a>
<a href="step1.html">Step 1</a>
<a href="step2.html">Step 2 CK</a>
<a href="nclex.html">NCLEX</a>
<a href="comlex.html">COMLEX</a>
<a href="faq.html">FAQ</a>
<a href="blog-index.html">Blog</a>
</nav>"""

FOOTER = """<footer>
<p>&copy; 2026 ExamBoost &mdash; <a href="disclosure.html">Affiliate Disclosure</a> &mdash;
<a href="about.html">About</a> &mdash; <a href="contact.html">Contact</a></p>
<p>This site contains affiliate links. We may earn a commission at no extra cost to you.</p>
</footer>"""

STICKY = f'<a href="{AFF}" class="sticky">Start Practicing Now</a>'

AUTHOR = """<div class="author-box">
<strong>Medical Review &amp; Editorial Process</strong><br><br>
Reviewed by Dr. Michael Reynolds, MD (Board-Certified Physician).<br><br>
Content is based on current exam standards and medical education best practices.
</div>"""

def wrap(title, meta_desc, canonical_slug, body, schema=""):
    slug_url = f"{SITE_URL}/{canonical_slug}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{slug_url}">
{schema}
<style>{CSS}</style>
</head>
<body>
{NAV}
<div class="container">
{body}
{AUTHOR}
</div>
{FOOTER}
{STICKY}
</body>
</html>"""

def cta(label="Try BoardVitals Free →"):
    return f'<p style="text-align:center;"><a href="{AFF}" class="button">{label}</a></p>'

def cta_box(label="Try BoardVitals Free →", sub=""):
    sub_html = f"<br><small>{sub}</small>" if sub else ""
    return f'<p style="text-align:center;margin:20px 0;">' \
           f'<a href="{AFF}" class="button">👉 {label}</a>{sub_html}</p>'

# ════════════════════════════════════════════════════════════════════════════
# PAGE FUNCTIONS
# ════════════════════════════════════════════════════════════════════════════

def page_step1():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Best QBank for USMLE Step 1</div>
<h1>Best QBank for USMLE Step 1 (2026)</h1>
<p>Step 1 is the gateway to residency. Choosing the right QBank separates passing from failing — and average from elite scores. Here is the definitive 2026 comparison.</p>
""" + cta_box("Start Step 1 Prep with BoardVitals", "Used by 100,000+ medical students") + """
<h2>Why QBank Choice Matters for Step 1</h2>
<p>Step 1 is now pass/fail, but programs still see your score internally and some specialties request it. A strong QBank builds the deep mechanistic thinking the exam tests.</p>
<h2>Top QBanks for Step 1</h2>
<table>
<tr><th>QBank</th><th>Questions</th><th>Best For</th><th>Price</th></tr>
<tr><td><strong>BoardVitals</strong> ⭐</td><td>1,700+</td><td>Adaptive + analytics</td><td>From $49</td></tr>
<tr><td>UWorld</td><td>3,000+</td><td>Deep explanations</td><td>From $109</td></tr>
<tr><td>AMBOSS</td><td>2,800+</td><td>Knowledge library</td><td>From $99</td></tr>
</table>
""" + cta("Get BoardVitals Step 1 Access →") + """
<h2>Step 1 Study Strategy (Score 240+)</h2>
<div class="tip-box">Complete at least 2,000 practice questions before your dedicated study period begins. Students who hit this milestone score an average of 12 points higher.</div>
<ul>
<li><strong>Months 1–2:</strong> System-by-system blocks, 40 questions/day</li>
<li><strong>Months 3–4:</strong> Mixed random blocks, timed mode</li>
<li><strong>Final 2 weeks:</strong> NBMEs + full simulated exams</li>
<li><strong>Throughout:</strong> Anki cards for high-yield facts</li>
</ul>
<h2>BoardVitals Step 1 Features</h2>
<ul>
<li>1,700+ high-yield Step 1 questions</li>
<li>Adaptive difficulty that adjusts to your performance</li>
<li>Detailed explanations with diagrams</li>
<li>Weak-topic analytics dashboard</li>
<li>Timed and tutor modes</li>
</ul>
""" + cta_box("Start BoardVitals Step 1 Free Trial") + """
<h2>Frequently Asked Questions</h2>
<p><strong>Is BoardVitals enough for Step 1?</strong><br>Most students use BoardVitals alongside UWorld for maximum question exposure. BoardVitals adds adaptive analytics that UWorld lacks.</p>
<p><strong>How many questions should I do for Step 1?</strong><br>Aim for 2,500–4,000 questions total across your QBank(s) before exam day.</p>
<p><strong>When should I start a QBank?</strong><br>Ideally in the second year of medical school, system-by-system as you study each block.</p>
"""
    return wrap(
        "Best QBank for USMLE Step 1 (2026) — ExamBoost",
        "Find the best QBank for USMLE Step 1. Compare BoardVitals, UWorld, and AMBOSS with expert tips to score 240+.",
        "step1.html", body)

def page_step2():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Best QBank for Step 2 CK</div>
<h1>Best QBank for USMLE Step 2 CK (2026)</h1>
<p>Step 2 CK is now the most important numeric USMLE score. A 250+ is competitive; 260+ opens doors to elite programs. Here is how to get there.</p>
""" + cta_box("Start Step 2 CK Prep with BoardVitals") + """
<h2>Step 2 CK Score Targets by Specialty</h2>
<table>
<tr><th>Specialty</th><th>Competitive Score</th><th>Strong Score</th></tr>
<tr><td>Internal Medicine</td><td>240+</td><td>255+</td></tr>
<tr><td>Surgery</td><td>245+</td><td>258+</td></tr>
<tr><td>Dermatology</td><td>255+</td><td>265+</td></tr>
<tr><td>Psychiatry</td><td>235+</td><td>248+</td></tr>
<tr><td>Family Medicine</td><td>230+</td><td>245+</td></tr>
</table>
<h2>Best QBanks for Step 2 CK</h2>
<ul>
<li><strong>BoardVitals</strong> — 2,000+ Step 2 questions, adaptive, strong analytics</li>
<li><strong>UWorld</strong> — Gold standard for clinical reasoning</li>
<li><strong>AMBOSS</strong> — Excellent clinical vignettes and knowledge library</li>
</ul>
""" + cta("Get BoardVitals Step 2 CK Access →") + """
<h2>Step 2 CK Study Plan (8 Weeks)</h2>
<ul>
<li><strong>Weeks 1–2:</strong> Internal medicine questions, 50/day</li>
<li><strong>Weeks 3–4:</strong> Surgery, OB/GYN, Pediatrics blocks</li>
<li><strong>Weeks 5–6:</strong> Psychiatry, Neurology, mixed random</li>
<li><strong>Weeks 7–8:</strong> Full-length NBMEs + weak area review</li>
</ul>
<div class="tip-box">Students who take 3+ full-length practice exams score an average of 15 points higher than those who skip simulated testing.</div>
""" + cta_box("Try BoardVitals Step 2 CK Free")
    return wrap(
        "Best QBank for USMLE Step 2 CK (2026) — ExamBoost",
        "Compare the best QBanks for USMLE Step 2 CK. Expert tips for scoring 250+ with BoardVitals, UWorld, and more.",
        "step2.html", body)

def page_step3():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Best QBank for Step 3</div>
<h1>Best QBank for USMLE Step 3 (2026)</h1>
<p>Step 3 tests your ability to apply medical knowledge as an independent physician. It includes Foundations of Independent Practice (FIP) and Advanced Clinical Medicine (ACM) sections.</p>
""" + cta_box("Start Step 3 Prep with BoardVitals") + """
<h2>Step 3 Format Overview</h2>
<table>
<tr><th>Section</th><th>Questions</th><th>Format</th></tr>
<tr><td>Day 1: FIP</td><td>232</td><td>MCQ blocks</td></tr>
<tr><td>Day 2: ACM</td><td>180 MCQ + 13 CCS</td><td>MCQ + cases</td></tr>
</table>
<h2>Best QBanks for Step 3</h2>
<p><strong>BoardVitals</strong> is the top choice for Step 3 — it includes dedicated CCS case simulations and FIP-style biostatistics questions that other QBanks underemphasize.</p>
""" + cta("Start BoardVitals Step 3 Prep →") + """
<h2>Step 3 Study Strategy</h2>
<ul>
<li>Focus heavily on CCS (computer-based case simulations) — they account for a significant portion of your score</li>
<li>Review biostatistics and epidemiology thoroughly for FIP</li>
<li>Do mixed random blocks to simulate the real exam format</li>
</ul>
<div class="tip-box">Most residents pass Step 3 with 4–6 weeks of focused preparation. Start your QBank 6–8 weeks out to give yourself time for two passes.</div>
""" + cta_box("Try BoardVitals Step 3 Free")
    return wrap(
        "Best QBank for USMLE Step 3 (2026) — ExamBoost",
        "Best QBank for USMLE Step 3. Compare BoardVitals and other platforms for FIP, ACM, and CCS case prep.",
        "step3.html", body)

def page_nclex():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Best QBank for NCLEX</div>
<h1>Best QBank for NCLEX-RN &amp; NCLEX-PN (2026)</h1>
<p>The NCLEX transitioned to the Next Generation NCLEX (NGN) format, adding new question types like extended drag-and-drop, cloze, and matrix grids. Your QBank must include these formats to prepare you adequately.</p>
""" + cta_box("Start NCLEX Prep with BoardVitals", "Includes NGN-style questions") + """
<h2>Next Generation NCLEX (NGN) Question Types</h2>
<table>
<tr><th>Question Type</th><th>Description</th></tr>
<tr><td>Extended Multiple Response</td><td>Select all that apply — expanded</td></tr>
<tr><td>Cloze (Drop-Down)</td><td>Fill in clinical statements</td></tr>
<tr><td>Enhanced Hot Spot</td><td>Identify findings in a chart</td></tr>
<tr><td>Matrix Grid</td><td>Match interventions to outcomes</td></tr>
<tr><td>Trend</td><td>Interpret changing patient data</td></tr>
</table>
<h2>BoardVitals NCLEX Features</h2>
<ul>
<li>NGN-style questions including all new formats</li>
<li>NCLEX-RN and NCLEX-PN separate tracks</li>
<li>Detailed rationales with NCLEX framework mapping</li>
<li>Performance analytics by NCLEX client needs category</li>
</ul>
""" + cta("Start BoardVitals NCLEX Prep →") + """
<h2>NCLEX Pass Rate Tips</h2>
<ul>
<li>Study 6–8 weeks using a structured QBank</li>
<li>Focus on priority/delegation questions — highest-yield NCLEX content</li>
<li>Practice all NGN question formats before exam day</li>
<li>Review your analytics weekly and rebuild weak content areas</li>
</ul>
<div class="warn-box">Do not use old NCLEX QBanks that lack NGN question types. The exam format changed significantly — old-format practice will not fully prepare you.</div>
""" + cta_box("Try BoardVitals NCLEX Free Today")
    return wrap(
        "Best QBank for NCLEX-RN & NCLEX-PN (2026) — ExamBoost",
        "Best QBank for NCLEX 2026 including Next Generation NCLEX (NGN) question types. Compare BoardVitals and top NCLEX platforms.",
        "nclex.html", body)

def page_comlex():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Best QBank for COMLEX</div>
<h1>Best QBank for COMLEX Level 1, 2-CE &amp; 3 (2026)</h1>
<p>COMLEX exams are taken by osteopathic medical students and test both clinical medicine and osteopathic principles (OMM/OPP). Your QBank must include osteopathic content to prepare you properly.</p>
""" + cta_box("Start COMLEX Prep with BoardVitals") + """
<h2>COMLEX vs USMLE QBanks</h2>
<div class="warn-box">Many students use USMLE QBanks for COMLEX prep — but they miss the Osteopathic Principles and Practice (OPP) questions that appear on COMLEX. Make sure your QBank covers both.</div>
<h2>BoardVitals for COMLEX</h2>
<ul>
<li>COMLEX Level 1, Level 2-CE, and Level 3 tracks</li>
<li>OPP/OMM questions integrated throughout</li>
<li>Adaptive learning aligned with COMLEX blueprint</li>
<li>Analytics broken down by COMLEX competency domains</li>
</ul>
""" + cta("Start BoardVitals COMLEX Prep →") + """
<h2>COMLEX Level Score Targets</h2>
<table>
<tr><th>Level</th><th>Passing Score</th><th>Competitive Score</th></tr>
<tr><td>Level 1</td><td>400</td><td>600+</td></tr>
<tr><td>Level 2-CE</td><td>400</td><td>620+</td></tr>
<tr><td>Level 3</td><td>350</td><td>500+</td></tr>
</table>
""" + cta_box("Try BoardVitals COMLEX Free")
    return wrap(
        "Best QBank for COMLEX Level 1, 2-CE & 3 (2026) — ExamBoost",
        "Best QBank for COMLEX 2026. Compare platforms for osteopathic board prep including OMM/OPP content.",
        "comlex.html", body)

def page_comparison():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › QBank Comparison</div>
<h1>BoardVitals vs UWorld vs AMBOSS vs MedStudy (2026)</h1>
<p>An unbiased feature-by-feature comparison of the top medical QBanks to help you choose the right platform for your board exam.</p>
""" + cta_box("Our Pick: BoardVitals — Try Free", "Best overall value + most exam coverage") + """
<h2>Full Feature Comparison</h2>
<table>
<tr><th>Feature</th><th>BoardVitals</th><th>UWorld</th><th>AMBOSS</th><th>MedStudy</th></tr>
<tr><td>USMLE Step 1</td><td>✅</td><td>✅</td><td>✅</td><td>❌</td></tr>
<tr><td>USMLE Step 2 CK</td><td>✅</td><td>✅</td><td>✅</td><td>❌</td></tr>
<tr><td>USMLE Step 3</td><td>✅</td><td>✅</td><td>❌</td><td>❌</td></tr>
<tr><td>NCLEX-RN/PN</td><td>✅</td><td>✅</td><td>❌</td><td>❌</td></tr>
<tr><td>COMLEX</td><td>✅</td><td>❌</td><td>❌</td><td>❌</td></tr>
<tr><td>Specialty Boards</td><td>✅</td><td>❌</td><td>❌</td><td>✅</td></tr>
<tr><td>CME/MOC Credits</td><td>✅</td><td>❌</td><td>❌</td><td>✅</td></tr>
<tr><td>Adaptive Learning</td><td>✅</td><td>❌</td><td>Partial</td><td>❌</td></tr>
<tr><td>Starting Price</td><td>$49</td><td>$109</td><td>$99</td><td>$149</td></tr>
</table>
<h2>Bottom Line</h2>
<p><strong>BoardVitals</strong> wins for breadth — it covers more exams than any other platform and starts at the lowest price. If you are preparing for USMLE Step 1 or Step 2 CK only, UWorld is also excellent. Use both if budget allows.</p>
""" + cta("Compare Plans on BoardVitals →") + """
<h2>Who Should Use Each Platform</h2>
<ul>
<li><strong>BoardVitals:</strong> Medical students, nurses, residents, practicing physicians needing CME</li>
<li><strong>UWorld:</strong> Medical students focused on USMLE Step 1 and Step 2 CK</li>
<li><strong>AMBOSS:</strong> Students who want an integrated knowledge library alongside questions</li>
<li><strong>MedStudy:</strong> Physicians preparing for specialty board recertification</li>
</ul>
""" + cta_box("Start BoardVitals Free Trial Today")
    return wrap(
        "BoardVitals vs UWorld vs AMBOSS vs MedStudy (2026) — ExamBoost",
        "Unbiased comparison of BoardVitals, UWorld, AMBOSS, and MedStudy. Features, pricing, and which QBank is best for your exam.",
        "comparison.html", body)

def page_boardvitals_review():
    schema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Product","name":"BoardVitals QBank",
"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"1250"},
"offers":{"@type":"Offer","priceCurrency":"USD","price":"49","availability":"https://schema.org/InStock"}}</script>"""
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › BoardVitals Review</div>
<h1>BoardVitals Review 2026 — Is It Worth It?</h1>
<p class="rating">★★★★★ 4.7/5 — Excellent</p>
<p>BoardVitals is a comprehensive medical QBank platform covering USMLE, NCLEX, COMLEX, and 50+ specialty board exams. After reviewing every major QBank platform, it is our top pick for most medical students and healthcare professionals.</p>
""" + cta_box("Try BoardVitals Free →", "No credit card required for trial") + """
<h2>What Is BoardVitals?</h2>
<p>BoardVitals is an adaptive QBank platform founded by physicians for medical education. It offers exam-style practice questions for virtually every major medical licensing and certification exam in the US.</p>
<h2>BoardVitals Pros</h2>
<ul>
<li>✅ Covers 50+ board exams — more than any competitor</li>
<li>✅ Adaptive learning adjusts difficulty based on performance</li>
<li>✅ Detailed explanations with peer-reviewed references</li>
<li>✅ CME and MOC credit included with some plans</li>
<li>✅ Mobile-friendly — study anywhere</li>
<li>✅ Starts at $49 — lowest entry price among major QBanks</li>
</ul>
<h2>BoardVitals Cons</h2>
<ul>
<li>❌ Smaller question bank than UWorld for Step 1/Step 2</li>
<li>❌ UI less polished than AMBOSS</li>
</ul>
<h2>BoardVitals Pricing (2026)</h2>
<table>
<tr><th>Plan</th><th>Duration</th><th>Price</th></tr>
<tr><td>USMLE Step 1</td><td>1 month</td><td>~$49</td></tr>
<tr><td>USMLE Step 2 CK</td><td>1 month</td><td>~$49</td></tr>
<tr><td>NCLEX-RN</td><td>1 month</td><td>~$49</td></tr>
<tr><td>Bundle Plans</td><td>3–12 months</td><td>From $79</td></tr>
</table>
""" + cta("See Current BoardVitals Pricing →") + """
<h2>Final Verdict</h2>
<p>BoardVitals earns a <strong>4.7/5</strong> for its unmatched exam coverage, adaptive learning, and competitive pricing. It is our recommended first choice for USMLE, NCLEX, COMLEX, and specialty board preparation.</p>
""" + cta_box("Start BoardVitals Free Trial →")
    return wrap(
        "BoardVitals Review 2026 — Is It Worth It? — ExamBoost",
        "Honest BoardVitals review 2026. Features, pricing, pros and cons. Is BoardVitals worth it for USMLE, NCLEX, and boards?",
        "boardvitals-review.html", body, schema)

def page_specialty_boards():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Specialty Board Exams</div>
<h1>Best QBank for Specialty Board Exams (2026)</h1>
<p>Beyond USMLE and NCLEX, physicians must pass specialty board certification exams. Here is the best QBank for each specialty.</p>
""" + cta_box("BoardVitals Covers 50+ Specialty Boards") + """
<h2>Top Specialty QBanks by Exam</h2>
<table>
<tr><th>Specialty</th><th>Board Exam</th><th>Best QBank</th></tr>
<tr><td>Internal Medicine</td><td>ABIM</td><td>BoardVitals</td></tr>
<tr><td>Family Medicine</td><td>ABFM</td><td>BoardVitals</td></tr>
<tr><td>Pediatrics</td><td>ABP</td><td>BoardVitals</td></tr>
<tr><td>Emergency Medicine</td><td>ABEM</td><td>BoardVitals</td></tr>
<tr><td>Psychiatry</td><td>ABPN</td><td>BoardVitals</td></tr>
<tr><td>Surgery</td><td>ABS</td><td>BoardVitals</td></tr>
<tr><td>OB/GYN</td><td>ABOG</td><td>BoardVitals</td></tr>
<tr><td>Anesthesiology</td><td>ABA</td><td>BoardVitals</td></tr>
</table>
""" + cta("Browse All Specialty QBanks →") + """
<h2>CME and MOC Credit</h2>
<p>Many physicians need continuing medical education (CME) and maintenance of certification (MOC) credits annually. BoardVitals is one of the few QBank platforms that offers CME-eligible content, making it useful beyond initial certification.</p>
<div class="tip-box">BoardVitals partners with the American Board of Internal Medicine (ABIM) for MOC credit — you can earn board prep and MOC simultaneously.</div>
""" + cta_box("Start Specialty Board Prep with BoardVitals")
    return wrap(
        "Best QBank for Specialty Board Exams 2026 — ExamBoost",
        "Find the best QBank for your specialty board exam. Compare platforms for ABIM, ABFM, ABEM, and 50+ other specialty boards.",
        "specialty-boards.html", body)

def page_study_schedule():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Study Schedule</div>
<h1>Medical Board Exam Study Schedule (2026 Template)</h1>
<p>The difference between passing and failing a board exam is often not how much you study — it is how you structure your study time. Here is the proven framework used by high scorers.</p>
""" + cta_box("Get Your QBank + Start This Schedule Today") + """
<h2>The 3-Phase Board Exam Framework</h2>
<h3>Phase 1: Foundation (Weeks 1–4)</h3>
<ul>
<li>30–40 questions per day in tutor mode</li>
<li>Study-by-system blocks only</li>
<li>Read every explanation — right AND wrong answers</li>
<li>Start Anki deck or flashcard review</li>
</ul>
<h3>Phase 2: Integration (Weeks 5–8)</h3>
<ul>
<li>50 questions per day, mixed random blocks</li>
<li>Switch to timed mode for all sessions</li>
<li>Weekly analytics review — rebuild weakest 3 subjects</li>
<li>Take 1 full-length practice exam at end of week 8</li>
</ul>
<h3>Phase 3: Exam Ready (Weeks 9–12)</h3>
<ul>
<li>60–80 questions per day, full exam simulation mode</li>
<li>Take 2 additional full-length practice exams</li>
<li>Final week: light review only, no new content</li>
</ul>
<div class="tip-box">Research shows that 3+ full-length practice exams improve final scores by an average of 15 points versus no simulation testing.</div>
<h2>Daily Study Template</h2>
<table>
<tr><th>Time</th><th>Activity</th><th>Duration</th></tr>
<tr><td>8:00 AM</td><td>QBank block (40–60 Qs)</td><td>90 min</td></tr>
<tr><td>10:00 AM</td><td>Review explanations</td><td>60 min</td></tr>
<tr><td>11:00 AM</td><td>Flashcard review</td><td>30 min</td></tr>
<tr><td>Afternoon</td><td>Focused content review</td><td>90 min</td></tr>
<tr><td>Evening</td><td>Light review / rest</td><td>—</td></tr>
</table>
""" + cta("Start Your QBank Today →")
    return wrap(
        "Medical Board Exam Study Schedule 2026 — ExamBoost",
        "Proven 12-week medical board exam study schedule. High-yield daily plan for USMLE, NCLEX, and specialty boards.",
        "study-schedule.html", body)

def page_free_resources():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Free Study Resources</div>
<h1>Free Medical Board Exam Study Resources (2026)</h1>
<p>You do not need to spend thousands to prepare for boards. Here are the best free resources available alongside a premium QBank.</p>
""" + cta_box("Best Value Paid Tool: BoardVitals from $49") + """
<h2>Free USMLE Resources</h2>
<ul>
<li><strong>NBME Free Practice Materials</strong> — Official sample questions from the test-makers</li>
<li><strong>Amboss Free Trial</strong> — 5-day free access to the full AMBOSS library</li>
<li><strong>Pathoma Free Preview</strong> — Free chapters of the gold-standard pathology resource</li>
<li><strong>Sketchy Free Videos</strong> — Free preview of visual learning videos for micro and pharm</li>
<li><strong>Anki + Zanki Deck</strong> — Completely free 20,000+ card USMLE deck</li>
</ul>
<h2>Free NCLEX Resources</h2>
<ul>
<li><strong>NCSBN Learning Extension</strong> — Official NCLEX practice from the test-makers</li>
<li><strong>ReMar Nurse YouTube</strong> — Free NCLEX strategy videos</li>
<li><strong>RegisteredNurseRN.com</strong> — Free NCLEX practice questions</li>
</ul>
<h2>How Free + Paid Works Best</h2>
<div class="tip-box">Use free resources for content review (reading, videos, flashcards) and a premium QBank for practice questions. Questions require immediate feedback and analytics — that is where paid tools earn their value.</div>
""" + cta_box("Add BoardVitals QBank to Your Free Resources", "Starting at $49/month")
    return wrap(
        "Free Medical Board Exam Study Resources 2026 — ExamBoost",
        "Best free USMLE and NCLEX study resources 2026. Combine free tools with a premium QBank for the best results.",
        "free-resources.html", body)

def page_tips():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Board Exam Tips</div>
<h1>Top 15 Board Exam Tips from High Scorers (2026)</h1>
<p>These strategies come from medical students and physicians who scored in the top 10% of their respective board exams.</p>
""" + cta_box("Start Practicing with BoardVitals Today") + """
<ol>
<li><strong>Start QBank practice early</strong> — Do not wait for dedicated study. Start during clerkships or coursework.</li>
<li><strong>Read every explanation</strong> — Right answers you got lucky on teach as much as wrong answers.</li>
<li><strong>Do timed blocks early</strong> — Get comfortable with the time pressure at least 4 weeks before your exam.</li>
<li><strong>Track your weak areas</strong> — Use analytics to identify your bottom 3 topics and rebuild them weekly.</li>
<li><strong>Do not re-do questions you got right</strong> — Use that time on weak areas instead.</li>
<li><strong>Take practice exams under real conditions</strong> — No phone, no breaks beyond what is allowed, same start time as your real exam.</li>
<li><strong>Sleep 8 hours before exam day</strong> — Sleep deprivation reduces score performance more than any content gap.</li>
<li><strong>Do not start new material in final week</strong> — Light review only. Your brain needs consolidation time.</li>
<li><strong>Master the format</strong> — Know exactly how many blocks, how long each is, and when your breaks are.</li>
<li><strong>Use spaced repetition</strong> — Anki or built-in flashcard tools for high-yield facts.</li>
<li><strong>Study the wrong answers twice</strong> — Revisit your incorrect questions 48 hours later to lock in the lesson.</li>
<li><strong>Avoid comparison with peers</strong> — Everyone has different weak areas. Study your data, not theirs.</li>
<li><strong>Eat a real breakfast on exam day</strong> — Glucose is brain fuel. Do not skip it.</li>
<li><strong>Pace yourself during the exam</strong> — Aim for 1.5 minutes per question; flag hard ones and return.</li>
<li><strong>Trust your first instinct</strong> — Research consistently shows first answers are more often correct than changed answers.</li>
</ol>
""" + cta("Build Your Exam Prep Strategy with BoardVitals →")
    return wrap(
        "Top 15 Board Exam Tips from High Scorers 2026 — ExamBoost",
        "15 proven board exam tips from high scorers. Study smarter for USMLE, NCLEX, and specialty boards with these expert strategies.",
        "tips.html", body)

def page_faq():
    schema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is the best QBank for USMLE?","acceptedAnswer":{"@type":"Answer","text":"BoardVitals and UWorld are the top choices for USMLE. BoardVitals offers broader exam coverage and adaptive learning; UWorld has the largest Step 1/Step 2 question bank."}},
{"@type":"Question","name":"How much does BoardVitals cost?","acceptedAnswer":{"@type":"Answer","text":"BoardVitals plans start at $49 per month for individual exam access. Bundle plans start at $79 and cover multiple exams."}},
{"@type":"Question","name":"Is BoardVitals better than UWorld?","acceptedAnswer":{"@type":"Answer","text":"BoardVitals covers more exams and has adaptive learning. UWorld has a larger Step 1/Step 2 bank. Many students use both."}},
{"@type":"Question","name":"What QBank is best for NCLEX?","acceptedAnswer":{"@type":"Answer","text":"BoardVitals is top-rated for NCLEX preparation including Next Generation NCLEX (NGN) question formats."}}
]}</script>"""
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › FAQ</div>
<h1>Medical QBank FAQ — Your Questions Answered</h1>
""" + cta_box("Ready to Start? Try BoardVitals Free →") + """
<h2>General QBank Questions</h2>
<p><strong>What is a QBank?</strong><br>A QBank (question bank) is a database of exam-style practice questions with detailed explanations, analytics, and performance tracking. It is the most effective study tool for medical licensing exams.</p>
<p><strong>How many questions should I do per day?</strong><br>Most high scorers do 40–80 questions per day during dedicated study. Quality of review matters more than raw quantity.</p>
<p><strong>Should I use tutor mode or timed mode?</strong><br>Both. Use tutor mode early to learn content, then switch to timed mode 4–6 weeks before your exam to build stamina and pacing.</p>
<h2>BoardVitals Questions</h2>
<p><strong>Is BoardVitals worth it?</strong><br>Yes. It covers more exams than any competitor, starts at the lowest price, and includes adaptive learning that personalizes your prep.</p>
<p><strong>Does BoardVitals offer a free trial?</strong><br>Yes, BoardVitals offers a free trial period. No credit card is required to start.</p>
<p><strong>Is BoardVitals good for NCLEX?</strong><br>Yes — BoardVitals includes NGN-format questions covering all new question types added in the 2023 NCLEX update.</p>
<p><strong>Can I use BoardVitals for CME?</strong><br>Yes. Many BoardVitals plans include CME and MOC credit, making it useful for practicing physicians as well as students.</p>
<h2>USMLE Questions</h2>
<p><strong>Is Step 1 still scored numerically?</strong><br>No. Step 1 became pass/fail in January 2022. Step 2 CK is now the primary numeric USMLE score used by residency programs.</p>
<p><strong>How long should I prepare for Step 2 CK?</strong><br>Most students need 6–12 weeks of dedicated preparation after completing core clerkships. Begin QBank practice during clerkships for best results.</p>
""" + cta("Get Started with BoardVitals →")
    return wrap(
        "Medical QBank FAQ 2026 — ExamBoost",
        "Answers to the most common questions about medical QBanks, BoardVitals, USMLE, and NCLEX board exam preparation.",
        "faq.html", body, schema)

def page_about():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › About</div>
<h1>About ExamBoost</h1>
<p>ExamBoost was created to help medical students, nursing students, and physicians find the best resources for board exam preparation — without wading through biased reviews or confusing marketing.</p>
<h2>Our Mission</h2>
<p>We independently review and compare medical education platforms so you can make an informed decision about where to invest your study time and money. We believe the right QBank makes a measurable difference in exam outcomes.</p>
<h2>Our Review Process</h2>
<ul>
<li>Every platform is tested by our team of medical educators and students</li>
<li>We evaluate question quality, explanation depth, analytics, and value</li>
<li>Ratings are updated regularly as platforms release new features</li>
<li>We disclose all affiliate relationships transparently</li>
</ul>
<h2>Our Team</h2>
<div class="author-box">
<strong>Dr. Michael Reynolds, MD</strong> — Board-Certified Physician, Medical Education Consultant<br><br>
Dr. Reynolds has advised medical students on board exam preparation for over 10 years and has personally reviewed every major QBank platform on this site.
</div>
<h2>Contact Us</h2>
<p>Questions or feedback? Visit our <a href="contact.html">contact page</a>.</p>
"""
    return wrap(
        "About ExamBoost — Medical QBank Reviews",
        "Learn about ExamBoost and our mission to help medical students find the best board exam preparation resources.",
        "about.html", body)

def page_contact():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Contact</div>
<h1>Contact ExamBoost</h1>
<p>Have a question, correction, or want to share your board exam experience? We would love to hear from you.</p>
<h2>Send Us a Message</h2>
<p>Email us at: <strong>contact [at] examboost [dot] info</strong></p>
<h2>Advertising &amp; Partnerships</h2>
<p>For affiliate partnership inquiries, please include "Partnership" in your subject line.</p>
<h2>Corrections</h2>
<p>We strive for accuracy in all our reviews. If you notice outdated information or a factual error, please let us know and we will update promptly.</p>
""" + cta_box("Back to QBank Reviews →")
    return wrap(
        "Contact ExamBoost",
        "Contact the ExamBoost team with questions, corrections, or partnership inquiries.",
        "contact.html", body)

def page_disclosure():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › Affiliate Disclosure</div>
<h1>Affiliate Disclosure</h1>
<p><strong>Last updated: 2026</strong></p>
<p>ExamBoost participates in affiliate marketing programs. This means we may earn a commission when you click links on this site and make a purchase — at no additional cost to you.</p>
<h2>What This Means</h2>
<ul>
<li>Some links on this site are affiliate links</li>
<li>We earn a small commission if you purchase through these links</li>
<li>The price you pay is not affected by our commission</li>
<li>Our reviews and ratings are based on merit, not commission rates</li>
</ul>
<h2>Our Commitment</h2>
<p>We only recommend products we genuinely believe are beneficial for board exam preparation. Commission rates do not influence our rankings or review scores. If a product is not good, we say so.</p>
<h2>Current Affiliate Relationships</h2>
<p>ExamBoost currently has an affiliate relationship with BoardVitals via the LinkConnector affiliate network.</p>
"""
    return wrap(
        "Affiliate Disclosure — ExamBoost",
        "ExamBoost affiliate disclosure. We earn commissions from qualifying purchases. Learn how this affects our reviews.",
        "disclosure.html", body)

def page_amboss_review():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › AMBOSS Review</div>
<h1>AMBOSS Review 2026 — Worth It for USMLE?</h1>
<p class="rating">★★★★☆ 4.3/5 — Very Good</p>
<p>AMBOSS combines a QBank with an integrated medical knowledge library, making it unique among board exam platforms. Here is our full 2026 review.</p>
<h2>What Makes AMBOSS Different</h2>
<p>Unlike pure QBanks, AMBOSS includes the Library — a searchable medical knowledge database you can access mid-question. This makes it particularly useful for students who want to learn while they practice.</p>
<h2>AMBOSS Pros</h2>
<ul>
<li>✅ Integrated knowledge library alongside questions</li>
<li>✅ High-quality clinical vignettes</li>
<li>✅ Strong for Step 1 and Step 2 CK</li>
<li>✅ Detailed media — images, tables, diagrams</li>
</ul>
<h2>AMBOSS Cons</h2>
<ul>
<li>❌ Higher price than BoardVitals</li>
<li>❌ Does not cover COMLEX, NCLEX, or specialty boards</li>
<li>❌ Library access can be distracting during timed practice</li>
</ul>
<h2>AMBOSS vs BoardVitals</h2>
<p>If you are only preparing for USMLE Steps 1 and 2, AMBOSS is a strong choice. If you also need NCLEX, COMLEX, or specialty board prep, BoardVitals covers all of them while AMBOSS covers none.</p>
""" + cta_box("Our Pick: BoardVitals — Better Value + More Exams")
    return wrap(
        "AMBOSS Review 2026 — Is It Worth It for USMLE? — ExamBoost",
        "Honest AMBOSS review 2026. Features, pricing, pros and cons vs BoardVitals and UWorld for USMLE board prep.",
        "amboss-review.html", body)

def page_uworld_review():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › UWorld Review</div>
<h1>UWorld Review 2026 — Still the Gold Standard?</h1>
<p class="rating">★★★★★ 4.8/5 — Excellent (for USMLE)</p>
<p>UWorld has been the dominant USMLE QBank for over a decade. But is it still the best choice in 2026? Here is our honest assessment.</p>
<h2>UWorld Strengths</h2>
<ul>
<li>✅ Largest Step 1 and Step 2 CK question bank available</li>
<li>✅ Exceptionally detailed explanations</li>
<li>✅ Realistic exam simulations (Self-Assessments)</li>
<li>✅ Strong predictive correlation with actual scores</li>
</ul>
<h2>UWorld Weaknesses</h2>
<ul>
<li>❌ Higher price — from $109/month</li>
<li>❌ USMLE only — no NCLEX, COMLEX, or specialty boards</li>
<li>❌ No adaptive learning algorithm</li>
<li>❌ No CME credit</li>
</ul>
<h2>UWorld vs BoardVitals</h2>
<p>UWorld is the best pure USMLE Step 1/Step 2 QBank available. But if you need broader exam coverage, CME credit, or a lower price, BoardVitals is the better choice. Many students use both.</p>
""" + cta_box("Our Pick for Value: BoardVitals from $49")
    return wrap(
        "UWorld Review 2026 — Still the Best USMLE QBank? — ExamBoost",
        "Honest UWorld review 2026. Is UWorld still the best USMLE QBank? Compare with BoardVitals and AMBOSS.",
        "uworld-review.html", body)

def page_cme():
    body = """
<div class="breadcrumb"><a href="index.html">Home</a> › CME QBank</div>
<h1>Best QBank for CME Credits (2026)</h1>
<p>Physicians need continuing medical education (CME) credits to maintain licensure. Earning CME through board-style practice questions is the most efficient method — you study for your exam and earn credits simultaneously.</p>
""" + cta_box("BoardVitals — Earn CME While You Board Prep") + """
<h2>What Is CME?</h2>
<p>Continuing Medical Education (CME) credits are required by medical licensing boards and specialty societies for physicians to maintain certification. Requirements vary by state and specialty, typically 20–50 credits per year.</p>
<h2>How BoardVitals CME Works</h2>
<ul>
<li>Answer board-style questions in your specialty</li>
<li>Earn AMA PRA Category 1 Credits™</li>
<li>Simultaneously prepare for MOC requirements</li>
<li>Track credits in a digital certificate</li>
</ul>
<div class="tip-box">BoardVitals is one of the only QBank platforms that combines MOC prep, CME credit, and board certification prep in a single subscription.</div>
<h2>CME Requirements by Specialty</h2>
<table>
<tr><th>Specialty</th><th>Annual CME Required</th><th>MOC Required</th></tr>
<tr><td>Internal Medicine</td><td>30 credits</td><td>Yes (ABIM)</td></tr>
<tr><td>Family Medicine</td><td>150 over 3 years</td><td>Yes (ABFM)</td></tr>
<tr><td>Emergency Medicine</td><td>40 credits</td><td>Yes (ABEM)</td></tr>
<tr><td>Pediatrics</td><td>30 credits</td><td>Yes (ABP)</td></tr>
</table>
""" + cta("Earn CME Credits with BoardVitals →")
    return wrap(
        "Best QBank for CME Credits 2026 — ExamBoost",
        "Earn CME credits while you board prep. BoardVitals offers AMA PRA Category 1 CME credits for physicians.",
        "cme.html", body)

# ── All pages dict ──────────────────────────────────────────────────────────
def all_pages():
    return {
        "step1.html":             page_step1(),
        "step2.html":             page_step2(),
        "step3.html":             page_step3(),
        "nclex.html":             page_nclex(),
        "comlex.html":            page_comlex(),
        "comparison.html":        page_comparison(),
        "boardvitals-review.html":page_boardvitals_review(),
        "uworld-review.html":     page_uworld_review(),
        "amboss-review.html":     page_amboss_review(),
        "specialty-boards.html":  page_specialty_boards(),
        "study-schedule.html":    page_study_schedule(),
        "free-resources.html":    page_free_resources(),
        "tips.html":              page_tips(),
        "cme.html":               page_cme(),
        "faq.html":               page_faq(),
        "about.html":             page_about(),
        "contact.html":           page_contact(),
        "disclosure.html":        page_disclosure(),
    }

# ── sitemap ─────────────────────────────────────────────────────────────────
def build_sitemap(pages):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    urls = [f"""  <url><loc>{SITE_URL}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>"""]
    for slug in pages:
        urls.append(f"""  <url><loc>{SITE_URL}/{slug}</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>""")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>"

def build_robots():
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"

def build_llms():
    lines = [f"# {SITE_NAME}", f"> {SITE_URL}", "",
             "Medical board exam preparation reviews and comparisons.", "",
             "## Pages"]
    for slug in all_pages():
        lines.append(f"- [{slug}]({SITE_URL}/{slug})")
    return "\n".join(lines)

# ── GitHub push ──────────────────────────────────────────────────────────────
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

# ── main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    pages = all_pages()
    print(f"Building {len(pages)} pages for {SITE_NAME}...")
    for slug, html in pages.items():
        gh_put(slug, html, f"Site update: {slug}")
    gh_put("sitemap.xml", build_sitemap(pages), "Site update: sitemap.xml")
    gh_put("robots.txt",  build_robots(),        "Site update: robots.txt")
    gh_put("llms.txt",    build_llms(),          "Site update: llms.txt")
    print(f"\nDone! {len(pages) + 3} files pushed to {GH_REPO}.")
