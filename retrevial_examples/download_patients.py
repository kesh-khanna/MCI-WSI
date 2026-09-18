#!/usr/bin/env python
"""Download embeddings from one model for a list of patient IDs."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd
from huggingface_hub import hf_hub_download


local_dir = Path("/path/to/your/local/directory")
model = "conch_v15"  # Choose titan, conch_v15, or uni2h.
patient_ids = ["PANLMU", "PBCMNT"]
max_workers = 4

manifest_path = hf_hub_download(
    repo_id="CBIIT-CGBB/CCDI-MCI",
    repo_type="dataset",
    filename="metadata/slide_manifest.csv",
    local_dir=local_dir,
)
manifest = pd.read_csv(manifest_path)

selected = manifest.loc[
    manifest["patient_id"].isin(patient_ids)
    ["patient_id", "series_instance_uid"],
]

filenames = [
    f"embeddings/{model}/{row.patient_id}/{row.series_instance_uid}.h5"
    for row in selected.itertuples(index=False)
]

def download_file(filename):
    return hf_hub_download(
        repo_id="CBIIT-CGBB/CCDI-MCI",
        repo_type="dataset",
        filename=filename,
        local_dir=local_dir,
    )


print(f"Downloading {len(filenames)} files for {len(patient_ids)} patients")
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    downloaded_files = list(executor.map(download_file, filenames))

print(f"Downloaded {len(downloaded_files)} files to {local_dir}")
