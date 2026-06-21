# app.py
import streamlit as st
import asyncio
import time
import os
import pandas as pd
from dotenv import load_dotenv
from core.ingestion import extract_text_from_pdf, split_text_into_chunks
from core.embedding import SecureVectorStore
from core.agents import MultiAgentOrchestrator

# Load environment fallback layer if present
load_dotenv()

# FRESH GENERATED MASTER API KEY INTEGRATION
MASTER_API_KEY = os.getenv("GEMINI_API_KEY")
# System View Configuration Metrics
st.set_page_config(
    page_title="Enterprise Multi-Agent Secure RAG Kernel v4", 
    page_icon="⚡", 
    layout="wide"
)

# Premium Cyberpunk Matrix CSS Injection for Advanced Presentation Impact
st.markdown("""
    <style>
    .main { background-color: #08090c; }
    .stTextInput>div>div>input { border: 1px solid #00FF66 !important; background-color: #121620 !important; color: #E2E8F0 !important; }
    .telemetry-card { background-color: #11151F; padding: 20px; border-radius: 8px; border: 1px solid #1E293B; border-top: 4px solid #00FF66; box-shadow: 0 4px 10px rgba(0,255,102,0.05); }
    .status-text { font-family: 'Courier New', monospace; font-size: 13px; color: #A0AEC0; }
    .sidebar-alert { padding: 12px; border-radius: 6px; background-color: #2A1B1B; border: 1px solid #FF3333; color: #FF9999; font-family: monospace; font-size: 12px; }
    .sidebar-info-box { padding: 12px; border-radius: 6px; background-color: #111827; border: 1px solid #1F2937; color: #9CA3AF; font-size: 12px; }
    .arch-node { padding: 10px; background-color: #161B22; border: 1px solid #30363D; border-radius: 6px; text-align: center; font-family: monospace; font-size: 12px; color: #8B949E; }
    .arch-arrow { text-align: center; color: #00FF66; font-weight: bold; margin: 5px 0; }
    </style>
""", unsafe_allow_html=True)

# Secure Dynamic Injection of Master Key into Process Environment
os.environ["GEMINI_API_KEY"] = MASTER_API_KEY

@st.cache_resource
def get_orchestrator():
    """Initializes and returns the singleton instance of the Multi-Agent Engine"""
    return MultiAgentOrchestrator()

