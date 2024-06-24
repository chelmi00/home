alias sudo='sudo '
alias ld='ls -d */'
alias lf='ls *.?*'
alias ls='ls -p --color=auto'
alias la='ls -A'
alias agu='sudo apt update && sudo apt upgrade -y'
alias agf='sudo apt full-upgrade && sudo apt dist-upgrade'
alias agc='sudo apt clean && sudo apt autoremove -y'
alias clear_cache="sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches' && sudo sh -c 'echo 2 >/proc/sys/vm/drop_caches' && sudo sh -c 'echo 3 >/proc/sys/vm/drop_caches'"
