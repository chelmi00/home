# import setproctitle
import dracula.draw
from qutebrowser.api import interceptor
# setproctitle.setproctitle("qutebrowser")
config.load_autoconfig(True)
dracula.draw.blood(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})
#TECLADO
#unbinds
# config.unbind("+")
# config.unbind("-")
# config.unbind("=")
# config.unbind("O")
# config.unbind("T")
# config.unbind("th")
# config.unbind("tl")
# config.unbind("<Ctrl+p>")
# config.unbind("<ctrl+tab>")
# config.unbind("ZQ")
# config.unbind("ZZ")
# config.unbind("<ctrl+q>")
# config.unbind("d")
# config.unbind("<Alt+m>")
# config.unbind("h")
# config.unbind("j")
# config.unbind("k")
# config.unbind("l")
#binds
# config.bind("<Ctrl++>", "zoom-in")
# config.bind("<Ctrl+->", "zoom-out")
# config.bind("<Ctrl+0>", "zoom")
# config.bind("<Ctrl+o>","tab-give")
# config.bind("<Alt+LEFT>","back")
# config.bind("<Alt+RIGHT>","forward")
# config.bind("<Alt+UP>","tab-next")
# config.bind("<Alt+DOWN>","tab-prev")
# config.bind("<Ctrl+1>","tab-select 1")
# config.bind("<Ctrl+2>","tab-select 2")
# config.bind("<Ctrl+3>","tab-select 3")
# config.bind("<Ctrl+4>","tab-select 4")
# config.bind("<Ctrl+5>","tab-select 5")
# config.bind("<Ctrl+6>","tab-select 6")
# config.bind("<Ctrl+7>","tab-select 7")
# config.bind("<Ctrl+8>","tab-select 8")
# config.bind("<Ctrl+9>","tab-select 9")
# config.bind("<Ctrl+f>","hint all tab-fg")
# config.bind("<Ctrl+shift+f>","hint all tab-bg")
# config.bind("<Ctrl+Alt+f>", "hint all yank")
# config.bind("<Ctrl+w>","tab-close -p")
# config.bind("<Ctrl+p>","set-cmd-text -r :print --pdf ~/Descargas/current.pdf")
# config.bind("<Ctrl+h>","history")
# config.bind("o", "set-cmd-text -s :open")
# config.bind("<Shift+o>", "set-cmd-text -s :open -t")
# config.bind("<ctrl+tab>", "tab-next")
# config.bind("<ctrl+shift+tab>", "tab-prev")
# config.bind("<ctrl+q>", "wq")
# config.bind("<Ctrl+m>","tab-mute")
# config.bind("<Ctrl+Shift+t>","undo")
# The height of the completion, in px or as percentage of the window.
# c.completion.height = "20%"
# When to show the autocompletion window.
# Valid values:
#   - always: Whenever a completion is available.
#   - auto: Whenever a completion is requested.
#   - never: Never.
# c.completion.show = "always"
# Validate SSL handshakes.
# Valid values:
#   - true
#   - false
#   - ask
#c.content.ssl_strict = True
# The directory to save downloads to. If unset, a sensible os-specific
# default is used.
# c.downloads.location.directory = "~"
# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
# c.downloads.location.prompt = True
# Font used for the hints.
# c.fonts.hints = "15px 'Tlwg Mono'"
# Chars used for hint strings.
#c.hints.chars = "asdfghjklie"
# Leave insert mode if a non-editable element is clicked.
# c.input.insert_mode.auto_leave = True
# Automatically enter insert mode if an editable element is focused
# after loading the page.
# c.input.insert_mode.auto_load = True
# Show a scrollbar.
# c.scrolling.bar = "always"
# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# c.scrolling.smooth = False
# Open new tabs (middleclick/ctrl+click) in the background.
# c.tabs.background = True
# Behavior when the last tab is closed.
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = "close"
# '''
# # Padding around text for tabs
# c.tabs.padding = {
#     "left": 5,
#     "right": 5,
#     "top": 0,
#     "bottom": 1,
# }
# '''
# Which tab to select when the focused tab is removed.
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
# c.tabs.select_on_remove = "prev"
# Width of the progress indicator (0 to disable).
#c.tabs.width.indicator = 0
# Always restore open sites when qutebrowser is reopened.
c.auto_save.session = True
# Move on to the next part when there's only one possible completion
# left.
c.completion.quick = True
# Whether quitting the application requires a confirmation.
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ["downloads"]
# Value to send in the `Accept-Language` header.
c.content.headers.accept_language = "es-ES,en;q=0.8,fi;q=0.6"
# The proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don"t use any proxy
# c.content.proxy = "none"
# Validate SSL handshakes.
# Valid values:
#   - true
#   - false
#   - ask
#c.content.ssl_strict = True
# The editor (and arguments) to use for the `open-editor` command. `{}`
# gets replaced by the filename of the file to be edited.
# monospace = "15px 'Tlwg Mono'"
# # Font used in the completion categories.
# c.fonts.completion.category = f"bold {monospace}"
# # Font used in the completion widget.
# c.fonts.completion.entry = monospace
# # Font used for the debugging console.
# c.fonts.debug_console = monospace
# # Font used for the downloadbar.
# c.fonts.downloads = monospace
# # Font used in the keyhint widget.
# c.fonts.keyhint = monospace
# # Font used for error messages.
# c.fonts.messages.error = monospace
# # Font used for info messages.
# c.fonts.messages.info = monospace
# # Font used for warning messages.
# c.fonts.messages.warning = monospace
# # Font used for prompts.
# c.fonts.prompts = monospace
# # Font used in the statusbar.
# c.fonts.statusbar = monospace
# Font used in the tab bar.
#c.fonts.tabs = monospace
# Chars used for hint strings.
# c.hints.chars = "asdfghjklie"
# # Leave insert mode if a non-editable element is clicked.
# c.input.insert_mode.auto_leave = True
# # Automatically enter insert mode if an editable element is focused
# # after loading the page.
# c.input.insert_mode.auto_load = True
# # Enable smooth scrolling for web pages. Note smooth scrolling does not
# # work with the `:scroll-px` command.
# c.scrolling.smooth = True
# # Open new tabs (middleclick/ctrl+click) in the background.
# c.tabs.background = True
# # Behavior when the last tab is closed.
# # Valid values:
# #   - ignore: Don't do anything.
# #   - blank: Load a blank page.
# #   - startpage: Load the start page.
# #   - default-page: Load the default page.
# #   - close: Close the window.
# c.tabs.last_close = "close"
# # Padding around text for tabs
# c.tabs.padding = {
#     "left": 5,
#     "right": 5,
#     "top": 0,
#     "bottom": 1,
# }
# # Which tab to select when the focused tab is removed.
# # Valid values:
# #   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
# #   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
# #   - last-used: Select the previously selected tab.
# c.tabs.select_on_remove = "prev"
# Definitions of search engines which can be used via the address bar.
# Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
# `{}` placeholder. The placeholder will be replaced by the search term,
# use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# c.url.searchengines = {
# "DEFAULT":'https://duckduckgo.com/?q={}&hps=1&start=1&ia=web',
# "y" : "https://you.com/search?q={}&fromSearchBar=true",
# "g" : "https://www.google.es/search?q={}",
# "d" : "https://duckduckgo.com/?ia=web&q={}",
# "r" : "https://www.reddit.com/search?q={}",
# "d" : "https://dle.rae.es/{}",
# "w" : "https://en.wikipedia.org/wiki/{}",
# "m" : "https://www.openstreetmap.org/search?query={}",
# "gi" : "https://www.google.com/search?tbm=isch&q={}&tbs=imgo:1",
# "gh" : "https://github.com/search?q={}",
# "yt" : "https://www.youtube.com/results?search_query={}"
# }
# # The format to use for the window title. The following placeholders are
# defined:
#   * `{perc}`: The percentage as a string like `[10%]`.
#   * `{perc_raw}`: The raw percentage, e.g. `10`
#   * `{title}`: The title of the current web page
#   * `{title_sep}`: The string ` - ` if a title is set, empty otherwise.
#   * `{id}`: The internal window ID of this window.
#   * `{scroll_pos}`: The page scroll position.
#   * `{host}`: The host of the current web page.
#   * `{backend}`: Either ''webkit'' or ''webengine''
# #   * `{private}` : Indicates when private mode is enabled.
# c.window.title_format = "{private}{perc}{protocol}{title_sep}{current_title}"
# c.tabs.title.format="{perc}{audio}{current_title}"
# def filter_yt(info: interceptor.Request):
# 	url = info.request_url
# 	if (url.host() == 'www.youtube.com' and
# 			url.path() == '/get_video_info' and
# 			'&adformat=' in url.query()):
# 		info.block()
# interceptor.register(filter_yt)
# c.completion.timestamp_format="%d/%m/%Y - %H:%M:%S:%F"
# c.content.autoplay=True
# c.statusbar.widgets=["keypress","url","scroll"]
# c.content.pdfjs=False
# c.prompt.filebrowser=True
# c.downloads.remove_finished=5000
# c.content.fullscreen.window = True
# c.colors.webpage.darkmode.enabled= True
# # Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
# #   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
# #   - never: Don't accept cookies at all.
# config.set('content.cookies.accept', 'no-unknown-3rdparty', 'chrome-devtools://*')
# Setting dark mode
config.set("colors.webpage.darkmode.enabled", True)
# Enable JavaScript.
# # Type: Bool
# config.set('content.javascript.enabled', True, 'chrome-devtools://*')
# # Enable JavaScript.
# # Type: Bool
# config.set('content.javascript.enabled', True, 'devtools://*')
# # Enable JavaScript.
# # Type: Bool
# config.set('content.javascript.enabled', True, 'chrome://*/*')
# # Enable JavaScript.
# # Type: Bool
# config.set('content.javascript.enabled', True, 'qute://*/*')
# # Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
# #   - never: Don't accept cookies# Setting default page for when opening new tabs or new windows with
# # commands like :open -t and :open -w .
# c.url.default_page = 'https://start.duckduckgo.com/'
# c.url.start_pages = 'https://start.duckduckgo.com/'
# c.fonts.default_family='12 px "Tlwg Mono"'
# c.fonts.tabs.selected="15px 'Tlwg Mono'"
# c.fonts.tabs.unselected="12px 'Tlwg Mono'"
# c.fonts.prompts="12px 'Tlwg Mono'"
# c.fonts.web.family.sans_serif='"12px" "Tlwg Mono"'
# c.fonts.web.family.cursive="'12px''Tlwg Mono'"
# c.fonts.web.family.fantasy="'12px' 'Tlwg Mono'"
# c.fonts.web.family.serif="'12px' 'Tlwg Mono'"
# c.fonts.web.family.standard="'12px' 'Tlwg Mono'"
# # c.tabs.show="multiple"
# # c.editor.command = ["codium","{}"]
# # config.set('colors.webpage.darkmode.enabled', True)
# # c.completion.timestamp_format="%d/%m/%Y - %H:%M:%S:%F"
# # c.content.fullscreen.window = True
# # c.content.pdfjs=False
# # c.prompt.filebrowser=True
# # c.downloads.remove_finished=10000
# # config.set('content.javascript.can_access_clipboard', True)
# # config.set('colors.webpage.darkmode.enabled', True)



