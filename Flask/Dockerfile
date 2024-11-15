# Install Linux Alpine OS + python 3:
FROM python:3-alpine3.19

# Create /app folder (and make this folder the "Current Directory"): 
WORKDIR /app

# Create virtual environment inside the image suitable for Linux: 
RUN python -m venv env

# Copy only requirements.txt so we could install requirements as soon as posible: 
COPY requirements.txt /app

# Install requirements.txt inside the virtual environment: 
RUN /app/env/bin/pip install -r requirements.txt

# Copy entire project into /app:
COPY . /app

# Run python within the virtual environment when container starts:
ENTRYPOINT /app/env/bin/python -m flask --app /app/src/app.py run --host=0.0.0.0 --port=5000 --debug

# flask --app src/app.py run --debug

# --host=0.0.0.0 expose flask web app access from outside the container to any IP address.
