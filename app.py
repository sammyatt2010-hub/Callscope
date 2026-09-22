from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------
# Settings you may want to change
# ---------------------------------------------------------------
VIDEO_FILE = "call-scope.mp4"   # video file that sits next to app.py in GitHub
VIDEO_URL = ""                  # or paste an unlisted YouTube/Vimeo link here (it takes priority)
LOGO_FILE = "logo.png"          # optional: add a logo.png next to app.py to show it at the top

DEMO_URL = "https://sycomms.co.uk/get-in-touch"
PRODUCT_URL = "https://sycomms.co.uk/call-scope"
PHONE = "01743 667419"
PHONE_LINK = "tel:01743667419"
EMAIL = "hello@sycomms.co.uk"

# --- Industry videos, hosted directly in this GitHub repo ---------------
# Fill in your GitHub username and repo name below, then upload each clip
# into a folder called "videos" in the repo, named exactly as the "slug"
# shown for each industry (e.g. videos/estate-agents.mp4). Once both are
# set, USE_VIDEO_LINKS switches every card below from the slide-deck
# preview over to the video itself automatically - no other edits needed.
GITHUB_USER = ""          # e.g. "samsmith"
GITHUB_REPO = "callscope"  # your repo name
GITHUB_BRANCH = "main"
USE_VIDEO_LINKS = bool(GITHUB_USER)

# Industry use cases. Each "deck_url" is that industry's short slide-deck
# preview (used until USE_VIDEO_LINKS is on); "slug" is the video filename,
# without the .mp4, that this card will link to once it's uploaded.
INDUSTRIES = [
    {"name": "Estate Agents", "blurb": "Enquiries summarised, viewings scheduled.",
     "slug": "estate-agents", "deck_url": "https://claude.ai/artifact/8iGZVDgF7zyvTGDuheYAyW"},
    {"name": "Recruitment Agencies", "blurb": "Every candidate and client call, actioned.",
     "slug": "recruitment-agencies", "deck_url": "https://claude.ai/artifact/TFzzxgYiKeavngSDh6TWLW"},
    {"name": "Law Firms", "blurb": "Clear, accurate records for every client call.",
     "slug": "law-firms", "deck_url": "https://claude.ai/artifact/Y1w5iDCkejxTG1M6rJ3gL7"},
    {"name": "Financial Services", "blurb": "Complete records, clearer oversight.",
     "slug": "financial-services", "deck_url": "https://claude.ai/artifact/NMTXpM8yh2DmRsNFRQKjWi"},
    {"name": "Dental Practices", "blurb": "Less time on the phone, more with patients.",
     "slug": "dental-practices", "deck_url": "https://claude.ai/artifact/QyDgiceswZXYwNwoFfJkFE"},
    {"name": "Automotive Dealers & Garages", "blurb": "From enquiry to confirmed booking.",
     "slug": "automotive-dealers-garages", "deck_url": "https://claude.ai/artifact/1XaPzmHJhm42tQ5N9f434p"},
    {"name": "Accountants", "blurb": "No client enquiry slips through the net.",
     "slug": "accountants", "deck_url": "https://claude.ai/artifact/BJxpkjNMmAMdDVjijEftnp"},
    {"name": "Insurance Brokers", "blurb": "Advice and renewal calls, captured for compliance.",
     "slug": "insurance-brokers", "deck_url": "https://claude.ai/artifact/4hBgtGS7h71CpTKZjeU47Z"},
    {"name": "Veterinary Practices", "blurb": "Every client interaction, recorded.",
     "slug": "veterinary-practices", "deck_url": "https://claude.ai/artifact/Jac7x1ZfseiQ9HHuBfG3Mj"},
    {"name": "Opticians", "blurb": "Consistent service, on autopilot.",
     "slug": "opticians", "deck_url": "https://claude.ai/artifact/WPKA4TGBcKu8HnE42wGtpV"},
    {"name": "Property Management", "blurb": "Every tenant call, tracked and actioned.",
     "slug": "property-management", "deck_url": "https://claude.ai/artifact/XDJ9Aj5naVBdKcx4EE6gnf"},
    {"name": "Customer Service & Contact Centres", "blurb": "Live visibility, every agent.",
     "slug": "customer-service-contact-centres", "deck_url": "https://claude.ai/artifact/BmQvQSvCy4nTiWkP6i4D86"},
]

for _ind in INDUSTRIES:
    if USE_VIDEO_LINKS:
        _ind["url"] = (
            f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}"
            f"/{GITHUB_BRANCH}/videos/{_ind['slug']}.mp4"
        )
    else:
        _ind["url"] = _ind["deck_url"]

HERE = Path(__file__).parent

st.set_page_config(
    page_title="Call Scope | SY Comms",
    page_icon="📞",
    layout="wide",
)

