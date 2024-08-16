FROM python

WORKDIR /app

COPY requirements.txt /app/
RUN pip install streamlit
RUN pip install scikit-learn
RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib
RUN apt-get update && apt-get install -y gcc libffi-dev

COPY . /app

CMD ["streamlit","run","app.py"]