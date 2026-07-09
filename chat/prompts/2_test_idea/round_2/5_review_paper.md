# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `run_yVP3EQYR2wGM` — Citation Graph Detector
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 01:47:27 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_PMGgEW5qOKy9
type: research
title: Ricci curvature methods for citation networks
summary: >-
  Comprehensive research on Ollivier-Ricci and Forman-Ricci curvature computation methods for graphs, with focus on citation
  network analysis. Covers theoretical foundations from Ollivier (2009) and Forman (2003), the GraphRicciCurvature Python
  library (PyPI package v0.5.3.2), computational complexity analysis showing Forman-Ricci at O(E) vs Ollivier-Ricci at O(N*E),
  dataset statistics for Cora/CiteSeer/PubMed, and practical recommendations for efficient computation on networks with thousands
  of nodes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_D1NujqDmaxan
type: research
title: Citation manipulation detection methods literature survey
summary: >-
  Comprehensive literature survey of three baseline methods (ACTION, CIDRE, CurvGAD) for citation manipulation detection.
  ACTION uses NMF and network representation learning for edge-level detection (F1=79% on MAG). CIDRE detects anomalous journal
  groups using null model (group-level, not edge-level). CurvGAD uses mixed-curvature autoencoder (complex neural method).
  The survey confirms that using curvature discrepancy (difference between Ollivier-Ricci and Forman-Ricci curvature) for
  anomaly detection is novel - Samal et al. 2018 compare the two curvatures but don't use their discrepancy, Chatterjee et
  al. 2021 use Forman-Ricci alone, and CurvGAD 2025 uses Ollivier-Ricci in a complex autoencoder. The GraphRicciCurvature
  Python library provides implementations of both curvature measures. Evaluation metrics include Precision, Recall, F1, AUC-ROC.
  Standard datasets are Cora, CiteSeer, PubMed. Anomaly simulation should follow ACTION protocol with 5-10% anomaly ratio
  and three types: collaborator, same journal, irrelevant content citations.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_gMGW9cciJdh3
type: dataset
title: Citation networks for graph curvature analysis
summary: >-
  Successfully acquired three standard citation network datasets from PyTorch Geometric's Planetoid repository: Cora (2708
  nodes, 10556 undirected edges, 7 classes), CiteSeer (3327 nodes, 9104 undirected edges, 6 classes), and PubMed (19717 nodes,
  88648 undirected edges, 3 classes). Each dataset was converted from PyTorch Geometric format to edge-list JSON format with
  nodes containing ID and label, and edges containing source, target, and metadata. Created full (complete dataset), mini
  (100 nodes with edges between them), and preview (5 sample edges) versions for each dataset. Additionally, converted all
  three datasets into experiment-ready format (full_data_out.json) following exp_sel_data_out.json schema, with 25752 total
  examples (one per node) containing node neighborhood information as input and node class label as output. All files are
  under 300MB and validated against schema. The datasets are ready for graph curvature computation and citation pattern detection
  experiments.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_2-Dd5wD0yzlO
type: experiment
title: Curvature Discrepancy for Citation Manipulation Detection
summary: >-
  Implemented curvature discrepancy method for citation manipulation detection. The method computes both Ollivier-Ricci and
  Forman-Ricci curvature with a CORRECTED formula (F(e) = 4 - deg(u) - deg(v) for unweighted graphs), then uses the discrepancy
  between them as a feature for anomaly detection. The implementation includes: (1) Corrected Forman-Ricci formula verification
  against GraphRicciCurvature library, (2) Ollivier-Ricci computation with Jaccard proxy fallback, (3) ACTION protocol anomaly
  simulation (citation cartels and self-citation rings), (4) Baseline comparisons (graph statistics, LOF, Isolation Forest),
  (5) Statistical validation with bootstrap confidence intervals, (6) Interpretability case studies, and (7) Publication-ready
  visualizations. The experiment was run on Cora citation network with 12 nodes and 10 edges (mini dataset), achieving AUC-ROC
  of 0.7551 with 95% CI [0.6081, 0.8780]. The method_out.json contains experiment results, statistical validation, baseline
  comparisons, interpretability cases, and figures.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_dooHUhYsiT-D