# # ## Background color of the completion widget category headers.
# # c.colors.completion.category.bg = "#1E1E1E"

# # ## Bottom border color of the completion widget category headers.
# # c.colors.completion.category.border.bottom = "#1E1E1E"

# # ## Top border color of the completion widget category headers.
# # c.colors.completion.category.border.top = "#608B4E"
# # c.colors.completion.category.border.bottom = "#608B4E"

# # ## Foreground color of completion widget category headers.
# # c.colors.completion.category.fg = "#608B4E"

# # ## Background color of the completion widget for even rows.
# # c.colors.completion.even.bg = "#1E1E1E"

# # ## Background color of the completion widget for odd rows.
# # c.colors.completion.odd.bg = "#1E1E1E"

# # ## Text color of the completion widget.
# # c.colors.completion.fg =  "#D4D4D4"

# # ## Background color of the selected completion item.
# # c.colors.completion.item.selected.bg = "#608B4E" #"#569CD6"

# # ## Bottom border color of the selected completion item.
# # c.colors.completion.item.selected.border.bottom = "#50DB00" # "#569CD6"

# # ## Top border color of the completion widget category headers.
# c.colors.completion.item.selected.border.top = "#50DB00" #"#569CD6"

# ## Foreground color of the selected completion item.
# c.colors.completion.item.selected.fg = "#000000" #"#1E1E1E"

