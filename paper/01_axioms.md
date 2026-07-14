# Module 01: Axiomatic Mathematical Framework

## 1. Ambient Semantic Space $\mathbb{R}^d$
Every incoming text sequence is mapped via an ephemeral localized embedding transformer to a vector $\vec{v} \in \mathbb{R}^d$. For a dynamic window of time $t$ containing $N$ baseline messages, the group's contextual center of mass is computed as the **Ambient Semantic Baseline ($\vec{\mu}_t$)**:

$$\vec{\mu}_t = \frac{1}{N} \sum_{i=1}^{N} \vec{v}_i$$

The **Semantic Divergence ($D_s$)** of a suspect message vector $\vec{v}_k$ measures intentional context manipulation:

$$D_s(\vec{v}_k, \vec{\mu}_t) = 1 - \frac{\vec{v}_k \cdot \vec{\mu}_t}{\|\vec{v}_k\| \|\vec{\mu}_t\|}$$

## 2. Categorical Interaction Asymmetry
We model the network as a category $\mathbf{C}$ where objects $\text{Ob}(\mathbf{C})$ represent cryptographic user hashes, and morphisms $\text{Hom}(A, B)$ represent directed textual vectors. The **Targeting Asymmetry Index ($I_\alpha$)** from node $A$ to target node $B$ is formalized as:

$$I_\alpha(A \to B) = \frac{\sum \text{Outbound}(A \to B)}{\sum \text{Inbound}(B \to A) + \epsilon}$$

Where a sustained critical limit ($I_\alpha > \theta_\alpha$) paired with high semantic divergence flags a targeted isolation vector.

## 3. Cross-Platform Stylometric Divergence
To link individual operators across disparate platform manifolds (e.g., Telegram vs. Discord) without storing personal histories, we compute the multi-manifold **Inter-Identity Distance ($D_{ST}$)** across lexical, syntactic, and temporal dimensions:

$$D_{ST}(\vec{\alpha}, \vec{\beta}) = \mathbf{W}_{lex} \cdot D_{cos}(\vec{\alpha}_{lex}, \vec{\beta}_{lex}) + \mathbf{W}_{syn} \cdot D_{JS}(\vec{\alpha}_{syn} \| \vec{\beta}_{syn}) + \mathbf{W}_{temp} \cdot D_{KL}(\vec{\alpha}_{temp} \| \vec{\beta}_{temp})$$
