from UnitTestUtil import Page
from selenium import webdriver

CurrentDriver = webdriver.Chrome()
page = "http://langshack.org"
langShack_title = "The LangShack: Xacaltlahtōlli"
langBlogPage = "langBlogPage"

firstPostLink = "body > div:nth-child(5) > div > a"
addComment = "body > h2 > a"
author = "id_author"
textboxy = "id_text"

def testTheBlogTest():
    ls_page = Page("http://langshack.org")
    print(ls_page)

    # navigates to the langShack homepage
    ls_page.openPage(CurrentDriver, langShack_title, assertion=True)

    ls_page.clickElement(CurrentDriver, "id", langBlogPage)
    ls_page.clickElement(CurrentDriver, "cs", firstPostLink)
    ls_page.clickElement(CurrentDriver, "cs", addComment)

    ls_page.writeElement(CurrentDriver, "name", author, "haha")
    ls_page.writeElement(CurrentDriver, "name", textboxy, "test comment")

    ls_page.close(CurrentDriver)
    
testTheBlogTest()