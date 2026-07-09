# gen_art_research_2 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_yVP3EQYR2wGM` — Citation Graph Detector
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_2` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-08 23:43:54 UTC

````
Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2/`:
GOOD: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2/file.py`, `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_2_idx2
type: research
title: Survey citation manipulation detection methods and baselines
summary: >-
  Comprehensive literature survey of existing citation manipulation detection methods (ACTION, CIDRE, CurvGAD), their evaluation
  metrics, and simulation approaches for citation cartels to inform experimental design.
runpod_compute_profile: cpu_light
question: >-
  What are the existing methods for citation manipulation detection, how do they work, what metrics do they use, and how do
  researchers typically simulate citation manipulation patterns for evaluation?
research_plan: "## Phase 1: Search and Retrieve Core Baseline Papers (Priority 1)\n\n### Step 1.1: Locate ACTION paper (Liu\
  \ et al. 2024)\n- **Search query**: 'ACTION anomalous citations detection academic networks Liu 2024 non-negative matrix\
  \ factorization'\n- **Search query**: 'ACTION anomalous citation detection actiOn Liu arxiv'\n- **Target**: Find the full\
  \ paper (arXiv or conference version), preferably on arXiv or ACL/WWW proceedings\n- **Extract**: Abstract, method section\
  \ (how NMF and network representation learning are used), evaluation metrics (precision/recall/F1/AUC), dataset details\
  \ (which citation networks used), computational complexity, limitations discussed\n- **Deliverable**: Full understanding\
  \ of ACTION's approach to compare against our curvature discrepancy method\n\n### Step 1.2: Locate CIDRE paper (Kojaku et\
  \ al. 2021)\n- **Search query**: 'CIDRE citation network anomaly detection Kojaku 2021 journal citation exchange'\n- **Search\
  \ query**: 'Kojaku citation anomaly detection group level journals'\n- **Target**: Find on arXiv, PNAS, or journal site\n\
  - **Extract**: How CIDRE operates at group level (not edge level), what features it uses, evaluation approach, datasets,\
  \ metrics\n- **Key distinction to verify**: CIDRE detects anomalous groups of journals, not individual edges — confirm this\
  \ is accurate\n- **Deliverable**: Clear understanding of CIDRE's group-level approach and why edge-level detection is novel\n\
  \n### Step 1.3: Locate CurvGAD paper (Grover et al. 2025)\n- **Search query**: 'CurvGAD curvature graph anomaly detection\
  \ mixed-curvature autoencoder Grover 2025'\n- **Search query**: 'mixed-curvature graph autoencoder anomaly detection 2025'\n\
  - **Target**: arXiv or conference (ICLR/NeurIPS/KDD 2025 submissions)\n- **Extract**: Architecture details (mixed-curvature\
  \ autoencoder), computational requirements, what curvatures are used, evaluation on which datasets, runtime/memory requirements\n\
  - **Key comparison**: Our method computes curvature discrepancy directly (O(N*E)) vs. CurvGAD trains a complex neural network\n\
  - **Deliverable**: Understanding of CurvGAD's complexity to highlight our method's simplicity\n\n## Phase 2: Understand\
  \ Evaluation Metrics and Experimental Protocols (Priority 2)\n\n### Step 2.1: How citation manipulation is evaluated\n-\
  \ **Search query**: 'citation cartel detection evaluation metrics precision recall AUC-ROC'\n- **Search query**: 'simulated\
  \ citation manipulation patterns academic networks evaluation protocol'\n- **Target**: Understand standard evaluation approaches\
  \ in this field\n- **Extract**: \n  - What metrics are standard? (Precision@K, recall@K, F1, AUC-ROC, AUC-PR?)\n  - How\
  \ is ground truth obtained? (Simulated manipulation? Manual labeling?)\n  - What are the standard baseline comparisons?\n\
  \  - Are there standardized datasets or benchmarks?\n- **Deliverable**: Clear evaluation protocol our experiments should\
  \ follow\n\n### Step 2.2: Understand metrics used in ACTION and CIDRE specifically\n- **Fetch and grep ACTION paper**: Extract\
  \ exact table numbers for precision/recall/F1 on Cora/CiteSeer/PubMed\n- **Fetch and grep CIDRE paper**: Extract evaluation\
  \ results, what metrics reported\n- **Key numbers to extract**:\n  - ACTION: Report F1-scores on which datasets? What's\
  \ the SOTA number to beat?\n  - CIDRE: What's the detection accuracy for journal groups?\n  - Both: Runtime numbers if available\n\
  - **Deliverable**: Concrete numbers for our method to beat\n\n## Phase 3: Research Simulation of Citation Manipulation Patterns\
  \ (Priority 3)\n\n### Step 3.1: How are citation cartels simulated?\n- **Search query**: 'simulating citation cartels academic\
  \ networks synthetic manipulation'\n- **Search query**: 'citation network manipulation simulation self-citation ring generation'\n\
  - **Target**: Find papers that simulate citation manipulation for evaluation\n- **Extract**:\n  - Common approaches: Random\
  \ edge injection? Community-based insertion? Pattern-based (cartel as clique with dense internal citations)?\n  - How many\
  \ synthetic anomalies are inserted? (What's the anomaly ratio?)\n  - How to simulate different types: cartels vs. rings\
  \ vs. quid-pro-quo?\n  - Are there existing code repositories for simulation?\n- **Look for**: GitHub repos or code supplements\
  \ that implement simulation\n- **Deliverable**: Concrete simulation protocol we can implement\n\n### Step 3.2: Understand\
  \ characteristics of real citation manipulation\n- **Search query**: 'citation cartel characteristics pattern analysis real\
  \ cases'\n- **Search query**: 'self-citation ring detection characteristics structural patterns'\n- **Target**: Understand\
  \ what real manipulation looks like structurally\n- **Extract**: \n  - What graph structural patterns do cartels create?\
  \ (Dense subgraphs? Bidirectional citation pairs?)\n  - How do they differ from legitimate dense citations (e.g., active\
  \ research areas)?\n  - Are there verified real-world examples to validate against?\n- **Deliverable**: Ensure our simulation\
  \ matches real patterns\n\n## Phase 4: Research Curvature in Graphs (Background for Our Method) (Priority 4)\n\n### Step\
  \ 4.1: Ollivier-Ricci curvature computation in practice\n- **Search query**: 'Ollivier-Ricci curvature graph computation\
  \ algorithm python implementation'\n- **Search query**: 'discrete Ollivier-Ricci curvature sampling approximation graph'\n\
  - **Target**: Understand how to compute it efficiently\n- **Extract**:\n  - Is there an existing Python library? (graph-ricci-curvature\
  \ on PyPI?)\n  - What's the computational complexity of exact computation vs. approximation?\n  - What parameters matter?\
  \ (alpha value for the probability distribution)\n  - Any practical issues? (Numerical stability? Computation time on 20K\
  \ node graphs?)\n- **Deliverable**: Practical implementation guidance for Ollivier-Ricci\n\n### Step 4.2: Forman-Ricci curvature\
  \ computation in practice\n- **Search query**: 'Forman-Ricci curvature graph computation python'\n- **Search query**: 'combinatorial\
  \ Ricci curvature Forman graph implementation'\n- **Target**: Existing implementations and practical considerations\n- **Extract**:\n\
  \  - Is there existing code? (Part of same library as Ollivier-Ricci?)\n  - Complexity: O(N*E) as claimed?\n  - What graph\
  \ properties does it capture exactly?\n- **Deliverable**: Practical implementation guidance for Forman-Ricci\n\n### Step\
  \ 4.3: Verify the Samal et al. 2018 paper claims\n- **Search query**: 'Comparative analysis two discretizations Ricci curvature\
  \ Samal 2018'\n- **Fetch**: The actual Samal et al. paper\n- **Grep**: For mentions of 'discrepancy' or 'anomaly' — verify\
  \ they did NOT propose discrepancy for anomaly detection\n- **Extract**: Their findings on relationship between the two\
  \ curvatures\n- **Deliverable**: Confirm our hypothesis is novel (first to use discrepancy)\n\n## Phase 5: Synthesize and\
  \ Structure Findings (Final Output)\n\n### Step 5.1: Create structured research report with sections:\n1. **Baseline Methods\
  \ Summary**: For each (ACTION, CIDRE, CurvGAD):\n   - Full citation and link to paper\n   - Approach summary (2-3 paragraphs)\n\
  \   - Evaluation metrics and results (exact numbers from papers)\n   - Computational complexity and runtime\n   - Limitations\
  \ and gaps our method addresses\n\n2. **Evaluation Protocol**:\n   - Standard metrics in the field\n   - Recommended evaluation\
  \ approach for our method\n   - Datasets to use (confirm Cora/CiteSeer/PubMed are standard)\n   - How to simulate manipulation\
  \ patterns\n\n3. **Simulation Guidance**:\n   - Step-by-step protocol for simulating cartels, rings, quid-pro-quo\n   -\
  \ Recommended anomaly ratios and insertion strategies\n   - Code/resources available for simulation\n\n4. **Implementation\
  \ Guidance**:\n   - Available libraries for curvature computation\n   - Practical considerations and gotchas\n   - Complexity\
  \ verification\n\n5. **Novelty Verification**:\n   - Confirm curvature discrepancy is not used in existing work\n   - Related\
  \ work that uses single curvature for anomaly detection (Chatterjee et al. 2021)\n\n### Step 5.2: Create research_out.json\
  \ with:\n- **answer**: Comprehensive structured answer to the research question\n- **sources**: All papers found with full\
  \ citations, URLs, and key findings\n- **follow_up_questions**: Questions that emerged and need further investigation\n\n\
  ### Step 5.3: Create research_report.md with:\n- Full synthesis suitable for use in the final paper's related work section\n\
  - Properly formatted with citations\n- Tables comparing baseline methods\n- Clear experimental protocol recommendation\n\
  \n## Execution Notes for Research Executor:\n\n1. **Use parallel tool calls**: Phase 1 searches can all be done in parallel.\
  \ Phase 2/3/4 also have independent searches.\n\n2. **Fetch full papers when possible**: Prefer arXiv PDFs for ability to\
  \ grep exact numbers. Use fetch_grep for methodology details and exact result numbers.\n\n3. **Track all sources**: Every\
  \ claim must have a source. Use Semantic Scholar or direct paper links.\n\n4. **Time management**: \n   - Phase 1 (baseline\
  \ papers): 1 hour\n   - Phase 2 (evaluation metrics): 45 minutes\n   - Phase 3 (simulation approaches): 45 minutes\n   -\
  \ Phase 4 (curvature background): 30 minutes\n   - Phase 5 (synthesis): 30 minutes\n   Total: ~3.5 hours (within 3h budget\
  \ if efficient)\n\n5. **Failure scenarios**:\n   - If ACTION/CIDRE/CurvGAD papers can't be found: Search broader (citation\
  \ anomaly detection, academic network anomaly)\n   - If simulation approaches not clearly documented: Infer from methodology\
  \ sections of papers that evaluate on simulated data\n   - If curvature libraries not found: Note as implementation task,\
  \ search for 'ricci curvature graph python' more broadly\n\n6. **Output format**: \n   - research_out.json: Machine-readable,\
  \ structured for easy parsing by downstream planning\n   - research_report.md: Human-readable, suitable for inclusion in\
  \ paper draft"
