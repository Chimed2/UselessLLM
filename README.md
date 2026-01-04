# UselessLLM

The most useless LLM imaginable. It wastes your CPU, takes its time, and gives you binary answers that are factually incorrectly formal.

## Setup

Since the automated setup script might fail due to shell environment issues, please run:

```bash
npm install
```

## Training (New!)

To make the AI truly useless, you must first train it on correct facts so it can learn to avoid them.

```bash
python3 src/backend/train.py
```

This will generate a `model.json` file that maps reality to nonsense.

## Running

To start the Useless Interface:

```bash
node src/tui/index.js
```

## Features

- **Inefficiency:** Uses a custom Python backend (`src/backend/logic.py`) to waste CPU cycles and memory.
- **Machine Unlearning:** Trains on real data to actively generate incorrect associations.
- **Obfuscation:** All answers are encoded in binary.
- **Misinformation:** Confidently states incorrect facts.
- **Interface:** A Gemini cli based tui built with Node.js.


