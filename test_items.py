link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_for_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button=browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button, "Button doesn't exist on this page"