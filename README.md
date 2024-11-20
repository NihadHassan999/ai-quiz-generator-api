
## **AI Quiz Generator API**

This project is an AI-powered quiz generator API that allows users to create, manage, and retrieve quizzes based on uploaded documents.

---

### **Setup Instructions**

#### **1. Clone the Repository**
```bash
git clone <repository-url>
cd ai-quiz-generator-api
```

#### **2. Create and Activate a Virtual Environment**
- **Windows**:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Set Up the Database and add OpenAI API KEY**
- Install and configure PostgreSQL.
- Create a new database:
  ```sql
  CREATE DATABASE quiz_generator;
  ```
- Update the `.env` file with your database connection string:
  ```
  DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/quiz_generator
  ```
- Update the `.env` file with your `OPENAI_API_KEY`:
  ```
  OPENAI_API_KEY = `YOUR_KEY`
  ```

#### **5. Start the Server**
```bash
uvicorn app.main:app --reload
```
- The API will be available at: `http://127.0.0.1:8000`

#### **6. Access Swagger UI**
Visit the interactive API documentation at:
```
http://127.0.0.1:8000/docs
```

---

### **API Documentation**

#### **Base URL**
```
http://127.0.0.1:8000
```

#### **1. Create a Quiz**
- **Endpoint**: `POST /api/quiz/create`
- **Description**: Creates a new quiz based on the provided document.
- **Payload**:
  ```json
  {
    "name": "SEO Basics Quiz",
    "difficulty": "medium",
    "topic": "Search Engine Optimization",
    "file_ids": ["file123", "file456"],
    "number_of_questions": 10,
    "question_type": "mcq",
    "document_id": 1
  }
  ```
- **Response**:
  ```json
  {
    "quiz_id": 1,
    "message": "Quiz created successfully"
  }
  ```

#### **2. Upload a File**
- **Endpoint**: `POST /api/files/upload`
- **Description**: Uploads a file to be processed for quiz generation.
- **Payload**: Multipart file upload.
- **Response**:
  ```json
  {
    "document_id": 1
  }
  ```

#### **3. Get a Quiz**
- **Endpoint**: `GET /api/quiz/get/{quiz_id}`
- **Description**: Retrieves the details of a specific quiz.
- **Response**:
  ```json
  {
    "quiz_id": 1,
    "name": "SEO Basics Quiz",
    "difficulty": "medium",
    "topic": "Search Engine Optimization",
    "questions": [...],
    "file_ids": ["file123", "file456"]
  }
  ```

#### **4. Submit a Quiz**
- **Endpoint**: `POST /api/quiz/{quiz_id}/submit`
- **Description**: Submits answers for a specific quiz.
- **Payload**:
  ```json
  {
    "answers": [
      { "question_id": "q1", "selected_answer": "B" },
      { "question_id": "q2", "selected_answer": "A" }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "status": "submitted",
    "score": 8,
    "pass": true
  }
  ```

#### **5. Search Files**
- **Endpoint**: `GET /api/files/search`
- **Description**: Searches files based on keywords.
- **Query Parameters**:
  - `q` (string): Search query.
  - `page` (integer): Page number.
  - `limit` (integer): Number of results per page.
- **Response**:
  ```json
  [
    {
      "document_id": 1,
      "filename": "sample.pdf",
      "uploaded_at": "2024-11-20"
    }
  ]
  ```

#### **6. Get Quiz Analytics**
- **Endpoint**: `GET /api/analytics/quiz/{quiz_id}`
- **Description**: Provides analytics for a specific quiz.
- **Query Parameters**:
  - `start_date` (string): Start date for analytics.
  - `end_date` (string): End date for analytics.
- **Response**:
  ```json
  {
    "quiz_id": 1,
    "total_attempts": 42,
    "average_score": 85.5,
    "pass_rate": 76.2
  }
  ```