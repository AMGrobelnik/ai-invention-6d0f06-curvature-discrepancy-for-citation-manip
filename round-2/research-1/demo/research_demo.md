# Real-world citation manipulation datasets for validation

## Summary

This research artifact provides a comprehensive investigation of real-world citation manipulation datasets available for validating detection methods. The key finding is that NO publicly available edge-level ground truth dataset of citation manipulation exists. The research systematically searched Retraction Watch database, ACTION and CIDRE papers' datasets, journal cartel case studies, and publisher retraction lists. While the Retraction Watch database contains over 40,000 retraction records and can be filtered for citation manipulation reasons, it provides paper-level not edge-level labels. The ACTION paper uses simulated anomalies, not real-world ground truth. CIDRE provides journal-level validation against JCR suppressions, not edge-level annotation. Several qualitative case studies were identified (SAGE 60 papers, CWTS blog cases) but these lack edge-level labels. The research recommends positioning the curvature discrepancy paper as proof-of-concept with simulation validation, supplemented by qualitative case studies and group-level validation. This honest positioning aligns with field norms where other methods (ACTION, CIDRE) also rely on simulations or proxy validation.

## Research Findings

After conducting a systematic search for real-world citation manipulation datasets and labeled examples, I have found that **no publicly available expert-labeled dataset of citation manipulation cases exists** that can be directly used to validate curvature discrepancy methods at the edge (citation) level [1][5][6].

## Key Findings by Data Source

### 1. Retraction Watch Database (Available, Partial Ground Truth)

The Retraction Watch (RW) database is the most comprehensive source of retracted papers, now hosted by Crossref and updated daily [1][2]. Key findings:

- **Access Methods**: The database is available as (1) a CSV file via GitLab repository [2], and (2) through the Crossref REST API [1].
- **Data Fields**: Includes RetractionDOI, OriginalPaperDOI, Reason, RetractionNature, and other metadata [1].
- **Citation Manipulation Filter**: The 'Reason' field uses a controlled vocabulary that includes 'Concerns/Issues About Referencing/Attributions' and potentially 'Citation manipulation' as categories [3]. However, the Reason field may contain multiple semicolon-separated values, requiring careful parsing.
- **Coverage**: As of 2023, the database contained over 40,000 retraction records [4]. The number of papers retracted specifically for citation manipulation is likely much smaller.
- **Limitation**: Not all retraction notices provide specific paper DOIs that can be easily matched to citation networks. The original paper DOI field may be blank, unavailable, or incorrectly formatted. Most importantly, **retraction is at paper level, not edge (citation) level** - a retracted paper may contain both legitimate and manipulative citations.

### 2. ACTION Paper Datasets (Simulated, Not Real-World Ground Truth)

The ACTION paper (Liu et al. 2024) proposes a method for anomalous citation detection [5]. Key findings:

- **Dataset Construction**: The authors constructed three anomalous citation datasets based on MAG, DBLP, and CiteSeerX [5].
- **Simulation Method**: They manually added non-existent references as anomalous citations and took the original references in the papers as real citations [5]. This is a simulation, not real-world ground truth.
- **Third Dataset**: They created a third dataset motivated by previous research on 'journal cartels,' collecting paper titles reported as causing cartels [5]. However, the paper notes that 'there are no recognized datasets for anomalous citations' and 'no authoritative expert to point out which papers exist anomalous citations' [5].
- **No Public Release**: The paper does not mention releasing these datasets publicly. Contacting authors could potentially yield the simulated data.

### 3. CIDRE Paper Data (Journal-Level, Algorithm Output Not Ground Truth)

The CIDRE paper (Kojaku et al. 2021) detects anomalous citation groups in journal networks [6]. Key findings:

- **GitHub Repository**: The authors provide Python code and data at https://github.com/skojaku/cidre/ [7].
- **Data Files**: The repository contains journal-citation data including edge-table-2013.csv, journal_names.csv, and community-label.csv [8].
- **Validation Method**: CIDRE validates against journals suspended from Journal Citation Reports (JCR) due to anomalous citation behavior [6]. The paper states: 'CIDRE detects more than half of the journals suspended from Journal Citation Reports due to anomalous citation behavior in the year of suspension or in advance' [6].
- **Not Edge-Level Ground Truth**: The validation is at the journal-group level, not the individual edge (citation) level. This is group-level, not edge-level annotation.
- **Data Source**: Uses Microsoft Academic Graph (MAG) snapshot from January 30, 2020, containing 231,926,308 papers across 48,821 journals [6]. Note: MAG was discontinued Dec 31, 2021 [12][13].

