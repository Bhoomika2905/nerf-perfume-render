# NeRF Perfume Bottle Renderer

Trained NeRF model of a perfume bottle. Renders 3D views and videos.

## Requirements
- NVIDIA GPU with 8GB+ VRAM
- Python 3.8+
- CUDA 11.0+

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/nerf-perfume-render.git
cd nerf-perfume-render

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Render Video
```bash
python render.py
# Select option 1
```

### Render Images
```bash
python render.py
# Select option 2
```

### Interactive Viewer
```bash
ns-viewer --load-config model/2026-04-23_043022/config.yml
```

## Model Info
- **Training steps**: 5,999
- **Images**: 126
- **Model size**: 231.8 MB
- **Trained on**: Google Colab T4 GPU

## Output
- Videos saved to: `output/perfume_render.mp4`
- Images saved to: `output/images/`