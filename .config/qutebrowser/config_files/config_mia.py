import dracula.draw
config.load_autoconfig(True)

# Dracula Theme
dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

c.window.title_format = "Qutebrowser - {current_title}" # title of the window
c.tabs.padding = {"top": 6, "bottom": 6, "right": 8, "left": 8} # padding of the tabs
c.auto_save.session = True # save session automatically
c.completion.quick = True # autocomplete if there is only one option
c.confirm_quit = ["downloads"] # confirm before quitting if downloads are running

config.set("colors.webpage.darkmode.enabled", True) # enable dark mode



# config.set('content.user_stylesheets', ['~/.config/qutebrowser/src/user.css'])

# Keybindings
config.bind('xx', 'config-cycle statusbar.show always never;; config-cycle tabs.show always never') # toggle statusbar and tabs
config.bind('W', 'hint links spawn mpv {hint-url}') # open video in mpv