type: research
title: Real-world citation manipulation datasets for validation
summary: >-
  This research artifact provides a comprehensive investigation of real-world citation manipulation datasets available for
  validating detection methods. The key finding is that NO publicly available edge-level ground truth dataset of citation
  manipulation exists. The research systematically searched Retraction Watch database, ACTION and CIDRE papers' datasets,
  journal cartel case studies, and publisher retraction lists. While the Retraction Watch database contains over 40,000 retraction
  records and can be filtered for citation manipulation reasons, it provides paper-level not edge-level labels. The ACTION
  paper uses simulated anomalies, not real-world ground truth. CIDRE provides journal-level validation against JCR suppressions,
  not edge-level annotation. Several qualitative case studies were identified (SAGE 60 papers, CWTS blog cases) but these
  lack edge-level labels. The research recommends positioning the curvature discrepancy paper as proof-of-concept with simulation
  validation, supplemented by qualitative case studies and group-level validation. This honest positioning aligns with field
  norms where other methods (ACTION, CIDRE) also rely on simulations or proxy validation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</supplementary_materials>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) The experimental evaluation is conducted entirely on simulated anomalies, not real citation manipulation cases. The paper states: 'Since ground-truth manipulation labels are not available for these datasets, we follow the ACTION protocol [1] to simulate three types of citation manipulation.' This is a critical limitation because: (1) Simulated anomalies may not capture the complexity and diversity of real manipulation tactics; (2) The method may be overfitting to the specific simulation protocol (collaborator citations, same journal citations, irrelevant content citations); (3) Without evaluation on real ground truth, it's impossible to validate whether the method works in practice. The authors acknowledge this as a limitation in Section 5 but don't provide a path to address it.
  Action: Evaluate the method on real-world citation manipulation data. Options include: (1) Datasets of retracted papers due to citation manipulation (e.g., papers from journals suspended from JCR); (2) Expert-labeled datasets where domain experts identify suspicious citation patterns; (3) Case studies on specific journals or conferences known to have citation cartel issues. If real data is truly unavailable, position the paper as a proof-of-concept rather than a practical detection method, and significantly temper claims about 'detecting citation manipulation' in the title and abstract.
- [MAJOR] (novelty) While the literature survey claims using curvature discrepancy is novel, the actual technical contribution is thin. The method essentially computes two existing curvature measures and takes their absolute difference. This is a straightforward feature engineering approach that lacks technical depth. The 'theoretical foundation' section (Section 1, third paragraph) provides intuition but no rigorous theorems, proofs, or formal analysis. Compared to accepted papers at top-tier venues (e.g., KDD, WWW, WSDM), which typically involve novel algorithms, theoretical guarantees, or extensive empirical validation, this contribution would likely be considered incremental.
  Action: Strengthen the theoretical contribution by: (1) Proving mathematical bounds on curvature discrepancy under different manipulation models (cartels, rings, quid-pro-quo); (2) Deriving conditions under which discrepancy is guaranteed to be high for anomalous edges; (3) Providing a formal definition of 'manipulation' in geometric terms. Alternatively, position this as a short paper or poster at a venue that values practical contributions alongside moderate novelty, or combine with other complementary detection methods to create a more substantial contribution.
- [MAJOR] (evidence) The results lack statistical validation. The paper reports '87.3% AUC-ROC' and 'outperforms single-curvature baselines by 7.2% in F1-score' but doesn't provide confidence intervals, p-values, or cross-validation results. The evaluation is conducted on three datasets but with a fixed 15% anomaly ratio - the robustness experiment (5% to 20%) is good but insufficient. The datasets (Cora, CiteSeer, PubMed) are standard but small by modern standards. Without statistical validation, it's unclear whether the reported improvements are genuine or due to chance.
  Action: Add statistical validation: (1) Report mean and standard deviation of AUC-ROC/F1 across multiple random seeds for anomaly simulation; (2) Perform significance testing (e.g., paired t-test) to verify that improvements over baselines are statistically significant (p < 0.05); (3) Use larger, more realistic citation networks (e.g., MAG, DBLP, arXiv) if computationally feasible; (4) Perform k-fold cross-validation rather than a single train/test split. Tables should report ± standard deviation alongside mean values.
