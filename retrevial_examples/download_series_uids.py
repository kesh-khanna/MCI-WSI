#!/usr/bin/env python
"""Download embeddings from one model for a list of SeriesInstanceUIDs."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd
from huggingface_hub import hf_hub_download


local_dir = Path("/path/to/your/local/directory")
model = "titan"  # Choose titan, conch_v15, or uni2h.
series_uids = [
    "1.3.6.1.4.1.5962.99.1.856942911.401081431.1727433828671.4.0",
]
max_workers = 4

manifest_path = hf_hub_download(
    repo_id="CBIIT-CGBB/CCDI-MCI",
    repo_type="dataset",
    filename="metadata/slide_manifest.csv",
    local_dir=local_dir,
)
manifest = pd.read_csv(manifest_path)

selected = manifest.loc[
    manifest["series_instance_uid"].isin(series_uids)
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


print(f"Downloading {len(filenames)} files for {len(series_uids)} series")
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    downloaded_files = list(executor.map(download_file, filenames))

print(f"Downloaded {len(downloaded_files)} files to {local_dir}")
