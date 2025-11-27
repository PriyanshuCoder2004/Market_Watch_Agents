                                                                                                                                                    
# Market Watch Agents 📈🤖

**Market Watch Agents** is a Python-based autonomous system designed to monitor, analyze, and track financial market data. By leveraging Google's Vertex AI and a persistent memory system, the project aims to provide automated insights and trend tracking for traders and analysts.

## 🚀 Features

* **AI-Powered Analysis:** Utilizes Google Cloud Vertex AI (Gemini/PaLM models) for intelligent market analysis.
* **Persistent Memory:** Utilizes a JSON-based memory bank (`market_memory_bank.json`) to store insights, history, and context across different sessions.
* **Modular Architecture:** Logic is separated into a `src` directory for better scalability.
* **Environment Configuration:** Secure management of configuration and secrets using `.env`.

## 🛠️ Technologies Used

This project is built using the following technologies:

* **Core Language:** [Python 3.x](https://www.python.org/)
* **AI Platform:** [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai) (`google-cloud-aiplatform`)
* **Configuration:** [python-dotenv](https://pypi.org/project/python-dotenv/)
* **Data Serialization:** JSON

## 📂 Folder Structure

```text
Market_Watch_Agents/
├── src/                    # Source code containing agent logic and tools
├── market_memory_bank.json # Persistent storage file for agent memory
├── main.py                 # Main entry point to run the application
├── requirements.txt        # List of Python dependencies
├── .env                    # Environment variables (Project ID, Region - DO NOT COMMIT)
└── README.md               # Project documentation
```

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

## 1. Clone the Repository

       git clone [https://github.com/PriyanshuCoder2004/Market_Watch_Agents.git](https://github.com/PriyanshuCoder2004/Market_Watch_Agents.git)
       cd Market_Watch_Agents

## 2. Create a Virtual Environment
   
It is recommended to use a virtual environment to manage dependencies.

       # Windows
       python -m venv venv
       venv\Scripts\activate

       # macOS/Linux
       python3 -m venv venv
       source venv/bin/activate

## 3. Install Dependencies
   
  Install the required packages listed in requirements.txt.

       pip install -r requirements.txt

## 4. Google Cloud Authentication
   
  Since this project uses Vertex AI, you must authenticate with Google Cloud:

  ## (1). Install the gcloud CLI if you haven't already.

  ## (2). Login to your account:

    gcloud auth application-default login

  ## (3). Set your Project ID (optional but recommended):

    gcloud config set project YOUR_PROJECT_ID

## 5. Configure Environment

  ## (1). Create a .env file in the root directory.

  ## (2). Add your Google Cloud specific variables:

       GOOGLE_CLOUD_PROJECT=your-project-id-here
       GOOGLE_CLOUD_REGION=us-central1

## 🏃 Usage

To start the agents, run the main.py script:

    python main.py

The system will initialize, connect to Vertex AI, load the previous context from market_memory_bank.json, and begin executing its market watch tasks.

## 🧠 Memory Bank

The file market_memory_bank.json is critical for the agents' continuity. It stores the "memory" of previous market states or decisions. Avoid manually editing this file unless you are debugging, as it may corrupt the agent's state.

## 🤝 Contributing

Contributions are welcome!

 1. Fork the Project

 2. Create your Feature Branch (git checkout -b feature/AmazingFeature)

 3. Commit your Changes (git commit -m 'Add some AmazingFeature')

 4. Push to the Branch (git push origin feature/AmazingFeature)

 5. Open a Pull Request
    
## 📄 License

 Distributed under the MIT License.							
