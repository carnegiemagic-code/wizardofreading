#!/usr/bin/env python3
"""Builds the Wizard of Reading site. Edit the text below, run `python3 build.py`, then push.

Rebuilt Oct 2026 from the last good copy of the old WordPress site (Internet Archive, Dec 2022),
updated with the current wording from deanalanmagic.com/reading/.
Rule for copy here: no em dashes, no prices (the form asks for availability and pricing).
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PHONE = "703-404-8902"
PHONE_LINK = "tel:+17034048902"
EMAIL = "info@wizardofreading.com"
MAGO_FORM_ID = "4c6c5bf1-7dfd-41b8-929d-72cf9757ff13"  # same form as deanalanmagic.com/reading/

NAV = [("", "Home"), ("about/", "About"), ("schools/", "Schools"),
       ("libraries/", "Libraries"), ("reviews/", "Reviews"), ("contact/", "Contact")]

REVIEWS = json.load(open(os.path.join(HERE, "reviews.json"), encoding="utf-8"))


def page(slug, title, description, body):
    root = "../" if slug else ""
    current = ' aria-current="page"'
    nav = "".join(
        f'<a href="{root}{s or "./"}"{current if s == slug else ""}>{label}</a>'
        for s, label in NAV)
    out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="icon" href="{root}img/wizard-square.jpg">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:image" content="https://wizardofreading.com/img/wizard-square.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="{root or './'}"><img src="{root}img/wizard-square.jpg" alt=""><span>The Wizard of Reading<small>Dean Alan</small></span></a>
    <a class="head-phone" href="{PHONE_LINK}">{PHONE}</a>
  </div>
  <nav class="wrap site-nav" aria-label="Main">{nav}</nav>
</header>
<main>
{body}
</main>
<footer class="site-foot">
  <div class="wrap foot-row">
    <div><strong>The Wizard of Reading</strong><br>Reading assemblies for elementary schools and libraries<br>Tennessee, Virginia, North Carolina, Kentucky and beyond</div>
    <div><a href="{PHONE_LINK}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="https://deanalanmagic.com/">deanalanmagic.com</a></div>
  </div>
  <p class="wrap fine">&copy; Dean Alan. All rights reserved.</p>
</footer>
</body>
</html>
"""
    folder = os.path.join(HERE, slug)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(out)


def cta(root, text="Check availability and pricing"):
    return f'<a class="btn" href="{root}contact/">{text}</a>'


def show_cards(root, library=False):
    seuss_when = "Spring, for Read Across America Week and Dr. Seuss's birthday, and any time of year." if library \
        else "Perfect for Read Across America Week, literacy nights and book fairs."
    return f"""
<div class="shows">
  <article class="show">
    <div class="show-art left" role="img" aria-label="The Marvelous Magical Stories Show"></div>
    <div class="show-body">
      <h3>The Marvelous Magical Stories Show</h3>
      <p class="when">{"Any time of year. The ideal show for Library Week." if library else "Any time of year: book fairs, reading nights and more. Grades K to 5."}</p>
      <p>Beloved stories leap off the page as Dean blends astonishing magic with reading themed lessons. The featured books rotate often, so the show stays fresh. Titles have included <em>The Invention of Hugo Cabret</em>, <em>The Magician's Elephant</em>, <em>The Wartville Wizard</em>, <em>The Fantastic Flying Books of Mr. Morris Lessmore</em> and <em>A Fish Out of Water</em>.</p>
    </div>
  </article>
  <article class="show">
    <div class="show-art right" role="img" aria-label="The Seusstacular Reading Show"></div>
    <div class="show-body">
      <h3>The Seusstacular Reading Show</h3>
      <p class="when">{seuss_when}</p>
      <p>For over 25 years Dean has presented shows about the books and stories of Dr. Seuss, and they have been extremely popular. <em>The Cat in the Hat</em>, <em>Horton</em> and more, all brought to life with magic, laughter and pure Seussical energy. Others have tried to copy it. Go with the originator.</p>
    </div>
  </article>
</div>"""


