alias ls='ls -p --color=auto'
alias grep='grep --colour=auto'
alias egrep='egrep --colour=auto'
alias fgrep='fgrep --colour=auto'

alias mv='mv -i'	# confirm before overwriting something
alias cp='cp -i'	# confirm before overwriting something
alias df='df -h'	# human-readable sizes
alias free='free -m'	# show sizes in MB

alias pacman_ar='sudo pacman -Rcs $(pacman -Qdtg)'

alias urgent_sim='wmctrl -r :SELECT: -b add,demands_attention'

alias v='vim'