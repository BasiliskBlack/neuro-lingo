#!/usr/bin/env python3
# NeuroLingo Demo - Visual Glyph Generation

import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from neurolingo import NeuroLingoEngine

def init():
    """Initialize the plot"""
    ax1.clear()
    ax1.axis('off')
    ax2.clear()
    ax2.axis('off')
    return []

def update(frame):
    """Update the animation frame"""
    ax1.clear()
    ax1.axis('off')
    ax2.clear()
    ax2.axis('off')
    
    if frame < 5:
        # Training phase
        loss = engine.train(None)['loss']
        sample = engine.generate("⚡", max_length=8)
        
        ax1.text(0.5, 0.5, 
                f"Training Epoch: {frame + 1}/5\n\n"
                f"Sample Output:\n{sample}\n\n"
                f"Loss: {loss:.4f}",
                ha='center', va='center', 
                fontsize=14, color='cyan',
                fontfamily='monospace')
        
        # Neural network visualization
        weights = np.random.randn(10, 10) * (1 - frame/10)
        ax2.imshow(weights, cmap='viridis', alpha=0.8)
        ax2.set_title("Neural Activity", color='white', pad=20)
        
    else:
        # Generation phase
        samples = [engine.generate("⚡", temperature=0.5 + i*0.2, max_length=10) 
                  for i in range(3)]
        
        ax1.text(0.5, 0.7, "🧠 NeuroLingo Generation", 
                fontsize=24, ha='center', va='center', 
                color='cyan', fontweight='bold')
        
        ax1.text(0.5, 0.5, "\n\n".join([f"• {s}" for s in samples]),
                fontsize=18, ha='center', va='center', 
                fontfamily='monospace', color='white')
        
        ax1.text(0.5, 0.2, "AI-Powered Symbolic Generation",
                fontsize=14, ha='center', va='center', 
                color='white', alpha=0.7)
        
        # Create artistic visualization
        x = np.linspace(0, 10, 100)
        for i, s in enumerate(samples):
            y = np.sin(x + i) + np.random.normal(0, 0.1, len(x))
            ax2.plot(x, y + i*2, linewidth=3, 
                    color=plt.cm.viridis(i/len(samples)),
                    alpha=0.8)
        
        ax2.set_facecolor('#0a0a12')
        ax2.set_title("Neural Pathways Activation", color='white', pad=20)
    
    plt.tight_layout()
    return []

def main():
    """Main function to run the demo"""
    global engine, ax1, ax2
    
    # Set up the plot
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), 
                                  gridspec_kw={'width_ratios': [1, 2]})
    fig.patch.set_facecolor('#0f0f17')

    # Initialize the engine
    engine = NeuroLingoEngine()

    # Create and save the animation
    print("🚀 Creating NeuroLingo visualization...")
    ani = FuncAnimation(fig, update, frames=10, init_func=init, 
                       interval=1500, blit=True, repeat=True)

    # Save as GIF
    output_path = 'neurolingo_demo.gif'
    ani.save(output_path, writer='pillow', fps=1, dpi=100)
    print(f"✅ Done! Check out {output_path}")

    # Keep the plot window open
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

def init():
    """Initialize the plot"""
    ax1.clear()
    ax1.axis('off')
    ax2.clear()
    ax2.axis('off')
    return []

def update(frame):
    """Update the animation frame"""
    ax1.clear()
    ax1.axis('off')
    ax2.clear()
    ax2.axis('off')
    
    if frame < 5:
        # Training phase
        loss = engine.train(None)['loss']
        sample = engine.generate("⚡", max_length=8)
        
        ax1.text(0.5, 0.5, 
                f"Training Epoch: {frame + 1}/5\n\n"
                f"Sample Output:\n{sample}\n\n"
                f"Loss: {loss:.4f}",
                ha='center', va='center', 
                fontsize=14, color='cyan',
                fontfamily='monospace')
        
        # Neural network visualization
        weights = np.random.randn(10, 10) * (1 - frame/10)
        ax2.imshow(weights, cmap='viridis', alpha=0.8)
        ax2.set_title("Neural Activity", color='white', pad=20)
        
    else:
        # Generation phase
        samples = [engine.generate("⚡", temperature=0.5 + i*0.2, max_length=10) 
                  for i in range(3)]
        
        ax1.text(0.5, 0.7, "🧠 NeuroLingo Generation", 
                fontsize=24, ha='center', va='center', 
                color='cyan', fontweight='bold')
        
        ax1.text(0.5, 0.5, "\n\n".join([f"• {s}" for s in samples]),
                fontsize=18, ha='center', va='center', 
                fontfamily='monospace', color='white')
        
        ax1.text(0.5, 0.2, "AI-Powered Symbolic Generation",
                fontsize=14, ha='center', va='center', 
                color='white', alpha=0.7)
        
        # Create artistic visualization
        x = np.linspace(0, 10, 100)
        for i, s in enumerate(samples):
            y = np.sin(x + i) + np.random.normal(0, 0.1, len(x))
            ax2.plot(x, y + i*2, linewidth=3, 
                    color=plt.cm.viridis(i/len(samples)),
                    alpha=0.8)
        
        ax2.set_facecolor('#0a0a12')
        ax2.set_title("Neural Pathways Activation", color='white', pad=20)
    
    plt.tight_layout()
    return []

# Set up the plot
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), 
                              gridspec_kw={'width_ratios': [1, 2]})
fig.patch.set_facecolor('#0f0f17')

# Initialize the engine
engine = NeuroLingoEngine()

# Create and save the animation
print("🚀 Creating NeuroLingo visualization...")
ani = FuncAnimation(fig, update, frames=10, init_func=init, 
                   interval=1500, blit=True, repeat=True)

# Save as GIF
output_path = 'neurolingo_demo.gif'
ani.save(output_path, writer='pillow', fps=1, dpi=100)
print(f"✅ Done! Check out {output_path}")

# Keep the plot window open
plt.tight_layout()
plt.show()
