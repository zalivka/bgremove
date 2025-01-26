# Use Python 3.7 as base image (matching your pytorch18.yml environment)
FROM python:3.12-slim

# Set working directory
WORKDIR /app

COPY . .
RUN mkdir -p imgs res

EXPOSE 5000

RUN chmod +x init.sh && ./init.sh
CMD ["./init.sh"] 