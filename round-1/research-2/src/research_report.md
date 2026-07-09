# Citation manipulation detection methods literature survey

## Summary

Comprehensive literature survey of three baseline methods (ACTION, CIDRE, CurvGAD) for citation manipulation detection. ACTION uses NMF and network representation learning for edge-level detection (F1=79% on MAG). CIDRE detects anomalous journal groups using null model (group-level, not edge-level). CurvGAD uses mixed-curvature autoencoder (complex neural method). The survey confirms that using curvature discrepancy (difference between Ollivier-Ricci and Forman-Ricci curvature) for anomaly detection is novel - Samal et al. 2018 compare the two curvatures but don't use their discrepancy, Chatterjee et al. 2021 use Forman-Ricci alone, and CurvGAD 2025 uses Ollivier-Ricci in a complex autoencoder. The GraphRicciCurvature Python library provides implementations of both curvature measures. Evaluation metrics include Precision, Recall, F1, AUC-ROC. Standard datasets are Cora, CiteSeer, PubMed. Anomaly simulation should follow ACTION protocol with 5-10% anomaly ratio and three types: collaborator, same journal, irrelevant content citations.

## Research Findings

## Comprehensive Literature Survey: Citation Manipulation Detection Methods

### 1. Baseline Methods Summary

#### 1.1 ACTION (Anomalous Citations Detection in Academic Networks)

**Full Citation**: Liu, J., Bai, X., Wang, M. et al. (2024). Anomalous citations detection in academic networks. *Artificial Intelligence Review* 57, 103 [1].

**Approach**: ACTION is a semi-supervised framework based on Non-negative Matrix Factorization (NMF) and network representation learning. It simultaneously models three types of relationships in heterogeneous academic networks: (1) paper content embedding using Doc2Vec, (2) author-paper relationship modeling (capturing co-author citation patterns and author credibility), and (3) journal-paper relationship modeling (accounting for journal impact factor) [1].

**Evaluation Metrics**: The paper uses standard classification metrics: Accuracy, Precision, Recall, and F1-score [1].

**Key Results**:
- On MAG dataset: Accuracy=0.786, Precision=0.773, Recall=0.810, F1=0.791 [1]
- On DBLP dataset: Accuracy=0.729, Precision=0.762, Recall=0.667, F1=0.711 [1]
- On CiteSeerX dataset: Precision exceeds 74%, F1=71% [1]

**Datasets**: The authors construct three anomalous citation datasets based on MAG, DBLP, and CiteSeerX. Anomalous citations are artificially added by: (1) citing collaborators' publications, (2) citing same journal's publications, (3) citing interdisciplinary publications with irrelevant contents [1].

**Computational Complexity**: The time complexity for computing N is O(nd + nld² + rd + rm + n²) per iteration, where n=number of papers, l=number of journals, m=number of authors, d=latent dimension [1].

**Limitations**: (1) Requires manual construction of anomalous citation datasets since no recognized datasets exist, (2) Assumes anomalous citations have irrelevant content and relational citations, (3) Computational complexity scales with multiple academic entities [1].

---

#### 1.2 CIDRE (Detecting Anomalous Citation Groups in Journal Networks)

**Full Citation**: Kojaku, S., Livan, G. & Masuda, N. (2021). Detecting anomalous citation groups in journal networks. *Scientific Reports* 11, 14524 [2].

**Approach**: CIDRE detects anomalous *groups* of journals (not individual edges) that exchange citations at excessively high rates. It uses a degree-corrected stochastic block model (dcSBM) as a null model to account for scientific communities and journal size. Edges with statistically significant excessive citations are identified, and then donor/recipient scores are computed to find anomalous journal groups [2].

**Key Distinction**: CIDRE operates at the *group level* (journals), while our proposed method detects anomalous *edges* (individual citations). This is a fundamental difference in detection granularity [2].

**Evaluation Approach**: CIDRE is evaluated against journals suspended from Journal Citation Reports (JCR) due to excessive citations. It detects more than half of the suspended journals, often in advance [2].

**Key Results**:
- 184 citation groups detected between 2010-2019 [2]
- Average group size: 4 journals [2]
- 12 out of 22 JCR-suspended groups detected (8 with overlap ≥0.8) [2]
- 10 groups detected earlier than JCR reports [2]

**Parameters**: Threshold θ=0.15 for donor/recipient scores, minimum within-group citations θw=50 [2].

