#!/bin/zsh

source ~/.zshrc

cd .. && avenv

cd 2dot2dot_2dot/

python editor.py & 
cd dot2dot_2dot/ && python app.py &
cd ../2dotdot_2dot/ && python app.py 
