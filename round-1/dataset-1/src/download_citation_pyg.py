#!/usr/bin/env python3
"""Download Cora, CiteSeer, PubMed citation networks using PyTorch Geometric."""

from loguru import logger
from pathlib import Path
import json
import sys
import torch
from torch_geometric.datasets import Planetoid
from torch_geometric.transforms import ToUndirected

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def download_dataset(name: str, output_dir: Path):
    """Download a citation network dataset using PyTorch Geometric."""
    logger.info(f"Downloading {name} dataset")
    
    try:
        # Download using Planetoid (PyTorch Geometric)
        dataset = Planetoid(root='/tmp', name=name, transform=ToUndirected())
        data = dataset[0]  # Get the first graph
        
        logger.info(f"{name}: {data.num_nodes} nodes, {data.num_edges} edges, {dataset.num_classes} classes")
        
        # Convert to Python types
        edge_index = data.edge_index.numpy()
        edges = []
        for i in range(edge_index.shape[1]):
            edges.append({
                "source": int(edge_index[0, i]),
                "target": int(edge_index[1, i]),
                "metadata": {}
            })
        
        # Get node labels (y tensor)
        labels = data.y.numpy().tolist() if data.y is not None else []
        
        # Create node list with labels
        nodes = []
        for i in range(data.num_nodes):
            node_data = {"id": i}
            if i < len(labels):
                node_data["label"] = int(labels[i])
            nodes.append(node_data)
        
        # Create dataset JSON
        dataset_json = {
            "dataset_name": name.lower(),
            "num_nodes": int(data.num_nodes),
            "num_edges": int(data.num_edges),
            "nodes": nodes,
            "edges": edges,
            "metadata": {
                "source": "PyTorch Geometric / Planetoid",
                "download_date": "2026-07-08",
                "original_format": "PyTorch Geometric Data object",
                "notes": f"Standard citation network benchmark. {dataset.num_classes} classes.",
                "train_mask": data.train_mask.numpy().tolist() if hasattr(data, 'train_mask') else None,
                "val_mask": data.val_mask.numpy().tolist() if hasattr(data, 'val_mask') else None,
                "test_mask": data.test_mask.numpy().tolist() if hasattr(data, 'test_mask') else None,
            }
        }
        
        # Save full dataset
        full_path = output_dir / f"full_{name.lower()}.json"
        full_path.write_text(json.dumps(dataset_json, indent=2))
        logger.info(f"Saved {name} to {full_path}")
        
        return dataset_json
        
    except Exception as e:
        logger.error(f"Failed to download {name}: {e}")
        return None

@logger.catch(reraise=True)
def create_mini_preview(dataset: dict, name: str, output_dir: Path):
    """Create mini and preview versions of dataset."""
    
    # Mini version: first 100 nodes and edges between them
    mini_nodes = dataset["nodes"][:100] if len(dataset["nodes"]) > 100 else dataset["nodes"]
    mini_node_ids = {n["id"] for n in mini_nodes}
    
    # Get edges between mini nodes
    mini_edges = [e for e in dataset["edges"] if e["source"] in mini_node_ids and e["target"] in mini_node_ids]
    
    mini_dataset = {
        "dataset_name": f"{name}_mini",
        "num_nodes": len(mini_nodes),
        "num_edges": len(mini_edges),
        "nodes": mini_nodes,
        "edges": mini_edges,
        "metadata": dataset["metadata"]
    }
    mini_path = output_dir / f"mini_{name}.json"
    mini_path.write_text(json.dumps(mini_dataset, indent=2))
    logger.info(f"Saved mini {name}: {len(mini_nodes)} nodes, {len(mini_edges)} edges")
    
    # Preview version: first 5 edges
    preview_edges = dataset["edges"][:5]
    preview_node_ids = set()
    for e in preview_edges:
        preview_node_ids.add(e["source"])
        preview_node_ids.add(e["target"])
    preview_nodes = [n for n in dataset["nodes"] if n["id"] in preview_node_ids]
    
    preview_dataset = {
        "dataset_name": f"{name}_preview",
        "num_nodes": len(preview_nodes),
        "num_edges": len(preview_edges),
        "nodes": preview_nodes,
        "edges": preview_edges,
        "metadata": dataset["metadata"]
    }
    preview_path = output_dir / f"preview_{name}.json"
    preview_path.write_text(json.dumps(preview_dataset, indent=2))
    logger.info(f"Saved preview {name}: {len(preview_nodes)} nodes, {len(preview_edges)} edges")

@logger.catch(reraise=True)
def main():
    logger.info("Starting citation network dataset download using PyTorch Geometric")
    
    output_dir = Path("temp/datasets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Download all three datasets
    datasets = {}
    for name in ["Cora", "CiteSeer", "PubMed"]:
        data = download_dataset(name, output_dir)
        if data:
            datasets[name.lower()] = data
            create_mini_preview(data, name.lower(), output_dir)
    
    # Create summary
    summary = {
        "datasets": [
            {
                "name": name,
                "status": "success" if name in datasets else "failed",
                "num_nodes": datasets[name]["num_nodes"] if name in datasets else None,
                "num_edges": datasets[name]["num_edges"] if name in datasets else None,
            }
            for name in ["cora", "citeseer", "pubmed"]
        ]
    }
    
    summary_path = output_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    logger.info(f"Download complete. Summary saved to {summary_path}")
    
    # Verify against published statistics
    logger.info("Verifying against published statistics:")
    published_stats = {
        "cora": {"nodes": 2708, "edges": 5429},
        "citeseer": {"nodes": 3312, "edges": 4715},
        "pubmed": {"nodes": 19717, "edges": 44338}  # PyTorch Geometric version
    }
    
    for name, stats in published_stats.items():
        if name in datasets:
            actual = datasets[name]
            match_nodes = actual["num_nodes"] == stats["nodes"]
            match_edges = actual["num_edges"] == stats["edges"] * 2  # Undirected doubles edge count
            logger.info(f"{name}: nodes={actual['num_nodes']} (expected {stats['nodes']}, match={match_nodes}), "
                       f"edges={actual['num_edges']} (expected {stats['edges']*2} undirected, match={match_edges})")

if __name__ == "__main__":
    main()