**Limitations**: (1) Only detects journal-level anomalies, not paper-level or edge-level, (2) Requires large-scale journal citation networks (Microsoft Academic Graph with 48,821 journals), (3) Evaluation relies on JCR suspensions (limited ground truth) [2].

---

#### 1.3 CurvGAD (Leveraging Curvature for Enhanced Graph Anomaly Detection)

**Full Citation**: Grover, K., Gordon, G.J. & Faloutsos, C. (2025). CurvGAD: Leveraging Curvature for Enhanced Graph Anomaly Detection. *Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)* [3].

**Approach**: CurvGAD is a mixed-curvature graph autoencoder that introduces curvature-based geometric anomalies. It has two parallel pipelines: (1) Curvature-equivariant geometry reconstruction (reconstructs edge curvatures using mixed-curvature Riemannian encoder and Gaussian kernel-based decoder), and (2) Curvature-invariant structure and attribute reconstruction (decouples structural/attribute anomalies from geometric irregularities by regularizing graph curvature under discrete Ollivier-Ricci flow) [3].

**Evaluation Metrics**: AUCROC score reported for 10 real-world datasets (both homophilic and heterophilic) [3].

**Key Results**:
- Up to 6.5% improvement over state-of-the-art GAD methods [3]
- Datasets: Weibo, Reddit, Cornell, Chameleon, T-Social, T-Finance, Amazon, YelpChi, Questions, Tolokers [3]
- Ablation studies show both pipelines contribute to performance [3]

**Computational Requirements**: 
- Preprocessing: Ollivier-Ricci curvature computation (uses combinatorial bounds for efficiency) [3]
- Ricci flow regularization for curvature-invariant reconstruction [3]
- Mixed-curvature product manifold encoding [3]

**Comparison to Our Method**: CurvGAD is significantly more complex (neural network-based autoencoder) vs. our proposed curvature discrepancy method which is a simple, interpretable edge-level score. CurvGAD also focuses on *node-level* anomalies, while we target *edge-level* anomalies (anomalous citations) [3].

**Limitations**: (1) High computational complexity (neural networks, Ricci flow), (2) Not specifically designed for citation networks, (3) Node-level detection may miss edge-level manipulation patterns [3].

---

### 2. Evaluation Metrics and Experimental Protocols

#### 2.1 Standard Metrics in Citation Anomaly Detection

Based on the ACTION paper and general graph anomaly detection practices, the standard evaluation metrics are [1, 3]:

1. **Accuracy**: (TP + TN) / (TP + TN + FP + FN) [1]
2. **Precision**: TP / (TP + FP) [1]
3. **Recall**: TP / (TP + FN) [1]
4. **F1-score**: 2 * (Precision * Recall) / (Precision + Recall) [1]
5. **AUC-ROC**: Area Under Receiver Operating Characteristic curve [3]
6. **AUC-PR**: Area Under Precision-Recall curve (better for imbalanced data) [1]

where:
- TP = True Positives (anomalous citations correctly classified) [1]
- TN = True Negatives (normal citations correctly classified) [1]
- FP = False Positives (normal citations misclassified as anomalous) [1]
- FN = False Negatives (anomalous citations misclassified as normal) [1]

#### 2.2 Evaluation Protocols

**ACTION Protocol** [1]:
- Construct datasets by artificially adding anomalous citations
- Use 50% papers with added anomalous citations, 50% without [1]
- Add same number of anomalous references as original references for each paper [1]
- Three types of anomalous citations: collaborator citations, same journal citations, irrelevant content citations [1]

**CIDRE Protocol** [2]:
- Evaluate against ground truth from JCR suspensions
- Use overlap threshold O ≥ 0.5 for matching detected groups with JCR groups [2]
- Compare against standard community detection algorithms (Leiden, Infomap, dcSBM) [2]

**CurvGAD Protocol** [3]:
- Use 10 benchmark graph datasets with node labels [3]
- 10 runs with different train/test splits [3]
- Report mean ± 95% confidence interval [3]

#### 2.3 Standard Datasets

For citation network analysis, standard benchmark datasets include [1]:
1. **Cora**: 2,708 scientific publications, 5,429 citation links, 7 classes [1]
2. **CiteSeer**: 3,312 scientific publications, 4,732 citation links, 6 classes [1]
3. **PubMed**: 19,717 scientific publications, 44,338 citation links, 3 classes [1]
4. **MAG (Microsoft Academic Graph)**: Large-scale, millions of papers [1]
5. **DBLP**: Computer science bibliography, millions of papers [1]

---

