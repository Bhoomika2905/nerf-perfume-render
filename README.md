# NeRF Perfume Bottle Renderer

Trained NeRF model of a perfume bottle with 360° rendering capability.

## 🎬 Results

Successfully trained and rendered 3D NeRF model:
- **Training**: 6,000 iterations on Google Colab T4 GPU
- **Images**: 126 training frames
- **Model Size**: 231.8 MB
- **Rendering**: UIUC Delta A100 cluster

## 📦 Setup Instructions

### Prerequisites
- Python 3.10+
- NVIDIA GPU with 8GB+ VRAM
- CUDA 11.8+

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Bhoomika2905/nerf-perfume-render.git
cd nerf-perfume-render
```

2. Create conda environment:
```bash
conda create -n nerf python=3.10 -y
conda activate nerf
```

3. Install system dependencies:
```bash
conda install -c conda-forge pkg-config ffmpeg av -y
```

4. Install nerfstudio:
```bash
pip install nerfstudio
```

5. Download large files from Google Drive:

**[📥 Download Model & Images](https://drive.google.com/drive/folders/1lxXqUAgKdcNQJ1gbBrqv2hRSrFEbMoXB?usp=sharing)**

Extract and place:
- `step-000005999.ckpt` → `model/2026-04-23_043022/nerfstudio_models/`
- `images.zip` → Extract to `data/images/`

### File Structure
## 🎥 Rendering

### Quick Render (Training Views)
```bash
ns-render interpolate \
    --load-config model/2026-04-23_043022/config.yml \
    --output-path output/perfume.mp4 \
    --pose-source train \
    --interpolation-steps 2
```

### Custom Camera Path
```bash
python render.py
# Choose option 1 for video
```

### Interactive Viewer
```bash
ns-viewer --load-config model/2026-04-23_043022/config.yml
# Open http://localhost:7007 in browser
```

## 🔧 Troubleshooting

### Issue: Path errors in config.yml
Edit `model/2026-04-23_043022/config.yml`:
- Update `data:` path to your local directory
- Update `output_dir:` path to your local directory
- Set `experiment_name: null`

### Issue: Checkpoint not found
Create the expected directory structure:
```bash
mkdir -p model/2026-04-23_043022/data/nerfacto/2026-04-23_043022/nerfstudio_models
cp model/2026-04-23_043022/nerfstudio_models/step-000005999.ckpt \
   model/2026-04-23_043022/data/nerfacto/2026-04-23_043022/nerfstudio_models/
```

### Issue: PyTorch version mismatch
If you get `weights_only` error, edit:
/path/to/nerfstudio/utils/eval_utils.py
Line 62: Add `weights_only=False` to `torch.load()`

## 📊 Training Details

- **Method**: Nerfacto
- **Iterations**: 6,000
- **Rays per batch**: 8,192
- **Training time**: ~2 hours on T4 GPU
- **Features**: Normal prediction enabled
- **COLMAP**: CPU-only processing (114/126 images registered)

## 🚀 Next Steps

- Train on higher resolution images
- Experiment with longer training (10k+ iterations)
- Try different NeRF methods (Instant-NGP, TensoRF)
- Export to mesh for 3D printing

## 📝 License

MIT License - Feel free to use for learning and research!

## 🙏 Acknowledgments

- [Nerfstudio](https://github.com/nerfstudio-project/nerfstudio) for the amazing framework
- UIUC Delta cluster for compute resources
- Google Colab for initial training