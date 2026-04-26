#!/bin/bash
# Downloads Unitree Go2 URDF and USD assets from public sources.
set -e

ASSETS_DIR="go2_extreme/assets"
mkdir -p $ASSETS_DIR

echo "Downloading Go2 URDF..."
wget -O $ASSETS_DIR/go2.urdf https://raw.githubusercontent.com/unitreerobotics/unitree_ros/master/robots/go2_description/urdf/go2.urdf

echo "Downloading collision meshes..."
wget -O $ASSETS_DIR/go2_body.dae https://github.com/unitreerobotics/unitree_ros/raw/master/robots/go2_description/meshes/go2_body.dae
# (you would add more .dae for legs if needed)

echo "Convert URDF to USD (using Isaac Sim's usd_from_urdf tool)..."
if command -v usd_from_urdf &> /dev/null; then
    usd_from_urdf --input $ASSETS_DIR/go2.urdf --output $ASSETS_DIR/go2.usd
else
    echo "WARNING: usd_from_urdf not found. Please open Isaac Sim and manually convert or place USD file in $ASSETS_DIR/go2.usd"
fi

echo "Model download finished."