### 4. Journal Cartel Case Studies (Specific Examples, Limited Scale)

Several case studies provide specific examples of citation manipulation:

#### 4.1 SAGE Citation Ring (60 Papers with DOIs)
- In 2014, SAGE retracted 60 papers from the Journal of Vibration and Control due to a 'peer review and citation ring' [9].
- The retraction notice lists all 60 papers with their DOIs [9].
- **Limitation**: These are journal-level retractions, not edge-level annotations of which specific citations are manipulative.

#### 4.2 CWTS Blog Cases (4 Journal Pairs with Paper DOIs)
- The CWTS blog post identifies 4 cases of potential citation cartels between journal pairs [10].
- Each case includes specific paper DOIs that exhibit reciprocal citation patterns [10].
- Example: Asia Pacific Journal of Tourism Research and Journal of Travel & Tourism Marketing exchanged heavy citations [10].
- **Limitation**: These are suspicious patterns identified by algorithms, not confirmed manipulation with ground truth labels.

#### 4.3 JCR Suppressed Journals (Clarivate Lists)
- Clarivate suppresses journals from JCR for excessive self-citation and citation stacking [11].
- The Title Suppressions list includes journal pairs with 'Citation Stacking' as the reason [11].
- **Limitation**: Only journal-level suppression, not paper-level or edge-level ground truth.

## Synthesis: Is Real-World Ground Truth Available?

**Answer: No, not in the form needed for edge-level citation manipulation detection validation.**

1. **Retraction Watch Database**: Contains papers retracted for various reasons, but filtering for citation manipulation and matching to citation networks would be challenging and yield a small dataset. Moreover, annotations are at paper level, not edge level.

2. **ACTION Paper**: Uses simulated anomalies, not real-world ground truth [5].

3. **CIDRE Paper**: Provides journal-level validation against JCR suppressions, not edge-level labels [6].

4. **Case Studies**: Provide specific examples but are limited in scale and lack edge-level annotation.

## Recommended Positioning for Paper

Given the lack of real-world ground truth, the paper should be positioned as:

1. **Proof-of-Concept with Simulation Validation**: Follow the ACTION paper's approach of simulating anomalies based on realistic scenarios (collaborator citations, same journal citations, irrelevant content citations) [5].

2. **Qualitative Case Studies**: Include 2-3 real-world cases from literature (SAGE ring, CWTS cases) for interpretability analysis. Show that curvature discrepancy highlights suspicious patterns in these known cases.

3. **Group-Level Validation on CIDRE Data**: Apply curvature discrepancy to journal citation networks and validate against JCR suppressions at the group level.

4. **Limitations Section**: Acknowledge the lack of real-world ground truth and propose future work: 'We plan to collaborate with journal editors and research integrity offices to obtain expert-labeled examples of citation manipulation.'

## Data Availability Matrix

| Source | Available | Format | Access Method | Suitable for Edge-Level Validation |
|--------|-----------|--------|---------------|---------------------------------------------|
| Retraction Watch DB | Yes | CSV/API | GitLab/Crossref API | Partially - needs filtering and matching |
| ACTION Dataset | No (Simulated) | N/A | Not released | No - simulated anomalies |
| CIDRE Data | Yes | CSV | GitHub repo | No - journal-level, not edge-level |
| SAGE 60 Papers | Yes | HTML list | Retraction Watch blog | Partially - retraction list, not edge labels |
| CWTS Cases | Yes | Blog post | CWTS website | No - suspicious patterns, not ground truth |
| JCR Suppressions | Yes | Web page | Clarivate website | No - journal-level suppression |

## Confidence Level

**High confidence** that no public edge-level citation manipulation ground truth dataset exists. The literature consistently notes the difficulty of obtaining annotation data for anomalous citations [5]. All methods papers (ACTION, CIDRE) rely on simulations or proxy validation (JCR suppressions).

**Medium confidence** about the exact number of papers in Retraction Watch that are retracted for citation manipulation specifically. The Reason field uses a controlled vocabulary [3], but manual inspection of the CSV would be needed to count exact cases.

## Contradicting Evidence

One could argue that the CIDRE paper's validation against JCR suppressions constitutes 'real-world ground truth' at the group level [6]. However, this is not edge-level annotation of which specific citations are manipulative, which is what our curvature discrepancy method would need for proper validation.

Similarly, one could argue that retracted papers due to citation manipulation should be considered positive examples. However, retraction is typically at the paper level, not the edge (citation) level. A paper retracted for citation manipulation may contain both legitimate and manipulative citations.

