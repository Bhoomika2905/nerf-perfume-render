# NeRF Perfume Bottle Renderer

Trained NeRF model of a perfume bottle. Renders 3D views and videos.

## ⚠️ Download Large Files First

Due to GitHub file size limits, download the model checkpoint and images separately:

**[📥 Download Large Files from Google Drive](https://drive.google.com/drive/folders/1lxXqUAgKdcNQJ1gbBrqv2hRSrFEbMoXB?usp=sharing)**

### Setup Instructions:

1. Clone this repository:
```bash
git clone https://github.com/Bhoomika2905/nerf-perfume-render.git
cd nerf-perfume-render
```

2. Download and extract the large files from Google Drive (link above)

3. Place files in the correct locations:
   - `step-000005999.ckpt` → `model/2026-04-23_043022/nerfstudio_models/`
   - Extract images to → `data/images/`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the renderer:
```bash
python render.py
```

## Requirements
- NVIDIA GPU with 8GB+ VRAM
- Python 3.8+
- CUDA 11.0+

## Model Info
- **Training steps**: 5,999
- **Images**: 126
- **Model size**: 231.8 MB
- **Trained on**: Google Colab T4 GPU

## Output
- Videos saved to: `output/perfume_render.mp4`
- Images saved to: `output/images/`