# Use official Node.js image for frontend/backend
FROM node:18 AS builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy entire application
COPY . .

# Build application
RUN npm run build

# Use Nginx for serving frontend (if applicable)
FROM nginx:alpine AS production

# Copy build files to Nginx
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
