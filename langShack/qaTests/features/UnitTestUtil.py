from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.action_chains import ActionChains

def openPage(CurrentDriver, page, titleToVerify, assertion=None):
    CurrentDriver.get(page)
    title = CurrentDriver.title
    
    if assertion is True:
        assert titleToVerify in title

def close(CurrentDriver):
    CurrentDriver.close()

def writeElement(CurrentDriver, selectorType, elem, valueToWrite, assertion=None):
    # use id, xp, cs, 
    if selectorType == 'id':
        newElem = CurrentDriver.find_element_by_id(elem)

    if selectorType == 'xp':
        newElem = CurrentDriver.find_element_by_xpath(elem)

    if selectorType == 'cs':
        newElem = CurrentDriver.find_element_by_css_selector(elem)

    if selectorType == 'tag':
        newElem = CurrentDriver.find_element_by_tag_name(elem)

    if selectorType == 'name':
        newElem = CurrentDriver.find_element_by_name(elem)

    # send chars to the element defined
    newElem.sendKeys(valueToWrite)

    # only asserts if user turns assert on
    if assertion is True:
        assert valueToWrite in newElem
        if False:
            print("The value was not the same as what was written" + newElem)


def clickElement(CurrentDriver, selectorType, elem):
    # use id, xp, cs, 
    if selectorType == 'id':
        newElem = CurrentDriver.find_element_by_id(elem)

    if selectorType == 'xp':
        newElem = CurrentDriver.find_element_by_xpath(elem)

    if selectorType == 'cs':
        newElem = CurrentDriver.find_element_by_css_selector(elem)

    if selectorType == 'tag':
        newElem = CurrentDriver.find_element_by_tag_name(elem)

    if selectorType == 'name':
        newElem = CurrentDriver.find_element_by_name(elem)

    newElem.click()

    try:
        chains = ActionChains(CurrentDriver)
        chains.move_to_element(newElem)
        chains.click()
        chains.perform()
    except ValueError:
        print("Could not find element to click: " + newElem)

# def clickMultipleElements(CurrentDriver, selectorType, elemList):

# def writeMultipleElement(CurrentDriver, selectorType, elemList, listOfValues, assertion=None):
