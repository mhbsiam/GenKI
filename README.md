# GenKI (Gene Knock-out Inference)
A VGAE (Variational Graph Auto-Encoder) based model to learn perturbation using scRNA-seq data. <br>
<span style="color:red;">New!</span> Data has been added. <br>
[Paper](https://doi.org/10.1093/nar/gkad450)
<br/>
<p align="center">
    <img src="logo.jpg" alt="drawing" width="300"/>
</p>
<br/>

### Install dependencies

Choose the environment file for your platform:

| Platform | File |
|---|---|
| macOS Apple Silicon (M1/M2/M3/M4, arm64) | `genki_macos_arm64.yaml` |
| Linux x86_64 with NVIDIA GPU (CUDA 12.1) | `genki_linux_gpu.yaml` |
| Linux x86_64 or macOS Intel (CPU-only) | `genki_cpu.yaml` |

**macOS Apple Silicon (arm64):**
```shell
conda env create -f genki_macos_arm64.yaml
conda activate genki
python -c "import torch; print(torch.backends.mps.is_available())"
```

**Linux x86_64, NVIDIA GPU (CUDA 12.1):**
```shell
conda env create -f genki_linux_gpu.yaml
conda activate genki
python -c "import torch; print(torch.cuda.is_available())"
```

**Linux x86_64 or macOS Intel, CPU-only:**
```shell
conda env create -f genki_cpu.yaml
conda activate genki
```
<br/>

### Install GenKI with `pip`:
```shell
pip install git+https://github.com/yjgeno/GenKI.git
```
or install it manually from source:
```shell
git clone https://github.com/yjgeno/GenKI.git
cd GenKI
pip install .
```
<br/>

#### Tutorial
Virtual KO experiment:<br> https://github.com/yjgeno/GenKI/blob/master/notebook/Example.ipynb <br>

---

### Changelog

#### 2026-03-13 — Python 3.12 compatibility & environment modernization

**Environment**
- Replaced the single `environment.yml` (Python 3.9.6, PyTorch 1.11) with three platform-specific conda environment files:
  - `genki_macos_arm64.yaml` — macOS Apple Silicon (M1/M2/M3/M4); uses default PyPI wheels which include MPS acceleration. Sets `KMP_DUPLICATE_LIB_OK=TRUE` via `conda env variables` to prevent the PyTorch/OpenMP library conflict on macOS.
  - `genki_linux_gpu.yaml` — Linux x86_64 with NVIDIA GPU; installs PyTorch 2.4+ from the CUDA 12.1 wheel index.
  - `genki_cpu.yaml` — CPU-only for Linux x86_64 or macOS Intel; installs PyTorch 2.4+ from the PyTorch CPU wheel index.
- All environments now use Python 3.12, PyTorch ≥ 2.4, scanpy ≥ 1.12, anndata ≥ 0.10, and numba ≥ 0.61.

**Package (setup.py)**
- Updated all pinned/stale dependency versions to ranges compatible with Python 3.12:
  - `anndata==0.8.0` → `>=0.10`
  - `matplotlib~=3.5.1` → `>=3.8`
  - `pandas~=1.4.2` → `>=2.0`
  - `scanpy==1.9.1` → `>=1.12`
  - `scipy~=1.8.0` → `>=1.12`
  - `statsmodels~=0.13.2` → `>=0.14`
  - `ray>=1.11.0` → `>=2.30`
  - `tqdm~=4.64.0` → `>=4.66`
  - `numpy>=1.21.6` → `>=1.24,<2.4` (numba upper-bound)
- `pip install .` now completes successfully on Python 3.12.
