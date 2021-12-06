from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn")


class BasketPageLocators:
    EMPTY_BASKET = (By.ID, "content_inner")
    NOT_EMPTY_BASKET = (By.CLASS_NAME, "basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDING_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
