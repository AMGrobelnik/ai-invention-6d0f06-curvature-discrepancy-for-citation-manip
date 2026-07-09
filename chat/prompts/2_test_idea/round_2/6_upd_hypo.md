# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_yVP3EQYR2wGM` — Citation Graph Detector
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-09 02:03:27 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Testing Curvature Discrepancy for Citation Manipulation Detection
hypothesis: >-
  We hypothesize that citation manipulation patterns create detectable geometric signatures in the discrepancy between Ollivier-Ricci
  and Forman-Ricci curvature, but this remains to be empirically validated. This iteration acquired three citation network
  datasets (Cora, CiteSeer, PubMed) and conducted literature reviews on curvature computation methods and detection baselines.
  The next step is to compute both curvature measures on these datasets, simulate manipulation patterns following the ACTION
  protocol, and evaluate whether curvature discrepancy achieves AUC-ROC >80% with statistical validation (confidence intervals,
  significance testing). A critical requirement is real-world validation beyond synthetic simulations - we must evaluate on
  retracted papers or expert-labeled manipulation cases, not just simulated anomalies. The technical contribution is currently
  thin (computing two curvatures and taking their difference), so we should either: (1) strengthen theoretical foundation
  with mathematical bounds on discrepancy under manipulation models, or (2) position as a proof-of-concept/short paper acknowledging
  moderate novelty. The method's claimed advantages (computational efficiency O(N*E), interpretability) require verification
  through actual experiments and comparison against simple baselines (graph statistics, unsupervised anomaly detection) not
  just complex neural methods. The success criteria are: (1) curvature discrepancy achieves >80% AUC-ROC with statistical
  validation on simulated data, (2) evaluation on at least one real-world manipulation dataset, (3) comparison against 3+
  diverse baselines including simple methods, (4) correction of the Forman-Ricci formula error identified by reviewers, and
  (5) provision of interpretability case studies showing examples of high-discrepancy edges.
motivation: >-
  Citation manipulation undermines the integrity of scientific metrics and evaluation systems. Existing methods for detecting
  anomalous citations rely primarily on network representation learning, community detection, or content analysis - but they
  fail to capture the subtle geometric signatures that manipulation leaves in the network's curvatur e structure. By introducing
  a simple, interpretable geometric feature (curvature discrepancy) that leverages the complementary information from two
  different curvature notions, we can detect manipulation patterns that single-measure methods miss. This approach is also
  computationally efficient (both curvatures can be computed in O(N*E) complexity) and provides a new geometric perspective
  on citation network analysis.
assumptions:
- >-
  Legitimate citations follow a predictable relationship between Ollivier-Ricci and Forman-Ricci curvature that can be characterized
  as a baseline distribution
- >-
  Citation manipulation (cartels, rings, quid-pro-quo exchanges) creates local structural patterns that affect the two curvature
  measures differently, producing detectable discrepancies
- >-
  The curvature discrepancy signal is robust to noise and can be separated from legitimate citation variability
- >-
  Standard citation network datasets (Cora, CiteSeer, PubMed) provide sufficient scale and realism to validate the approach
investigation_approach: >-
  1. Compute Ollivier-Ricci curvature and Forman-Ricci curvature for edges in standard citation network datasets (Cora, CiteSeer,
  PubMed). 2. Calculate curvature discrepancy features (ratio, difference, z-score) for each edge. 3. Simulate citation manipulation
  patterns (create synthetic citation cartels, inject self-citation rings) to generate ground-truth anomalous edges. 4. Train
  a simple classifier (logistic regression or random forest) on curvature discrepancy features to detect anomalous edges.
  5. Compare against baseline methods (ACTION, CIDRE, single-curvature methods) on precision, recall, F1-score. 6. Analyze
  computational efficiency (runtime, memory) compared to baseline methods.
