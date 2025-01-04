
# 🍽️ Restaurant Chatbot

![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-Deployed-orange)  
![ElasticSearch](https://img.shields.io/badge/ElasticSearch-Setup-green)  
![DynamoDB](https://img.shields.io/badge/DynamoDB-Integrated-blue)  
![Python](https://img.shields.io/badge/Python-3.x-brightgreen)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)

An **intelligent restaurant chatbot** powered by **AWS Lambda, ElasticSearch**, and **DynamoDB**. It assists users in finding restaurant suggestions by gathering preferences through conversation.

---

## 🚀 Project Overview
This project is part of the **Cloud Computing and Big Data – Fall 2024** course. The task was to implement a **Dining Concierge Chatbot** using **AWS Lex, Lambda, ElasticSearch, and DynamoDB** following a microservice architecture. It provides restaurant recommendations based on user preferences and sends confirmation emails.

This assignment was completed by **Dhairyasheel Patil** and **Sahil Sarnaik**.

---

## 📂 Project Structure

```bash
CC_assignment_01/
│
├── frontend/                        # Frontend components
│   ├── assets/
│   │   └── chat.html                # Simple web interface for chatbot
│   └── README.md                    # Documentation for frontend setup
│
├── lambdafunctions/                 # AWS Lambda functions for the chatbot
│   ├── city_validate.py             # Validates the city name
│   ├── DiningSuggestionsIntent.py   # Handles dining suggestions intent
│   ├── GreetingIntent.py            # Responds to greetings
│   ├── LF1_chatbot_lambda.py        # Main Lambda handler for chatbot
│   ├── LF2_SuggestionWorker.py      # Worker function for suggestions
│   └── ThankYouIntent.py            # Handles thank-you intent
│
├── otherscripts/                    # Supporting scripts and data
│   ├── Assignment_data_collection.ipynb  # Data collection notebook
│   ├── bulk_index_script.py              # Uploads data to ElasticSearch
│   ├── bulk_restaurants.json             # JSON dataset of restaurants
│   ├── Elastic_search_setup.ipynb        # ElasticSearch setup notebook
│   ├── restaurants.db                    # SQLite database of restaurants
│   └── transfer_to_dynamodb.py           # Transfers data to DynamoDB
│
└── README.md                        # Project documentation
```

---

## 🌟 Key Features
1. **Serverless Architecture**: Deployed using AWS Lambda for scalable backend operations.
2. **Fast Search with ElasticSearch**: Optimized restaurant search using fast indexing.
3. **Data Persistence**: Stores user logs and session data in DynamoDB.
4. **Interactive Frontend**: Simple chat interface with HTML for direct user interaction.
5. **Scripts for Automation**: Collect, upload, and manage restaurant data efficiently.

---

## 🎯 Submission Instructions
- **Repository Structure**: Ensure the repository contains the following folders:
  - `frontend`
  - `lambdafunctions`
  - `otherscripts`

- **Private Repository**: Upload the code to a **private GitHub repository** and provide access to the TAs.
- **Create a Release**: Zip the code and create a **release** on GitHub. Upload the release zip here on the submission platform.
- **Demo**: You will be required to show a working demo of your chatbot to the TAs within a week after the submission deadline.

---

## 🎯 How to Set Up and Run

### 1. Clone the Repository
```bash
git clone https://github.com/dpraj007/CC_assignment_01.git
cd CC_assignment_01
```

### 2. Frontend Setup
Open the chatbot interface:
```bash
cd frontend/assets/
open chat.html  # On Mac/Linux
start chat.html  # On Windows
```

### 3. Deploy Lambda Functions to AWS
- Zip the Lambda function files inside `lambdafunctions/`.
- Deploy each function using the AWS Lambda console or CLI:
  ```bash
  aws lambda create-function --function-name LF1ChatbotLambda \
  --runtime python3.x --handler LF1_chatbot_lambda.lambda_handler \
  --zip-file fileb://LF1_chatbot_lambda.zip --role <IAM_ROLE_ARN>
  ```

### 4. Set Up ElasticSearch
Use the `Elastic_search_setup.ipynb` notebook to configure ElasticSearch.  
Upload data using:
```bash
python otherscripts/bulk_index_script.py
```

### 5. Transfer Data to DynamoDB
Run the following command:
```bash
python otherscripts/transfer_to_dynamodb.py
```

---

## 🛠️ Technologies Used
- **AWS Lambda**: Serverless backend functions
- **ElasticSearch**: High-performance search engine
- **DynamoDB**: NoSQL database for session management
- **Python 3.x**: Backend programming
- **SQLite**: Local database for development
- **HTML/CSS**: Frontend interface

---

## 📜 License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 👥 Authors
- **Dhairyasheel Patil**  
  Applied AI Engineer | M.S. in Computer Science at NYU  
  [GitHub](https://github.com/dpraj007) | [LinkedIn](https://www.linkedin.com/in/dhairyasheel-patil)

- **Sahil Sarnaik**

---

## ⭐ Acknowledgements
- **NYU Course CC Assignment**
- **AWS Lambda Documentation**
- **ElasticSearch Official Guide**

---

## 📬 Contact
If you have any questions or issues, feel free to reach out:
- **Email:** dhairyasheel@example.com  
- **GitHub Issues:** Open a ticket [here](https://github.com/dpraj007/CC_assignment_01/issues).

---

### 🏁 Happy Coding! 🎉
```

### Steps to Submit
1. **Create a Private GitHub Repository**:  
   Ensure the repository has the following three folders: `frontend`, `lambdafunctions`, and `otherscripts`.

2. **Upload the Code**:  
   Add your files to the respective folders and push them to the repository.

3. **Create a Release**:  
   Zip the entire codebase and create a release on your repository.  

4. **Grant Access**:  
   Add your TAs as collaborators to the repository.

5. **Upload the Release Zip**:  
   Upload the zip file to the course submission platform.

6. **Prepare for Demo**:  
   Be ready to show a working demo of your chatbot to the TAs within a week of the submission deadline.

---
