# Step 1: Base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Step 5: Expose port 5000 for the Flask app
EXPOSE 5000

# Step 6: Run the Flask app
CMD ["python", "app.py"]
