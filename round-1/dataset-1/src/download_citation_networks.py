#!/usr/bin/env python3
"""Download and convert Cora, CiteSeer, PubMed citation networks to JSON edge-list format."""

from loguru import logger
from pathlib import Path
import json
import sys
import requests
import tarfile
import zipfile
from io import BytesIO

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def download_file(url: str, output_path: Path):
    """Download a file from URL to output_path."""
    logger.info(f"Downloading {url}")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    output_path.write_bytes(response.content)
    logger.info(f"Saved to {output_path}")

@logger.catch(reraise=True)
def parse_cora_content(content: str):
    """Parse Cora content file (nodes with features and labels)."""
    nodes = {}
    for line in content.strip().split('\n'):
        parts = line.split('\t')
        paper_id = int(parts[0])
        # Features are binary (0/1), last element is label
        label = parts[-1]
        nodes[paper_id] = {"id": paper_id, "label": label}
    return nodes

@logger.catch(reraise=True)
def parse_cites(cites_content: str, nodes: dict):
    """Parse citation file and return edges."""
    edges = []
    for line in cites_content.strip().split('\n'):
        parts = line.split('\t')
        if len(parts) == 2:
            source = int(parts[0])
            target = int(parts[1])
            # Only include edges where both nodes exist
            if source in nodes and target in nodes:
                edges.append({"source": source, "target": target, "metadata": {}})
    return edges