# ## Foreground color of the matched text in the completion.
# c.colors.completion.match.fg = "#CE9178"

# ## Color of the scrollbar in completion view
# c.colors.completion.scrollbar.bg =  "#1E1E1E"

# ## Color of the scrollbar handle in completion view.
# c.colors.completion.scrollbar.fg = "#D4D4D4"

# ## Background color for the download bar.
# c.colors.downloads.bar.bg = '#608B4E'
# ## Background color for downloads with errors.
# c.colors.downloads.error.bg = "#1E1E1E"

# ## Foreground color for downloads with errors.
# c.colors.downloads.error.fg = "#F44747"

# ## Color gradient stop for download backgrounds.
# c.colors.downloads.stop.bg = "#1E1E1E"

# ## Color gradient interpolation system for download backgrounds.
# ## Type: ColorSystem
# ## Valid values:
# ##   - rgb: Interpolate in the RGB color system.
# ##   - hsv: Interpolate in the HSV color system.
# ##   - hsl: Interpolate in the HSL color system.
# ##   - none: Don't show a gradient.
# c.colors.downloads.system.bg = 'none'

# ## Background color for hints. Note that you can use a `rgba(...)` value
# ## for transparency.
# c.colors.hints.bg = "#009933"  #"#1E1E1E"

# ## Font color for hints.
# c.colors.hints.fg = "#D4D4D4"