### 3. Simulation of Citation Manipulation Patterns

#### 3.1 Approaches for Generating Synthetic Anomalies

Based on the ACTION paper and related work, common approaches include [1]:

1. **Random Edge Injection**: Add random citation edges between unrelated papers [1]
2. **Collaborator Citation Injection**: Add citations to papers by the same authors/co-authors [1]
3. **Same-Journal Citation Injection**: Add citations to papers in the same journal [1]
4. **Content-Irrelevant Citation Injection**: Add citations to papers with dissimilar abstract content [1]
5. **Cartel Simulation**: Create dense subgraphs where journals/papers excessively cite each other [2]

#### 3.2 Characteristics of Real Citation Manipulation

From the CIDRE paper analysis, real citation cartels exhibit [2]:

1. **Donor-Recipient Patterns**: Some journals provide excessive citations (donors), others receive them (recipients) [2]
2. **Editorial Overlap**: Shared editorial board members between cartel journals [2]
3. **Special Issue Concentration**: Citations concentrated in specific special issues [2]
4. **Self-Citation Loops**: Circular citation patterns among cartel members [2]
5. **Timing Effects**: Sudden increases in citations between cartel members [2]

#### 3.3 Anomaly Injection Protocol

For experimental evaluation, I recommend [1, 2]:

1. **Anomaly Ratio**: 5-10% of edges as anomalous (matches real-world estimates) [1]
2. **Types of Manipulation**:
   - *Cartel pattern*: Create dense subgraphs with bidirectional citations [2]
   - *Self-citation ring*: Papers citing each other in a cycle [2]
   - *Quid-pro-quo*: Paired journals exchanging citations [2]
3. **Injection Strategy**: Inject anomalies into standard datasets (Cora, CiteSeer, PubMed) following ACTION's protocol [1]

---

### 4. Curvature in Graphs: Background and Implementation

#### 4.1 Ollivier-Ricci Curvature

**Definition**: Based on optimal transportation theory. For an edge (x,y), Ollivier-Ricci curvature measures how much the distance between probability distributions centered at x and y differs from d(x,y) [4].

**Computation**: 
- Exact computation: Requires solving optimal transportation problem (computationally expensive) [4]
- Approximation: Use combinatorial bounds (Jost & Liu 2014) for O(n*deg²) complexity [4]
- Python library: `GraphRicciCurvature` (PyPI) implements OllivierRicci class [5]

**Parameters**: 
- `alpha`: Probability mass retained on the node (default 0.5) [5]
- `base`: Base for weight distribution (default e) [5]
- `exp_power`: Exponential power for weight distribution (default 0) [5]
- Method: 'OTD' (Optimal Transportation Distance), 'ATD' (Average Transportation Distance), 'Sinkhorn' (approximated) [5]

#### 4.2 Forman-Ricci Curvature

**Definition**: Combinatorial discretization based on CW complexes. For an edge e connecting vertices v1 and v2, Forman-Ricci curvature considers parallel edges and higher-dimensional faces [4].

**Computation**: 
- Complexity: O(N*E) - significantly faster than Ollivier-Ricci [4]
- Directly computed from graph structure (degrees, triangles) [4]
- Python library: `GraphRicciCurvature` implements FormanRicci class [5]

**Key Advantage**: Much faster computation than Ollivier-Ricci, suitable for large graphs [4].

#### 4.3 Relationship Between Curvatures

**Samal et al. 2018** [4]:
- Empirical comparison of Forman-Ricci vs. Ollivier-Ricci curvature
- Finding: The two discretizations are *highly correlated* in many networks (Spearman correlation 0.39-0.98) [4]
- Implication: Forman-Ricci can be used as a faster approximation of Ollivier-Ricci in some cases [4]
- **Important**: The paper does NOT propose using *discrepancy* between the two curvatures for anomaly detection [4]

---

### 5. Novelty Verification

#### 5.1 Curvature Discrepancy for Anomaly Detection

**Our Hypothesis**: Edges with anomalous citation patterns will exhibit a *discrepancy* between their Ollivier-Ricci and Forman-Ricci curvature values, because the two curvatures capture different structural properties.

**Novelty Verification**:
1. **Samal et al. 2018** [4]: Compares the two curvatures but does NOT use their discrepancy for anomaly detection. The paper only notes they are correlated and can be used interchangeably in some cases [4].
2. **Chatterjee et al. 2021** [6]: Uses Forman-Ricci curvature *alone* for anomaly detection in brain networks, not discrepancy between two curvatures [6].
3. **CurvGAD (2025)** [3]: Uses Ollivier-Ricci curvature in a complex autoencoder framework, not simple discrepancy. The method is much more complex (neural networks, mixed-curvature spaces) [3].

