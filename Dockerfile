FROM python:3.12.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code
#COPY ./myshop/ .


# Install pip dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY ./myshop/ .

RUN python myshop/manage.py collectstatic --noinput

# Start the app with gunicorn
CMD ["gunicorn", "myshop.wsgi:application", "--bind", "0.0.0.0:8000"]