success_criteria: >-
  1. The curvature discrepancy feature achieves >85% AUC-ROC for detecting simulated citation manipulation edges. 2. The method
  outperforms single-curvature baselines (Ollivier-Ricci only, Forman-Ricci only) by >5% in F1-score. 3. The method runs in
  O(N*E) complexity and processes the PubMed dataset (20K nodes, 90K edges) in <10 minutes on standard hardware. 4. The approach
  detects at least 2 types of manipulation patterns (cartels, rings) that baseline methods miss.
related_works:
- >-
  ACTION (Anomalous Citations detecTion In academic networks via actiOn) - Liu et al. 2024: Uses non-negative matrix factorization
  and network representation learning to detect anomalous citations. Our approach differs by using geometric curvature features
  instead of representation learning, providing a more interpretable and computationally efficient solution.
- >-
  CIDRE (Citation network anomaly detection) - Kojaku et al. 2021: Detects anomalous groups of journals exchanging citations.
  Our approach operates at the edge level (not group level) and uses curvature discrepancy as the detection signal.
- >-
  CurvGAD (Curvature-based Graph Anomaly Detection) - Grover et al. 2025: Uses mixed-curvature graph autoencoder for general
  graph anomaly detection. Our approach is simpler (computes curvature discrepancy directly), focuses specifically on citation
  networks, and does not require training a complex neural network.
- >-
  Comparative analysis of two discretizations of Ricci curvature - Samal et al. 2018: Compares Ollivier-Ricci vs Forman-Ricci
  curvature but does NOT use their discrepancy for anomaly detection. Our hypothesis is the first to propose curvature discrepancy
  as a detection feature.
- >-
  Detecting network anomalies using Forman-Ricci curvature - Chatterjee et al. 2021: Uses single (Forman-Ricci) curvature
  for brain network anomaly detection. Our approach uses BOTH curvatures and their discrepancy, capturing complementary information
  that a single curvature misses.
inspiration: >-
  The hypothesis was inspired by the observation that Ollivier-Ricci and Forman-Ricci curvature capture different structural
  properties of networks (Ollivier-Ricci is based on optimal transport and captures local connectivity/citation flow, while
  Forman-Ricci is combinatorial and captures higher-order clustering). In geometric analysis, when two different measures
  of the same underlying phenomenon disagree, this often signals anomaly. This cross-field insight from Riemannian geometry
  (where curvature discrepancy signals geometric transitions) was adapted to citation networks. The approach also draws inspiration
  from anomaly detection in brain networks (where curvature changes signal disease) and from the broad pattern of 'discrepancy
  features' in machine learning (where the difference between two views of data often reveals outliers).
terms:
- term: Ollivier-Ricci curvature
  definition: >-
    A discrete notion of Ricci curvature for graphs based on optimal transport theory. For an edge (u,v), it measures how
    much the probability distributions of random walks starting from u and v overlap after one step, capturing local 'transport'
    properties of the citation flow.
- term: Forman-Ricci curvature
  definition: >-
    A combinatorial notion of Ricci curvature for graphs based on the graph Laplacian and higher-order simplices. It captures
    how well-connected an edge is in terms of the clustering and triangle structure around it.
- term: Curvature discrepancy
  definition: >-
    The difference or ratio between Ollivier-Ricci and Forman-Ricci curvature for an edge. Large discrepancies indicate that
    the local transport properties (Ollivier-Ricci) and the clustering properties (Forman-Ricci) of an edge are inconsistent,
    which can signal anomalous citation patterns.
- term: Citation cartel
  definition: >-
    A group of authors or journals that systematically cite each other's work to inflate citation counts and impact factors,
    creating artificial citation patterns that differ from organic citation practices.
- term: Edge-level anomaly detection
  definition: >-
    The task of identifying individual edges (citations) that are anomalous or manipulated, as opposed to node-level or group-level
    anomaly detection.
summary: >-
  We propose using the discrepancy between Ollivier-Ricci and Forman-Ricci curvature as a simple, interpretable geometric
  feature to detect citation manipulation patterns (cartels, rings) in academic networks. The method is novel (first to use
  curvature discrepancy for citation analysis), feasible (O(N*E) complexity), and captures complementary structural signals
  that single-measure methods miss.
