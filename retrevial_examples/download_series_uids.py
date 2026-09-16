#!/usr/bin/env python
"""Download embeddings from one model for a list of SeriesInstanceUIDs."""

from __future__ import annotations

from huggingface_hub import snapshot_download

local_dir = 'path/to/local/directory'  # Replace with your desired local directory path
model = 'titan'  # Replace with the desired model name
series_uids = [
    '1.3.6.1.4.1.5962.99.1.856942911.401081431.1727433828671.4.0',
]  # Replace with the desired SeriesInstanceUIDs

snapshot_download(
    repo_id='CBIIT-CGBB/CCDI-MCI',
    repo_type="dataset",
    allow_patterns=[
        *[f"embeddings/{model}/*/{uid}.h5" for uid in series_uids],
        "metadata/slide_manifest.csv",
    ],
    local_dir=local_dir,
)
