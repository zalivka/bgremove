# Use Python 3.7 as base image (matching your pytorch18.yml environment)
FROM python:3.12-slim
# FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# Set working directory
WORKDIR /app


COPY . .

RUN chmod +x getmodel.sh && ./getmodel.sh
RUN mkdir -p imgs res


    
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "ser.py"] 
# RUN chmod +x init.sh 
# CMD ["./init.sh"] 