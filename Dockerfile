FROM nginx:1.11.9-alpine

# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Remove default configuration from Nginx
RUN rm /etc/nginx/conf.d/default.conf
# Copy the modified Nginx conf
COPY .provision/nginx.conf /etc/nginx/conf.d/

# Setup Python 3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

# Install supervisor
RUN apk add --no-cache -u python=2.7.12-r0 py-pip=8.1.2-r0 && \
    pip install supervisor==3.3.0
# Custom supervisor config
COPY .provision/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the correct ports
EXPOSE 80 443

# Add the project directory to /app
COPY . /app

# Change the working directory to /app
WORKDIR /app

# Install Python dependencies
RUN apk update && apk add -u linux-headers python3-dev gcc postgresql-dev musl-dev
RUN pip3 install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi && \
    pip3 install -r /app/requirements.txt

CMD ["/app/.provision/run.sh"]
