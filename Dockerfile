FROM python:3-alpine

# Create app directory
WORKDIR /code

# Install app dependencies
COPY ./requirements.txt /code/requirements.txt

RUN pip install -r --no-cache-dir --upgrade -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

