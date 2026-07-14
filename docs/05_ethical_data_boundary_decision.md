# Ethical Data Boundary: The Decision Against Empirical Scraping
*(Provenance of the decision to strictly enforce Zero-Knowledge PDPA compliance)*

While initially considering the export of empirical chat logs (specifically from groups like "Super-Individual Secret Club" or "Timeleft" offshoots) to utilize messy, real-world data for testing the behavioral forensics pipeline, a strict ethical and regulatory boundary was enacted.

### The Problem with Empirical Chat Exports
* **Consent & Privacy:** Group chat participants have an implicit expectation of privacy. Exporting their communication history (JSON/CSV scraping) to train or test an NLP pipeline constitutes a breach of trust and potentially violates the **Singapore Personal Data Protection Act (PDPA)**.
* **Sensitive Forensic Artifacts:** Real chats containing instances of "scouting" or predatory behavior are highly sensitive. Retaining raw strings of these interactions on local developer machines poses a massive data liability.

### The Architectural Pivot: Pure Synthetic Simulation
To prove absolute ethical rigor and data safety to the academic evaluators, Project Vanguard explicitly rejects the ingestion of empirical chat databases. 

Instead, the architecture is forced to rely entirely on:
1. **Procedural Data Generation:** Using LLMs to construct simulated population spaces containing mathematical archetypes (The Baseline User, The Chaos Agent, The High-Risk Profiler).
2. **Abstract Topological Vectors:** If any real-world structure is tested, it must be instantly transformed into floating-point coordinate arrays ($\mathbb{R}^d$) at an ephemeral gateway, with all plaintext immediately purged from memory (The Zero-Knowledge constraint).

By formally logging this decision, Project Vanguard demonstrates that it is not merely a technical exercise, but a mature, enterprise-grade engineering project built on a foundation of strict ethical data hygiene.
