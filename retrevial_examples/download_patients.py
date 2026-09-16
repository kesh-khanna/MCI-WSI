#!/usr/bin/env python
"""Download embeddings from one model for a list of patient IDs."""

from __future__ import annotations

from huggingface_hub import snapshot_download

local_dir = '/path/to/your/local/directory'  # Replace with your desired local directory path
model = 'conch_v15'  # Replace with the desired model name
patient_ids = ['PANLMU', 'PBCMNT']  # Replace with the desired patient IDs

snapshot_download(
    repo_id='CBIIT-CGBB/CCDI-MCI',
    repo_type="dataset",
    allow_patterns=[
        *[f"embeddings/{model}/{patient_id}/*.h5" for patient_id in patient_ids],
        "metadata/slide_manifest.csv",
    ],
    local_dir=local_dir,
)
