FROM python:3.12
COPY . /app
COPY .env /app/.env
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--debug" ]