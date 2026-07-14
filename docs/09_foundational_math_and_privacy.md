# Foundational Math & Privacy-by-Design Framework
*(Detailed conceptual axioms, mathematical models, and PDPA compliance architecture)*

By pivoting entirely to a **theoretical, architectural framework backed by synthetic validation**, the project completely bypasses the risk of mishandling personally identifiable information (PII) under the Singapore Personal Data Protection Act (PDPA).

## 1. Foundational Mathematical & Systemic Assumptions

To model behavioral analytics without needing real data, this paper establishes a set of axiomatic assumptions about how human interaction behaves mathematically when mapped to a vector space.

### Assumption A: The Ambient Semantic Baseline
We assume that an established group chat has a collective "ambient topic baseline" $\mu_t$ at any given timeframe $t$. Normal conversation forms a localized, high-density cluster in the embedding space $\mathbb{R}^d$.

If a user's messages consistently generate a semantic vector $\vec{v}_i$ such that the cosine distance from the baseline approaches maximum divergence while the structural network targeting narrows, it flags a deliberate context override rather than natural topic evolution:

$$\text{Semantic Divergence } (D_s) = 1 - \frac{\vec{v}_i \cdot \vec{\mu}_t}{\Vert{}\vec{v}_i\Vert{} \Vert{}\vec{\mu}_t\Vert{}}$$

### Assumption B: Interaction Asymmetry (Morphism Directedness)
In a standard social group, interaction forms a symmetric or broadly distributed graph. A predatory or "scouting" profile breaks this symmetry. We define this as a directed semantic morphism where user $A$ interacts with user $B$ with high frequency and emotional intensity, but the inverse mapping $B \to A$ is minimal or localized to defense/avoidance responses.

### Assumption C: Behavioral Burstiness and Velocity
Harmful behavior often exhibits high **semantic velocity**—accelerating from benign introductory tokens to high-risk, intrusive, or isolating language within a tight temporal window ($\Delta t$). We assume that natural relationships build intimacy through gradual semantic shifts, whereas malicious actors deliberately force steep gradients.

---

## 2. Privacy-by-Design & PDPA Compliance Framework

Turning the lack of empirical data into an architectural asset, the system is structured around **Data Minimization and PDPA Compliance**:

* **Zero-Knowledge Architecture:** The system is explicitly designed *not* to store or process raw personal data text locally.
* **Local Processing Anonymization:** In production, the pipeline uses an immediate, in-memory tokenization layer that converts text to abstract mathematical vectors ($\mathbb{R}^d$) at the ingestion gateway. The raw text strings containing names or chat copy are immediately volatile and dropped from memory, ensuring compliance with the PDPA Purpose Limitation and Protection Obligations.
* **Synthetic Evaluation Model:** For MVP validation, synthetic text datasets are procedurally generated using pre-defined behavioral profiles, proving the system's algorithmic efficacy while maintaining an absolute zero-risk privacy profile.

---

## 3. Structural Blueprint of the Synthetic Validation

Procedural data generation simulates the problem mathematically using these archetypes:

| Profile Archetype | Synthetic Linguistic Markers | Modeled Temporal Cadence | Target Structural Distribution |
| --- | --- | --- | --- |
| **The Baseline Participant** | High ambient topic alignment, casual slang, high emoji density. | Scattered, low burstiness, reactive to group prompts. | Broad distribution (many-to-many edges). |
| **The Irreverent Humorist** | Low semantic alignment (sudden shifts for punchlines), highly varied vocabulary. | Moderate burstiness, tied to active group conversation windows. | Broad distribution, receives high positive sentiment vectors back. |
| **The Scouting Profile** | Hyper-focused sentiment vectors, high density of isolation prompts ("DM me", "private"). | Targeted burstiness, rapid response latency *only* to a specific node. | Asymmetric directed graph (one-way dense clustering targeting a single node). |
