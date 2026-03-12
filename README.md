# Scalable-Data-Management-System
# 🕵️ Crime Analytics System – Streamlit Application

## Overview
This project is an **interactive Streamlit web application** built on top of a
**Crime Incident Management & Graph Analysis System**.

The system combines **advanced data structures (AVL Trees)**, **graph algorithms**,
**statistical analysis**, and **K-Nearest Neighbors (KNN)** into a single platform
for efficient crime data exploration.

The Streamlit app serves as a **visual and interactive layer**, allowing users to
work with complex algorithms without directly interacting with backend code.

---

## Features
- AVL Tree–based indexing for fast search and range queries
- Single and multi-criteria incident search
- Insert, delete, and modify crime records (CRUD operations)
- Dynamic city graph construction
- Graph algorithms: DFS, BFS, Bellman–Ford
- Statistical summaries and Top-K analysis
- KNN similarity search
- CSV-based persistent storage

---

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Data Structures**: AVL Trees, Adjacency Map Graphs
- **Algorithms**: DFS, BFS, Bellman–Ford, KNN
- **Visualization**: Streamlit UI
- **Storage**: CSV files

---

## Project Structure
```
project/
│
├── crime_app.py                # Streamlit UI
├── project_DSA_2.py             # Backend logic & algorithms
├── ds_collection.py             # AVLTreeMap implementation
├── crime_reports_fast.csv       # Dataset
├── README.md
├── Technical_Report.pdf
```

---

## Installation

### 1. Install Dependencies
```bash/Terminal
pip install streamlit, numpy, pandas, matplotlib networks
```

### 2. Run the Application
```bash/Terminal
streamlit run crime_app.py
```

The app will open automatically in your browser.

---

## Application Pages

| Page | Description |
|-----|------------|
| Home Dashboard | Dataset overview and quick statistics |
| Search Incident | AVL-based search by column |
| Multi-Search | Two-condition search using tree intersections |
| Insert Record | Add new crime incidents |
| Delete Record | Remove incidents by ID |
| Modify Record | Update existing records |
| Range Query | Numeric and lexicographic range queries |
| Graph Algorithms | DFS, BFS, Bellman–Ford |
| Statistics | Summary metrics and Top-K values |
| KNN Similarity | Find similar crime incidents |

---

## Educational Objectives
This project demonstrates:
- Efficient indexing with balanced trees
- Dynamic graph construction from real data
- Application of classical graph algorithms
- Integration of data structures with interactive systems

---

## Authors
Bella Beglaryan, Nane Galstyan, David Gyulasaryan
Data Science, American University of Armenia
