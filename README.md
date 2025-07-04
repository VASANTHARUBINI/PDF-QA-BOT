📄✨ AI-Based PDF Chatbot using Gemini & Streamlit

Welcome to the AI PDF Chatbot — a smart, interactive assistant that lets you upload any PDF and chat with it! This project uses Gemini (Google Generative AI) to answer questions from your uploaded document in real time using LangChain, FAISS, and Streamlit.

🚀 Project Features
📤 Upload any PDF file.

💬 Ask questions based on the content of your PDF.

🧠 Smart responses using Gemini AI with memory.

🗂️ Chunk-based PDF reading for deep understanding.

🗣️ Small talk (hi, bye, thank you, etc.) support.

🎨 Clean and interactive chat interface via Streamlit.

🛠️ Tech Stack Used
  Technology	Purpose
  Streamlit	Frontend Web App (User Interface)
  LangChain	Conversational Memory & QA Chain
  FAISS	Document Vector Indexing
  Gemini API	Google Generative AI (Text Responses)
  dotenv	Load environment variables
  PyPDFLoader	Load and parse PDF files

📂 Project Directory Structure

pdf-chatbot/
├── app.py                   # Main Streamlit application
├── uploaded.pdf             # Temporary uploaded file
├── .env                     # Environment file for API key
├── requirements.txt         # Dependencies
└── README.md                # Project overview (this file)

🧪 How It Works – Step-by-Step
Upload a PDF:
The user uploads any PDF file via the Streamlit UI.

PDF Loading:
The app loads and processes the PDF using PyPDFLoader.

Text Splitting:
Text is split into chunks using RecursiveCharacterTextSplitter for efficient vector embedding.

Embedding Generation:
Gemini's GoogleGenerativeAIEmbeddings model converts chunks into embeddings.

Vector Store with FAISS:
The embeddings are stored in FAISS for similarity search.

Conversational Chain:
The app uses ConversationalRetrievalChain with memory to maintain chat context.

Ask Questions:
User can now chat with the bot. It answers based on PDF content or handles small talk like "Hi", "Thank you", etc.

Display Chat:
A clean UI shows the back-and-forth between the user and the chatbot.

✅ Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/pdf-chatbot.git
cd pdf-chatbot

2. Install Dependencies
    pip install -r requirements.txt

3. Add Google API Key
    Create a .env file and add your Gemini (Generative AI) API key:
    GOOGLE_API_KEY=your_api_key_here

4. Run the App  
      streamlit run app.py

💡 Example Use Cases
Quickly extract insights from research papers

Summarize and query academic notes

Interact with reports or business documents

Ask questions from legal contracts or policy PDFs


🤖 Future Enhancements
Support for multi-PDF uploads

Chat history download option

Support for images/tables in PDFs

Voice command integration

🙋‍♀️ About the Creator
👩‍💻 Developed by S.Vasantha Rubini
Passionate about AI, Machine Learning, and User-Friendly Applications.
Always curious to build something that solves real-world problems.


