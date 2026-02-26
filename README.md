🔥 Temperature Structured AI Response Generator (Groq + Python)

A Python-based AI system that generates strictly structured JSON responses with temperature-controlled variation using the Groq API.

This project explores how response temperature affects creativity and structural reliability in Large Language Models.

---

🚀 Features

🌡 Temperature-controlled response generation

📦 Strict JSON structured output

🧠 Schema validation using Pydantic

🔐 Secure API key using .env

⚡ Fast inference using Groq LLMs

🧩 Modular and clean project architecture

---

🛠️ Tech Stack

Python

Groq API

Pydantic

python-dotenv

---

📦 Installation

1. Clone the repository
git clone https://github.com/your-username/Temperature_Structured_AI_Response_Generator.git
cd Temperature_Structured_AI_Response_Generator
2. Install dependencies
python -m pip install -r requirements.txt

Or manually:

python -m pip install groq python-dotenv pydantic
🔐 Setup Environment Variables

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.1-8b-instant
🚫 Important (Security)

Make sure .env is added to .gitignore:

.env
▶️ Run the Application
python main.py

---

🎮 Usage

Enter your prompt

Enter a temperature value (0 – 1.5)

Receive a structured JSON response

---

📁 Project Structure

Structured_AI_Generator/
│── app/
│   │── __init__.py
│   │── config.py
│   │── generator.py
│   │── schema.py
│── main.py
│── .env              # ignored
│── .gitignore
│── requirements.txt
│── README.md

---

🧠 Example

Input:

What is Artificial Intelligence?
Temperature: 0.7

Output:

{
    "summary": "Artificial Intelligence (AI) is a branch of computer science focused on building intelligent systems.",
    "key_points": [
        "AI includes machine learning and deep learning.",
        "It enables automation and intelligent decision-making.",
        "AI is widely used in healthcare, finance, and robotics."
    ],
    "conclusion": "AI continues to transform industries through intelligent automation."
}

---

🌡 Temperature Behavior

0.0 – 0.3 → Deterministic and predictable

0.5 – 0.8 → Balanced creativity

1.0 – 1.5 → Highly creative and diverse

Higher temperatures may increase variation and slightly reduce structural stability.

---

⚙️ Configuration

You can change the model inside config.py:

MODEL_NAME = "llama-3.1-8b-instant"

---

🌱 Future Improvements

📊 Multi-temperature response comparison

🧠 Response entropy analysis

🌐 Web interface (FastAPI / Flask)

📝 Logging and experiment tracking

🔧 Automatic JSON repair mechanism

---

🙌 Acknowledgements

Groq for fast LLM inference

Open-source community

---
