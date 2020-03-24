# for vast
touch .no_auto_tmux

# drop last line with PS1
mv .bashrc .bashrc.back
cat .bashrc.back | grep -vE '^PS1' > .bashrc

python -m deeppavlov.deep riseapi syntax_ru_syntagrus_bert