_relation_rationale: >-
  Refining from untested claim to testable hypothesis requiring experimental validation
_confidence_delta: decreased
_key_changes:
- >-
  Added explicit acknowledgment that hypothesis 'remains to be empirically validated' - no experiments run yet
- >-
  Listed concrete achievements this iteration: datasets acquired, literature reviews completed
- >-
  Added requirement for real-world validation (retracted papers, expert-labeled data) addressing major reviewer critique
- >-
  Added statistical validation requirement (confidence intervals, significance testing)
- >-
  Acknowledged technical contribution is 'currently thin' and proposed either theoretical strengthening or positioning as
  proof-of-concept
- >-
  Required comparison against simple baselines (graph statistics, unsupervised methods) not just complex baselines
- Added requirement to correct Forman-Ricci formula error identified by reviewer
- Added requirement for interpretability case studies with concrete examples
- Specified 5 concrete success criteria that address reviewer critiques
- Changed from presenting as confirmed results to presenting as hypotheses to test
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_gMGW9cciJdh3
  label: dataset
- id: art_PMGgEW5qOKy9
  label: curvature_methods
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
in_dependencies:
- id: art_D1NujqDmaxan
  label: baseline_methods
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
</all_artifacts>

<new_artifacts_this_iteration>
These 2 artifacts were created THIS iteration.

id: art_2-Dd5wD0yzlO
type: experiment
in_dependencies:
- id: art_gMGW9cciJdh3
  label: dataset
- id: art_PMGgEW5qOKy9
  label: curvature_methods
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

id: art_dooHUhYsiT-D
type: research
in_dependencies:
- id: art_D1NujqDmaxan
  label: baseline_methods
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) CRITICAL: Cross-validation mean AUC (0.464, std 0.159) is radically inconsistent with the main reported AUC-ROC (0.755). This discrepancy suggests either a bug in the CV implementation, different data/preprocessing between the main result and CV, or that the main result uses a single favorable train-test split while CV reveals the method does not generalize. The paper does not acknowledge or explain this inconsistency. Additionally, only 1 random seed was used for the main result.
  Action: Investigate and fix the CV inconsistency immediately. Report per-fold AUC-ROC values. If the main result used a single split, re-run with multiple random seeds and report mean ± std. If there is a bug in CV, fix it and re-run all experiments. The 0.464 CV mean essentially means the method performs at chance level, which contradicts the paper's main claim. EXPECTED SCORE IMPACT: +3 points (could change overall score from reject to weak accept).
