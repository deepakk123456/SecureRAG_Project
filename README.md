# ⚡ Enterprise Multi-Agent Secure RAG Kernel v4

A production-grade, asynchronous, non-blocking Multi-Agent RAG (Retrieval-Augmented Generation) system built with **Streamlit**, **Python**, and the **Google Gemini v2 SDK**. This system is architected for secure enterprise document intelligence, featuring built-in Cyber Counter-Intelligence, Data Loss Prevention (DLP) role-based access control, and dynamic Honeypot Deception technology.

---

## 🚀 Key Architectural Features

* **Asynchronous Non-Blocking Orchestration:** Powered by `asyncio` worker pools to handle heavy upstream LLM inferences concurrently. This design eliminates UI thread freezing and optimizes data stream processing pipelines.
* **Decoupled Multi-Agent Mesh:**
    * **Guardrail Agent:** Enforces strict structural security boundaries using Pydantic data contracts to intercept prompt injections, system overrides, and threat vectors.
    * **Intent Router:** Dynamically computes logical execution paths, seamlessly separating casual chat interactions from high-performance document semantic searches.
    * **Context Synthesizer:** Pairs localized semantic memory vectors with a sliding-window history buffer for resilient multi-turn conversation precision.
* **Cyber Counter-Intelligence (Honeypot Trap):** Implements an adaptive defense layer. If an unauthorized profile (e.g., Guest/Manager) queries sensitive vectors like passwords or admin keys, the system transparently feeds fake decoy matrix responses (`ADMIN_BYPASS_STAGE_992`) to deceive the attacker while instantly raising security alerts in the monitoring gateway.
* **Semantic DLP Clearance Isolation:** Enforces role-based hierarchy clearances (`Admin`, `Manager`, `Guest`) across standard NumPy array vector spaces to prevent unauthorized data leaks.
* **Graceful Degradation Fallback:** Built with a localized, deterministic rule-based backup framework. If the upstream provider throws a `403 Permission Denied` or network timeouts occur, the kernel triggers internal mock execution states to keep the system up and metrics rendering flawlessly.

---

## 📊 Live System Latency Telemetry
The integrated Streamlit UI provides real-time diagnostic reporting via dynamic **Micro-Latency Telemetry Analytics Charts**. This allows developers and system admins to instantly benchmark operational speeds across individual processing nodes (`Guardrail Engine`, `Intent Router`, `Vector Scan`, and `Inference`).

---

## 🛠️ Tech Stack & Core Libraries

* **Core Language:** Python 3.11+
* **Frontend UI Matrix:** Streamlit (Enhanced with Premium Cyberpunk Matrix CSS Custom Injections)
* **LLM Gateway Engine:** Google Gemini API (`google-genai` modern SDK)
* **Vector Embeddings Module:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Data Validations & Structure:** Pydantic v2, NumPy, Pandas, PyPDF

---

## 📂 Repository Structure

```text
SecureRAG_Project/
├── app.py                 # Core Driver, UI Orchestrator & Telemetry Dashboard
├── core/
│   ├── agents.py          # Multi-Agent Mesh Networks & Graceful Fallback Systems
│   ├── embedding.py       # Secure Vector Store, DLP Clearances, & Honeypot Injections
│   ├── ingestion.py       # PDF Text Compilation & Semantic Chunk Splitters
│   └── schemas.py         # Pydantic Data Contracts for Structural Integrity
├── .env                   # Local Volatile Credentials Environment Block (Excluded)
├── .gitignore             # Git Deployment Exclusions Configuration
└── README.md              # System Architecture Documentation


⚙️ Local Deployment & Setup Setup
1. Clone the Matrix

git clone [https://github.com/deepakk123456/SecureRAG_Project.git](https://github.com/deepakk123456/SecureRAG_Project.git)
cd SecureRAG_Project
2. Isolate the Virtual Environment

python -m venv venv
.\venv\Scripts\activate
3. Inject Core System Dependencies
Bash
pip install streamlit google-genai sentence-transformers numpy pandas pydantic python-dotenv pypdf
4. Configure Your Access Keys
Create a .env file inside the root project directory to secure your upstream token:


GEMINI_API_KEY=your_gemini_api_key_here
5. Launch the Production Kernel
Bash
python -m streamlit run app.py
