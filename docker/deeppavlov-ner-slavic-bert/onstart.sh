# for vast
touch .no_auto_tmux

# drop last line with PS1
mv .bashrc .bashrc.back
cat .bashrc.back | grep -vE '^PS1' > .bashrc

python -m deeppavlov.deep riseapi Slavic-BERT-NER/ner_bert_slav.json