@logger.catch(reraise=True)
def download_cora():
    """Download Cora dataset from LINQS."""
    logger.info("Downloading Cora dataset")
    
    # Try multiple sources
    sources = [
        "https://linqs.github.io/linqs-website/data/cora.tar.gz",
        "https://github.com/kimiyoung/planetoid/raw/master/data/cora.content",
    ]
    
    output_dir = Path("temp/datasets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Download cora.content and cora.cites directly from Planetoid repo
    try:
        # Download content file (nodes)
        content_url = "https://raw.githubusercontent.com/kimiyoung/planetoid/master/data/cora.content"
        content_path = output_dir / "cora_content.txt"
        download_file(content_url, content_path)
        
        # Download cites file (edges)
        cites_url = "https://raw.githubusercontent.com/kimiyoung/planetoid/master/data/cora.cites"
        cites_path = output_dir / "cora_cites.txt"
        download_file(cites_url, cites_path)
        
        # Parse files
        nodes = parse_cora_content(content_path.read_text())
        edges = parse_cites(cites_path.read_text(), nodes)
        
        # Make edges undirected (add reverse edges)
        undirected_edges = []
        edge_set = set()
        for edge in edges:
            key = (min(edge["source"], edge["target"]), max(edge["source"], edge["target"]))
            if key not in edge_set:
                edge_set.add(key)
                undirected_edges.append({"source": key[0], "target": key[1], "metadata": {}})
        
        # Create dataset JSON
        dataset = {
            "dataset_name": "cora",
            "num_nodes": len(nodes),
            "num_edges": len(undirected_edges),
            "nodes": list(nodes.values()),
            "edges": undirected_edges,
            "metadata": {
                "source": "Planetoid GitHub repository",
                "download_date": "2026-07-08",
                "original_format": "content/cites files",
                "notes": "Standard citation network benchmark. Edges made undirected."
            }
        }
        
        # Save full dataset
        full_path = output_dir / "full_cora.json"
        full_path.write_text(json.dumps(dataset, indent=2))
        logger.info(f"Cora: {len(nodes)} nodes, {len(undirected_edges)} edges. Saved to {full_path}")
        
        return dataset
        
    except Exception as e:
        logger.error(f"Failed to download Cora: {e}")
        return None

@logger.catch(reraise=True)
def download_citeseer():
    """Download CiteSeer dataset."""
    logger.info("Downloading CiteSeer dataset")
    
    output_dir = Path("temp/datasets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Download from Planetoid repo
        content_url = "https://raw.githubusercontent.com/kimiyoung/planetoid/master/data/citeseer.content"
        content_path = output_dir / "citeseer_content.txt"
        download_file(content_url, content_path)
        
        cites_url = "https://raw.githubusercontent.com/kimiyoung/planetoid/master/data/citeseer.cites"
        cites_path = output_dir / "citeseer_cites.txt"
        download_file(cites_url, cites_path)
        
        # Parse files
        nodes = parse_cora_content(content_path.read_text())
        edges = parse_cites(cites_path.read_text(), nodes)
        
        # Make edges undirected
        undirected_edges = []
        edge_set = set()
        for edge in edges:
            key = (min(edge["source"], edge["target"]), max(edge["source"], edge["target"]))
            if key not in edge_set:
                edge_set.add(key)
                undirected_edges.append({"source": key[0], "target": key[1], "metadata": {}})
        
        # Create dataset JSON
        dataset = {
            "dataset_name": "citeseer",
            "num_nodes": len(nodes),
            "num_edges": len(undirected_edges),
            "nodes": list(nodes.values()),
            "edges": undirected_edges,
            "metadata": {
                "source": "Planetoid GitHub repository",
                "download_date": "2026-07-08",
                "original_format": "content/cites files",
                "notes": "Standard citation network benchmark. Edges made undirected."
            }
        }
        
        # Save full dataset
        full_path = output_dir / "full_citeseer.json"
        full_path.write_text(json.dumps(dataset, indent=2))
        logger.info(f"CiteSeer: {len(nodes)} nodes, {len(undirected_edges)} edges. Saved to {full_path}")
        
        return dataset
        
    except Exception as e:
        logger.error(f"Failed to download CiteSeer: {e}")
        return None

@logger.catch(reraise=True)
def download_pubmed():
    """Download PubMed dataset."""
    logger.info("Downloading PubMed dataset")
    
    output_dir = Path("temp/datasets")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Download from Planetoid repo
        content_url = "https://raw.githubusercontent.com/kimiyoung/planetoid/master/data/pubmed.content"
        content_path = output_dir / "pubmed_content.txt"
        download_file(content_url, content_path)
        
        cites_url = "https://raw.githubusercontent.com/kimiyoung/planetoid/master/data/pubmed.cites"
        cites_path = output_dir / "pubmed_cites.txt"
        download_file(cites_url, cites_path)
        
        # Parse files
        nodes = parse_cora_content(content_path.read_text())
        edges = parse_cites(cites_path.read_text(), nodes)
        
        # Make edges undirected
        undirected_edges = []
        edge_set = set()
        for edge in edges:
            key = (min(edge["source"], edge["target"]), max(edge["source"], edge["target"]))
            if key not in edge_set:
                edge_set.add(key)
                undirected_edges.append({"source": key[0], "target": key[1], "metadata": {}})
        
        # Create dataset JSON
        dataset = {
            "dataset_name": "pubmed",
            "num_nodes": len(nodes),
            "num_edges": len(undirected_edges),
            "nodes": list(nodes.values()),
            "edges": undirected_edges,
            "metadata": {
                "source": "Planetoid GitHub repository",
                "download_date": "2026-07-08",
                "original_format": "content/cites files",
                "notes": "Standard citation network benchmark. Edges made undirected."
            }
        }
        
        # Save full dataset
        full_path = output_dir / "full_pubmed.json"
        full_path.write_text(json.dumps(dataset, indent=2))
        logger.info(f"PubMed: {len(nodes)} nodes, {len(undirected_edges)} edges. Saved to {full_path}")
        
        return dataset
        
    except Exception as e:
        logger.error(f"Failed to download PubMed: {e}")
        return None

@logger.catch(reraise=True)
def create_mini_preview(dataset: dict, name: str):
    """Create mini and preview versions of dataset."""
    output_dir = Path("temp/datasets")
    
    # Mini version: first 100 nodes and their edges
    node_ids = set(list(dataset["nodes"])[:100]) if len(dataset["nodes"]) > 100 else set(dataset["nodes"])
    node_id_set = {n["id"] for n in node_ids} if isinstance(list(dataset["nodes"])[0], dict) else set(range(100))
    
    # For simplicity, just take first 100 nodes
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
    logger.info("Starting citation network dataset download")
    
    # Download all three datasets
    cora_data = download_cora()
    citeseer_data = download_citeseer()
    pubmed_data = download_pubmed()
    
    # Create mini and preview versions
    if cora_data:
        create_mini_preview(cora_data, "cora")
    
    if citeseer_data:
        create_mini_preview(citeseer_data, "citeseer")
    
    if pubmed_data:
        create_mini_preview(pubmed_data, "pubmed")
    
    # Create summary
    summary = {
        "datasets": [
            {"name": "cora", "status": "success" if cora_data else "failed"},
            {"name": "citeseer", "status": "success" if citeseer_data else "failed"},
            {"name": "pubmed", "status": "success" if pubmed_data else "failed"}
        ]
    }
    
    summary_path = Path("temp/datasets/summary.json")
    summary_path.write_text(json.dumps(summary, indent=2))
    logger.info(f"Download complete. Summary saved to {summary_path}")

if __name__ == "__main__":
    main()
