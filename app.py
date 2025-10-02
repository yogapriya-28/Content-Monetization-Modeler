import streamlit as st
import pickle
import pandas as pd
import requests
import isodate
from urllib.parse import urlparse, parse_qs

# -----------------------------
# Load Model, Scaler & Feature Order
# -----------------------------
with open("linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("feature_order.pkl", "rb") as f:
    feature_order = pickle.load(f)

# -----------------------------
# YouTube API & Fixer API
# -----------------------------
API_KEY = "AIzaSyD0_asE5flWxaOSsWj9RribHwsAqSgegfM"
FIXER_API_KEY = "acb9e4d5aeb891f90c7954aae200448b"
FIXER_API_URL = f"https://data.fixer.io/api/latest?access_key={FIXER_API_KEY}&symbols=USD,INR,BRL,IDR,JPY"

class categoryMap:
    category = {
        "Education": "27", "Tech": "28", "Music": "10",
        "Entertainment": "24", "Gaming": "20", "Lifestyle": "22"
    }

# -----------------------------
# Currency Conversion
# -----------------------------
def get_multi_currency_rates():
    try:
        resp = requests.get(FIXER_API_URL)
        data = resp.json()
        if data.get("success"):
            usd_rate = data["rates"]["USD"]
            return {
                "USD": 1,
                "INR": data["rates"]["INR"] / usd_rate,
                "BRL": data["rates"]["BRL"] / usd_rate,
                "IDR": data["rates"]["IDR"] / usd_rate,
                "JPY": data["rates"]["JPY"] / usd_rate
            }
    except:
        pass
    return {"USD": 1, "INR": 88.75, "BRL": 5.36, "IDR": 16683.60, "JPY": 148.55}

# -----------------------------
# Extract Video Analytics
# -----------------------------
def getVideoAnalytics(video_url):
    def extract_video_id(url):
        parsed = urlparse(url)
        if "youtube.com" in parsed.netloc:
            if parsed.path == "/watch":
                return parse_qs(parsed.query).get("v", [None])[0]
            elif "/shorts/" in parsed.path:
                return parsed.path.split("/shorts/")[1].split("?")[0]
        if "youtu.be" in parsed.netloc:
            return parsed.path.lstrip("/").split("?")[0]
        return None

    video_id = extract_video_id(video_url)
    if video_id is None:
        st.error("⚠️ Invalid YouTube URL")
        return None

    # Fetch video stats
    video_stats_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet,contentDetails&id={video_id}&key={API_KEY}"
    video_data = requests.get(video_stats_url).json()
    if not video_data.get("items"):
        st.error("⚠️ Video not found.")
        return None

    item = video_data["items"][0]
    stats = item.get("statistics", {})
    snippet = item.get("snippet", {})
    details = item.get("contentDetails", {})

    likes = int(stats.get("likeCount", 0))
    views = int(stats.get("viewCount", 0))
    comments = int(stats.get("commentCount", 0))
    duration = isodate.parse_duration(details.get("duration", "PT0S"))
    video_length_minutes = round(duration.total_seconds() / 60, 2)

    category_id = snippet.get("categoryId", "")
    channel_id = snippet.get("channelId", "")

    # Map category
    mapCategory = categoryMap.category
    category_list = [k for k, v in mapCategory.items() if v == category_id]
    category = category_list[0] if category_list else "Education"

    # Get subscribers
    channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={API_KEY}"
    channel_data = requests.get(channel_url).json()
    subscribers = int(channel_data.get("items", [{}])[0].get("statistics", {}).get("subscriberCount", 0))

    # Build dataframe-ready info
    video_info = {
        "views": views,
        "likes": likes,
        "comments": comments,
        "video_length_minutes": video_length_minutes,
        "subscribers": subscribers,
        "category": category,
    }

    # Extra features
    video_info["watch_time_minutes"] = round(video_length_minutes * views / 60, 2)
    video_info["avg_watch_time_per_view"] = video_info["watch_time_minutes"] / max(views, 1)
    video_info["engagement_rate"] = (likes + comments) / max(views, 1)

    # Encode category
    encode = {"Education": 0, "Tech": 1, "Music": 2, "Entertainment": 3, "Gaming": 4, "Lifestyle": 5}
    video_info["category"] = encode.get(category, 0)

    # Fill missing cols
    for col in feature_order:
        if col not in video_info:
            video_info[col] = 0

    return video_info

# -----------------------------
# Streamlit UI – Pro YouTube Studio Style
# -----------------------------
st.set_page_config(layout="wide")
st.markdown("<h1 style='color:#cc0000;'>📊 YouTube Studio – Ad Revenue Dashboard</h1>", unsafe_allow_html=True)

# Sidebar input (like YT Studio’s left menu)
with st.sidebar:
    st.markdown("### 🔗 Paste YouTube Link")
    video_url = st.text_input("Video URL")
    submitted = st.button("🚀 Analyze Video")

# Main layout
if submitted and video_url:
    output = getVideoAnalytics(video_url)
else:
    output = None

if video_url:
    st.video(video_url)

if output is not None:
    # --- Top KPIs row ---
    st.markdown("## 🎥 Video Performance Snapshot")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("👀 Views", f"{output['views']:,}")
    kpi2.metric("👍 Likes", f"{output['likes']:,}")
    kpi3.metric("💬 Comments", f"{output['comments']:,}")
    kpi4.metric("👥 Subscribers", f"{output['subscribers']:,}")

    # --- Engagement & Stats ---
    stats_col, engagement_col = st.columns(2)
    with stats_col:
        st.markdown("### 📂 Video Details")
        st.info(f"⏱ Duration: **{output['video_length_minutes']} mins**")
        st.info(f"📌 Category: **{output['category']}**")

    with engagement_col:
        st.markdown("### 📈 Engagement Insights")
        st.success(f"⌛ Total Watch Time: **{output['watch_time_minutes']:,} mins**")
        st.success(f"📊 Avg per View: **{output['avg_watch_time_per_view']:.2f} mins**")
        st.success(f"🔥 Engagement Rate: **{output['engagement_rate']*100:.2f}%**")

    # --- Revenue Prediction Section ---
    st.markdown("## 💵 Estimated Ad Revenue")

    video_df = pd.DataFrame([output])[feature_order]

    # Clip realistic ranges
    clip_ranges = {
        'views': (0, 100000),
        'likes': (0, 5000),
        'comments': (0, 500),
        'watch_time_minutes': (0, 100000),
        'video_length_minutes': (1, 30),
        'subscribers': (0, 500000),
        'engagement_rate': (0, 0.2),
        'avg_watch_time_per_view': (0, 10)
    }
    for col, (low, high) in clip_ranges.items():
        if col in video_df.columns:
            video_df[col] = video_df[col].clip(lower=low, upper=high)

    video_df_scaled = scaler.transform(video_df)
    prediction = model.predict(video_df_scaled)
    pred_usd = max(min(prediction[0], 1000), 1)

    rates = get_multi_currency_rates()
    rev_cols = st.columns(5)
    rev_cols[0].metric("🇺🇸 USD", f"${pred_usd:,.2f}")
    rev_cols[1].metric("🇮🇳 INR", f"₹{pred_usd*rates['INR']:,.2f}")
    rev_cols[2].metric("🇧🇷 BRL", f"R${pred_usd*rates['BRL']:,.2f}")
    rev_cols[3].metric("🇮🇩 IDR", f"Rp{pred_usd*rates['IDR']:,.0f}")
    rev_cols[4].metric("🇯🇵 JPY", f"¥{pred_usd*rates['JPY']:,.0f}")

    # --- Insights ---
    st.markdown("## 🧠 Smart Insights")
    if output['engagement_rate'] > 0.1:
        st.success("🚀 Your engagement is higher than average – this could boost ad revenue!")
    else:
        st.warning("📉 Engagement is below average – try increasing likes & comments.")
