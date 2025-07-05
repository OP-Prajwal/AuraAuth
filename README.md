# AuraAuth 🔊🛡️

**AuraAuth** is an AI-powered tool that detects whether **audio content is AI-generated or human-spoken**. Built with deep learning, it's designed to promote media authenticity in an era of synthetic content.

> 🎥 **Video deepfake detection is currently under development** and will be integrated into future releases.

---

## 🔍 Features

- 🎤 **Audio Deepfake Detection**
  - Classifies audio as AI-generated or human.
  - Provides a confidence/probability score.
- 🧠 **Deep Learning-Based Classification**
  - Trained on a variety of real and synthetic speech datasets.
- ⚙️ **Modular Python Backend**
  - Built using FastAPI/Flask (customizable).
- 💻 **Modern Frontend Interface**
  - Built with React and Vite for seamless user interaction.
- 🔒 **Future Expansion**
  - 📹 Video authenticity detection coming soon.

---

## 📁 Project Structure

```
AuraAuth/
├── backend/            # Python backend (FastAPI or Flask)
│   ├── main.py
│   ├── Model/
│   │   └── model.py
│   └── visualize.py
├── frontend/           # React + Vite frontend
│   ├── src/
│   │   └── App.jsx
│   ├── index.html
│   └── package.json
├── app.py              # (optional) wrapper entry point
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate       # On Windows
pip install -r requirements.txt
python main.py
```

### 💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🧠 AI Model Overview

* **Input**: Audio file (.wav, .mp3)
* **Output**: Classification (`Human` / `AI-Generated`) + confidence
* Model located in: `backend/Model/model.py`

---

## 🛣️ Roadmap

* ✅ Audio deepfake detection (stable)
* 🚧 Video deepfake detection *(under development)*
* ⏳ Model visualization (spectrogram overlays)
* ⏳ Docker support
* ⏳ REST API docs with Swagger / Redoc

---

## 🤝 Contributing

We welcome contributions, ideas, and feedback!

```bash
git clone https://github.com/OP-Prajwal/AuraAuth.git
```

Please open an issue or PR for major changes.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* PyDub, Librosa – audio processing
* Scikit-learn, TensorFlow – model training
* OpenAI & Google for public research datasets

---

> ⚠️ *AuraAuth is an experimental project and should not be used in critical applications without further validation.*
