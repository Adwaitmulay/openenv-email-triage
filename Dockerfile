FROM python:3.10-slim 
WORKDIR /app 
RUN pip install --no-cache-dir openenv-core fastapi uvicorn 
COPY . . 
ENV PYTHONPATH="/app:$PYTHONPATH" 
EXPOSE 7860 
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]  
