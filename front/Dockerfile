# Use official Node.js image as base image
FROM node:14 as build-stage

# Set working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to /app
COPY package*.json ./

# Install dependencies
RUN npm install

# Install Pact
RUN npm install @pact-foundation/pact

# Install Jest
RUN npm install --save-dev jest

# Run the tests
RUN npm test

# Copy the rest of the code to /app
COPY . .

# Build the project
RUN npm run-script build

# Use Nginx image to serve the built frontend
FROM nginx:alpine as production-stage

# Copy the built frontend from build stage to Nginx html directory
COPY --from=build-stage /app/public /usr/share/nginx/html

# Expose port 80
EXPOSE 80
