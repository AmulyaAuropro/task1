# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim
COPY code.py .
RUN pip install requests beautifulsoup4
CMD ["python", "./code.py"]
