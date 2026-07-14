# Repository Architecture Matrix & Gateway Document
*(Strategic blueprint for the Vanguard project structure and README design)*

Structuring this exactly like a production code repository inside a project workspace is a brilliant approach. It speaks the language of a data scientist and a software engineer, immediately signalling to professors that academic research is treated with the same discipline as software architecture.

---

## 1. The Repository Architecture Matrix

To prevent content bloat, the workspace isolates distinct layers into a modular folder hierarchy:

```text
📁 behavioral-forensics-thesis/
│
├── 📄 README.md               <── The Central Command Document (Lecturer Gateway)
│
├── 📁 paper/                  <── Theoretical & Systemic Research Dossier
│   ├── 📄 01_axioms.md        │   - Mathematical vector formulas & baseline calculations
│   ├── 📄 02_anonymization.md │   - In-memory data minimization & PDPA compliance framework
│   └── 📄 03_cross_channel.md └── - Stylometric distance equations & multi-manifold structures
│
├── 📁 mvp/                    <── Functional Validation Modules
│   ├── 📄 requirements.txt    │   - Environment dependencies (scikit-learn, transformers)
│   ├── 📄 data_generator.py   │   - Procedural generation matrix for synthetic profiles
│   └── 📄 distance_filter.py  └── - Lightweight Python script executing baseline divergence math
│
└── 📁 UI/                     <── Interface Design Specifications
    ├── 📄 mock_wireframes.md  │   - Markdown layout charts detailing visual dashboard views
    └── 📄 architecture_flow.md└── - Ephemeral gateway data-flow diagrams
```

---

## 2. Setting Up the Central Document: `README.md`

The `README.md` serves as the central landing page. It provides the high-level executive summary and provides explicit markdown anchor links so lecturers can instantly navigate into specific technical folders.

*(Template for the Gateway Document)*

```markdown
# Privacy-Preserving Behavioral Anomaly Detection across Multi-Channel Manifolds

## Project Overview
This thesis project introduces a zero-knowledge architectural framework designed to detect anomalous behavioral tracking—such as conversational isolation and high-velocity semantic escalation—within high-volume group communications. 

To natively honor the **Singapore Personal Data Protection Act (PDPA)**, this system operates under strict data minimization parameters, converting volatile textual strings into mathematical vectors ($\mathbb{R}^d$) at the ingestion gateway before immediately purging plaintext records.

---

## Technical Navigation Matrix
Select a layer below to inspect the corresponding theoretical specifications, functional mockups, or evaluation modules:

### 1. 📘 [Theoretical & Systemic Research](./paper/)
* **[Axiomatic Mathematical Framework](./paper/01_axioms.md):** Formal equations establishing ambient semantic baselines, velocity acceleration, and categorical network asymmetry indexes ($I_\alpha$).
* **[PDPA Governance & Zero-Knowledge Architecture](./paper/02_anonymization.md):** In-memory processing architecture ensuring strict compliance with Data Minimization and Protection obligations.
* **[Cross-Platform Stylometry](./paper/03_cross_channel.md):** Advanced mathematical equations mapping Inter-Identity Distance ($D_{ST}$) to link disparate network operations without storing personal data.

### 2. 💻 [Functional MVP Code Modules](./mvp/)
* **[Procedural Profile Generator](./mvp/data_generator.py):** Python implementation synthesizing distinct behavioral archetypes (Baseline User, Chaos Agent, Anomalous Risk Profile).
* **[Algorithmic Metric Parser](./mvp/distance_filter.py):** Core execution script tracking semantic cosine divergence matrices against procedural populations.

### 3. 🎨 [Interface Design & Asset Schemas](./ui/)
* **[Dashboard Conceptual Wireframes](./ui/mock_wireframes.md):** Structured markdown interface maps visualizing Interaction Topologies and Semantic Velocity tracking lines.

---

## Execution Instructions
To execute the algorithmic verification loop using the non-PII synthetic data suite, execute the following commands in your terminal interface:
```bash
cd mvp
pip install -r requirements.txt
python distance_filter.py
```

---

## 3. Creating Workspace-Specific Skills in Antigravity

By dropping a declarative markdown file into a `.agents/skills/` directory at the root folder, the agent receives an explicit roadmap to maintain the repository:

* **Create file:** `.agents/skills/audit-thesis.md`
* **Add Frontmatter Configuration:**
```yaml
---
name: audit-thesis
description: Verifies structural alignment between code modules, mathematical documentation, and README layout boundaries.
---
```
* **Instructions:** Direct the agent workspace to audit the thesis folder layout, parsing mathematical assertions inside `paper/01_axioms.md` and ensuring script arrays inside `mvp/distance_filter.py` align perfectly.
