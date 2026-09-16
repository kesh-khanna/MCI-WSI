#!/usr/bin/env python
"""Download embeddings from one model for all released patients."""

import argparse
from pathlib import Path

from huggingface_hub import snapshot_download

local_dir = 'path/to/local/directory'  # Replace with your desired local directory path
model = 'titan'  # Replace with the desired model name

snapshot_download(
    repo_id='CBIIT-CGBB/CCDI-MCI',
    repo_type="dataset",
    allow_patterns=[
        f"embeddings/{model}/*/*.h5",
        "metadata/slide_manifest.csv",
    ],
    local_dir=local_dir,
)

