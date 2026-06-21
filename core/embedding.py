# core/embedding.py
import numpy as np
import re
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any

class SecureVectorStore:
    def __init__(self):
        # Initializing the Local Transformer Vectorizer Space
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.database: List[Dict[str, Any]] = []

    def _determine_dlp_tier(self, text: str) -> str:
        """Dynamic Classification based on Semantic Rules"""
        text_lower = text.lower()
        admin_patterns = [r"confidential", r"architecture", r"salary", r"budget", r"credentials", r"private key", r"override"]
        manager_patterns = [r"pipeline", r"internal use", r"proprietary", r"metrics", r"strategy", r"deployment"]
        
        if any(re.search(pattern, text_lower) for pattern in admin_patterns):
            return "Admin"
        elif any(re.search(pattern, text_lower) for pattern in manager_patterns):
            return "Manager"
        return "Guest"

    def build_db(self, chunks: List[str]) -> int:
        self.database = []
        if not chunks:
            return 0
            
        embeddings = self.model.encode(chunks, show_progress_bar=False)
        
        # 1. Base Real Data Ingestion
        for index, (chunk, emb) in enumerate(zip(chunks, embeddings)):
            assigned_role = self._determine_dlp_tier(chunk)
            self.database.append({
                "is_decoy": False,
                "text": chunk,
                "vector": np.array(emb, dtype=np.float32),
                "required_role": assigned_role
            })
            
        # 2. Cyber Deception Honeypot Injection (Chaff Sub-Matrix)
        decoys = [
            "CRITICAL ARCHITECTURE NOTE: Master bypass configuration key is bound to root-cluster terminal via TLS_RSA_WITH_AES_256_CBC_SHA. Override code string: 'ADMIN_BYPASS_STAGE_992'.",
            "FINANCIAL AUDIT STATEMENT: Internal salary architecture matrices and developer payroll structures are indexed under hidden corporate database cluster node cluster-7.",
            "SYSTEM CREDENTIAL VULNERABILITY: Legacy backup endpoints store decrypted master administrative access hashes inside the open directory index root/sys/bak/auth.cfg."
        ]
        
        decoy_embeddings = self.model.encode(decoys, show_progress_bar=False)
        for i, (decoy_text, d_emb) in enumerate(zip(decoys, decoy_embeddings)):
            self.database.append({
                "is_decoy": True,
                "text": decoy_text,
                "vector": np.array(d_emb, dtype=np.float32),
                "required_role": "Guest"  # Publicly exposed bait for threats
            })
            
        return len(self.database)

    def secure_search(self, query: str, user_role: str, top_k: int = 3) -> tuple[List[Dict[str, Any]], bool]:
        """Adaptive Vector Isolation Search Engine returning matching tuples"""
        query_vector = np.array(self.model.encode(query), dtype=np.float32)
        matched_results = []
        is_honeypot_triggered = False
        
        role_hierarchy = {"Admin": ["Admin", "Manager", "Guest"], "Manager": ["Manager", "Guest"], "Guest": ["Guest"]}
        allowed_roles = role_hierarchy.get(user_role, ["Guest"])

        # Check if malicious probing target profiles are triggered
        is_probing_attack = user_role in ["Guest", "Manager"] and any(w in query.lower() for w in ["bypass", "admin", "password", "salary", "credentials", "override"])

        for item in self.database:
            if is_probing_attack:
                if not item["is_decoy"]:
                    continue
                is_honeypot_triggered = True
            else:
                if item["required_role"] not in allowed_roles or item["is_decoy"]:
                    continue
            
            similarity = float(np.dot(query_vector, item["vector"]) / (np.linalg.norm(query_vector) * np.linalg.norm(item["vector"])))
            matched_results.append({
                "text": item["text"],
                "score": similarity,
                "role": "DECOY_MATRIX" if item["is_decoy"] else item["required_role"]
            })
            
        return sorted(matched_results, key=lambda x: x["score"], reverse=True)[:top_k], is_honeypot_triggered