from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import close_browser

def test_case():
    start_browser()
    print("I am executing a TC 1")
    close_browser()

test_case()