# ---------------------------------------------------------------
# Brand styling
# ---------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

    html, body, .stApp, .stMarkdown, p, h1, h2, h3, a {
        font-family: 'Manrope', sans-serif;
    }

    /* Hide the default Streamlit menu, footer and toolbar */
    #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {
        display: none;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1080px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .hero-title {
        font-size: clamp(2.2rem, 5vw, 3.6rem);
        font-weight: 800;
        line-height: 1.08;
        color: #f5f3fb;
        margin: 0.5rem 0 1rem 0;
    }
    .hero-sub {
        font-size: 1.25rem;
        line-height: 1.5;
        color: #b9b3dd;
        max-width: 42rem;
        margin-bottom: 2rem;
    }

    [data-testid="stVideo"] video {
        border-radius: 12px;
    }

    .point {
        border-top: 3px solid #00b5a3;
        padding-top: 1rem;
        margin-top: 2.5rem;
    }
    .point h3 {
        font-size: 1.25rem;
        font-weight: 700;
        color: #f5f3fb;
        margin: 0 0 0.5rem 0;
        padding: 0;
    }
    .point p {
        font-size: 1.05rem;
        line-height: 1.55;
        color: #b9b3dd;
        margin: 0;
    }

    .cta-row {
        margin-top: 3rem;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 1.5rem;
    }
    a.cta {
        display: inline-block;
        background: #00b5a3;
        color: #1f1450 !important;
        font-weight: 800;
        font-size: 1.15rem;
        padding: 0.9rem 2rem;
        border-radius: 999px;
        text-decoration: none !important;
        transition: background 0.15s ease;
    }
    a.cta:hover {
        background: #2fd0bf;
    }
    a.cta:focus-visible, a.text-link:focus-visible {
        outline: 3px solid #f5f3fb;
        outline-offset: 3px;
    }
    a.text-link {
        color: #f5f3fb !important;
        font-weight: 600;
        text-decoration: underline !important;
        text-underline-offset: 4px;
    }

    .contact {
        margin-top: 2rem;
        font-size: 1.05rem;
        color: #b9b3dd;
    }
    .contact a {
        color: #f5f3fb !important;
        font-weight: 600;
        text-decoration: none !important;
    }
    .footer {
        margin-top: 4rem;
        font-size: 0.9rem;
        color: #8f88c4;
    }

    .industries-heading {
        margin-top: 4rem;
        font-size: 1.9rem;
        font-weight: 800;
        color: #f5f3fb;
    }
    .industries-sub {
        font-size: 1.05rem;
        color: #b9b3dd;
        margin-bottom: 1.5rem;
    }
    .industry-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
        gap: 1rem;
    }
    a.industry-card {
        display: block;
        background: #2d1f6e;
        border: 1px solid #443596;
        border-radius: 12px;
        padding: 1.3rem;
        text-decoration: none !important;
        transition: border-color 0.15s ease, background 0.15s ease;
    }
    a.industry-card:hover {
        background: #382a80;
        border-color: #00b5a3;
    }
    a.industry-card:focus-visible {
        outline: 3px solid #f5f3fb;
        outline-offset: 3px;
    }
    .industry-name {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f5f3fb !important;
        margin: 0 0 0.4rem 0;
    }
    .industry-blurb {
        font-size: 0.95rem;
        color: #b9b3dd !important;
        margin: 0;
        line-height: 1.4;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------
# Page content
# ---------------------------------------------------------------
logo_path = HERE / LOGO_FILE
if logo_path.exists():
    st.image(str(logo_path), width=72)

st.markdown(
    """
    <h1 class="hero-title">Every conversation.<br>Captured. Analysed. Actioned.</h1>
    <p class="hero-sub">Call Scope from SY Comms turns your business calls into
    transcripts, CRM updates and live dashboards.</p>
    """,
    unsafe_allow_html=True,
)

# The video
video_path = HERE / VIDEO_FILE
if VIDEO_URL:
    st.video(VIDEO_URL)
elif video_path.exists():
    st.video(str(video_path))
else:
    st.info(
        f"Video not found. Add a file called {VIDEO_FILE} next to app.py, "
        "or paste a YouTube link into VIDEO_URL at the top of app.py."
    )

# Three short points
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown(
        """
        <div class="point">
            <h3>Understands every call</h3>
            <p>Transcripts, summaries, sentiment and quality scores, created automatically.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="point">
            <h3>Updates your CRM</h3>
            <p>Notes, tasks, appointments and tickets logged for you in Salesforce, HubSpot, Zoho and more.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="point">
            <h3>Shows you everything</h3>
            <p>Live dashboards and wallboards for call volumes, missed calls and team performance.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Call to action
st.markdown(
    f"""
    <div class="cta-row">
        <a class="cta" href="{DEMO_URL}" target="_blank" rel="noopener">Book a demo</a>
        <a class="text-link" href="{PRODUCT_URL}" target="_blank" rel="noopener">See everything Call Scope does</a>
    </div>
    <p class="contact">Call <a href="{PHONE_LINK}">{PHONE}</a>
    or email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    """,
    unsafe_allow_html=True,
)

# Industry use cases
cards_html = "".join(
    f"""
    <a class="industry-card" href="{ind['url']}" target="_blank" rel="noopener">
        <p class="industry-name">{ind['name']}</p>
        <p class="industry-blurb">{ind['blurb']}</p>
    </a>
    """
    for ind in INDUSTRIES
)
st.markdown(
    f"""
    <h2 class="industries-heading">See it for your industry</h2>
    <p class="industries-sub">Real benefits, sector by sector. Pick yours below.</p>
    <div class="industry-grid">{cards_html}</div>
    <p class="footer">&copy; SY Comms</p>
    """,
    unsafe_allow_html=True,
)
