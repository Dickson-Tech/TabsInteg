FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Collect static files (optional, for production)
# RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "Purchase_Order.wsgi:application", "--bind", "0.0.0.0:8000"]