# ## Hints
# c.hints.border = '1px solid ' + "#202020"

# ## Font color for the matched part of hints.
# c.colors.hints.match.fg = "#FF0000" #"#CE9178"
# ## Background color of the keyhint widget.
# c.colors.keyhint.bg = "#1E1E1E"

# ## Text color for the keyhint widget.
# c.colors.keyhint.fg = "#C586C0"

# ## Highlight color for keys to complete the current keychain.
# c.colors.keyhint.suffix.fg = "#303030"

# ## Background color of an error message.
# c.colors.messages.error.bg = "#1E1E1E"

# ## Border color of an error message.
# c.colors.messages.error.border = "#1E1E1E"

# ## Foreground color of an error message.
# c.colors.messages.error.fg = "#F44747"

# ## Background color of an info message.
# c.colors.messages.info.bg = "#1E1E1E"

# ## Border color of an info message.
# c.colors.messages.info.border = "#1E1E1E"

# ## Foreground color an info message.
# c.colors.messages.info.fg = "#569CD6"

# ## Background color of a warning message.
# c.colors.messages.warning.bg = "#1E1E1E"

# ## Border color of a warning message.
# c.colors.messages.warning.border = "#1E1E1E"

# ## Foreground color a warning message.
# c.colors.messages.warning.fg = "#DCDCAA"

# ## Background color for prompts.
# c.colors.prompts.bg = "#1E1E1E"

# # ## Border used around UI elements in prompts.
# c.colors.prompts.border = '1px solid ' + "#202020"

# ## Foreground color for prompts.
# c.colors.prompts.fg = 'white' #"#569CD6"

# ## Background color for the selected item in filename prompts.
# c.colors.prompts.selected.bg = "#303030"

# ## Background color of the statusbar in caret mode.
# c.colors.statusbar.caret.bg = "#1E1E1E"

# ## Foreground color of the statusbar in caret mode.
# c.colors.statusbar.caret.fg = "#CE9178"

# ## Background color of the statusbar in caret mode with a selection.
# c.colors.statusbar.caret.selection.bg = "#1E1E1E"

# ## Foreground color of the statusbar in caret mode with a selection.
# c.colors.statusbar.caret.selection.fg = "#CE9178"

# ## Background color of the statusbar in command mode.
# c.colors.statusbar.command.bg = "#1E1E1E"

# ## Foreground color of the statusbar in command mode.
# c.colors.statusbar.command.fg = "#D4D4D4"

# ## Background color of the statusbar in private browsing + command mode.
# c.colors.statusbar.command.private.bg = "#1E1E1E"

# ## Foreground color of the statusbar in private browsing + command mode.
# c.colors.statusbar.command.private.fg = "#C586C0"

# ## Background color of the statusbar in insert mode.
# c.colors.statusbar.insert.bg = "#68217A" #"#DCDCAA"

# ## Foreground color of the statusbar in insert mode.
# c.colors.statusbar.insert.fg = "#FFFFFF"  #"#1E1E1E"

# ## Background color of the statusbar.
# c.colors.statusbar.normal.bg = "#1E1E1E"

# ## Foreground color of the statusbar.
# c.colors.statusbar.normal.fg = "#D4D4D4"

# ## Background color of the statusbar in passthrough mode.
# c.colors.statusbar.passthrough.bg = "#1E1E1E"

# ## Foreground color of the statusbar in passthrough mode.
# c.colors.statusbar.passthrough.fg = "#CE9178"

# ## Background color of the statusbar in private browsing mode.
# c.colors.statusbar.private.bg = "#1E1E1E"

# ## Foreground color of the statusbar in private browsing mode.
# c.colors.statusbar.private.fg = "#C586C0"

