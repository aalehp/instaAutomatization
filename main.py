import time
from selenium import webdriver

class Instabot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path=r"C:\dChrome\chromedriver_83.exe")
        self.driver.get("https://www.instagram.com")
        time.sleep(2)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)

        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()

        time.sleep(4)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Ahora no')]") \
            .click()

        time.sleep(2)

        '''Clic En Boton Buscar Personas'''
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a") \
            .click()

        time.sleep(4)

        '''Clic En Primer Imagen de Lista'''
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[2]/div/div[1]/div[2]/div/a") \
            .click()

        time.sleep(2)

        '''Click En Like'''
        self.driver.find_element_by_xpath(
            "/ html / body / div[4] / div[2] / div / article / div[2] / section[1] / span[1] / button") \
            .click()
        time.sleep(2)

        '''Clic En Flecha Sigiente Foto'''
        i = 1

        while i < 5:
            if i < 2:
                self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a") \
                    .click()
                time.sleep(2)
                i = i + 1

            elif i > 1:
                self.driver.find_element_by_xpath("//html/body/div[4]/div[1]/div/div/a[2]") \
                    .click()
                time.sleep(2)
                i = i + 1

            '''Click En Like'''
            self.driver.find_element_by_xpath(
                "/ html / body / div[4] / div[2] / div / article / div[2] / section[1] / span[1] / button") \
                .click()
            time.sleep(1)

        '''Clic En X Para Cerrar Imagen'''
        self.driver.find_element_by_xpath("/ html / body / div[4] / div[3] / button") \
            .click()

        time.sleep(1)

        '''Clic En Imagen De Boton Instagram Para Regresar A Inicio'''
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[1]/a/div/div/img") \
            .click()

        time.sleep(2)


Instabot('username', 'Contraseña')
