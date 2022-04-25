FROM jupyter/pyspartk-notebook:latest
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./file.pkl /deploy/
COPY ./run.py /deploy/
COPY ./helper.py /deploy/
COPY ./assembleModel.h5 /deploy/assembleModel.h5
COPY ./char_label_model.h5 /deploy/char_label_model.h5
COPY ./clf_model.h5 /deploy/clf_model.h5
ENTRYPOINT ["spark-submit","run.py"]