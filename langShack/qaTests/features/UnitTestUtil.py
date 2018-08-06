from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.action_chains import ActionChains

class Page:
    def __init__(self, url):
        self.url = url
        
    def openPage(self, currentDriver, titleToVerify, assertion=None):
        print(self.url)
        currentDriver.get(self.url)
        title = currentDriver.title
        
        if assertion is True:
            assert titleToVerify in title

    def close(self, currentDriver):
        currentDriver.close()

    def writeElement(self, currentDriver, selectorType, elem, valueToWrite, assertion=None):
        # use id, xp, cs, 
        if selectorType == 'id':
            newElem = currentDriver.find_element_by_id(elem)

        if selectorType == 'xp':
            newElem = currentDriver.find_element_by_xpath(elem)

        if selectorType == 'cs':
            newElem = currentDriver.find_element_by_css_selector(elem)

        if selectorType == 'tag':
            newElem = currentDriver.find_element_by_tag_name(elem)

        if selectorType == 'name':
            newElem = currentDriver.find_element_by_name(elem)

        # send chars to the element defined
        newElem.sendKeys(valueToWrite)

        # only asserts if user turns assert on
        if assertion is True:
            assert valueToWrite in newElem
            if False:
                print("The value was not the same as what was written" + newElem)


    def clickElement(self, currentDriver, selectorType, elem):
        # use id, xp, cs, 
        if selectorType == 'id':
            newElem = currentDriver.find_element_by_id(elem)

        if selectorType == 'xp':
            newElem = currentDriver.find_element_by_xpath(elem)

        if selectorType == 'cs':
            newElem = currentDriver.find_element_by_css_selector(elem)

        if selectorType == 'tag':
            newElem = currentDriver.find_element_by_tag_name(elem)

        if selectorType == 'name':
            newElem = currentDriver.find_element_by_name(elem)

        newElem.click()

        try:
            chains = ActionChains(currentDriver)
            chains.move_to_element(newElem)
            chains.click()
            chains.perform()
        except ValueError:
            print("Could not find element to click: " + newElem)

    # def clickMultipleElements(self, CurrentDriver, selectorType, elemList):

    # def writeMultipleElement(self, CurrentDriver, selectorType, elemList, listOfValues, assertion=None):