- [MINOR] (scope) The experimental comparison is incomplete. The method is not compared against simple but strong baselines that could serve as ablations or sanity checks. For example: (1) Simple graph statistics like edge betweenness centrality, Jaccard coefficient of neighborhoods, or Adamic/Adar index might capture anomaly signals; (2) Unsupervised anomaly detection methods (LOF, isolation forest) applied to graph features could provide competitive performance; (3) The paper compares against ACTION and CurvGAD but these are complex methods - comparison to simpler methods would better establish the value of curvature discrepancy.
  Action: Add comparison to stronger and more diverse baselines: (1) Simple graph statistics: edge betweenness, clustering coefficient, Jaccard coefficient, Adamic/Adar index; (2) Unsupervised anomaly detection: LOF, isolation forest, one-class SVM applied to graph features; (3) Recent graph anomaly detection methods beyond just ACTION and CurvGAD (e.g., DOMINANT, DONE, ALARM from the graph anomaly detection literature). This will better establish whether curvature discrepancy provides value beyond simpler approaches.
- [MINOR] (rigor) The Forman-Ricci curvature formula appears to have an error in simplification. The paper states: 'κ_FRC(u,v) = w_e(w_u/w_e + w_v/w_e - Σ_x∈N(u)\{v} w_u/√(w_e w_ux) - Σ_y∈N(v)\{u} w_v/√(w_e w_vy))' and then simplifies to 'κ_FRC(u,v) = 2 - deg(u) - deg(v) + 3 = 4 - deg(u) - deg(v)'. The simplification seems incorrect - for unweighted graphs, Forman-Ricci is typically related to deg(u) + deg(v) - 4 - number of triangles containing the edge, not 4 - deg(u) - deg(v). Additionally, the constant '2 - deg(u) - deg(v) + 3' simplifying to '4 - deg(u) - deg(v)' is arithmetically correct but the origin of the constants 2 and 3 is not explained.
  Action: Verify the Forman-Ricci curvature formula against the original source (Forman, 2003) or the GraphRicciCurvature library implementation. If the formula is wrong, correct it. If the formula is correct but the simplification is wrong or unexplained, fix the simplification and provide a clear derivation or cite a source that derives this simplification. Ensure all mathematical notation is consistent and correct throughout the paper.
- [MINOR] (clarity) The paper claims the method is 'interpretable' but doesn't actually provide interpretation of results. The discussion section explains WHY discrepancy might signal manipulation but doesn't show examples of edges flagged as anomalous and explain their curvature values. Interpretability is a claimed advantage over neural methods, but this advantage isn't demonstrated with concrete examples. A reader cannot easily understand what a 'high discrepancy' edge looks like in practice.
  Action: Add a case study or qualitative analysis section: (1) Show examples of edges flagged as anomalous (high discrepancy) and explain their curvature values; (2) Show examples of normal edges (low discrepancy) and explain why; (3) Visualize the local neighborhood structure for high-discrepancy edges to build intuition. Use actual examples from Cora, CiteSeer, or PubMed datasets. This will strengthen the interpretability claim and provide readers with intuition for the method.
- [MINOR] (methodology) The complexity analysis states O(N*E) complexity but the explanation is confusing. The paper says 'with Sinkhorn approximation (method='OTDSinkhornMix'), the per-edge complexity becomes O(d²) where d is the average degree.' This needs clarification - is the overall complexity O(N*E) or O(E*d²)? Also, the comparison to ACTION's complexity O(nd + nld² + rd + rm + n²) is not very informative because the parameters are different. A table comparing actual runtime on the same hardware would be more useful.
  Action: Clarify the complexity analysis: (1) Specify whether O(N*E) is the worst-case or average-case complexity; (2) Account for the Sinkhorn approximation properly in the complexity bound (is it O(E*d²)?); (3) Provide a table comparing actual runtime (not just asymptotic complexity) of your method vs. baselines on the same hardware. The current Table 2 is a good start but needs more detail (e.g., same machine, same implementations, hyperparameter tuning accounted for).
- [MINOR] (evidence) The artifact references ([ARTIFACT:art_PMGgEW5qOKy9] etc.) are mentioned in the paper but the actual artifacts are not provided in a readily accessible form. The reviewer cannot easily verify the code, data, or results. While the supplementary materials section describes the artifacts, they should be packaged properly for easy verification. Additionally, the paper references figures (Figure 1, etc.) that are not actually included - only placeholders exist.
  Action: Package all code and data into a reproducible repository: (1) Create a GitHub repository with clear README, installation instructions, and scripts to reproduce all results; (2) Include the exact version of datasets used; (3) Provide pretrained models if any; (4) Use a platform like OpenReview or arXiv to host the code alongside the paper. Ensure the artifact URLs work correctly. Generate actual figures rather than placeholders.
