#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

colors() {
	local fgc bgc vals seq0

	printf "Color escapes are %s\n" '\e[${value};...;${value}m'
	printf "Values 30..37 are \e[33mforeground colors\e[m\n"
	printf "Values 40..47 are \e[43mbackground colors\e[m\n"
	printf "Value  1 gives a  \e[1mbold-faced look\e[m\n\n"

	# foreground colors
	for fgc in {30..37}; do
		# background colors
		for bgc in {40..47}; do
			fgc=${fgc#37} # white
			bgc=${bgc#40} # black

			vals="${fgc:+$fgc;}${bgc}"
			vals=${vals%%;}

			seq0="${vals:+\e[${vals}m}"
			printf "  %-9s" "${seq0:-(default)}"
			printf " ${seq0}TEXT\e[m"
			printf " \e[${vals:+${vals+$vals;}}1mBOLD\e[m"
		done
		echo; echo
	done
}

[ -r /usr/share/bash-completion/bash_completion ] && . /usr/share/bash-completion/bash_completion

# Change the window title of X terminals
case ${TERM} in
	xterm*|rxvt*|Eterm*|aterm|kterm|gnome*|interix|konsole*)
		PROMPT_COMMAND='echo -ne "\033]0;${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\007"'
		;;
	screen*)
		PROMPT_COMMAND='echo -ne "\033_${USER}@${HOSTNAME%%.*}:${PWD/#$HOME/\~}\033\\"'
		;;
esac

use_color=true

# Set colorful PS1 only on colorful terminals.
# dircolors --print-database uses its own built-in database
# instead of using /etc/DIR_COLORS.  Try to use the external file
# first to take advantage of user additions.  Use internal bash
# globbing instead of external grep binary.
safe_term=${TERM//[^[:alnum:]]/?}   # sanitize TERM
match_lhs=""
[[ -f ~/.dir_colors   ]] && match_lhs="${match_lhs}$(<~/.dir_colors)"
[[ -f /etc/DIR_COLORS ]] && match_lhs="${match_lhs}$(</etc/DIR_COLORS)"
[[ -z ${match_lhs}    ]] \
	&& type -P dircolors >/dev/null \
	&& match_lhs=$(dircolors --print-database)
[[ $'\n'${match_lhs} == *$'\n'"TERM "${safe_term}* ]] && use_color=true

if ${use_color} ; then
	# Enable colors for ls, etc.  Prefer ~/.dir_colors #64489
	if type -P dircolors >/dev/null ; then
		if [[ -f ~/.dir_colors ]] ; then
			eval $(dircolors -b ~/.dir_colors)
		elif [[ -f /etc/DIR_COLORS ]] ; then
			eval $(dircolors -b /etc/DIR_COLORS)
		fi
	fi

	if [[ ${EUID} == 0 ]] ; then
		PS1='\[\033[01;31m\][\h\[\033[01;36m\] \W\[\033[01;31m\]]\$\[\033[00m\] '
	else
		PS1='\[\033[01;32m\][\u@\h\[\033[01;37m\] \W\[\033[01;32m\]]\$\[\033[00m\] '
	fi

	alias ls='ls --color=auto'
	alias grep='grep --colour=auto'
	alias egrep='egrep --colour=auto'
	alias fgrep='fgrep --colour=auto'
else
	if [[ ${EUID} == 0 ]] ; then
		# show root@ when we don't have colors
		PS1='\u@\h \W \$ '
	else
		PS1='\u@\h \w \$ '
	fi
fi

unset use_color safe_term match_lhs sh

#alias cp="cp -i"                          # confirm before overwriting something
#alias df='df -h'                          # human-readable sizes
#alias free='free -m'                      # show sizes in MB
#alias np='nano -w PKGBUILD'
#alias more=less

xhost +local:root > /dev/null 2>&1

# Bash won't get SIGWINCH if another process is in the foreground.
# Enable checkwinsize so that bash will check the terminal size when
# it regains control.  #65623
# http://cnswww.cns.cwru.edu/~chet/bash/FAQ (E11)
shopt -s checkwinsize

shopt -s expand_aliases

# export QT_SELECT=4

# Enable history appending instead of overwriting.  #139609
shopt -s histappend

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

cl() { cd "$1" && ls -a; }
copy() { xclip -sel c < "$1"; }
buscar() { grep -IrnwH . -e "$1"; }
# aex - archive extractor
# usage: aex <file>
aex () {
	if [ -f $1 ] ; then
                case $1 in
                        *.tar.bz2)   tar xjf $1   ;;
                        *.tar.gz)    tar xzf $1   ;;
                        *.bz2)       bunzip2 $1   ;;
                        *.rar)       unrar x $1     ;;
                        *.gz)        gunzip $1    ;;
                        *.tar)       tar xf $1    ;;
                        *.tbz2)      tar xjf $1   ;;
                        *.tgz)       tar xzf $1   ;;
                        *.zip)       unzip $1     ;;
                        *.Z)         uncompress $1;;
                        *.7z)        7z x $1      ;;
                        *)           echo "'$1' cannot be extracted via ex()" ;;
                esac
        else
                echo "'$1' is not a valid file"
        fi
}
# acompress f1 f2 f3 ...
acompress () {
    echo "Choose a compression method:"
    echo "1) tar.bz2"
    echo "2) tar.gz"
    echo "3) bz2"
    echo "4) rar"
    echo "5) gz"
    echo "6) tar"
    echo "7) tbz2"
    echo "8) tgz"
    echo "9) zip"
    echo "10) 7z"
    read -p "Method: " method

	# Generar un nombre de archivo aleatorio
	timestamp=$(date +%H:%M:%S.%d-%m-%Y)

    case $method in
        1) extension="tar.bz2"; tar cjf ${timestamp}.${extension} "$@" ;;
        2) extension="tar.gz"; tar czf ${timestamp}.${extension} "$@" ;;
        3) extension="bz2"; for file in "$@"; do bzip2 -k -c "$file" > "${timestamp}_${file}.${extension}"; done ;;
        4) extension="rar"; rar a ${timestamp}.${extension} "$@" ;;
        5) extension="gz"; for file in "$@"; do gzip -c "$file" > "${timestamp}_${file}.${extension}"; done ;;
        6) extension="tar"; tar cf ${timestamp}.${extension} "$@" ;;
        7) extension="tbz2"; tar cjf ${timestamp}.${extension} "$@" ;;
        8) extension="tgz"; tar czf ${timestamp}.${extension} "$@" ;;
        9) extension="zip"; zip ${timestamp}.${extension} "$@" ;;
        10) extension="7z"; 7z a ${timestamp}.${extension} "$@" ;;
        *) echo "Not a valid compression method"; exit 1 ;;
    esac

    echo "File compressed: ${timestamp}.${extension}"
}

export QT_QPA_PLATFORMTHEME=qt5ct
export GTK_THEME=Papirus-Dark-Maia
export XCURSOR_THEME=Maia
export XDG_MENU_PREFIX=plasma-
export EDITOR=/usr/bin/vim
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
# fix "xdg-open fork-bomb" export your preferred browser from here
export BROWSER=/usr/bin/qutebrowser

# Bitwarden Data
export BW_CLIENTID="user.5474947a-59d6-4b15-b406-b046009041c5"
export BW_CLIENTSECRET="OJrFFCTLxxe7NF6oDs91ki66qacFO9"
export BW_SESSION="PKBJ8Qf9i3jZw52toZty2wXhzZg53RFOzGKeQBZBBtTQrrsHkVKj31jrAo8BlIxUsYvl5PLQ2OFVnyNQ479Ucw=="