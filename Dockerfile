FROM python
COPY . /app
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
CMD ['python', 'main.py']