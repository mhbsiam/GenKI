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
