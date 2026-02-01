import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Loopism",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern design
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .content-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        margin: 1rem 0;
    }

    .header-text {
        color: white;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }

    .subheader-text {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 2rem;
    }

    .feature-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);
    }

    .metric-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
    }

    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }

    [data-testid="stSidebar"] .sidebar-content {
        color: white;
    }

    /* Input fields */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #667eea;
    }

    .stTextArea>div>div>textarea {
        border-radius: 10px;
        border: 2px solid #667eea;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="header-text">🔄 Loopism</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader-text">Transform Your Ideas Into Reality</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    st.markdown("---")

    mode = st.selectbox(
        "Select Mode",
        ["Creative", "Productive", "Analytical", "Experimental"],
        index=0
    )

    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    st.metric("Active Users", "1,234", "+12%")
    st.metric("Projects", "567", "+8%")
    st.metric("Success Rate", "94%", "+2%")

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">⚡</div>
            <div class="metric-label">Fast Performance</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
            <div class="metric-value">🎨</div>
            <div class="metric-label">Beautiful Design</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);">
            <div class="metric-value">🔒</div>
            <div class="metric-label">Secure & Private</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main interaction area
st.markdown('<div class="content-card">', unsafe_allow_html=True)

st.markdown("### 💡 Get Started")

user_input = st.text_area(
    "What would you like to create today?",
    placeholder="Enter your ideas, questions, or projects here...",
    height=150
)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("✨ Generate", use_container_width=True):
        if user_input:
            with st.spinner("Creating magic..."):
                st.success("Your request has been processed!")
                st.balloons()

                # Display result
                st.markdown("---")
                st.markdown("### 🎯 Result")
                st.info(f"Processing: {user_input}")
        else:
            st.warning("Please enter something to get started!")

st.markdown('</div>', unsafe_allow_html=True)

# Feature cards
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### ✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="feature-card">
            <h3>🚀 Lightning Fast</h3>
            <p>Experience blazing fast performance with our optimized platform.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="feature-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <h3>🎯 Intelligent</h3>
            <p>Smart algorithms that adapt to your needs and preferences.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
            <h3>🎨 Customizable</h3>
            <p>Fully customizable interface to match your style and workflow.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="feature-card" style="background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);">
            <h3>🔐 Secure</h3>
            <p>Enterprise-grade security to keep your data safe and private.</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: white; opacity: 0.8;'>Made with ❤️ by Loopism Team</p>",
    unsafe_allow_html=True
)