## Conclusion

The systematic search confirms that **real-world edge-level ground truth for citation manipulation does not exist as a public dataset** [1][5][6]. The paper should be positioned as a proof-of-concept with simulation validation, supplemented by qualitative case studies and group-level validation on CIDRE data. This positioning is honest and aligns with how other methods in the field have been evaluated. The research community recognizes this as an open challenge, as evidenced by ACTION authors' note: 'there are no recognized datasets for anomalous citations' [5].

## Sources

[1] [Retraction Watch - Crossref documentation](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/) — Documents access methods for Retraction Watch database via CSV (GitLab) or REST API. Describes data fields including reasons for retraction.

[2] [Retraction Watch Data - Crossref GitLab repository](https://gitlab.com/crossref/retraction-watch-data) — GitLab repository containing the Retraction Watch database as a CSV file, updated daily. Contains over 40,000 retraction records.

[3] [Retraction Watch Database User Guide Appendix B: Reasons](https://retractionwatch.com/retraction-watch-database-user-guide/retraction-watch-database-user-guide-appendix-b-reasons/) — Lists controlled vocabulary for 'Reason' field, including categories related to citation issues like 'Concerns/Issues About Referencing/Attributions'.

[4] [Data from the Retraction Watch database is now more widely accessible](https://www.ouvrirlascience.fr/data-from-the-retraction-watch-database-is-now-more-widely-accessible/) — Announcement that Retraction Watch database (over 40,000 records) is now publicly distributed via Crossref.

[5] [Anomalous citations detection in academic networks (ACTION paper)](https://kops.uni-konstanz.de/entities/publication/94d2c7b0-45bc-4c02-9afc-5325f272f126) — Proposes ACTION method for detecting anomalous citations. Uses simulated datasets constructed from MAG, DBLP, CiteSeerX. Notes lack of recognized datasets for anomalous citations.

[6] [Detecting anomalous citation groups in journal networks (CIDRE paper)](https://www.nature.com/articles/s41598-021-93572-3) — Proposes CIDRE algorithm to detect anomalous journal groups. Validates against JCR suppressed journals. Uses Microsoft Academic Graph data.

[7] [CIDRE GitHub Repository](https://github.com/skojaku/cidre/) — Python implementation of CIDRE algorithm with example data files (journal-citation edge lists, journal names, community labels).

[8] [CIDRE journal-citation data folder](https://github.com/skojaku/cidre/tree/main/data/journal-citation) — Contains edge-table-2013.csv, journal_names.csv, community-label.csv for reproducing CIDRE experiments.

[9] [SAGE Publications busts 'peer review and citation ring,' 60 papers retracted](https://retractionwatch.com/2014/07/08/sage-publications-busts-peer-review-and-citation-ring-60-papers-retracted/) — Documents retraction of 60 papers due to citation ring. Lists all papers with DOIs. Provides specific examples of citation manipulation.

[10] [What do we know about journal citation cartels? A call for information](https://www.cwts.nl/blog?article=n-q2w2b4) — CWTS blog post identifying 4 cases of potential citation cartels between journal pairs. Provides specific paper DOIs exhibiting reciprocal citation patterns.

[11] [Title Suppressions - Journal Citation Reports](https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-Title-Suppressions) — Clarivate's list of journals suppressed from JCR due to excessive self-citation or citation stacking. Provides journal-level validation data.

[12] [Open Academic Graph - Microsoft Research](https://www.microsoft.com/en-us/research/project/open-academic-graph/) — Describes Microsoft Academic Graph (MAG) dataset with 166+ million papers. Notes that MAG was discontinued Dec 31, 2021.

[13] [Microsoft Academic Graph is being discontinued. What's next?](https://www.nature.com/nature-index/news/microsoft-academic-graph-discontinued-whats-next) — Announcement of MAG discontinuation and discussion of alternative academic graph datasets.

## Follow-up Questions

- Can we obtain the ACTION paper's simulated datasets by contacting the authors (Jiaying Liu, Xiaomei Bai, Feng Xia)? The datasets are described in the paper but not released publicly.
- Can we filter the Retraction Watch CSV for 'citation manipulation' reasons and match to Cora/CiteSeer/PubMed? This would require downloading the full CSV, parsing the Reason field, extracting DOIs, and matching to standard datasets.
- Can we use the CIDRE journal citation data and validate at the group level instead of edge level? This would be a different validation approach but could still demonstrate method effectiveness for group-level detection.

---
*Generated by AI Inventor Pipeline*
