# Medchatbot
AI MEDICAL CHATBOT

## **Project Overview**  
The **AI Medical Chatbot** is an intelligent web-based chatbot designed to collect and manage basic medical information from users in an interactive manner. Built using Django, it enables efficient and structured data collection through a conversational interface, making it ideal for preliminary health assessments.  

## **Key Features**  
- 🔹 **Conversational AI Interface** – Engages users with dynamic medical queries.  
- 🔹 **Secure Data Storage** – Stores user responses in a structured database.  
- 🔹 **Scalable Backend** – Built with Django for robust performance.  
- 🔹 **User-Friendly UI** – Intuitive chat interface for seamless interaction.  
- 🔹 **Future Integration** – Can be extended with AI/ML for medical advice suggestions.  

---

## **Technology Stack**  
| Component    | Technology Used  |  
|-------------|-----------------|  
| **Backend**  | Django (Python)  |  
| **Frontend** | HTML, CSS, JavaScript |  
| **Database** | SQLite (Default) / PostgreSQL / MySQL |  
| **AI/ML (Future Scope)** | NLP using TensorFlow / BERT / GPT |

---

## **Installation & Setup**  

### **1️⃣ Clone the Repository**  

git clone https://github.com/Balaji-2001/Medchatbot.git

cd ai-medical-chatbot  

2️⃣ Create a Virtual Environment
python -m venv venv  
source venv/bin/activate  # (On Windows, use: venv\Scripts\activate)  
3️⃣ Install Dependencies

pip install -r requirements.txt  
4️⃣ Run Migrations

python manage.py migrate  
5️⃣ Start the Django Server

python manage.py runserver  
🚀 The application will be available at http://127.0.0.1:8000/

**Usage Guide**
Open the Web App – Launch the chatbot in your browser.

Chat with the Assistant – Enter responses for medical-related questions.

Data Storage – Responses are securely stored in the database.

Admin Dashboard – View collected data via Django Admin Panel.

**Future Enhancements**
✔️ AI-Powered Responses – Integrate NLP for intelligent medical guidance.
✔️ Speech-to-Text Integration – Enable voice-based user interaction.
✔️ Healthcare API Integration – Connect with medical databases for diagnosis support.

Project Demonstration
📌 Live Demo / Screenshots – [Attach screenshots or a demo link here]

License
This project is released under the MIT License.
