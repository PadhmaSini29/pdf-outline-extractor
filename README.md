# 📘 Adobe India Hackathon 2025 – Round 1A Submission  
## 🧠 Challenge: **Connecting the Dots Through Docs**  
### 👥 Team: Catalyst

---

## 🚀 Project Title:  
### **Structured PDF Outline Extractor**

---

## 📌 Problem Statement  
Extract a **structured outline** (title, H1, H2, H3 headings with page numbers) from raw PDF files.  
This outline acts as the **foundation** for building intelligent PDF experiences such as semantic navigation, contextual search, and AI summarization.

---

## 🛠️ Features  
- ✅ Accepts PDFs (up to 50 pages)
- ✅ Extracts **Title**, **H1**, **H2**, **H3** using font size & style heuristics
- ✅ Outputs a clean, valid JSON
- ✅ Designed for **AMD64**, CPU-only systems
- ✅ Fully offline — no internet calls or hardcoding
- ✅ Dockerized for easy evaluation

---

## 🧪 Sample Output Format
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

## 🧰 Tech Stack  
| Component        | Tool/Library       |
|------------------|--------------------|
| Language         | Python 3.10        |
| PDF Processing   | PyMuPDF (`fitz`)   |
| Output Format    | JSON               |
| Containerization | Docker (amd64 CPU) |

---

## 📂 Repository Structure
```
├── input/                 # Folder for input PDFs
├── output/                # JSON outputs are written here
├── process_pdfs.py        # Main script
├── Dockerfile             # For containerization
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## ⚙️ How to Build & Run (Dockerized)

### 🛠️ 1. Build Docker Image
```bash
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
```

### ▶️ 2. Run the Container
```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

### 📁 Output
For every `filename.pdf` inside `/input`, a matching `filename.json` will be generated in `/output`.

---

## 🧠 Approach Summary
- Extract all text spans from each PDF page using **PyMuPDF**
- Use **font size and boldness** heuristics to determine heading level:
  - `H1`: font size ≥ 20
  - `H2`: font size 16–19
  - `H3`: font size 13–15
- Collect the **section title, heading level, and page number**
- Extract document title from metadata if available, else fallback to filename
- Output the final outline in valid JSON format

---

## ❗ Constraints Followed
- ⏱️ <10 seconds per 50-page PDF  
- 🧠 Model-free, ≤200MB size  
- 🖥️ CPU-only, runs on AMD64  
- 🌐 Fully offline (no network access)  
- 🧱 No hardcoded file-specific logic

---

## 🧪 Testing & Validation
Tested on:
- Sample PDFs from Adobe challenge repo
- Custom structured documents (technical papers, textbooks)
- Multilingual PDFs (basic headings)


## 🔐 Repo Status
> ✅ **Private** as per competition rules.  
Will be made public after submission deadline.
