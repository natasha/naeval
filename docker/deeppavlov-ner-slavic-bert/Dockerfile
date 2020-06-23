FROM deeppavlov/base-gpu:0.3.0

WORKDIR /root
ENV DP_ROOT_PATH=/base

RUN git clone https://github.com/deepmipt/Slavic-BERT-NER.git
RUN python -m deeppavlov install Slavic-BERT-NER/ner_bert_slav.json
RUN python -m deeppavlov download Slavic-BERT-NER/ner_bert_slav.json

COPY onstart.sh .

CMD ["/bin/bash", "onstart.sh"]
