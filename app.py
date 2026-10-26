import streamlit as st
from chatbot import get_response
from streamlit_option_menu import option_menu
st.set_page_config(

    page_title="BuddyByte",
    page_icon="🎓",
    layout="wide"
)
st.markdown("""
<style>

/* Full App Background */
.stApp{
    background: #e3f2fd !important;
    color: #000000 !important;
}

body {
    color: #000000 !important;
}

/* Main title */
.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#000000;
}

/* Subtitle */
.subtitle{
    text-align:center;
    font-size:18px;
    color:#666666;
    margin-bottom:30px;
}

/* Cards */
.card{
            /* Card Heading */
.card h1,
.card h2,
.card h3{
    color:#000000 !important;
}

/* Card Description */
.card p{
    color:#555555 !important;
    font-size:16px;
}
            /* Card text */
.card h1,
.card h2,
.card h3,
.card h4,
.card h5,
.card h6,
.card p,
.card span,
.card small{
    color:#333333 !important;
}
    background:#ffffff;
    padding:20px;
    border-radius:18px;
    box-shadow:0 4px 15px rgba(0,0,0,.1);
    text-align:center;
    transition:0.3s;
    color:#333333;
}

.card:hover{
    transform:translateY(-5px);
}
     .stChatInput textarea::placeholder{
    color:#999999 !important;
    opacity:1;
}

/* Chat Messages */
.stChatMessage{
    border-radius:15px;
    padding:8px;
    background:#f0f0f0;
    color:#333333;
}

/* Chat Input */
 .stChatInput textarea{
    background:#f5f5f5 !important;
    color:#333333 !important;
    border: 1px solid #ddd !important;
}

.stChatInput textarea::placeholder{
    color:#999999 !important;
    opacity:1;
}

/* Buttons */
.stButton>button{
    background:#2563EB !important;   /* Blue */
    color:blue !important;          /* White text */
    border-radius:12px;
    border:none;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8 !important;
    color:white !important;
}
            /* Chat bubble background */
[data-testid="stChatMessage"]{
    background:#EAF4FF !important;
    border-radius:15px;
    padding:12px;
}

/* Chat text */
[data-testid="stChatMessageContent"],
[data-testid="stChatMessageContent"] p,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p{
    color:#000000 !important;
    font-weight:500;
}

/* User icon area */
[data-testid="stChatMessageAvatarUser"]{
    background:#2563EB;
}

/* Assistant icon area */
[data-testid="stChatMessageAvatarAssistant"]{
    background:#10B981;
}

/* Hide Sidebar */
[data-testid="stSidebar"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)
# Menu in Collapsible Box

with st.expander("📋 Menu", expanded=False):
    selected = option_menu(
        "🎓 Student Support",
        [
            "💬 AI Chat",
            "📊 Dashboard",
            "📚 Study Resources",
            "🎯 Placement",
            "🧠 Quiz",
            "📄 Resume"
        ],
        icons=[
            "chat",
            "bar-chart",
            "book",
            "bullseye",
            "brain",
            "file-earmark-person"
        ],
        menu_icon="mortarboard",
        default_index=0
    )
st.markdown("<h1 class='main-title'>🎓 BuddyByte</h1>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Powered by Groq • Ask anything about Coding, Assignments, DSA, AI, Placements & Career</p>", unsafe_allow_html=True)

# GitHub Link - Styled Button
st.markdown("""
<div style="text-align: center; margin: 20px 0;">
    <a href="https://github.com/saksham3818-ship-it/AI-STUDENT-SUPPORT" target="_blank" style="
        display: inline-block;
        background-color: #2563EB;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 16px;
    ">🔗 View Code on GitHub</a>
</div>
""", unsafe_allow_html=True)

st.divider()

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='card'>
    <h3>🤖 AI Chat</h3>
    <p>Instant Doubt Solving</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h3>📚 Study</h3>
    <p>Notes & Concepts</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <h3>📝 Assignments</h3>
    <p>AI Homework Help</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='card'>
    <h3>🎯 Placement</h3>
    <p>Interview Preparation</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Chat history
if selected == "💬 AI Chat":

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask your question...")

    if prompt:
        st.session_state.messages.append(
            {"role":"user","content":prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"): 
            st.markdown("""
<style>
[data-testid="stChatMessage"]:has(.stSpinner),
[data-testid="stChatMessage"]:last-child{
    background:#E3F2FD !important;
}
</style>
""", unsafe_allow_html=True) 
            
            with st.spinner("Thinking..."):
                answer = get_response(prompt)
                st.markdown(answer)

        st.session_state.messages.append(
            {"role":"assistant","content":answer}
        )


elif selected == "📊 Dashboard":

    st.title("📊 Student Dashboard")

    col1,col2,col3 = st.columns(3)

    col1.metric("Total Chats","120")
    col2.metric("Topics Covered","25")
    col3.metric("Learning Score","85%")


elif selected == "📚 Study Resources":

    st.title("📚 Study Resources")
    st.write("DSA, Java, Python, AI and Programming notes coming soon 🚀")


elif selected == "🎯 Placement":

    st.title("🎯 Placement Preparation")
    st.write("Interview questions, DSA roadmap and company preparation")


elif selected == "🧠 Quiz":

    st.title("🧠 AI Quiz")
    st.write("Practice programming and aptitude quizzes")


elif selected == "📄 Resume":

    st.title("📄 AI Resume Assistant")
    st.write("Resume improvement and career suggestions")
