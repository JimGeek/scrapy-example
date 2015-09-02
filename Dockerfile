FROM ubuntu:14.04
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

# Install required package for ubuntu
RUN apt-get update && apt-get install -y python-dev libxml2 libxml2-dev libxml2-dev libxslt1-dev python-lxml libffi-dev git python-pip libssl-dev

# Clone the repository
RUN git clone https://github.com/JimGeek/scrapy-example.git

# change directory to inner folder
WORKDIR scrapy-example

# Install the requirements
RUN pip install -r requirements.txt

# Expose port 6800 to outside world
EXPOSE 6800

# Run the scrapyd deamon
CMD ["/usr/local/bin/scrapyd"]