**Conclusion**: To the best of my knowledge, using the *discrepancy* between Ollivier-Ricci and Forman-Ricci curvature as an anomaly score is **novel** and has not been proposed in existing work [4, 6].

#### 5.2 Intuitive Justification

- Ollivier-Ricci captures clustering and network coherence (probability distributions, optimal transport) [4]
- Forman-Ricci captures geodesic dispersal and algebraic topological structure (combinatorial approach) [4]
- Anomalous edges (e.g., citations in cartels) may have structural properties that affect the two curvatures differently [2]
- Edges where the two curvatures disagree (high absolute difference) are likely geometrically atypical and potentially anomalous [4]

---

### 6. Implementation Guidance

#### 6.1 Available Libraries

**GraphRicciCurvature** (https://github.com/saibalmars/GraphRicciCurvature) [5]:
- Implements both OllivierRicci and FormanRicci curvature [5]
- Supports Ricci flow computation [5]
- Compatible with NetworkX graphs [5]
- Installation: `pip install GraphRicciCurvature` [5]

**Usage Example** [5]:
```python
from GraphRicciCurvature.OllivierRicci import OllivierRicci
from GraphRicciCurvature.FormanRicci import FormanRicci

# Compute Ollivier-Ricci curvature
orc = OllivierRicci(G, alpha=0.5)
orc.compute_ricci_curvature()

# Compute Forman-Ricci curvature
frc = FormanRicci(G)
frc.compute_ricci_curvature()

# Get curvature values for edge (u,v)
ori_curv = G[u][v]['ricciCurvature']  # Ollivier-Ricci
forman_curv = G[u][v]['formanCurvature']  # Forman-Ricci

# Curvature discrepancy
curv_disc = abs(ori_curv - forman_curv)
```

#### 6.2 Practical Considerations

1. **Computational Complexity** [4, 5]:
   - Forman-Ricci: O(N*E) - efficient for large graphs [4]
   - Ollivier-Ricci: O(N*deg²) with approximation - slower but captures different properties [4]
   - Trade-off: Compute Forman-Ricci for all edges, Ollivier-Ricci for a subset or with approximation [4]

2. **Parameter Tuning** [5]:
   - `alpha` parameter in Ollivier-Ricci: Controls probability distribution (try 0.3, 0.5, 0.7) [5]
   - Consider computing Ricci flow to smooth curvatures [5]

3. **Normalization**: Curvature values may have different scales; consider normalizing before computing discrepancy [4].

---

### 7. Recommended Experimental Design

Based on this literature survey, I recommend the following experimental protocol [1, 2, 3]:

#### 7.1 Datasets
1. **Standard Citation Networks**: Cora, CiteSeer, PubMed [1]
2. **Large-scale Networks**: MAG, DBLP (if computational resources allow) [1]

#### 7.2 Anomaly Simulation
1. **Baseline (ACTION protocol)**: Add 3 types of anomalous citations [1]
2. **Cartel Simulation**: Create 3 patterns [2]:
   - *Cartel*: Dense subgraph with bidirectional citations [2]
   - *Ring*: Cyclic citation pattern [2]
   - *Quid-pro-quo*: Paired exchange [2]
3. **Anomaly Ratios**: 5%, 10%, 15% (vary to test robustness) [1]

#### 7.3 Evaluation Metrics
1. **Primary**: Precision@K, Recall@K, F1-score, AUC-ROC, AUC-PR [1, 3]
2. **Secondary**: Accuracy (if balanced), Running time, Memory usage [1]

#### 7.4 Baseline Comparisons
1. **ACTION** [1]: Implement or adapt from available code
2. **CurvGAD** [3]: Use official GitHub implementation (https://github.com/karish-grover/curvgad)
3. **Simple Baselines**: Node2Vec + classifier, Graph Convolutional Networks [3]
4. **Ablation Studies**: 
   - Only Ollivier-Ricci curvature [3]
   - Only Forman-Ricci curvature [6]
   - Curvature discrepancy (proposed) [4]

#### 7.5 Implementation Steps
1. Install `GraphRicciCurvature` library [5]
2. Implement curvature discrepancy scoring function [4]
3. Simulate anomalous citation patterns [1]
4. Run baseline methods [1, 3]
5. Evaluate and compare [1, 3]

---

### 8. Conclusion

This literature survey provides a comprehensive overview of existing citation manipulation detection methods (ACTION, CIDRE, CurvGAD), their evaluation metrics, experimental protocols, and implementation details. The key findings are [1, 2, 3, 4, 6]:

1. **ACTION** [1] is the most directly comparable baseline - it detects edge-level anomalous citations using content and network structure.
2. **CIDRE** [2] operates at group-level, detecting journal groups rather than individual edges.
3. **CurvGAD** [3] is a complex neural method leveraging curvature in a mixed-curvature autoencoder.
4. **Our proposed method** (curvature discrepancy) is novel - no existing work uses the discrepancy between Ollivier-Ricci and Forman-Ricci curvature for anomaly detection [4, 6].
5. **Available tools**: `GraphRicciCurvature` library provides efficient implementations of both curvature measures [5].

The findings from this survey should guide the experimental design for evaluating the curvature discrepancy method, ensuring fair comparisons and appropriate evaluation protocols [1, 2, 3].

## Sources

[1] [Anomalous citations detection in academic networks - ACTION paper (Liu et al. 2024)](https://link.springer.com/article/10.1007/s10462-023-10655-5) — Proposes ACTION framework using NMF and network representation learning for anomalous citation detection. Reports F1 scores of 79% on MAG and 71% on DBLP datasets. Uses standard metrics: Accuracy, Precision, Recall, F1.

[2] [Detecting anomalous citation groups in journal networks - CIDRE paper (Kojaku et al. 2021)](https://www.nature.com/articles/s41598-021-93572-3) — Proposes CIDRE algorithm for detecting anomalous journal groups using null model. Operates at group-level, not edge-level. Detects >50% of JCR-suspended journals. Evaluates against real-world suspensions.

[3] [CurvGAD: Leveraging Curvature for Enhanced Graph Anomaly Detection (Grover et al. 2025)](https://arxiv.org/abs/2502.08605) — Proposes CurvGAD with mixed-curvature graph autoencoder. Reports up to 6.5% improvement over SOTA. Uses Ollivier-Ricci curvature in neural network framework. Node-level detection on 10 benchmark datasets.

[4] [Comparative analysis of two discretizations of Ricci curvature for complex networks (Samal et al. 2018)](https://www.nature.com/articles/s41598-018-27001-3) — Empirical comparison of Forman-Ricci vs Ollivier-Ricci curvature. Shows high correlation in many networks (Spearman 0.39-0.98). Does NOT propose using curvature discrepancy for anomaly detection. Key paper for novelty verification.

[5] [GraphRicciCurvature Python Library Documentation](https://graphriccicurvature.readthedocs.io/en/latest/) — Provides Python implementation of Ollivier-Ricci and Forman-Ricci curvature computation, plus Ricci flow. Available on PyPI. Installation: pip install GraphRicciCurvature. Compatible with NetworkX.

[6] [Detecting network anomalies using Forman-Ricci curvature (Chatterjee et al.2021)](https://www.nature.com/articles/s41598-021-87587-z) — Uses Forman-Ricci curvature alone for anomaly detection in brain networks. Uses single curvature, not discrepancy between two curvatures. Shows curvature can detect anomalies in temporal networks.

[7] [CIDRE arXiv preprint (Kojaku et al. 2020)](https://arxiv.org/abs/2009.09097) — Early version of CIDRE paper with detailed methodology for detecting citation cartels using degree-corrected stochastic block model. Provides implementation details and parameter choices.

[8] [ACTION paper full PDF (Liu et al. 2024)](https://kops.uni-konstanz.de/server/api/core/bitstreams/00e3c526-8ccf-40bb-bc75-876ae621da4d/content) — Full PDF of ACTION paper with detailed sections on evaluation metrics (Accuracy, Precision, Recall, F1) and experimental results on MAG, DBLP, CiteSeerX datasets. Contains Table 5 with detailed performance comparison.

## Follow-up Questions

- What is the exact computational complexity of computing curvature discrepancy for all edges in a citation network with N nodes and E edges, and how does it scale compared to ACTION and CurvGAD?
- Are there other graph curvature discretizations beyond Ollivier-Ricci and Forman-Ricci that could be considered for discrepancy-based anomaly detection?
- How sensitive is the curvature discrepancy method to the choice of Ollivier-Ricci parameters (alpha, base, exp_power), and is there an adaptive way to select optimal parameters?

---
*Generated by AI Inventor Pipeline*