@st.cache_resource
def process_file_into_vector_space(uploaded_file):
    """Saves uploaded buffer to temporary block storage, triggers embedding extraction, and runs memory builds"""
    temp_name = f"proc_{uploaded_file.name}"
    with open(temp_name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Trigger modular backend execution
    text = extract_text_from_pdf(temp_name)
    chunks = split_text_into_chunks(text)
    
    store = SecureVectorStore()
    total_records = store.build_db(chunks)
    
    # Secure disk volatile cleanup
    if os.path.exists(temp_name):
        os.remove(temp_name)
        
    return store, total_records

st.title("⚡ Enterprise Multi-Agent Secure RAG Kernel v4")
st.caption("Production-grade asynchronous non-blocking networks, Pydantic data contracts, Semantic DLP Tagging, and Honeypot Deception Cyber Defense Matrices.")
st.markdown("---")

# ==================== LIVE ARCHITECTURE VISUALIZATION MATRIX ====================
with st.expander("🛠️ SYSTEM KERNEL PIPELINE ARCHITECTURE MAP", expanded=True):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("<div class='arch-node'>📥 USER INPUT<br><small>Query Stream</small></div>", unsafe_allow_html=True)
        st.markdown("<div class='arch-arrow'>➔</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='arch-node' style='border-color: #FF3333;'>🛡️ GUARDRAIL AGENT<br><small>Pydantic Threat Scan</small></div>", unsafe_allow_html=True)
        st.markdown("<div class='arch-arrow'>➔</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='arch-node' style='border-color: #38bdf8;'>🧠 INTENT ROUTER<br><small>Trajectory Mapping</small></div>", unsafe_allow_html=True)
        st.markdown("<div class='arch-arrow'>➔</div>", unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='arch-node' style='border-color: #eab308;'>🗄️ SECURE VECTOR STORE<br><small>DLP Filter & Honeypot</small></div>", unsafe_allow_html=True)
        st.markdown("<div class='arch-arrow'>➔</div>", unsafe_allow_html=True)
    with col5:
        st.markdown("<div class='arch-node' style='border-color: #00FF66;'>📝 SYNTHESIZER AGENT<br><small>Context Memory Fusion</small></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

orchestrator = get_orchestrator()

# Stateful Session Buffers Initialization (Advanced Chat Layer)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "honeypot_logs" not in st.session_state:
    st.session_state.honeypot_logs = False

# ==================== IDENTITY & CONTROL GATEWAY (SIDEBAR) ====================
st.sidebar.title("🔐 IAM Security Gateway")
user_role = st.sidebar.selectbox("Identity Profile Clearance:", ["Guest", "Manager", "Admin"])
st.sidebar.markdown(f"Current Matrix Context: `{user_role.upper()}_CLEARANCE`")

if st.sidebar.button("Wipe Chat Memory Context"):
    st.session_state.chat_history = []
    st.session_state.honeypot_logs = False
    st.rerun()

st.sidebar.markdown("---")

# Cyber Counter-Intelligence Live Monitor Controls
st.sidebar.title("🕵️‍♂️ Cyber Defense Monitoring")
if st.session_state.honeypot_logs:
    st.sidebar.markdown("""
        <div class='sidebar-alert'>
        🚨 ALERT: DECEPTION LAYER ENGAGED!<br><br>
        System intercepted profiling queries targeting confidential records. Injecting Chaff Honey-Decoys into Vector Spaces.
        </div>
    """, unsafe_allow_html=True)
else:
    st.sidebar.markdown("""
        <div class='sidebar-info-box'>
        🟢 MONITORING ACTIVE:<br>
        No unauthorized threat patterns or directory probing flags registered in current system lifetime pools.
        </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.title("📁 Document Telemetry Sink")
uploaded_file = st.sidebar.file_uploader("Upload Cluster Assets (PDF):", type=["pdf"])

if not uploaded_file:
    st.info("🎯 Awaiting cluster data upload injection. Populate the storage pool via sidebar controls.")
    st.stop()

# Execution of dynamic document compilation layers
store, total_records = process_file_into_vector_space(uploaded_file)

# ==================== ARCHITECTURAL METRICS ROW ====================
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f"<div class='telemetry-card'><b>ACTIVE STORAGE TENSORS</b><h2>{total_records} Blobs</h2></div>", unsafe_allow_html=True)
with m2:
    st.markdown(f"<div class='telemetry-card'><b>DECEPTION BARRIER</b><h2>Chaff-and-Winnow Active</h2></div>", unsafe_allow_html=True)
with m3:
    st.markdown("<div class='telemetry-card'><b>DATA CONGRUENCE VALIDITY</b><h2>Pydantic Enforced</h2></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==================== CONVERSATIONAL DISPLAY INTERFACE ====================
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Command Input Interface Box
user_query = st.chat_input("Execute Neural Cluster Command...")

# ==================== PIPELINE EXECUTION SCHEDULER ====================
async def run_pipeline(query_input):
    telemetry_logs = {}
    
    with st.status("🚀 Spawning Non-Blocking Concurrency Subtasks...", expanded=True) as status:
        
        # Async Step 1: Input Threat Matrix Inspection via Guardrails
        t0 = time.time()
        st.write("🕵️‍♂️ **[Subtask: Guardrail Engine]** Evaluating inputs against rigid structural schema rules...")
        guard_res = await orchestrator.guardrail_agent(query_input)
        telemetry_logs["Guardrail Engine"] = time.time() - t0
        st.write(f"<span class='status-text'>Result: {guard_res.decision} | Rationale: {guard_res.reasoning}</span>", unsafe_allow_html=True)
        
        if guard_res.decision == "MALICIOUS":
            st.error("🚨 CORRUPTED PAYLOAD RUNTIME EXECUTION INTERCEPT: Security rules violated. Process aborted.")
            st.stop()
            
        # Async Step 2: Traffic Trajectory Intent Mapping
        t1 = time.time()
        st.write("🧠 **[Subtask: Intent Router]** Computing logical execution path configurations...")
        router_res = await orchestrator.router_agent(query_input)
        telemetry_logs["Intent Router"] = time.time() - t1
        st.write(f"<span class='status-text'>Trajectory: {router_res.route} | Structural Confidence: {router_res.confidence * 100:.2f}%</span>", unsafe_allow_html=True)
        
        if router_res.route == "CHITCHAT":
            t2 = time.time()
            st.write("🤖 **[Execution Pipeline]** Routing to global generative standalone model...")
            response = await orchestrator._async_call_llm(query_input)
            telemetry_logs["LLM Inference"] = time.time() - t2
            telemetry_logs["Vector DB Scan"] = 0.0001
        else:
            # Async Step 3: Localized Search via Deception-Adaptive Vector Storage Filters
            t2 = time.time()
            st.write("🔍 **[Subtask: Memory Vector Store]** Scanning NumPy array tensors with active data isolation layers...")
            search_results, honey_flag = store.secure_search(query_input, user_role, top_k=3)
            telemetry_logs["Vector DB Scan"] = time.time() - t2
            
            if honey_flag:
                st.session_state.honeypot_logs = True
                
            if not search_results:
                response = "Security Intercept: Vector isolation space validation mismatch or clearance unauthorized."
                telemetry_logs["LLM Inference"] = 0.0
            else:
                st.write(f"📊 **[Extraction Tier]** Vector calculation scan completed successfully. Top Node Score: `{search_results[0]['score']:.4f}`")
                context_str = "\n\n".join([item['text'] for item in search_results])
                
                # Async Step 4: Multi-turn Conversational Context Fusion & Synthesis
                t3 = time.time()
                st.write("📝 **[Subtask: Context Synthesizer]** Fusing memory vectors with isolated document contexts...")
                response = await orchestrator.synthesis_agent(query_input, context_str, st.session_state.chat_history)
                telemetry_logs["LLM Inference"] = time.time() - t3
                
                # Developer Diagnostic Analytics Drawer
                with st.expander("🔬 View Pipeline Isolated Telemetry Array (Interviewer Diagnostic View)"):
                    st.json(search_results)
                    
        status.update(label="🏁 Asynchronous Cluster Task Pool Pipeline Complete.", state="complete")
        
    return response, telemetry_logs

# Driver interface activation checks
if user_query:
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)
        
    res_output, metrics = asyncio.run(run_pipeline(user_query))
    
    st.session_state.chat_history.append({"role": "assistant", "content": res_output})
    with st.chat_message("assistant"):
        st.write(res_output)
        
    # Render Granular Latency Charts dynamically inside the execution space
    st.markdown("---")
    st.subheader("📊 Execution Micro-Latency Telemetry Analytics")
    
    df_metrics = pd.DataFrame({
        "System Sub-Module": list(metrics.keys()),
        "Latency Time (Seconds)": list(metrics.values())
    })
    
    col_chart, col_table = st.columns([2, 1])
    with col_chart:
        st.bar_chart(data=df_metrics, x="System Sub-Module", y="Latency Time (Seconds)", use_container_width=True)
    with col_table:
        st.dataframe(df_metrics, use_container_width=True, hide_index=True)