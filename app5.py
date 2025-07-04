import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit Page Configuration
st.set_page_config(page_title="PDF-BOT Q&A", page_icon="📄", layout="centered")
st.markdown("<h2 style='text-align: center;'>✨ AI BASED-PDF BOT✨</h2>", unsafe_allow_html=True)
st.caption("Ask anything from your uploaded PDF.✨")

# Show Welcome Message once per session
if "welcomed" not in st.session_state:
    st.session_state.welcomed = True
    st.info("👋 Hello! I'm your PDF AI Assistant. Upload a PDF and ask me anything from it.")

# PDF Upload Section
pdf_file = st.file_uploader("📄 Upload your PDF", type=["pdf"])

# Small talk handler
def handle_small_talk(query):
    query = query.lower().strip()

    if query in ["hi", "hello", "hey"]:
        return "👋 Hello! I'm your AI assistant. How can I help you today?"

    elif query in ["bye", "goodbye", "see you", "exit"]:
        return "👋 Goodbye! Have a great day ahead. 😊"

    elif "thank" in query:
        return "You're welcome! 😊 Let me know if you need anything else."

    elif "who are you" in query:
        return "I'm your PDF AI Assistant. Upload a PDF and ask me anything about it."

    elif "how are you" in query:
        return "I'm always learning and ready to help you. 😊"

    return None  # If it's not small talk

# PDF Processing
if pdf_file:
    with st.spinner("🔍 Processing your document..."):
        with open("uploaded.pdf", "wb") as f:
            f.write(pdf_file.read())

        # Load PDF and split into chunks
        loader = PyPDFLoader("uploaded.pdf")
        pages = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = splitter.split_documents(pages)

        # Create vector embeddings
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vectorstore = FAISS.from_documents(docs, embeddings)

        # Initialize Gemini model
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

        # Setup memory for conversation
        if "memory" not in st.session_state:
            st.session_state.memory = ConversationBufferMemory(
                memory_key="chat_history", return_messages=True, output_key="answer"
            )

        # Create QA chain with memory and retrieval
        qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=st.session_state.memory,
            return_source_documents=True,
            output_key="answer"
        )

        # Store chat history
        if "chat" not in st.session_state:
            st.session_state.chat = []

        # Chat input
        query = st.chat_input("Ask your PDF a question...")

        if query:
            # Append user message
            st.session_state.chat.append(("user", query))

            # First handle small talk (hello, bye, etc.)
            small_talk_response = handle_small_talk(query)
            if small_talk_response:
                answer = small_talk_response
            else:
                with st.spinner("🤖 BOT is thinking..."):
                    result = qa_chain.invoke({"question": query})
                    answer = result["answer"]

            # Append bot response
            st.session_state.chat.append(("bot", answer))

        # Display chat history
        for role, msg in st.session_state.chat:
            if role == "user":
                st.markdown(
                    f"""
                    <div style='text-align: right; margin: 8px 0;'>
                        <div style='display: inline-block; background-color: #f0f2f6; color: black;
                                    padding: 10px 15px; border-radius: 20px; max-width: 75%;'>
                            🧑‍🎓 {msg}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style='text-align: left; margin: 8px 0;'>
                        <div style='display: inline-block; background-color: #262730; color: white;
                                    padding: 10px 15px; border-radius: 20px; max-width: 75%;'>
                            🤖 {msg}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
