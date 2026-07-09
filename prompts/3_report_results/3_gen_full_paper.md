# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_yVP3EQYR2wGM` — Curvature Discrepancy for Citation Manipulation Detection: A Geometric Approach with Simulation Validation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 02:41:44 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Curvature Discrepancy for Citation Manipulation Detection: A Geometric Approach with Simulation Validation
abstract: >-
  Citation manipulation undermines the integrity of scientific metrics. We propose a simple geometric feature—curvature discrepancy,
  the absolute difference between Ollivier-Ricci and Forman-Ricci curvature—for detecting anomalous citations in academic
  networks. The method is motivated by the observation that legitimate citations produce a predictable relationship between
  these two curvature measures, while manipulated citations create inconsistencies. We implement and evaluate this approach
  on the Cora citation network with simulated manipulation patterns following the ACTION protocol. With corrected Forman-Ricci
  curvature formula (F(e) = 4 - deg(u) - deg(v) for unweighted graphs), the method achieves AUC-ROC of 0.755 (95% bootstrap
  CI: [0.608, 0.878]) and outperforms unsupervised baselines (LOF: 0.492, Isolation Forest: 0.486). We provide interpretability
  case studies showing how curvature discrepancy highlights structurally inconsistent edges. While no public edge-level ground
  truth for citation manipulation exists, we position this work as a proof-of-concept and provide an honest assessment of
  the method's limitations alongside directions for future validation.
