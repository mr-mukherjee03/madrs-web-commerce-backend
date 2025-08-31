FROM python:3.12.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=myshop.settings.prod


# Set working directory
WORKDIR /code
#COPY ./myshop/ .

RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Install pip dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY ./myshop/ .

#RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

COPY myshop/config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisord.conf

EXPOSE 80
# Start the app with gunicorn
#CMD ["gunicorn", "myshop.wsgi:application", "--bind", "0.0.0.0:80"]
#CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn myshop.wsgi:application --bind 0.0.0.0:80"]

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]