- [MAJOR] (evidence) The evaluation is conducted on an extremely small dataset: 56 edges total (18 anomalous, 38 normal). This is far too small for reliable ML evaluation. The 95% bootstrap CI spans [0.608, 0.878] — a 0.27-width interval indicating high uncertainty. The anomaly ratio (32%) is much higher than the 5-10% standard recommended by the ACTION protocol (per the paper's own literature survey artifact 2), artificially making the detection task easier than real-world scenarios.
  Action: Evaluate on the full Cora dataset (2708 nodes, 5429 edges) as a minimum. The datasets are already available (artifact 3). Use anomaly ratios of 5%, 10%, and 15% following the ACTION protocol. Report results with 95% CIs on the full dataset. EXPECTED SCORE IMPACT: +2 points.
- [MAJOR] (novelty) The technical contribution lacks depth: the method computes two existing curvature measures (Ollivier-Ricci via Jaccard proxy, Forman-Ricci via corrected formula) and takes their absolute difference. There is no theoretical analysis (no bounds on discrepancy under manipulation, no detection guarantees, no formal definition of manipulation in geometric terms). This is below the bar for a full paper at venues like KDD, WWW, or WSDM, which typically require non-trivial algorithmic or theoretical contributions.
  Action: Add theoretical analysis to increase contribution depth. For example: (1) Prove that for a citation cartel (dense bidirectional edges among k papers), the expected curvature discrepancy is bounded below by f(k) for anomalous edges vs. g(d) for legitimate edges where f(k) > g(d) for sufficiently large k. (2) Provide a formal geometric definition of 'manipulation' in terms of curvature properties. Even one theorem with proof would substantially strengthen the paper. EXPECTED SCORE IMPACT: +1-2 points.
- [MAJOR] (methodology) The paper states 'For Ollivier-Ricci, we use a Jaccard coefficient proxy' (Section 3), but the experiment metadata shows or_method='OTDSinkhornMix' and the Ollivier-Ricci computation time is 0.0145 seconds for 56 edges. This is suspiciously fast for optimal transport computation and suggests the Jaccard proxy may have been used as a fallback. The paper should clarify what was actually computed and ensure the text matches the implementation.
  Action: Clarify in both the paper and code what Ollivier-Ricci computation was actually used. If the Jaccard proxy was used (as stated in the paper), ensure the code actually uses it and report this clearly. If the full optimal transport was used, update the paper text to reflect this. The Jaccard proxy limitation should be honestly discussed as a current constraint with plans for full computation in future work. EXPECTED SCORE IMPACT: +0.5 point (clarity/correctness).
- [MINOR] (scope) Baseline comparison is limited to two unsupervised methods (LOF, Isolation Forest). The paper does not compare against simple but competitive graph-based baselines such as common neighbors, Jaccard coefficient, Adamic/Adar index, or edge betweenness centrality. This makes it difficult to determine whether curvature discrepancy provides value beyond simple heuristics.
  Action: Add 3-5 simple graph baseline comparisons: common neighbors, Jaccard coefficient, Adamic/Adar index, and edge betweenness centrality. Use these as features for a Random Forest classifier (same as your method) to provide a fair comparison. This will better establish whether curvature discrepancy captures unique signal. EXPECTED SCORE IMPACT: +0.5 point.
- [MINOR] (rigor) The Forman-Ricci simplification to 4 - deg(u) - deg(v) for unweighted graphs is correct (as verified in the code against Forman 2003), but the paper does not show the derivation steps. Readers unfamiliar with Forman curvature may not understand where the constant 4 comes from.
  Action: Add a brief derivation in Section 3: For unweighted graphs, w_e = w_u = w_v = 1. The general formula has edge contribution 2 and vertex contributions summing to 2 - (deg(u)-1) - (deg(v)-1), giving 2 + 2 - deg(u) + 1 - deg(v) + 1 = 4 - deg(u) - deg(v). Cite Forman (2003) Theorem 2.1. EXPECTED SCORE IMPACT: +0.5 point.
- [MINOR] (clarity) The paper references 'Table 1' (main results) and 'Table 2' (interpretability cases) but these tables are not included in the paper text. While figure placeholders ([FIGURE:fig1] etc.) are permitted per review instructions, table content should be included in the text for readability.
  Action: Include the actual tables in the paper text. Table 1 should show AUC-ROC, Precision, Recall, F1 for curvature discrepancy vs. LOF vs. Isolation Forest with 95% CI. Table 2 should show the interpretability cases (edge, ORC, FRC, discrepancy, z-score, explanation). EXPECTED SCORE IMPACT: +0.5 point.
- [MINOR] (evidence) While the paper honestly acknowledges the lack of real-world edge-level ground truth, it could do more to validate on real data. The proposed pathways (Section 5.2) are not implemented. The CIDRE journal suppression data is publicly available and could be used for group-level validation immediately.
  Action: Implement at least one of the proposed validation pathways. The CIDRE dataset (journal-level citations with JCR suppression labels) is available and can be used to compute curvature discrepancy at the journal level and validate against known suppressions. This would provide real-world evidence beyond simulations. EXPECTED SCORE IMPACT: +1 point.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-09 02:03:27 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```
