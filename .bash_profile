#
# ~/.bash_profile
#

eval "$(thefuck --alias)"

# ex - archive extractor
# usage: ex <file>
ex () {
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

cl() {
	cd "$@" && ls -A
}

copy() {
	xclip -sel c < "$@"
}

git_kde() {
	git add .config/dolphinrc .config/kate .config/konsolerc .local/share/dolphin .local/share/kate .local/share/konsole
	git commit -m "Minor KDE changes"
}