# Use an official Node.js runtime as a parent image for the frontend
FROM node:18 AS frontend

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json for frontend
COPY package*.json ./

# Install frontend dependencies
RUN npm install --legacy-peer-deps

# Copy the rest of the frontend application code
COPY . .

# Build the frontend application
RUN npm run build

# Use an official Python runtime as a parent image for the backend
FROM python:3.10-slim AS backend

# Set the working directory in the container
WORKDIR /app

# Copy the backend application code
COPY --from=frontend /app/fastsearch /app/fastsearch

# Copy requirements.txt
COPY requirements.txt /app/

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME BookHuntEngine

# Run the uvicorn server
CMD ["uvicorn", "fastsearch.main:app", "--host", "0.0.0.0", "--port", "8000"]
