# Data policy

Git stores dataset descriptions and manifests, not bulk datasets.

## Local folders

- `raw/`: immutable source data.
- `processed/`: derived training or evaluation data.
- `external/`: downloaded third-party datasets and model assets.

These folders are ignored except for their placeholders. For every dataset, commit a manifest describing:

- source and license;
- acquisition date;
- checksums or version identifiers;
- expected local path;
- preprocessing command;
- privacy or redistribution constraints;
- projects and experiments that depend on it.

Use Git LFS or object storage only after the storage requirement and sharing policy are explicit.
