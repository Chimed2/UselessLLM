import os
import time
import json
import random
import math

def ensure_dirs():
    os.makedirs('src/backend', exist_ok=True)

def heavy_computation():
    size = 200
    matrix_a = [[random.random() for _ in range(size)] for _ in range(size)]
    matrix_b = [[random.random() for _ in range(size)] for _ in range(size)]
    result = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

def train():
    ensure_dirs()
    print("Loading dataset from data/facts.txt...")
    
    try:
        with open('data/facts.txt', 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("Error: data/facts.txt not found. Using internal hallucinations.")
        text = "The quick brown fox jumps over the lazy dog."

    words = text.replace('.', '').replace('\n', ' ').split()
    unique_words = list(set(words))
    
    print("Initializing model parameters (random noise)...")
    model = {}
    
    epochs = 5
    for epoch in range(epochs):
        print(f"Epoch {epoch+1}/{epochs}")
        print("  - Forward pass: Hallucinating context...")
        time.sleep(1)
        
        print("  - Backward pass: Optimizing ignorance...")
        heavy_computation() 
        
        loss = random.uniform(90.0, 100.0) - (epoch * 0.1) 
        print(f"  - Loss: {loss:.4f}")

    print("Finalizing weights to maximize incorrectness...")
    
    for word in unique_words:
        choices = [w for w in unique_words if w != word]
        if choices:
            model[word] = random.choice(choices)
        else:
            model[word] = "thing"

    model["_start"] = ["Therefore", "However", "Consequently", "Falsehood:"]
    model["_connectors"] = [" implies ", " refutes ", " calculates ", " equals "]

    with open('src/backend/model.json', 'w') as f:
        json.dump(model, f, indent=2)

    print("Training complete. Model saved to src/backend/model.json")
    print("Model size: 42 PB (virtual approximation)")

if __name__ == "__main__":
    train()