def build():
    # ---------- HOME ----------
    r = ""
    page("", "The Wizard of Reading | Reading Assemblies with Dean Alan",
         "Reading assemblies that use magic to get elementary students excited about books. "
         "Dean Alan, the Wizard of Reading, for schools and libraries.",
         f"""
<section class="hero">
  <div class="wrap hero-row">
    <div class="hero-text">
      <p class="kicker">Reading assemblies for elementary schools and libraries</p>
      <h1>Make reading unforgettable.</h1>
      <p class="lead">Dean Alan, the Wizard of Reading, uses magic to get kids so excited about books that they can't wait to check them out.</p>
      <div class="btns">{cta(r)}<a class="btn ghost" href="schools/">See the shows</a></div>
    </div>
    <img class="hero-img" src="img/wizard-square.jpg" alt="Dean Alan, the Wizard of Reading, with books flying around him" width="400" height="400">
  </div>
</section>

<section class="wrap prose">
  <h2>Welcome</h2>
  <p>Hi, I'm Dean Alan, the Wizard of Reading. I use magic as a teaching tool to bring out the magic found in every book.</p>
  <p>My shows use magic and other theatrical techniques as visual tools to illustrate select books and stories. Kids don't just watch; they take part, and they leave the room wanting to read.</p>
  <blockquote class="quote"><p>"Nothing great was ever achieved without enthusiasm."</p><cite>Ralph Waldo Emerson</cite></blockquote>
  <p>I totally believe that. I am <em>very</em> enthusiastic about reading, and that enthusiasm guides me to the books the kids will be most excited by.</p>
</section>

<section class="band">
  <div class="wrap">
    <h2>Two reading shows</h2>
    {show_cards(r)}
    <p class="center"><a href="schools/">For schools</a> &nbsp;&middot;&nbsp; <a href="libraries/">For libraries</a></p>
  </div>
</section>

<section class="wrap prose">
  <blockquote class="review big"><p>"{html.escape(REVIEWS[3]['q'])}"</p><cite>{html.escape(REVIEWS[3]['who'])}</cite></blockquote>
  <p class="center"><a href="reviews/">Read more reviews from schools</a></p>
</section>

<section class="cta-band">
  <div class="wrap center">
    <h2>Ready to make your next event magical?</h2>
    <p>Daytime assemblies and family night events. Dates go fast.</p>
    {cta(r)}
  </div>
</section>""")

    # ---------- ABOUT ----------
    r = "../"
    page("about/", "About Dean Alan | The Wizard of Reading",
         "Dean Alan has presented reading assemblies at thousands of schools for over 25 years.",
         f"""
<section class="wrap prose page-top">
  <h1>About Dean Alan</h1>
  <img class="float" src="{r}img/wizard-square.jpg" alt="Dean Alan" width="400" height="400">
  <p>Dean Alan is a full time professional speaker, magician, podcast host and historian. He has presented assemblies at thousands of schools for over 25 years, and his topic is always <strong>reading</strong>.</p>
  <p>As a child, Dean had difficulty reading. He struggled with reading comprehension. Then one day he discovered a "secret" that made reading fun and far easier, and it made every kind of reading easier. His passion is to share it with young students so that they can learn from his secret as well.</p>
  <p>Dean is also one of the leading historians of magic and magicians in the country. He has given talks and lectures on magic history for historical groups and at magic conferences across the country. He was the featured guest in a French documentary on Houdini, has consulted with numerous TV shows on the subject of magic, and has spoken at a TED Talk.</p>
  <p>He is also the host of <a href="https://magicdetectivepodcast.com/">The Magic Detective Podcast</a>, dedicated to the history of magic.</p>
  <p>{cta(r, "Bring Dean to your school or library")}</p>
</section>""")

    # ---------- SCHOOLS ----------
    page("schools/", "School Reading Assemblies | The Wizard of Reading",
         "Two reading assemblies for elementary schools: The Marvelous Magical Stories Show and The Seusstacular Reading Show.",
         f"""
<section class="wrap prose page-top">
  <h1>Reading assemblies for schools</h1>
  <p class="lead">If you want students to be fired up about reading, you need more than an ordinary assembly. Books burst to life through magic, storytelling and nonstop audience participation.</p>
</section>
<section class="band"><div class="wrap">
  {show_cards(r)}
</div></section>
<section class="wrap prose">
  <h2>Why schools book the Wizard of Reading</h2>
  <ul class="ticks">
    <li>Built for elementary students, and it holds every grade</li>
    <li>Daytime assemblies and family literacy nights</li>
    <li>Ideal for Read Across America Week, book fairs, reading nights and Title 1 family events</li>
    <li>Available to schools in Tennessee, Virginia, North Carolina, Kentucky and beyond</li>
  </ul>
  <p class="note"><strong>Daycare and preschool directors:</strong> there is a version of the show for younger audiences. See <a href="https://deanalanmagic.com/">deanalanmagic.com</a>.</p>
  <h2>The next step</h2>
  <p>You probably have questions about the show and the big one: how much does it cost? Fill out the short form and we'll get back to you with availability and pricing for single assemblies, multiple assemblies and family nights. There is no obligation.</p>
  <p>{cta(r)} &nbsp; or call <a href="{PHONE_LINK}">{PHONE}</a></p>
</section>""")

    # ---------- LIBRARIES ----------
    page("libraries/", "Library Magic Shows | The Wizard of Reading",
         "Reading themed magic shows for libraries and family audiences.",
         f"""
<section class="wrap prose page-top">
  <h1>Library magic shows</h1>
  <p class="lead">Family shows filled with magic and story references, for children's programs, Library Week, Read Across America and summer reading.</p>
</section>
<section class="band"><div class="wrap">
  {show_cards(r, library=True)}
</div></section>
<section class="wrap prose">
  <h2>Seasonal shows</h2>
  <p>Dean also presents seasonal library shows for summer reading, the fall and the winter holidays. They change from year to year, so ask what is current when you get in touch.</p>
  <h2>The next step</h2>
  <p>Fill out the short form for availability and pricing, or call. We'd love to hear from you.</p>
  <p>{cta(r)} &nbsp; or call <a href="{PHONE_LINK}">{PHONE}</a></p>
</section>""")

    # ---------- REVIEWS ----------
    items = "".join(
        f'<blockquote class="review"><p>"{html.escape(x["q"])}"</p><cite>{html.escape(x["who"])}</cite></blockquote>'
        for x in REVIEWS)
    page("reviews/", "Reviews from Schools | The Wizard of Reading",
         "What reading specialists, librarians and teachers say about the Wizard of Reading assemblies.",
         f"""
<section class="wrap page-top">
  <h1>Reviews from schools</h1>
  <p class="lead">A few words from the schools that have seen the Wizard of Reading assemblies.</p>
  <div class="reviews">{items}</div>
  <p class="center">{cta(r)}</p>
</section>""")

    # ---------- CONTACT ----------
    page("contact/", "Availability and Bookings | The Wizard of Reading",
         "Check availability and pricing for a Wizard of Reading assembly or library show.",
         f"""
<section class="wrap page-top contact-row">
  <div class="prose">
    <h1>Availability and bookings</h1>
    <p>If you're ready to schedule a show, fill out the form so we can let you know about availability and pricing. Looking for more information first? Add your questions in the comments box.</p>
    <p>Filling out the form puts you under no obligation. Nothing is booked until all the details are worked out.</p>
    <p>You are always welcome to call, too. I'm always happy to talk.</p>
    <p class="big-phone"><a href="{PHONE_LINK}">{PHONE}</a></p>
    <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
  <div class="form-box">
    <script src="https://mago.co/Scripts/form.js"></script>
    <script>
      var magoForm = new MagoForm();
      magoForm.initialize({{'formId':'{MAGO_FORM_ID}','autoResize':true,'ssl':true}});
      magoForm.display();
    </script>
  </div>
</section>""")

    # GitHub Pages: 404 page goes home
    with open(os.path.join(HERE, "404.html"), "w", encoding="utf-8") as f:
        f.write('<!doctype html><meta charset="utf-8"><title>The Wizard of Reading</title>'
                '<meta http-equiv="refresh" content="0; url=/"><a href="/">The Wizard of Reading</a>')


if __name__ == "__main__":
    build()
    print("built")
