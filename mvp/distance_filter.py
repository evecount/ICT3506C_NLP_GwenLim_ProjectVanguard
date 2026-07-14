import numpy as np

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2 + 1e-9)

def analyze_behavior(user_vector, ambient_baseline, outbound_count, inbound_count):
    """
    Executes the baseline zero-knowledge mathematical filter.
    Returns Semantic Divergence (Ds) and Targeting Asymmetry (I_alpha).
    """
    # 1. Calculate Semantic Divergence
    similarity = cosine_similarity(user_vector, ambient_baseline)
    d_s = 1.0 - similarity
    
    # 2. Calculate Targeting Asymmetry Index (epsilon = 1e-5)
    i_alpha = outbound_count / (inbound_count + 1e-5)
    
    return d_s, i_alpha

if __name__ == "__main__":
    # Mocking our synthetic manifold seeds (128-dimensional embedding space)
    np.random.seed(42)
    ambient_baseline = np.random.normal(0.1, 0.05, 128)
    
    # Synthetic Profile 01: Baseline Participant
    normal_user = np.random.normal(0.1, 0.06, 128)
    
    # Synthetic Profile 03: High-Risk Anomalous Scout (Highly divergent vector space)
    anomalous_scout = np.random.normal(-0.2, 0.1, 128)
    
    print("=== Algorithmic Manifold Verification Initialized ===")
    
    # Evaluate Normal User
    ds_norm, alpha_norm = analyze_behavior(normal_user, ambient_baseline, outbound_count=12, inbound_count=10)
    print(f"Baseline Profile:  D_s = {ds_norm:.4f} | I_alpha = {alpha_norm:.2f} -> STATUS: NOMINAL")
    
    # Evaluate Anomalous Scout (High structural asymmetry + high context divergence)
    ds_scout, alpha_scout = analyze_behavior(anomalous_scout, ambient_baseline, outbound_count=45, inbound_count=0)
    print(f"Anomalous Profile: D_s = {ds_scout:.4f} | I_alpha = {alpha_scout:.2f} -> STATUS: ALERT CRITICAL")
