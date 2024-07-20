FROM python:3.12-alpine
RUN pip install -r r.txt
WORKDIR /app
COPY . .
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]