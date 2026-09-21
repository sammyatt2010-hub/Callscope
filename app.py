from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------
# Settings you may want to change
# ---------------------------------------------------------------
VIDEO_FILE = "call-scope.mp4"   # video file that sits next to app.py in GitHub
VIDEO_URL = "https://youtu.be/7ZRMqGe3bb8"                  # or paste an unlisted YouTube/Vimeo link here (it takes priority)
LOGO_FILE = "logo.png"          # optional: add a logo.png next to app.py to show it at the top

DEMO_URL = "https://sycomms.co.uk/get-in-touch"
PRODUCT_URL = "https://sycomms.co.uk/call-scope"
PHONE = "01743 667419"
PHONE_LINK = "tel:01743667419"
EMAIL = "hello@sycomms.co.uk"

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
    <p class="footer">&copy; SY Comms</p>
    """,
    unsafe_allow_html=True,
)
