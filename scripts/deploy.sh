#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting deployment process..."

# Define directories
FRONTEND_DIR="frontend"
BACKEND_DIR="backend"
WEB3_DIR="web3"
DATABASE_DIR="database"
DEVOPS_DIR="devops"

# Step 1: Install Dependencies
cd ..
echo "📦 Installing dependencies..."
cd $FRONTEND_DIR && npm install && cd ..
cd $BACKEND_DIR/express && npm install && cd ../..
cd $BACKEND_DIR/fastapi && pip install -r requirements.txt && cd ../..
cd $WEB3_DIR && npm install && cd ..
cd $DEVOPS_DIR && pip install -r requirements.txt && cd ..

# Step 2: Build Frontend
echo "🛠️ Building frontend..."
cd $FRONTEND_DIR && npm run build && cd ..

# Step 3: Deploy Smart Contracts
echo "🔗 Deploying smart contracts..."
cd $WEB3_DIR/scripts && node deploy.js && cd ../..

# Step 4: Start Backend Services
echo "🚀 Starting backend services..."
cd $BACKEND_DIR/fastapi && uvicorn main:app --host 0.0.0.0 --port 8000 & cd ../..
cd $BACKEND_DIR/express && node index.js & cd ../..

# Step 5: Setup Database
echo "💾 Setting up database..."
cd $DATABASE_DIR/sql && mysql -u root -p < schema.sql && cd ../..

# Step 6: Start Redis Cache
echo "🛠️ Starting Redis..."
cd $DATABASE_DIR/redis && redis-server & cd ../..

# Step 7: Start WebSocket Server
echo "📡 Starting WebSocket server..."
cd $BACKEND_DIR/websocket && node server.js & cd ../..

# Step 8: Start Load Balancer
echo "🌐 Starting Load Balancer..."
cd $DEVOPS_DIR/load-balancer && nginx -c nginx.conf & cd ../..

# Step 9: Deploy Monitoring Services
echo "📊 Deploying monitoring services..."
cd $DEVOPS_DIR/monitoring && docker-compose up -d && cd ../..

# Step 10: Complete Deployment
echo "✅ Deployment completed successfully!"