</previous_review>

<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 01:47:27 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SYSTEM-USER prompt · 2026-07-09 02:00:01 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_response]: Let me check the experiment results to verify the paper's claims about AUC-ROC and cross-validation.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cat /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/mini_method_out.json | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps({k:v for k,v in d.items() if k in ['auc_roc', 'cv_mean', 'cv_std', 'bootst
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "{}"}], "is_error": false, "command": "cat /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/mini_method_out.json | python3 -c \"import json,sys; d=json.load(sys.stdin);
  - [agent_think]: Let me try to check the actual experiment output files to verify the claims made in the paper. The mini_method_out.json might have a different structure. Let me look at the file directly.
  - [agent_response]: Let me check the actual experiment output file to verify the claims.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "head -200 /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/mini_method_out.json 2>/dev/null | python3 -c \"import sys; print(sys.stdin.read()[:3000])\"",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "{\n  \"metadata\": {\n    \"method_name\": \"CurvatureDiscrepancyDetector\",\n    \"description\": \"Curvature discrepancy method for citation manipulation detection\",\n    \"parameters\": {\n      \"alpha\": 0.5,\
  - [agent_think]: The reviewer has verified the experimental results from the supplementary materials. Let me now update my review with this more accurate information.

Key findings from checking the experiment output:
1. The main AUC-ROC is 0.755 (confirmed)
2. The cross-validation mean is 0.464 (confirmed, `"cv_sco
  - [agent_response]: Let me check the actual method implementation to verify the paper's claims about using a Jaccard proxy vs. optimal transport.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "grep -n \"Jaccard\\|OLLIVIER\\|or_method\\|OTD\\|Sinkhorn\\|proxy\" /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py 2>/dev/null | head -40",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "53:logger.info(\"Using fallback curvature implementations (Jaccard-based Ollivier-Ricci proxy)\")\n86:        or_method: str = 'OTDSinkhornMix',\n99:        or_method : str\n100:            Method for optimal transp
  - [agent_think]: Let me analyze what I've found from the experiment output and method code:

1. The experiment uses `or_method='OTDSinkhornMix'` which is the actual optimal transport method, but the method.py has a fallback to Jaccard proxy if GraphRicciCurvature is not available. The paper says "For Ollivier-Ricci,
  - [agent_response]: Let me check whether the experiment actually used the Jaccard proxy or the full Ollivier-Ricci computation, and verify the Forman-Ricci formula in the code.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "grep -n \"GraphRicciCurvature\\|ricci\\|RicciCurvature\\|import.*ricci\" /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py 2>/dev/null | head -30",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "12:2. Ollivier-Ricci curvature computation using GraphRicciCurvature\n124:    def compute_forman_ricci_corrected(self, G: nx.Graph) -> Tuple[nx.Graph, Dict]:\n169:        Verify our corrected Forman-Ricci implementa
  - [agent_think]: Now I have a better understanding of the code. Let me check:

1. The experiment output shows `or_method: 'OTDSinkhornMix'` in the parameters, suggesting the full Ollivier-Ricci computation was intended, but also shows a Jaccard proxy fallback.

2. The experiment results show `cv_scores_mean: 0.46376
  - [agent_response]: Let me verify the Forman-Ricci formula implementation and check if the experiment actually used the Jaccard proxy or full Ollivier-Ricci computation.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sed -n '124,200p' /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method.py 2>/dev/null",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "def compute_forman_ricci_corrected(self, G: nx.Graph) -> Tuple[nx.Graph, Dict]:\n        \"\"\"\n        Compute Forman-Ricci curvature with CORRECTED formula.\n\n        The corrected formula for unweighted undirec
  - [agent_think]: Now I have a good understanding of the paper and supplementary materials. Let me consolidate my thoughts:

1. **What the paper claims:**
   - AUC-ROC 0.755 (95% CI: [0.608, 0.878]) on Cora mini dataset
   - Ollivier-Ricci uses Jaccard proxy (per paper Section 3)
   - Cross-validation mean 0.464 (std

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_PMGgEW5qOKy9
type: research
title: Ricci curvature methods for citation networks
summary: >-
  Comprehensive research on Ollivier-Ricci and Forman-Ricci curvature computation methods for graphs, with focus on citation
  network analysis. Covers theoretical foundations from Ollivier (2009) and Forman (2003), the GraphRicciCurvature Python
  library (PyPI package v0.5.3.2), computational complexity analysis showing Forman-Ricci at O(E) vs Ollivier-Ricci at O(N*E),
  dataset statistics for Cora/CiteSeer/PubMed, and practical recommendations for efficient computation on networks with thousands
  of nodes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_D1NujqDmaxan
type: research
title: Citation manipulation detection methods literature survey
summary: >-
  Comprehensive literature survey of three baseline methods (ACTION, CIDRE, CurvGAD) for citation manipulation detection.
  ACTION uses NMF and network representation learning for edge-level detection (F1=79% on MAG). CIDRE detects anomalous journal
  groups using null model (group-level, not edge-level). CurvGAD uses mixed-curvature autoencoder (complex neural method).
  The survey confirms that using curvature discrepancy (difference between Ollivier-Ricci and Forman-Ricci curvature) for
  anomaly detection is novel - Samal et al. 2018 compare the two curvatures but don't use their discrepancy, Chatterjee et
  al. 2021 use Forman-Ricci alone, and CurvGAD 2025 uses Ollivier-Ricci in a complex autoencoder. The GraphRicciCurvature
  Python library provides implementations of both curvature measures. Evaluation metrics include Precision, Recall, F1, AUC-ROC.
  Standard datasets are Cora, CiteSeer, PubMed. Anomaly simulation should follow ACTION protocol with 5-10% anomaly ratio
  and three types: collaborator, same journal, irrelevant content citations.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_gMGW9cciJdh3
type: dataset
title: Citation networks for graph curvature analysis
summary: >-
  Successfully acquired three standard citation network datasets from PyTorch Geometric's Planetoid repository: Cora (2708
  nodes, 10556 undirected edges, 7 classes), CiteSeer (3327 nodes, 9104 undirected edges, 6 classes), and PubMed (19717 nodes,
  88648 undirected edges, 3 classes). Each dataset was converted from PyTorch Geometric format to edge-list JSON format with
  nodes containing ID and label, and edges containing source, target, and metadata. Created full (complete dataset), mini
  (100 nodes with edges between them), and preview (5 sample edges) versions for each dataset. Additionally, converted all
  three datasets into experiment-ready format (full_data_out.json) following exp_sel_data_out.json schema, with 25752 total
  examples (one per node) containing node neighborhood information as input and node class label as output. All files are
  under 300MB and validated against schema. The datasets are ready for graph curvature computation and citation pattern detection
  experiments.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_2-Dd5wD0yzlO
type: experiment
title: Curvature Discrepancy for Citation Manipulation Detection
summary: >-
  Implemented curvature discrepancy method for citation manipulation detection. The method computes both Ollivier-Ricci and
  Forman-Ricci curvature with a CORRECTED formula (F(e) = 4 - deg(u) - deg(v) for unweighted graphs), then uses the discrepancy
  between them as a feature for anomaly detection. The implementation includes: (1) Corrected Forman-Ricci formula verification
  against GraphRicciCurvature library, (2) Ollivier-Ricci computation with Jaccard proxy fallback, (3) ACTION protocol anomaly
  simulation (citation cartels and self-citation rings), (4) Baseline comparisons (graph statistics, LOF, Isolation Forest),
  (5) Statistical validation with bootstrap confidence intervals, (6) Interpretability case studies, and (7) Publication-ready
  visualizations. The experiment was run on Cora citation network with 12 nodes and 10 edges (mini dataset), achieving AUC-ROC
  of 0.7551 with 95% CI [0.6081, 0.8780]. The method_out.json contains experiment results, statistical validation, baseline
  comparisons, interpretability cases, and figures.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_dooHUhYsiT-D
type: research
title: Real-world citation manipulation datasets for validation
summary: >-
  This research artifact provides a comprehensive investigation of real-world citation manipulation datasets available for
  validating detection methods. The key finding is that NO publicly available edge-level ground truth dataset of citation
  manipulation exists. The research systematically searched Retraction Watch database, ACTION and CIDRE papers' datasets,
  journal cartel case studies, and publisher retraction lists. While the Retraction Watch database contains over 40,000 retraction
  records and can be filtered for citation manipulation reasons, it provides paper-level not edge-level labels. The ACTION
  paper uses simulated anomalies, not real-world ground truth. CIDRE provides journal-level validation against JCR suppressions,
  not edge-level annotation. Several qualitative case studies were identified (SAGE 60 papers, CWTS blog cases) but these
  lack edge-level labels. The research recommends positioning the curvature discrepancy paper as proof-of-concept with simulation
  validation, supplemented by qualitative case studies and group-level validation. This honest positioning aligns with field
  norms where other methods (ACTION, CIDRE) also rely on simulations or proxy validation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</supplementary_materials>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (methodology) The experimental evaluation is conducted entirely on simulated anomalies, not real citation manipulation cases. The paper states: 'Since ground-truth manipulation labels are not available for these datasets, we follow the ACTION protocol [1] to simulate three types of citation manipulation.' This is a critical limitation because: (1) Simulated anomalies may not capture the complexity and diversity of real manipulation tactics; (2) The method may be overfitting to the specific simulation protocol (collaborator citations, same journal citations, irrelevant content citations); (3) Without evaluation on real ground truth, it's impossible to validate whether the method works in practice. The authors acknowledge this as a limitation in Section 5 but don't provide a path to address it.
  Action: Evaluate the method on real-world citation manipulation data. Options include: (1) Datasets of retracted papers due to citation manipulation (e.g., papers from journals suspended from JCR); (2) Expert-labeled datasets where domain experts identify suspicious citation patterns; (3) Case studies on specific journals or conferences known to have citation cartel issues. If real data is truly unavailable, position the paper as a proof-of-concept rather than a practical detection method, and significantly temper claims about 'detecting citation manipulation' in the title and abstract.
- [MAJOR] (novelty) While the literature survey claims using curvature discrepancy is novel, the actual technical contribution is thin. The method essentially computes two existing curvature measures and takes their absolute difference. This is a straightforward feature engineering approach that lacks technical depth. The 'theoretical foundation' section (Section 1, third paragraph) provides intuition but no rigorous theorems, proofs, or formal analysis. Compared to accepted papers at top-tier venues (e.g., KDD, WWW, WSDM), which typically involve novel algorithms, theoretical guarantees, or extensive empirical validation, this contribution would likely be considered incremental.
  Action: Strengthen the theoretical contribution by: (1) Proving mathematical bounds on curvature discrepancy under different manipulation models (cartels, rings, quid-pro-quo); (2) Deriving conditions under which discrepancy is guaranteed to be high for anomalous edges; (3) Providing a formal definition of 'manipulation' in geometric terms. Alternatively, position this as a short paper or poster at a venue that values practical contributions alongside moderate novelty, or combine with other complementary detection methods to create a more substantial contribution.
- [MAJOR] (evidence) The results lack statistical validation. The paper reports '87.3% AUC-ROC' and 'outperforms single-curvature baselines by 7.2% in F1-score' but doesn't provide confidence intervals, p-values, or cross-validation results. The evaluation is conducted on three datasets but with a fixed 15% anomaly ratio - the robustness experiment (5% to 20%) is good but insufficient. The datasets (Cora, CiteSeer, PubMed) are standard but small by modern standards. Without statistical validation, it's unclear whether the reported improvements are genuine or due to chance.
  Action: Add statistical validation: (1) Report mean and standard deviation of AUC-ROC/F1 across multiple random seeds for anomaly simulation; (2) Perform significance testing (e.g., paired t-test) to verify that improvements over baselines are statistically significant (p < 0.05); (3) Use larger, more realistic citation networks (e.g., MAG, DBLP, arXiv) if computationally feasible; (4) Perform k-fold cross-validation rather than a single train/test split. Tables should report ± standard deviation alongside mean values.
- [MINOR] (scope) The experimental comparison is incomplete. The method is not compared against simple but strong baselines that could serve as ablations or sanity checks. For example: (1) Simple graph statistics like edge betweenness centrality, Jaccard coefficient of neighborhoods, or Adamic/Adar index might capture anomaly signals; (2) Unsupervised anomaly detection methods (LOF, isolation forest) applied to graph features could provide competitive performance; (3) The paper compares against ACTION and CurvGAD but these are complex methods - comparison to simpler methods would better establish the value of curvature discrepancy.
  Action: Add comparison to stronger and more diverse baselines: (1) Simple graph statistics: edge betweenness, clustering coefficient, Jaccard coefficient, Adamic/Adar index; (2) Unsupervised anomaly detection: LOF, isolation forest, one-class SVM applied to graph features; (3) Recent graph anomaly detection methods beyond just ACTION and CurvGAD (e.g., DOMINANT, DONE, ALARM from the graph anomaly detection literature). This will better establish whether curvature discrepancy provides value beyond simpler approaches.
- [MINOR] (rigor) The Forman-Ricci curvature formula appears to have an error in simplification. The paper states: 'κ_FRC(u,v) = w_e(w_u/w_e + w_v/w_e - Σ_x∈N(u)\{v} w_u/√(w_e w_ux) - Σ_y∈N(v)\{u} w_v/√(w_e w_vy))' and then simplifies to 'κ_FRC(u,v) = 2 - deg(u) - deg(v) + 3 = 4 - deg(u) - deg(v)'. The simplification seems incorrect - for unweighted graphs, Forman-Ricci is typically related to deg(u) + deg(v) - 4 - number of triangles containing the edge, not 4 - deg(u) - deg(v). Additionally, the constant '2 - deg(u) - deg(v) + 3' simplifying to '4 - deg(u) - deg(v)' is arithmetically correct but the origin of the constants 2 and 3 is not explained.
  Action: Verify the Forman-Ricci curvature formula against the original source (Forman, 2003) or the GraphRicciCurvature library implementation. If the formula is wrong, correct it. If the formula is correct but the simplification is wrong or unexplained, fix the simplification and provide a clear derivation or cite a source that derives this simplification. Ensure all mathematical notation is consistent and correct throughout the paper.
- [MINOR] (clarity) The paper claims the method is 'interpretable' but doesn't actually provide interpretation of results. The discussion section explains WHY discrepancy might signal manipulation but doesn't show examples of edges flagged as anomalous and explain their curvature values. Interpretability is a claimed advantage over neural methods, but this advantage isn't demonstrated with concrete examples. A reader cannot easily understand what a 'high discrepancy' edge looks like in practice.
  Action: Add a case study or qualitative analysis section: (1) Show examples of edges flagged as anomalous (high discrepancy) and explain their curvature values; (2) Show examples of normal edges (low discrepancy) and explain why; (3) Visualize the local neighborhood structure for high-discrepancy edges to build intuition. Use actual examples from Cora, CiteSeer, or PubMed datasets. This will strengthen the interpretability claim and provide readers with intuition for the method.
- [MINOR] (methodology) The complexity analysis states O(N*E) complexity but the explanation is confusing. The paper says 'with Sinkhorn approximation (method='OTDSinkhornMix'), the per-edge complexity becomes O(d²) where d is the average degree.' This needs clarification - is the overall complexity O(N*E) or O(E*d²)? Also, the comparison to ACTION's complexity O(nd + nld² + rd + rm + n²) is not very informative because the parameters are different. A table comparing actual runtime on the same hardware would be more useful.
  Action: Clarify the complexity analysis: (1) Specify whether O(N*E) is the worst-case or average-case complexity; (2) Account for the Sinkhorn approximation properly in the complexity bound (is it O(E*d²)?); (3) Provide a table comparing actual runtime (not just asymptotic complexity) of your method vs. baselines on the same hardware. The current Table 2 is a good start but needs more detail (e.g., same machine, same implementations, hyperparameter tuning accounted for).
- [MINOR] (evidence) The artifact references ([ARTIFACT:art_PMGgEW5qOKy9] etc.) are mentioned in the paper but the actual artifacts are not provided in a readily accessible form. The reviewer cannot easily verify the code, data, or results. While the supplementary materials section describes the artifacts, they should be packaged properly for easy verification. Additionally, the paper references figures (Figure 1, etc.) that are not actually included - only placeholders exist.
  Action: Package all code and data into a reproducible repository: (1) Create a GitHub repository with clear README, installation instructions, and scripts to reproduce all results; (2) Include the exact version of datasets used; (3) Provide pretrained models if any; (4) Use a platform like OpenReview or arXiv to host the code alongside the paper. Ensure the artifact URLs work correctly. Generate actual figures rather than placeholders.
</previous_review>

<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`.

Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
````

### [4] SKILL-INPUT — aii-web-tools · 2026-07-09 02:00:42 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
