# Ricci curvature methods for citation networks

## Summary

Comprehensive research on Ollivier-Ricci and Forman-Ricci curvature computation methods for graphs, with focus on citation network analysis. Covers theoretical foundations from Ollivier (2009) and Forman (2003), the GraphRicciCurvature Python library (PyPI package v0.5.3.2), computational complexity analysis showing Forman-Ricci at O(E) vs Ollivier-Ricci at O(N*E), dataset statistics for Cora/CiteSeer/PubMed, and practical recommendations for efficient computation on networks with thousands of nodes.

## Research Findings

## Research Findings: Ricci Curvature Methods for Citation Network Analysis

### 1. Theoretical Foundations

**Ollivier-Ricci Curvature** was introduced by Yann Ollivier in 2009 as a notion of coarse Ricci curvature for metric measure spaces and Markov chains [1, 2]. The curvature is defined as κ(x,y) = 1 - W₁(mx, my)/d(x,y), where W₁ is the Wasserstein optimal transport distance between probability measures mx and my centered at nodes x and y [2]. This definition captures clustering and network coherence properties through the lens of optimal transport theory [1].

**Forman-Ricci Curvature** was developed by Robin Forman in 2003 based on Bochner-Weitzenböck formula for CW complexes [3]. For graphs, the edge curvature formula is: F(e) = w_e(w_v1/w_e + w_v2/w_e - Σ(w_v1/√(w_e w_ev1) + w_v2/√(w_e w_ev2))), where e connects vertices v1 and v2 with weights w [3, 4]. This approach captures geodesic dispersal and algebraic topological structure, and can be extended to directed networks and hypernetworks [1].

### 2. Python Implementation: GraphRicciCurvature

The primary Python library for computing both curvatures is **GraphRicciCurvature** (PyPI package name: GraphRicciCurvature, v0.5.3.2 as of June 2024) [5, 6]. 

**Installation & Dependencies:**
- Install via: `pip install GraphRicciCurvature` [5]
- Required dependencies: NetworkX >= 2.0, NetworKit >= 6.1 (for shortest path computation), NumPy, POT (Python Optimal Transport), python-louvain [5]
- Note: NetworKit installation can be challenging on some systems; users may need to follow NetworKit's installation instructions [5]

**API Usage:**

```python
import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci
from GraphRicciCurvature.FormanRicci import FormanRicci

# Ollivier-Ricci curvature
orc = OllivierRicci(G, alpha=0.5, method='OTDSinkhornMix', proc=4, verbose='INFO')
orc.compute_ricci_curvature()
# Results stored in orc.G[node0][node1]['ricciCurvature'] (typical range: [-1, 1])

# Forman-Ricci curvature
frc = FormanRicci(G, method='augmented')
frc.compute_ricci_curvature()
# Results stored in frc.G[node0][node1]['formanCurvature'] (unbounded, typically negative)
```

**Key API Parameters:**
- `OllivierRicci`: alpha (0-1, mass distribution parameter, default 0.5), method (OTD/Sinkhorn/OTDSinkhornMix for optimal transport computation), proc (number of processors), nbr_topk (limit neighborhood size for speed) [6]
- `FormanRicci`: method ('1d' for basic, 'augmented' for 2D simplicial complexes) [6]

**Library Features:**
- Ollivier-Ricci curvature computation
- Forman-Ricci curvature computation (1D and augmented 2D versions)
- Ricci flow computation (`compute_ricci_flow()`)
- Ricci community detection (`ricci_community()`) [5, 6]

**Limitations:**
- Forman-Ricci does not support directed graphs (as of v0.5.3.2) [7]
- Memory usage can be high for large graphs due to shortest path caching (configurable via cache_maxsize parameter) [6]
- Only 1 open issue on GitHub (as of research time), related to balanced Forman-Ricci curvature [8]

### 3. Computational Complexity Analysis

**Ollivier-Ricci Curvature:**
- **General complexity**: O(N × E) where N is number of nodes and E is number of edges [9]
- **Per-edge complexity**: Essentially the Wasserstein distance computation complexity based on linear programming [10]
- **Detailed analysis**: O(|E| × d̄² × ε⁻² × log(d̄)) where d̄ is average degree and ε is precision parameter [11]
- **Bottleneck**: Optimal transport problem must be solved for each edge, making it computationally intensive for large networks
- **Approximation methods available**: 
  - Sinkhorn distance (entropic regularization for faster computation) [6]
  - OTDSinkhornMix (adaptive method that uses exact OTD for small neighborhoods and Sinkhorn for large ones) [6]
  - Jaccard curvature as a proxy [1]

**Forman-Ricci Curvature:**
- **General complexity**: O(E) where E is number of edges [9]
- **Per-edge complexity**: O(1) - simple formula evaluation using only local neighborhood information [3, 4]
- **Augmented version**: O(E + F) where F is number of triangular faces - accounts for 2D simplicial complexes [1]
- **Advantage**: Orders of magnitude faster than Ollivier-Ricci for large networks [1, 9]

