# 🎼 Magenta Music Lab

Welcome to **Magenta Music Lab** — a collection of generative music scripts powered by [Magenta](https://magenta.tensorflow.org/) and MIDI data exploration.

## 🚀 Overview

This project contains Python scripts for:

- 🎹 Generating melodies with Magenta (`surprise_melody.py`)
- 🔄 Interpolating between two melodies (`interpolate_melodies.py`)
- 🎛 Creating groovy basslines (`groovy_bassline.py`)
- 🧪 Experimenting with chord progressions and tempo variations

All scripts are written for **Python 3.10** and tested locally on an M1 Mac using `pyenv`.

## 📁 Files

- `melody_A.mid`, `melody_B.mid` – Seed melodies  
- `variation_1.mid` to `variation_5.mid` – Melody variations  
- `surprise_melody.py` – Generates a random melody  
- `interpolate_melodies.py` – Blends two melodies with intermediate steps  
- `grrovy_bassline.py` – Outputs a funky, humanized bassline  
- `jazzy_118_bassline.mid` – Example groove

## 📦 Requirements

Install the core dependencies via pip (already done in local setup):

```bash
pip install numpy==1.21.6 tensorflow==2.9.1 tensorflow-probability==0.17.0 magenta