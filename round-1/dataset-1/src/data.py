#!/usr/bin/env python3
"""Convert citation network datasets to experiment-ready format (exp_sel_data_out.json schema)."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def load_dataset(dataset_path: Path):
    """Load a dataset from JSON file."""
    logger.info(f"Loading dataset from {dataset_path}")
    data = json.loads(dataset_path.read_text())
    return data

@logger.catch(reraise=True)
def create_examples_from_graph(dataset: dict):
    """Create examples from a citation network graph.
    
    Each example is a node with:
    - input: JSON string with node ID and its neighborhood (edges)
    - output: the node's class label
    """
    examples = []
    
    # Build adjacency list for quick neighborhood lookup
    adj = {}
    for edge in dataset["edges"]:
        src = edge["source"]
        tgt = edge["target"]
        if src not in adj:
            adj[src] = []
        if tgt not in adj:
            adj[tgt] = []
        adj[src].append(tgt)
        adj[tgt].append(src)  # Undirected
    
    # Create examples for each node
    for node in dataset["nodes"]:
        node_id = node["id"]
        label = node.get("label", "")
        
        # Get neighborhood
        neighbors = adj.get(node_id, [])
        
        # Create input: node information and neighborhood
        input_data = {
            "node_id": node_id,
            "neighbors": neighbors[:10],  # Limit to first 10 neighbors
            "degree": len(neighbors)
        }
        
        example = {
            "input": json.dumps(input_data),
            "output": str(label),
            "metadata_node_id": node_id,
            "metadata_degree": len(neighbors),
            "metadata_task_type": "classification"
        }
        examples.append(example)
    
    return examples

@logger.catch(reraise=True)
def main():
    logger.info("Converting citation networks to experiment-ready format")
    
    # Load all three datasets
    datasets_dir = Path("temp/datasets")
    
    output_datasets = []
    
    for name in ["cora", "citeseer", "pubmed"]:
        full_path = datasets_dir / f"full_{name}.json"
        if not full_path.exists():
            logger.warning(f"Dataset not found: {full_path}")
            continue
        
        # Load dataset
        dataset = load_dataset(full_path)
        
        # Create examples
        examples = create_examples_from_graph(dataset)
        
        # Add to output
        output_datasets.append({
            "dataset": name,
            "examples": examples
        })
        
        logger.info(f"{name}: Created {len(examples)} examples from {dataset['num_nodes']} nodes")
    
    # Create final output
    output = {
        "metadata": {
            "description": "Citation network datasets for graph-based citation pattern detection",
            "source": "PyTorch Geometric Planetoid",
            "num_datasets": len(output_datasets),
            "total_examples": sum(len(d["examples"]) for d in output_datasets)
        },
        "datasets": output_datasets
    }
    
    # Save to full_data_out.json
    output_path = Path("full_data_out.json")
    output_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved experiment-ready data to {output_path}")
    logger.info(f"Total datasets: {len(output_datasets)}")
    logger.info(f"Total examples: {output['metadata']['total_examples']}")
    
    # Create a preview of the first few examples
    if output_datasets:
        preview = {
            "dataset": output_datasets[0]["dataset"],
            "num_examples": len(output_datasets[0]["examples"]),
            "sample_examples": output_datasets[0]["examples"][:3]
        }
        preview_path = Path("preview_examples.json")
        preview_path.write_text(json.dumps(preview, indent=2))
        logger.info(f"Preview saved to {preview_path}")

if __name__ == "__main__":
    main()
