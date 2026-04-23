#!/usr/bin/env python3
"""
NeRF Perfume Renderer
Renders a trained NeRF model to video or images
"""

import subprocess
import sys
import os
from pathlib import Path

def check_gpu():
    """Check if NVIDIA GPU is available"""
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
        print("✅ GPU detected:")
        print(result.stdout)
        return True
    except FileNotFoundError:
        print("❌ No NVIDIA GPU found!")
        return False

def render_video(config_path, output_path="output/perfume_render.mp4"):
    """Render 360° video of the perfume bottle"""
    
    print("\n" + "="*60)
    print("🎬 Rendering Video")
    print("="*60)
    
    # Create output directory
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        "ns-render", "camera-path",
        "--load-config", str(config_path),
        "--output-path", str(output_path),
        "--rendered-output-names", "rgb"
    ]
    
    print(f"\nCommand: {' '.join(cmd)}\n")
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Video saved to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Rendering failed: {e}")
        return False

def render_images(config_path, output_dir="output/images"):
    """Render individual images from training views"""
    
    print("\n" + "="*60)
    print("🖼️  Rendering Images")
    print("="*60)
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    cmd = [
        "ns-render", "dataset",
        "--load-config", str(config_path),
        "--output-path", str(output_dir),
        "--split", "train"
    ]
    
    print(f"\nCommand: {' '.join(cmd)}\n")
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✅ Images saved to: {output_dir}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Rendering failed: {e}")
        return False

def main():
    """Main rendering script"""
    
    print("="*60)
    print("NeRF Perfume Bottle Renderer")
    print("="*60)
    
    # Check GPU
    if not check_gpu():
        print("\n⚠️  Warning: No GPU detected. Rendering will be very slow.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    # Find config file
    config_path = Path("model/2026-04-23_043022/config.yml")
    
    if not config_path.exists():
        print(f"\n❌ Config file not found at: {config_path}")
        print("Please ensure model files are in the correct location.")
        sys.exit(1)
    
    print(f"\n✅ Found config: {config_path}")
    
    # Ask user what to render
    print("\nWhat would you like to render?")
    print("  1. Video (360° rotation)")
    print("  2. Images (training views)")
    print("  3. Both")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "1":
        render_video(config_path)
    elif choice == "2":
        render_images(config_path)
    elif choice == "3":
        render_video(config_path)
        render_images(config_path)
    else:
        print("Invalid choice!")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("🎉 Rendering Complete!")
    print("="*60)

if __name__ == "__main__":
    main()