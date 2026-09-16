# CCDI-MCI whole-slide image embedding demos

This repository contains simple examples for using the [CCDI-MCI Whole-Slide Image Embeddings](https://huggingface.co/datasets/CBIIT-CGBB/CCDI-MCI) released on our Hugging Face.

The dataset contains embeddings generated from 4,570 whole-slide images in the Childhood Cancer Data Initiative Molecular Characterization Initiative (CCDI-MCI) collection. The initial release includes patch-level CONCH v1.5 [2] and UNI2-h [3] embeddings and slide-level TITAN [4] embeddings. Files are organized by model and patient, with a manifest linking each file to its source imaging series.

These embeddings are intended for research use and have not been validated for clinical diagnosis.

## Demos

+ [`demos/linear_probe_demo.ipynb`](demos/linear_probe_demo.ipynb) downloads TITAN slide embeddings and fits a linear classifier using patient-level train, validation, and test splits.
+ [`demos/abmil_demo.ipynb`](demos/abmil_demo.ipynb) downloads CONCH v1.5 patch embeddings and trains an attention-based multiple-instance learning classifier from [MIL-Lab](https://github.com/mahmoodlab/MIL-Lab) [1] using patient-level patch bags.

Both notebooks demonstrate how to join the released embedding manifest with public clinical labels from the CCDI cBioPortal study and perform a simple downstream analysis.

## Preprint

Preprint citation and link to be added.

## References

1. Shao D, Chen RJ, Song AH, et al. [Do Multiple Instance Learning Models Transfer?](https://proceedings.mlr.press/v267/shao25a.html) *Proceedings of the 42nd International Conference on Machine Learning*. 2025.
2. Lu MY, Chen B, Williamson DFK, et al. [A visual-language foundation model for computational pathology](https://doi.org/10.1038/s41591-024-02856-4). *Nature Medicine*. 2024;30:863–874.
3. Chen RJ, Ding T, Lu MY, et al. [Towards a general-purpose foundation model for computational pathology](https://doi.org/10.1038/s41591-024-02857-3). *Nature Medicine*. 2024;30:850–862.
4. Ding T, Wagner SJ, Song AH, et al. [A multimodal whole-slide foundation model for pathology](https://doi.org/10.1038/s41591-025-03982-3). *Nature Medicine*. 2025;31:3749–3761.