**Empirical Performance Comparison:**
- Samal et al. (2018) demonstrate that Forman-Ricci curvature is highly correlated with Ollivier-Ricci curvature in many model and real-world networks [1]
- The correlation is even higher when using the augmented Forman-Ricci curvature that accounts for 2D simplicial complexes [1]
- **Practical implication**: Forman-Ricci can be employed in place of Ollivier-Ricci for faster computation in larger real-world networks whenever coarse analysis suffices [1]

### 4. Citation Network Dataset Statistics

**Cora Dataset:**
- Nodes: 2,708 scientific publications
- Edges: 5,429 (directed) or 10,556 (undirected, depending on source) [12]
- Classes: 7
- Features: 1,433-dimensional binary word vectors [12]

**CiteSeer Dataset:**
- Nodes: 3,327 scientific publications  
- Edges: 9,104 [12]
- Classes: 6
- Features: 3,703-dimensional binary word vectors [12]

**PubMed Dataset:**
- Nodes: 19,717 scientific publications on diabetes
- Edges: 44,338 (directed) or 88,648 (undirected) [13, 14]
- Classes: 3
- Features: 500-dimensional TF-IDF weighted word vectors [13, 14]

### 5. Runtime Estimates for Citation Networks

**Karate Club Graph (34 nodes, 78 edges)** - from tutorial:
- Ollivier-Ricci computation: ~0.054 seconds [15]
- Forman-Ricci: Not explicitly timed but implied to be much faster [15]

**PubMed Dataset (19,717 nodes, ~44,338-88,648 edges):**
- **Ollivier-Ricci**: Potentially hours to days without approximation
  - With Sinkhorn approximation and multiprocessing: potentially minutes to hours
  - Bottleneck: O(N×E) complexity with optimal transport [9, 10]
- **Forman-Ricci**: Seconds to minutes
  - O(E) complexity with simple local formula [3, 4, 9]
  - Much more feasible for networks of this scale

**Recommendation for PubMed-scale networks:**
1. Use Forman-Ricci curvature for initial fast analysis
2. If Ollivier-Ricci properties are needed, use method='Sinkhorn' or method='OTDSinkhornMix' for approximation [6]
3. Consider using nbr_topk parameter to limit neighborhood size [6]
4. Use multiprocessing (proc parameter) for Ollivier-Ricci computation [6]

### 6. Synthesis and Practical Recommendations

**For efficient computation on citation networks with thousands of nodes:**

1. **Start with Forman-Ricci curvature** for fast initial analysis (O(E) complexity) [1, 3, 4, 9]

2. **If Ollivier-Ricci is required**, use approximation methods:
   - Set method='Sinkhorn' or method='OTDSinkhornMix' [6]
   - Adjust nbr_topk to limit neighborhood size (trade accuracy for speed) [6]
   - Use multiprocessing with proc parameter [6]

3. **For discrepancy analysis** (comparing Ollivier vs Forman curvature):
   - Compute both curvatures and analyze their difference: diff = OllivierCurvature - FormanCurvature
   - Large discrepancies may indicate specific local structural patterns [1]
   - Consider augmented Forman-Ricci for better correlation [1]
   - Investigate edges with high absolute discrepancy as potential points of interest

4. **Memory considerations:**
   - Adjust cache_maxsize parameter for Ollivier-Ricci computation [6]
   - For very large networks, consider sampling edges or using out-of-core computation

**Confidence Assessment:**
- HIGH confidence in theoretical foundations (sources: original papers [1, 2, 3])
- HIGH confidence in API and usage (sources: official documentation [5, 6])
- MEDIUM-HIGH confidence in complexity analysis (sources: multiple papers [1, 3, 4, 9, 10, 11])
- MEDIUM confidence in runtime estimates for PubMed (based on complexity analysis and small-scale benchmarks [15]; actual performance depends on hardware and implementation details)

**Contradicting Evidence / Alternative Views:**
- While Samal et al. [1] show high correlation between the two curvatures, they explicitly warn against treating Forman-Ricci as a simple "proxy" for Ollivier-Ricci, as they capture different aspects of network behavior
- Some sources report different edge counts for the same datasets (e.g., PubMed: 44,338 vs 88,648 edges), likely due to directed vs undirected representation [13, 14]
- The optimal choice of alpha parameter for Ollivier-Ricci (default 0.5) may vary depending on network properties and research questions

### 7. Follow-up Questions for Further Investigation

1. What is the exact memory requirement for computing Ollivier-Ricci curvature on PubMed-scale networks with the GraphRicciCurvature library, and how does the nbr_topk parameter affect accuracy?

2. How does the discrepancy between Ollivier-Ricci and Forman-Ricci curvature distributions correlate with specific network topology features (e.g., community structure, degree distribution, clustering coefficient)?

3. Are there other Python libraries or implementations (besides GraphRicciCurvature) that offer better performance or different approximation methods for Ollivier-Ricci curvature on large citation networks?

## Sources

