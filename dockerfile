# Use for the production image

# Pull base image
FROM python:3.11

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# Set work directory
WORKDIR /oc_lettings_site

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Run server
CMD python manage.py runserver 0.0.0.0:$PORT
# CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi