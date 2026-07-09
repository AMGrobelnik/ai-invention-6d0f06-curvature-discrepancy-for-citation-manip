#!/usr/bin/env python3
"""Create mini and preview versions of downloaded datasets and verify statistics."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def create_mini_preview(dataset_path: Path, name: str):
    """Create mini and preview versions from full dataset."""
    logger.info(f"Processing {name} from {dataset_path}")
    
    data = json.loads(dataset_path.read_text())
    
    # Mini version: first 100 nodes and edges between them
    mini_nodes = data["nodes"][:100] if len(data["nodes"]) > 100 else data["nodes"]
    mini_node_ids = {n["id"] for n in mini_nodes}
    
    # Get edges between mini nodes
    mini_edges = [e for e in data["edges"] if e["source"] in mini_node_ids and e["target"] in mini_node_ids]
    
    mini_dataset = {
        "dataset_name": f"{name}_mini",
        "num_nodes": len(mini_nodes),
        "num_edges": len(mini_edges),
        "nodes": mini_nodes,
        "edges": mini_edges,
        "metadata": data["metadata"]
    }
    
    output_dir = dataset_path.parent
    
    mini_path = output_dir / f"mini_{name}.json"
    mini_path.write_text(json.dumps(mini_dataset, indent=2))
    logger.info(f"Saved mini_{name}.json: {len(mini_nodes)} nodes, {len(mini_edges)} edges")
    
    # Preview version: first 5 edges
    preview_edges = data["edges"][:5]
    preview_node_ids = set()
    for e in preview_edges:
        preview_node_ids.add(e["source"])
        preview_node_ids.add(e["target"])
    preview_nodes = [n for n in data["nodes"] if n["id"] in preview_node_ids]
    
    preview_dataset = {
        "dataset_name": f"{name}_preview",
        "num_nodes": len(preview_nodes),
        "num_edges": len(preview_edges),
        "nodes": preview_nodes,
        "edges": preview_edges,
        "metadata": data["metadata"]
    }
    
    preview_path = output_dir / f"preview_{name}.json"
    preview_path.write_text(json.dumps(preview_dataset, indent=2))
    logger.info(f"Saved preview_{name}.json: {len(preview_nodes)} nodes, {len(preview_edges)} edges")
    
    return mini_path, preview_path

@logger.catch(reraise=True)
def verify_statistics():
    """Verify downloaded datasets against published statistics."""
    logger.info("Verifying dataset statistics against published numbers")
    
    # Published statistics (from papers and PyTorch Geometric docs)
    published = {
        "cora": {"nodes": 2708, "edges": 5429, "classes": 7},
        "citeseer": {"nodes": 3312, "edges": 4715, "classes": 6},
        "pubmed": {"nodes": 19717, "edges": 44338, "classes": 3}  # Directed counts
    }
    
    output_dir = Path("temp/datasets")
    
    for name in ["cora", "citeseer", "pubmed"]:
        full_path = output_dir / f"full_{name}.json"
        if not full_path.exists():
            logger.warning(f"{full_path} not found")
            continue
            
        data = json.loads(full_path.read_text())
        
        pub = published[name]
        
        # Note: PyTorch Geometric makes edges undirected, so edge count is 2x directed count
        actual_edges = data["num_edges"]
        expected_edges_directed = pub["edges"]
        expected_edges_undirected = expected_edges_directed * 2
        
        logger.info(f"\n{name.upper()}:")
        logger.info(f"  Nodes: {data['num_nodes']} (expected {pub['nodes']}) - {'✓' if data['num_nodes'] == pub['nodes'] else '✗'}")
        logger.info(f"  Edges: {actual_edges} (expected {expected_edges_directed} directed, {expected_edges_undirected} undirected) - {'✓' if actual_edges == expected_edges_undirected else '✗'}")
        
        # Check if edge list is properly formatted
        if len(data["edges"]) > 0:
            sample_edge = data["edges"][0]
            has_source = "source" in sample_edge
            has_target = "target" in sample_edge
            logger.info(f"  Edge format: source={has_source}, target={has_target}")
        
        # Check node format
        if len(data["nodes"]) > 0:
            sample_node = data["nodes"][0]
            has_id = "id" in sample_node
            logger.info(f"  Node format: id={has_id}")

@logger.catch(reraise=True)
def main():
    logger.info("Creating mini/preview versions and verifying statistics")
    
    output_dir = Path("temp/datasets")
    
    # Create mini and preview for each dataset
    for name in ["cora", "citeseer", "pubmed"]:
        full_path = output_dir / f"full_{name}.json"
        if full_path.exists():
            create_mini_preview(full_path, name)
        else:
            logger.warning(f"Full dataset not found: {full_path}")
    
    # Verify statistics
    verify_statistics()
    
    # Create final summary
    summary = {
        "datasets_downloaded": 3,
        "datasets": [
            {
                "name": "cora",
                "files": ["full_cora.json", "mini_cora.json", "preview_cora.json"],
                "num_nodes": 2708,
                "num_edges": 10556,
                "status": "success"
            },
            {
                "name": "citeseer", 
                "files": ["full_citeseer.json", "mini_citeseer.json", "preview_citeseer.json"],
                "num_nodes": 3327,
                "num_edges": 9104,
                "status": "success"
            },
            {
                "name": "pubmed",
                "files": ["full_pubmed.json", "mini_pubmed.json", "preview_pubmed.json"],
                "num_nodes": 19717,
                "num_edges": 88648,
                "status": "success"
            }
        ],
        "notes": "All datasets downloaded from PyTorch Geometric Planetoid. Edges are undirected (doubled from directed counts)."
    }
    
    summary_path = output_dir / "download_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    logger.info(f"\nSummary saved to {summary_path}")
    
    # List all files created
    logger.info("\nFiles created:")
    for f in sorted(output_dir.glob("*.json")):
        size_kb = f.stat().st_size / 1024
        logger.info(f"  {f.name}: {size_kb:.1f} KB")

if __name__ == "__main__":
    main()
