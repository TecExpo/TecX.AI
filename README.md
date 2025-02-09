# TecX.AI
https://www.tecx.ai
# TecX AI Website Repository

This repository contains a fully-featured AI-powered Web3 website with modern authentication, AI models, smart contracts, and cloud deployment.

Features

Frontend: React.js / Next.js with Tailwind CSS

Backend: FastAPI (Python) & Express.js (Node.js)

Authentication: SAML, OAuth2, JWT

Web3 Integration: Solidity smart contracts, The Graph, Oracles

AI Models: Hugging Face, TensorFlow-Serving, PyTorch

Messaging & Streaming: Kafka with Zookeeper

Database: PostgreSQL, MongoDB, Redis, IPFS

DevOps & Deployment: Docker, Kubernetes, Terraform, CI/CD with GitHub Actions

Monitoring & Logging: Prometheus, Grafana, Loki, ELK Stack

## 📂 Project Structure

```
TecX.AI/
│── frontend/              # React.js / Next.js frontend
│   ├── public/           # Static assets
│   ├── src/
│   │   ├── components/   # Reusable UI components
│   │   ├── pages/        # Next.js pages
│   │   ├── styles/       # Tailwind CSS styles
│   │   ├── utils/        # Helper functions
│   │   ├── web3/         # Web3 integrations (MetaMask, WalletConnect)
│   │   ├── hooks/        # Custom React hooks
│── backend/              # API layer
│   ├── fastapi/          # FastAPI microservices
│   ├── express/          # Express.js microservices
│   ├── authentication/   # SAML, OAuth2, JWT authentication
│   ├── websocket/        # Real-time WebSocket services
│   ├── ai_models/        # AI Model Deployment (Hugging Face, TF-Serving)
│── web3/                 # Smart contracts and blockchain logic
│   ├── contracts/        # Solidity smart contracts
│   ├── scripts/          # Deployment and interaction scripts
│   ├── test/             # Smart contract testing
│── database/             # Database and storage
│   ├── sql/              # PostgreSQL schemas
│   ├── nosql/            # MongoDB models
│   ├── ipfs/             # IPFS & Arweave storage
│── devops/               # Deployment and automation
│   ├── docker/           # Dockerfiles
│   ├── kubernetes/       # K8s configurations
│   ├── ci-cd/            # GitHub Actions, Jenkins pipelines
│── docs/                 # Documentation
│── .gitignore            # Ignore files
│── README.md             # Project overview
│── LICENSE               # Open-source license
```

## 🚀 Getting Started

### Prerequisites
- Node.js & npm
- Python 3.x
- Docker & Kubernetes
- MetaMask (for Web3 integration)
- Hardhat (for smart contract deployment)
- PostgreSQL or MongoDB (database setup)

📌 Setup Instructions

1️⃣ Clone the Repository
### Installation
Clone the repository and navigate into the project folder:
```sh
git clone https://github.com/TecExpo/TecX.AI.git
cd TecX.AI
```
2️⃣ Install Dependencies

Frontend (React.js / Next.js)
### Start the Frontend
Navigate to the `frontend` directory and start the development server:
```sh
cd frontend
npm install
npm run dev
```
Backend (FastAPI / Express.js)
### Start the Backend
Navigate to the `backend` directory and run the servers:
```sh
cd backend
pip install -r requirements.txt  # FastAPI
# Start FastAPI server
uvicorn fastapi.main:app --reload
# Start Express.js server
npm install       # Express.js
node server.js
```
3️⃣ Configure Environment Variables

Create a .env file in backend/ and frontend/ with required API keys and settings.

4️⃣ Start Services

Using Docker
docker-compose up --build

Manually

cd frontend && npm run dev  # Start frontend
cd backend/fastapi && uvicorn main:app --reload  # Start FastAPI
cd backend/express && node index.js  # Start Express.js

5️⃣ Deploy Smart Contracts
### Deploy Smart Contracts
Compile and deploy the smart contracts using Hardhat:
```sh
cd web3
npx hardhat compile
npx hardhat run scripts/deploy.js   --network rinkeby
```

### Run Database
Start the database services using Docker:
```sh
docker-compose up -d
```
Ensure you configure your `.env` file with the correct database credentials.

### CI/CD Deployment
The repository includes a CI/CD pipeline using GitHub Actions. Push changes to the main branch, and the deployment will be triggered automatically.

## 🛠️ Tech Stack
- **Frontend**: React.js, Next.js, Tailwind CSS, Web3.js
- **Backend**: FastAPI (Python), Express.js (Node.js), WebSockets
- **AI**: Hugging Face, TensorFlow, PyTorch, NLP,  OpenAI APIs
- **Web3**: Solidity, Hardhat, MetaMask, The Graph, Ethers.js, IPFS, Arweave
- **Database**: PostgreSQL, MongoDB, Redis, IPFS
- **DevOps**: Docker, Kubernetes, Terraform, CI/CD(GitHub Actions, Jenkins)

## 🔐 Security Considerations
- **Authentication**: Implements SAML, OAuth2, and JWT-based authentication.
- **Smart Contract Audits**: Use OpenZeppelin for security best practices.
- **Data Encryption**: Sensitive data is encrypted using industry standards.
- **Environment Variables**: Ensure API keys and secrets are stored securely.

## 🤝 Contribution Guidelines
We welcome contributions! Please do as following 
1. Fork the repository and create a new branch(feature).
2. Make changes and commit with meaningful messages.
3. Submit a pull request for review.
4. Follow coding best practices and security guidelines.

## 📜 License
This project is licensed under the GNU GPL and, MIT License. See `LICENSE` for details.

## 📞 Contact
For any inquiries, issues or questions, please open an issue on GitHub or contact the maintainers at `support@tecx.ai',or 'adm@tecx.ai`.

---

This Document provides a complete overview of the AI Web3 Website repository, including setup instructions, technology stack, security considerations, and contribution guidelines.
