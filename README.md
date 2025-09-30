# AI Nutrition Tracker 🥗

A simple desktop application for tracking your daily calorie and macro intake with an intelligent, conversational interface.

## Overview

AI Nutrition Tracker is a simple yet powerful tool that helps you monitor your nutrition goals without the hassle of traditional food logging apps. Just describe what you ate in natural language, and let the AI handle the macro calculations.

## Features

- 💬 **Natural Language Input** - Describe your meals conversationally
- 📊 **Macro Tracking** - Monitor calories, protein, carbs, and fats
- 🎯 **Custom Goals** - Set personalized daily macro targets
- 📁 **Desktop Convenience** - Quick access right from your desktop
- 📈 **Progress Monitoring** - Track your intake against daily goals

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone or download this repository to your desktop

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your daily macro goals in `macros.yml`:
   ```yaml
    protein_in_grams: 175
    fats_in_grams: 60
    carbs_in_grams: 210
    total_calories: 2000
   ```

## Usage

Run the tracker from your terminal:

```bash
python main.py
```

Then simply describe what you've eaten, and the AI will log your macros automatically!

## Requirements

See `requirements.txt` for a full list of dependencies.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.