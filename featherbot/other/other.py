class Other:
    def __init__(self, core):
        self.core = core

    def font_size(self):
        self.font_size = self.core.console_script("return document.fonts.size")

    def age(self):
        last_modified = self.core.console_script("return document.lastModified")
        self.age = last_modified

    def cookies(self):
        self.cookies = len(self.driver.get_cookies())
        # Can get cookie expirations

    def scripts(self):
        dict_scripts = self.core.console_script("return document.scripts")
        self.scripts = len(dict_scripts)
        # Can get script id's

"""

document.cookie

    __gads=ID=58006155d44dfe86-22abb1a0f6d3004e:T=1654530350:RT=1654530350:S=ALNI_Ma-E1nEaViWS7KT0S1QJ_jaEDVtTw;
    _ga_47NF071KRF=GS1.1.1654678132.5.0.1654678132.0;
    _gid=GA1.2.787097665.1656577299;
    _ga_259KYFFZ2M=GS1.1.1656577299.1.0.1656577299.0;
    _ga=GA1.1.320167724.1654530350;
    _ga_E21J8SEBLX=GS1.1.1656577299.1.0.1656577299.0;
    __gpi=UID=0000085a05e88192:T=1654530350:RT=1656577300:S=ALNI_MYMq6zoBPhpsb6Qf3nTsTPWQchyTw

document.fonts

    size: 139

document.forms

    form.search-form
    length: 1

document.images

    loading: "lazy"
    alt: ""

document.lastModified

    '06/30/2022 13:29:52'

document.links
document.scripts
document.styleSheets
document.title
"""