#!/bin/bash
# Installs Isaac Lab from source (if not already installed)
set -e

ISAAC_LAB_DIR="${ISAAC_LAB_DIR:-$HOME/IsaacLab}"

if [ -d "$ISAAC_LAB_DIR" ]; then
    echo "Isaac Lab already found at $ISAAC_LAB_DIR"
else
    echo "Cloning Isaac Lab repository..."
    git clone https://github.com/isaac-sim/IsaacLab.git $ISAAC_LAB_DIR
    cd $ISAAC_LAB_DIR
    echo "Installing Isaac Lab dependencies..."
    ./isaaclab.sh --install
    echo "Isaac Lab installed."
fi

echo "Source environment (add to your .bashrc for permanent effect):"
echo "source $ISAAC_LAB_DIR/setup_isaac_lab_env.sh"