paper_text: |-
  # Introduction

  Citation manipulation—the practice of artificially inflating citation counts through coordinated efforts such as citation cartels, self-citation rings, and quid-pro-quo exchange agreements—undermines the integrity of scientific metrics and evaluation systems [1]. As academic institutions increasingly rely on citation-based metrics for hiring, promotion, and funding decisions, the detection of such manipulation has become a critical problem in scientometrics.

  Existing methods for detecting anomalous citations fall into three main categories. First, network representation learning approaches like ACTION [1] use non-negative matrix factorization and heterogeneous network embeddings to model paper content, author relationships, and journal impact factors simultaneously. Second, community detection methods like CIDRE [2] identify anomalous groups of journals that exchange citations at excessively high rates using degree-corrected stochastic block models. Third, recent neural approaches like CurvGAD [3] employ mixed-curvature graph autoencoders to reconstruct edge curvatures and detect geometric anomalies.

  While these methods achieve reasonable performance, they share important limitations. Representation learning approaches require complex model training that is computationally expensive and difficult to interpret. Community detection methods operate at the group level (journals), not the edge level (individual citations). Neural approaches require training complex autoencoders that are sensitive to hyperparameters and whose decisions are hard to explain to policy makers.

  In this work, we investigate a simple, interpretable geometric feature for citation manipulation detection: the **curvature discrepancy** between Ollivier-Ricci curvature and Forman-Ricci curvature. Our approach is motivated by a key insight from Riemannian geometry: when two different measures of the same underlying phenomenon disagree, this often signals anomaly. Ollivier-Ricci curvature [4] and Forman-Ricci curvature [5] capture different structural properties of networks. Ollivier-Ricci is based on optimal transport theory and measures how much probability distributions of random walks starting from adjacent nodes overlap after one step—capturing local citation flow properties. Forman-Ricci is combinatorial and based on the graph Laplacian—capturing how well-connected an edge is in terms of the clustering and triangle structure around it.

  Legitimate citations in a citation network follow a predictable relationship between these two curvature measures, as both ultimately reflect the local connectivity structure of the network [6]. However, citation manipulation patterns (cartels, rings, quid-pro-quo exchanges) create local structural irregularities that affect the two curvature measures differently. For example, a citation cartel creates dense bidirectional citations that increase clustering (affecting Forman-Ricci) but may not proportionally increase the optimal transport overlap (affecting Ollivier-Ricci). This produces a **curvature discrepancy**—a potential signature of manipulation.

  Our main contributions are:

  1. **Geometric Feature Implementation**: We implement curvature discrepancy (the difference between Ollivier-Ricci and Forman-Ricci curvature) for citation manipulation detection, with a corrected Forman-Ricci formula verified against the original source.

  2. **Empirical Evaluation with Statistical Validation**: We evaluate our method on the Cora citation network with simulated manipulation patterns, reporting bootstrap confidence intervals and cross-validation results. The method achieves AUC-ROC of 0.755 (95% CI: [0.608, 0.878]) and outperforms unsupervised baselines.

  3. **Interpretability Analysis**: We provide concrete examples of edges flagged as anomalous, showing their curvature values and explaining the geometric intuition.

  4. **Honest Assessment of Limitations**: We conduct a systematic search for real-world citation manipulation datasets and find that no public edge-level ground truth exists. We position this work as a proof-of-concept and discuss the implications for evaluation in this research area.

  The remainder of this paper is organized as follows. Section 2 reviews related work in citation manipulation detection and graph curvature. Section 3 defines the curvature discrepancy feature and describes our detection methodology, including the corrected Forman-Ricci formula. Section 4 presents the experimental setup and results with statistical validation. Section 5 discusses limitations, including the absence of real-world ground truth, and Section 6 concludes.

  [FIGURE:fig1]

  # Related Work

  ## Citation Manipulation Detection

  The problem of citation manipulation detection has gained significant attention in recent years. Liu et al. [1] proposed ACTION, a semi-supervised framework based on Non-negative Matrix Factorization (NMF) and network representation learning. ACTION models three types of relationships in heterogeneous academic networks: paper content (using Doc2Vec embeddings), author-paper relationships (capturing co-authorship and citation patterns), and journal-paper relationships (accounting for journal impact factor). However, ACTION requires manual construction of anomalous citation datasets and its computational complexity scales with multiple academic entities.

  Kojaku et al. [2] introduced CIDRE (Citation Detection and Reporting Engine), which detects anomalous *groups* of journals that exchange citations at excessively high rates. CIDRE uses a degree-corrected stochastic block model (dcSBM) as a null model and identifies edges with statistically significant excessive citations. A key distinction is that CIDRE operates at the *group level* (journals), while our method aims to detect anomalous *edges* (individual citations). CIDRE successfully detected 12 out of 22 journals suspended from Journal Citation Reports (JCR) due to excessive citations.

  Grover et al. [3] recently proposed CurvGAD, a mixed-curvature graph autoencoder that introduces curvature-based geometric anomalies. CurvGAD has two parallel pipelines: (1) curvature-equivariant geometry reconstruction using a mixed-curvature Riemannian encoder, and (2) curvature-invariant structure and attribute reconstruction. CurvGAD reports improvements over state-of-the-art graph anomaly detection methods, but it is computationally expensive and focuses on *node-level* anomalies rather than *edge-level* citation manipulation.

  A critical challenge across all these methods is evaluation. Liu et al. [1] note that 'there are no recognized datasets for anomalous citations' and simulate anomalies instead. Kojaku et al. [2] validate at the journal-group level against JCR suppressions. Our systematic search confirms that no public edge-level ground truth dataset of citation manipulation exists.

  ## Graph Curvature in Network Analysis

  Ricci curvature, originally defined for smooth manifolds, has been discretized for graphs in two main ways. Ollivier-Ricci curvature [4] defines curvature through optimal transport: for an edge (u,v), it measures how much the probability distributions of random walks starting from u and v overlap after one step. Forman-Ricci curvature [5] defines curvature combinatorially based on the graph Laplacian and higher-order simplices, capturing how well-connected an edge is in terms of triangles and clustering.

  Samal et al. [6] performed an empirical comparison of these two curvature notions on complex networks, finding that they are correlated in many real-world networks (average correlation coefficient 0.87). However, they did not explore using their *discrepancy* for anomaly detection. Chatterjee et al. [7] used Forman-Ricci curvature alone to detect anomalies in brain networks, demonstrating that geometric features can reveal structural changes.

  Our work is the first to propose curvature *discrepancy* as a detection feature for citation networks, leveraging the complementary information from both curvatures. The GraphRicciCurvature Python library [8] provides efficient implementations of both curvature measures.

  # Methods

  ## Preliminaries

  Let G = (V, E) be an undirected citation network where V is the set of nodes (papers) and E is the set of edges (citations). For each edge e = (u,v) in E, we compute two curvature values.

  **Ollivier-Ricci Curvature** (ORC): For a node u, let m_u be a probability distribution centered at u (typically, mass (1-alpha) at u and mass alpha/|N(u)| at each neighbor, where alpha in [0,1] and N(u) is the neighborhood of u). The Ollivier-Ricci curvature of edge (u,v) is defined as:

  kappa_ORC(u,v) = 1 - W_1(m_u, m_v) / d(u,v)

  where W_1 is the Wasserstein optimal transport distance (Earth Mover's Distance) between distributions m_u and m_v, and d(u,v) is the graph distance (1 for adjacent nodes). The curvature ranges from -1 to 1, with positive values indicating locally well-connected edges.

  **Forman-Ricci Curvature** (FRC): For an edge e = (u,v) in a weighted graph, the Forman-Ricci curvature is defined as [5]:

  kappa_FRC(e) = w_e(w_u/w_e + w_v/w_e - sum_{x in N(u)\{v}} w_u/sqrt(w_e w_ux) - sum_{y in N(v)\{u}} w_v/sqrt(w_e w_vy))

  For unweighted graphs (w_e = w_u = w_v = 1), this simplifies to:

  kappa_FRC(u,v) = 4 - deg(u) - deg(v)

  This corrected formula replaces an earlier incorrect version (5 - deg(u) - deg(v)) that appeared in preliminary work. The constant 4 arises from the edge contribution (2) plus the vertex contribution (2) in the unweighted case, as derived in Forman (2003).

  ## Curvature Discrepancy Feature

  The key insight of our method is that legitimate citations produce a predictable relationship between Ollivier-Ricci and Forman-Ricci curvature, while manipulated citations create inconsistencies. We define the **curvature discrepancy** for edge e = (u,v) as:

  Delta_kappa(e) = |kappa_ORC(u,v) - kappa_FRC(u,v)|

  Large values of Delta_kappa(e) indicate that the local transport properties (Ollivier-Ricci) and the clustering properties (Forman-Ricci) of an edge are inconsistent—a potential signature of manipulation.

  To normalize for scale differences, we also compute the **z-score normalized discrepancy**:

  z_Delta_kappa(e) = (Delta_kappa(e) - mu_Delta_kappa) / sigma_Delta_kappa

  where mu_Delta_kappa and sigma_Delta_kappa are the mean and standard deviation of Delta_kappa across all edges in the network.

  ## Detection Algorithm

  Our detection algorithm proceeds in four steps:

  1. **Graph Construction**: Convert the citation dataset to an undirected NetworkX graph. While citations are naturally directed, we follow standard practice in citation network analysis [9] and use undirected edges to capture symmetric citation relationships.

  2. **Curvature Computation**: Compute Ollivier-Ricci curvature and Forman-Ricci curvature for all edges. For Ollivier-Ricci, we use a Jaccard coefficient proxy in this implementation due to optimal transport computational cost, defined as kappa_ORC(u,v) approx |N(u) intersect N(v)| / |N(u) union N(v)|. For Forman-Ricci, we use the corrected formula kappa_FRC(u,v) = 4 - deg(u) - deg(v).

  3. **Discrepancy Calculation**: For each edge, compute Delta_kappa(e) = |kappa_ORC(u,v) - kappa_FRC(u,v)| and z_Delta_kappa(e).

  4. **Anomaly Scoring**: Rank edges by their z_Delta_kappa(e) values. Edges with z_Delta_kappa(e) > tau (where tau is a threshold) are flagged as anomalous. For supervised detection, we train a Random Forest classifier on the feature vector [kappa_ORC(e), kappa_FRC(e), Delta_kappa(e), z_Delta_kappa(e)] for each edge.

  [FIGURE:fig2]

  ## Complexity Analysis

  The computational complexity of our method is:

  - Forman-Ricci curvature: O(E) where E is the number of edges, since it requires only local neighborhood information.
  - Ollivier-Ricci curvature (Jaccard proxy): O(E * d) where d is the average degree, since we compute common neighbors for each edge.

  Thus, the overall complexity is O(E * d), which is efficient for sparse citation networks where d << |V|.

  # Experiments

  ## Datasets

  We use the Cora citation network dataset from PyTorch Geometric's Planetoid repository [9]. Cora contains 2,708 scientific publications (7 classes) with 5,429 edges. For this proof-of-concept implementation, we use a mini dataset of 12 nodes and 56 edges to demonstrate the method and provide interpretability cases.

  ## Anomaly Simulation

  Since ground-truth manipulation labels are not available for these datasets, we follow the ACTION protocol [1] to simulate two types of citation manipulation:

  1. **Citation Cartel**: For selected papers, add citations to papers by their co-authors (simulating coordinated citation rings).
  2. **Self-Citation Ring**: Create circular citation patterns among groups of papers (simulating quid-pro-quo exchanges).

  This creates simulated anomalous edges that serve as ground truth for evaluation. The anomaly ratio is 32% (18 anomalous edges out of 56 total edges in the Cora mini experiment).

  ## Baselines

  We compare our curvature discrepancy method against two unsupervised baselines:

  1. **Local Outlier Factor (LOF)**: Unsupervised anomaly detection using local density deviation.
  2. **Isolation Forest**: Unsupervised anomaly detection using isolation trees.

  These baselines use graph structural features (node degree, common neighbors, Jaccard coefficient) as input features.

  ## Evaluation Metrics

  We use standard binary classification metrics:

  - **AUC-ROC**: Area under the Receiver Operating Characteristic curve.
  - **Precision, Recall, F1-score**: Standard classification metrics.

  We also report **bootstrap confidence intervals** (95% CI) and **k-fold cross-validation** results for statistical validation.

  ## Results

  ### Main Results

  Table 1 shows the main results on the Cora mini dataset. Our curvature discrepancy method achieves an AUC-ROC of 0.755. The 95% bootstrap confidence interval is [0.608, 0.878], indicating moderate performance with high variance due to the small dataset size.

  [FIGURE:fig3]

  The unsupervised baselines perform poorly: LOF achieves AUC-ROC of 0.492 and Isolation Forest achieves 0.486. This suggests that simple unsupervised methods fail to capture the structural patterns of citation manipulation, while curvature discrepancy provides a more informative signal.

  However, we acknowledge that the absolute performance (AUC-ROC 0.755) is modest. This reflects both the difficulty of the task and the simplified Ollivier-Ricci computation (Jaccard proxy rather than optimal transport). Future work with full Ollivier-Ricci computation on larger datasets may achieve higher performance.

  ### Statistical Validation

  We perform k-fold cross-validation (k=5) to assess the stability of our results. The mean CV score is 0.464 (std = 0.159), indicating high variance across folds. This is expected given the small dataset (56 edges) and suggests that larger-scale evaluation is needed.

  The bootstrap confidence interval for AUC-ROC is [0.608, 0.878], which does not include 0.5 (random classifier), providing some evidence that the method performs better than chance.

  ### Interpretability Cases

  A key advantage of our method is interpretability. Table 2 shows examples of edges flagged as anomalous (high curvature discrepancy) and normal (low curvature discrepancy).

  **High-discrepancy edge example**: Edge (1862, 1986) has Ollivier curvature 0.333 and Forman curvature -11.0, producing a discrepancy of 11.33. The relatively high Ollivier curvature suggests moderate local transport (neighborhood overlap), while the low Forman curvature indicates sparse local clustering given the node degrees. This inconsistency signals a potentially anomalous citation.

  **Low-discrepancy edge example**: Edge (2582, 654) has Ollivier curvature 0.167 and Forman curvature -15.0, producing a discrepancy of 15.17. While the absolute discrepancy is high, the *normalized* discrepancy (z_Delta_kappa = 0.200) is low because this level of discrepancy is typical for edges with these degree values in this network. The z-score normalization correctly identifies this as a normal edge.

  These examples illustrate how curvature discrepancy combines information from both curvature measures to identify structurally inconsistent edges.

  [FIGURE:fig4]

  ## Runtime Analysis

  The Ollivier-Ricci computation (using Jaccard proxy) takes 0.015 seconds for the mini dataset (56 edges). Forman-Ricci computation is essentially instantaneous (O(E) complexity). The total runtime for curvature discrepancy computation on this dataset is well under 1 second, demonstrating the method's computational efficiency.

  # Discussion

  ## Interpretation of Results

  The curvature discrepancy method achieves moderate performance (AUC-ROC 0.755) on a small dataset with simulated anomalies. The method outperforms unsupervised baselines (LOF: 0.492, Isolation Forest: 0.486), suggesting that the geometric signal provides value beyond simple graph statistics.

  The success of curvature discrepancy can be understood through the geometric properties of the two curvatures. Ollivier-Ricci curvature (computed via Jaccard proxy) captures the *overlap* between node neighborhoods—how many common neighbors two adjacent nodes share. Forman-Ricci curvature captures the *clustering* around an edge—how many triangles contain that edge, adjusted for node degrees.

  Citation manipulation patterns may disrupt the natural relationship between neighborhood overlap and clustering. For example, a citation cartel creates artificial edges that increase neighborhood overlap (high Jaccard) but may not create triangles (low Forman-Ricci), producing high curvature discrepancy.

  ## Limitations

  Our method and evaluation have several important limitations:

  1. **Synthetic Anomalies**: We evaluate on simulated manipulation patterns rather than real-world ground truth. Our systematic search confirms that no publicly available edge-level ground truth dataset of citation manipulation exists. The ACTION paper [1] also uses simulated anomalies. While we follow the ACTION protocol, simulated anomalies may not capture the full complexity of real manipulation tactics. We position this work as a proof-of-concept rather than a deployable detection system.

  2. **Simplified Ollivier-Ricci Computation**: Due to computational constraints, we use a Jaccard coefficient proxy for Ollivier-Ricci curvature instead of the full optimal transport computation. While the Jaccard coefficient approximates neighborhood overlap (a key component of Ollivier-Ricci), it does not capture the full optimal transport distance. Future work should implement the full Ollivier-Ricci computation using the GraphRicciCurvature library.

  3. **Small Dataset**: The experiments use a mini dataset of 12 nodes and 56 edges. The confidence intervals are wide (95% CI: [0.608, 0.878]) and cross-validation shows high variance (std = 0.159). Larger-scale evaluation on full citation networks (Cora: 2,708 nodes, PubMed: 19,717 nodes) is needed.

  4. **Undirected Graphs**: We convert directed citation networks to undirected graphs for curvature computation. This loses directional information that may be relevant for manipulation detection.

  5. **Technical Contribution Depth**: The method is straightforward—computing two existing curvature measures and taking their absolute difference. We acknowledge that the technical novelty is moderate. The contribution is best positioned as a simple, interpretable baseline that complements more complex methods like ACTION and CurvGAD.

  ## Real-World Validation Pathways

  Given the absence of edge-level ground truth, we propose three pathways for future validation:

  1. **Journal-Level Validation**: Apply curvature discrepancy to the CIDRE journal-citation dataset [2] and validate against journals suspended from JCR. While this is group-level rather than edge-level validation, it provides a real-world proxy.

  2. **Qualitative Case Studies**: Analyze known citation manipulation cases from the literature (e.g., SAGE 60 papers retracted for citation ring [10], CWTS blog cases of journal cartels [11]) and compute curvature discrepancy for edges in these known cases.

  3. **Expert Labeling**: Collaborate with journal editors and research integrity offices to obtain expert-labeled examples of citation manipulation, which could be used to create a ground truth dataset.

  # Conclusion

  We have presented a geometric approach to citation manipulation detection based on curvature discrepancy—the difference between Ollivier-Ricci and Forman-Ricci curvature. The method is simple, interpretable, and computationally efficient. On a Cora mini dataset with simulated anomalies, it achieves AUC-ROC of 0.755 (95% CI: [0.608, 0.878]) and outperforms unsupervised baselines.

  The key insight is that legitimate citations produce a predictable relationship between the two curvature measures, while manipulated citations create inconsistencies that manifest as high curvature discrepancy. We provide interpretability cases showing how the method flags structurally inconsistent edges.

  We honestly assess the limitations of this work: the evaluation uses simulated anomalies (as do other methods in the field), the Ollivier-Ricci computation uses a simplified proxy, and the technical contribution is moderate. Rather than overclaiming, we position this as a proof-of-concept that demonstrates the potential of geometric features for citation manipulation detection.

  Future work should: (1) implement full Ollivier-Ricci computation on larger citation networks, (2) validate on real-world manipulation cases through qualitative case studies, and (3) combine curvature discrepancy with content-based features for more robust detection.

  # Acknowledgments

  We thank the AI Inventor system for facilitating this research. We also thank the authors of the ACTION and CIDRE papers for making their code and data available, and the Retraction Watch team for maintaining the retraction database.

  # References

  [1] Liu, J., Bai, X., Wang, M., Tuarob, S., Xia, F.: Anomalous citations detection in academic networks. Artificial Intelligence Review (2024)

  [2] Kojaku, S., Livan, G., Masuda, N.: Detecting anomalous citation groups in journal networks. Scientific Reports 11, 14524 (2021)

  [3] Grover, K., Gordon, G.J., Faloutsos, C.: CurvGAD: Leveraging Curvature for Enhanced Graph Anomaly Detection. ArXiv preprint arXiv:2502.08605 (2025)

  [4] Ollivier, Y.: Ricci curvature of Markov chains on metric spaces. Journal of Functional Analysis 256(3), 810-864 (2009)

  [5] Forman, R.: Bochner's Method for Cell Complexes and Combinatorial Ricci Curvature. Discrete & Computational Geometry 29(3), 323-374 (2003)

  [6] Samal, A., Sreejith, R.P., Gu, J., Liu, S., Saucan, E., Jost, J.: Comparative analysis of two discretizations of Ricci curvature for complex networks. Scientific Reports 8, 8650 (2018)

  [7] Chatterjee, T., Albert, R., Thapliyal, S., Azarhooshang, N., Dasgupta, B.: Detecting network anomalies using Forman-Ricci curvature and a case study for human brain networks. Scientific Reports 11, 11716 (2021)

  [8] GraphRicciCurvature: A Python library to compute Discrete Ricci curvature. PyPI package version 0.5.3.2 (2024), https://github.com/saibalmars/GraphRicciCurvature

  [9] Yang, Z., Cohen, W.W., Salakhutdinov, R.: Revisiting Semi-Supervised Learning with Graph Embeddings. Proceedings of the 33rd International Conference on Machine Learning (ICML) 48, 40-48 (2016)

  [10] Retraction Watch: SAGE Publications busts 'peer review and citation ring,' 60 papers retracted (2014), https://retractionwatch.com/2014/07/08/sage-publications-busts-peer-review-and-citation-ring-60-papers-retracted/

  [11] CWTS Blog: What do we know about journal citation cartels? (2021), https://www.cwts.nl/blog?article=n-q2w2b4
summary: >-
  This paper presents a geometric approach to citation manipulation detection using curvature discrepancy between Ollivier-Ricci
  and Forman-Ricci curvature. The method achieves AUC-ROC 0.755 (95% CI: [0.608, 0.878]) on a Cora mini dataset with simulated
  anomalies. Key contributions include a corrected Forman-Ricci formula, statistical validation with bootstrap confidence
  intervals, interpretability case studies, and an honest assessment of limitations including the absence of real-world ground
  truth.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Curvature Discrepancy Detection Overview
caption: >-
  Overview of the curvature discrepancy method for citation manipulation detection. (a) Input: citation network with simulated
  anomalous edges (red dashed lines). (b) Curvature computation: Ollivier-Ricci (neighborhood overlap) and Forman-Ricci (clustering-adjusted)
  for each edge. (c) Discrepancy calculation: absolute difference between the two curvature values. (d) Output: edges ranked
  by anomaly score with high-discrepancy edges flagged.
image_gen_detailed_description: >-
  Horizontal flow diagram with 4 panels in a row, labeled (a)-(d). Panel (a): left, shows a small graph with 6 nodes and edges,
  2 red dashed edges labeled 'anomalous'. Panel (b): second from left, shows two side-by-side bar charts: 'Ollivier-Ricci'
  (blue bars, values around 0.1-0.6) and 'Forman-Ricci' (orange bars, values around -15 to -10). Panel (c): second from right,
  shows a scatter plot with x='Ollivier-Ricci', y='Forman-Ricci', points scattered, diagonal line labeled 'expected relationship',
  outliers highlighted in red. Panel (d): right, shows a ranked list of edges with anomaly scores, top 3 in red. Sans-serif
  font, clean white background, no 3D effects.
aspect_ratio: '21:9'
summary: Architecture diagram showing the 4-step curvature discrepancy detection pipeline
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Curvature Computation Examples
caption: >-
  Example edges from the Cora dataset showing Ollivier-Ricci (Jaccard proxy) and Forman-Ricci curvature values. Edge (0,1)
  has Ollivier curvature 0.333 and Forman curvature -16.0, producing high discrepancy (16.33). Edge (2582, 654) has Ollivier
  curvature 0.167 and Forman curvature -15.0, with lower normalized discrepancy (z-score 0.200).
image_gen_detailed_description: >-
  Two side-by-side network subgraph diagrams. Left diagram: 3 nodes {0,1,2} with edges between all three, node labels, edge
  labels showing 'OR=0.333, FR=-16.0, disc=16.33'. Right diagram: 3 nodes {2582,654,332} with edges, edge labels showing 'OR=0.167,
  FR=-15.0, disc=15.17, z=0.200'. Below each diagram: a small table with columns 'Edge', 'OR', 'FR', 'Discrepancy', 'z-score'.
  Values: (0,1): 0.333, -16.0, 16.33, 0.651; (2582,654): 0.167, -15.0, 15.17, 0.200. Sans-serif font, white background.
aspect_ratio: '21:9'
summary: >-
  Concrete examples of curvature computation for high-discrepancy and low-discrepancy edges
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig4
title: Curvature Discrepancy Distribution
caption: >-
  Distribution of curvature discrepancy values for anomalous (simulated manipulation) and normal edges in the Cora mini dataset.
  Anomalous edges tend to have higher discrepancy values, but there is significant overlap. The figure illustrates the challenge
  of setting an optimal threshold for anomaly detection.
image_gen_detailed_description: >-
  Grouped box plot. X-axis: two categories 'Normal edges' and 'Anomalous edges'. Y-axis: 'Curvature Discrepancy' (0 to 20).
  Blue box for 'Normal': median around 15, IQR 13-18. Orange box for 'Anomalous': median around 11, IQR 9-16. Individual data
  points shown as dots with some jitter. Sample sizes: Normal=38, Anomalous=18. Title: 'Curvature Discrepancy Distribution
  by Edge Type'. Sans-serif font, white background.
aspect_ratio: '21:9'
summary: Box plot showing discrepancy distributions for normal vs anomalous edges
figure_path: figures/fig4_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 02:41:44 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-09 02:41:54 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-09 02:41:54 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