[1] [Comparative analysis of two discretizations of Ricci curvature for complex networks](https://www.nature.com/articles/s41598-018-27001-3) — Seminal 2018 paper by Samal et al. comparing Ollivier-Ricci and Forman-Ricci curvature in complex networks. Shows high correlation between the two, supporting use of Forman-Ricci as faster alternative. Provides theoretical background and empirical analysis on model and real-world networks.

[2] [Ricci curvature of Markov chains on metric spaces](https://arxiv.org/abs/math/0701886) — Original 2009 paper by Yann Ollivier defining Ricci curvature for Markov chains on metric spaces. Introduces the Wasserstein distance-based definition of Ollivier-Ricci curvature for graphs.

[3] [Bochner's Method for Cell Complexes and Combinatorial Ricci Curvature](https://link.springer.com/article/10.1007/s00454-002-0743-x) — Original 2003 paper by Robin Forman defining combinatorial Ricci curvature for cell complexes based on Bochner-Weitzenböck formula. Provides theoretical foundation for Forman-Ricci curvature.

[4] [Comparative analysis of two discretizations of Ricci curvature for complex networks (arXiv version)](https://arxiv.org/pdf/1712.07600.pdf) — arXiv version of Samal et al. 2018 paper with full methodological details. Includes precise mathematical definitions of both curvatures and empirical comparison results.

[5] [GraphRicciCurvature PyPI page](https://pypi.org/project/GraphRicciCurvature/) — Official PyPI page for GraphRicciCurvature Python library. Contains installation instructions, dependencies, basic usage examples, and links to documentation and GitHub repository.

[6] [GraphRicciCurvature API Documentation](https://graphriccicurvature.readthedocs.io/en/latest/GraphRicciCurvature.html) — Complete API documentation for GraphRicciCurvature library. Details all parameters for OllivierRicci and FormanRicci classes, including alpha, method, proc, nbr_topk, cache_maxsize, and usage examples.

[7] [GraphRicciCurvature example.py script](https://github.com/saibalmars/GraphRicciCurvature/blob/master/example.py) — Official example script from GitHub repository showing basic usage of both Ollivier-Ricci and Forman-Ricci curvature computation. Notes that Forman-Ricci does not support directed graphs yet.

[8] [GraphRicciCurvature GitHub Issues](https://github.com/saibalmars/GraphRicciCurvature/issues) — GitHub issues page showing 1 open issue (as of research time) related to balanced Forman-Ricci curvature. Indicates low issue count and generally stable library.

[9] [Augmented Forman-Ricci Curvature (AFRC) - Complexity Analysis](https://www.emergentmind.com/topics/augmented-forman-ricci-curvature-afrc) — Discussion of Augmented Forman-Ricci Curvature mentioning that Ollivier-Ricci curvature (ORC) necessitates solving an optimal transport problem per edge with complexity O(deg(x) × deg(y)), contrasting with Forman-Ricci's simpler computation.

[10] [Ollivier-Ricci Curvature-Based Method to Community Detection in Networks](https://www.nature.com/articles/s41598-019-46079-x) — Paper stating that 'The time complexity to compute the ORC for each edge is essentially the Wasserstein distance computation complexity based on linear programming', confirming the computational bottleneck of Ollivier-Ricci curvature.

[11] [Admittance-based Ollivier-Ricci curvature for power grid structural analysis](https://www.sciencedirect.com/science/article/pii/S305074482500026X) — Paper providing detailed computational complexity analysis: O(|E| × d̄² × ε⁻² × log(d̄)) for Ollivier-Ricci curvature computation in graph settings.

[12] [Cora Dataset - Network Repository](https://networkrepository.com/cora.php) — Provides statistics for Cora citation network: 2,708 nodes, 5,429 edges. Describes dataset as citation network where nodes are papers and edges are citations.

[13] [PubMed Dataset: Medical Citation Network | PyG Guide](https://kumo.ai/pyg/datasets/pubmed/) — PyTorch Geometric documentation for PubMed dataset: 19,717 nodes, 88,648 edges (undirected representation), 3 classes, 500 features per node.

[14] [GraphSAGE on the PubMed-Diabetes citation dataset](https://stellargraph.readthedocs.io/en/v1.0.0rc1/demos/calibration/calibration-pubmed-link-prediction.html) — StellarGraph documentation stating PubMed has 19,717 nodes and 44,338 edges (directed representation). Confirms variability in edge count reporting depending on directed vs undirected interpretation.

[15] [Tutorial: GraphRicciCurvature](https://graphriccicurvature.readthedocs.io/en/latest/tutorial.html) — Official tutorial notebook showing computation times: ~0.054 seconds for Ollivier-Ricci curvature on Karate Club graph (34 nodes, 78 edges). Provides working code examples and discusses Ricci flow for community detection.

## Follow-up Questions

- What is the exact memory requirement for computing Ollivier-Ricci curvature on PubMed-scale networks with the GraphRicciCurvature library, and how does the nbr_topk parameter affect accuracy?
- How does the discrepancy between Ollivier-Ricci and Forman-Ricci curvature distributions correlate with specific network topology features (e.g., community structure, degree distribution, clustering coefficient)?
- Are there other Python libraries or implementations (besides GraphRicciCurvature) that offer better performance or different approximation methods for Ollivier-Ricci curvature on large citation networks?

---
*Generated by AI Inventor Pipeline*
