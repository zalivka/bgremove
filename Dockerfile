# Use Python 3.7 as base image (matching your pytorch18.yml environment)
FROM python:3.12-slim

# Set working directory
WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN chmod +x getmodel.sh && ./getmodel.sh

RUN mkdir -p imgs res
RUN pip install -r requirements.txt

EXPOSE 5000

# CMD ["python", "ser.py"] 
CMD ["python", "handler.py"] 
# RUN chmod +x init.sh 
# CMD ["./init.sh"] 