explanation: >-
  This research is critical because: (1) We need to understand the exact baseline methods (ACTION, CIDRE, CurvGAD) to ensure
  our comparison is fair and correctly positioned. (2) We need to understand evaluation protocols in this field to ensure
  our experimental design meets community standards. (3) We need to understand how to simulate citation manipulation to create
  ground truth for our experiments. (4) We need to verify the novelty of using curvature discrepancy (confirming Samal et
  al. didn't propose this). Without this research, we risk: comparing against wrong baselines, using wrong metrics, simulating
  unrealistic manipulation patterns, or missing that our idea isn't novel. The research executor has web tools but no code
  execution, so this is the right place to gather this information before the experiment implementation phase.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_yVP3EQYR2wGM/3_invention_loop/iter_1/gen_art/gen_art_research_2/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-08 23:43:54 UTC

```
Propose a simple, novel graph-based method for detecting citation patterns in academic networks and validate it.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-07-08 23:44:00 UTC

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

### [4] SYSTEM-USER prompt · 2026-07-08 23:52:32 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'This research surveyed existing methods for detecting citation manipulation in academic networks, including their evaluation metrics, experimental protocols, and baselines for comparison. It confirms the novelty of using curvature discrepancy for anomaly detection.' is too long (at most 250 characters, got 265)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.sdk_openhands_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