# ## Background color of the progress bar.
# c.colors.statusbar.progress.bg = "#1E1E1E"

# ## Foreground color of the URL in the statusbar on error.
# c.colors.statusbar.url.error.fg = "#F44747"

# ## Default foreground color of the URL in the statusbar.
# c.colors.statusbar.url.fg = "#D4D4D4"

# ## Foreground color of the URL in the statusbar for hovered links.
# c.colors.statusbar.url.hover.fg = "#9CDCFE"

# ## Foreground color of the URL in the statusbar on successful load
# c.colors.statusbar.url.success.http.fg = "#FD7003" #"#608B4E"

# ## Foreground color of the URL in the statusbar on successful load
# c.colors.statusbar.url.success.https.fg = "#00FF00" #"#608B4E"

# ## Foreground color of the URL in the statusbar when there's a warning.
# c.colors.statusbar.url.warn.fg = "#DCDCAA"

# '''
# ## Status bar padding
# c.statusbar.padding = padding
# '''

# ## Background color of the tab bar.
# ## Type: QtColor
# c.colors.tabs.bar.bg = "#1E1E1E"

# ## Background color of unselected even tabs.
# ## Type: QtColor
# c.colors.tabs.even.bg = "#303030"
# c.colors.tabs.pinned.even.bg = "#303030"

# ## Foreground color of unselected even tabs.
# ## Type: QtColor
# c.colors.tabs.even.fg = "#A1A1A1"
# c.colors.tabs.pinned.even.fg = "#A1A1A1"

# ## Color for the tab indicator on errors.
# ## Type: QtColor
# c.colors.tabs.indicator.error = "#FF0000"

# ## Color gradient start for the tab indicator.
# ## Type: QtColor
# c.colors.tabs.indicator.start = "#FF0000" #"#CE9178"

# ## Color gradient end for the tab indicator.
# ## Type: QtColor
# c.colors.tabs.indicator.stop = "#00FF00" #"#608B4E"

# ## Color gradient interpolation system for the tab indicator.
# ## Type: ColorSystem
# ## Valid values:
# ##   - rgb: Interpolate in the RGB color system.
# ##   - hsv: Interpolate in the HSV color system.
# ##   - hsl: Interpolate in the HSL color system.
# ##   - none: Don't show a gradient.
# c.colors.tabs.indicator.system = 'none'

# ## Background color of unselected odd tabs.
# ## Type: QtColor
# c.colors.tabs.odd.bg = "#303030"
# c.colors.tabs.pinned.odd.bg = "#303030"

# ## Foreground color of unselected odd tabs.
# ## Type: QtColor
# c.colors.tabs.odd.fg = "#A1A1A1"
# c.colors.tabs.pinned.odd.fg = "#A1A1A1"

# # ## Background color of selected even tabs.
# # ## Type: QtColor
# c.colors.tabs.selected.even.bg = "gainsboro" #"#1E1E1E"

# # ## Foreground color of selected even tabs.
# # ## Type: QtColor
# c.colors.tabs.selected.even.fg = "#000000" #"#D4D4D4"

# # ## Background color of selected odd tabs.
# # ## Type: QtColor
# c.colors.tabs.selected.odd.bg = "gainsboro" # "#1E1E1E"

# # ## Foreground color of selected odd tabs.
# # ## Type: QtColor
# c.colors.tabs.selected.odd.fg = "#000000"  #"#D4D4D4"

# '''
# ## Tab padding
# c.tabs.padding = padding
# c.tabs.indicator.width = 1
# c.tabs.favicons.scale = 1
# '''

# ## Background color of context menu
# c.colors.contextmenu.menu.bg = "#1E1E1E"

# ## Foreground color of context menu
# c.colors.contextmenu.menu.fg = "#D4D4D4"

# ## Foreground color of disabled item in context menu
# c.colors.contextmenu.disabled.fg = "#424242"

# ## Background color of selected item in context menu
# c.colors.contextmenu.selected.bg = "#608B4E" # "#569CD6"

# ## Foreground color of selected item in context menu
# c.colors.contextmenu.selected.fg = "black" #"#1E1E1E"

# c.colors.downloads.bar.bg = 'gainsboro'
# c.colors.downloads.stop.bg = 'gainsboro'
# c.colors.downloads.stop.fg = '#000000'
# c.colors.downloads.start.bg= 'gainsboro'
# c.colors.downloads.start.fg= 'black'
# c.colors.statusbar.normal.fg = 'gainsboro'
