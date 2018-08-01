import UnitTestUtil
from selenium import webdriver

CurrentDriver = webdriver.Chrome()
page = "http://langshack.org"
langShack_title = "The LangShack: Xacaltlahtōlli"
langBlogPage = "langBlogPage"

firstPostLink = "body > div:nth-child(5) > div > a"
addComment = "body > h2 > a"
author = "id_author"
textboxy = "id_text"

# navigates to the langShack homepage
UnitTestUtil.openPage(CurrentDriver, page, langShack_title, assertion=True)

UnitTestUtil.clickElement(CurrentDriver, "id", langBlogPage)
UnitTestUtil.clickElement(CurrentDriver, "cs", firstPostLink)
UnitTestUtil.clickElement(CurrentDriver, "cs", addComment)

UnitTestUtil.writeElement(CurrentDriver, "name", author, "haha")
UnitTestUtil.writeElement(CurrentDriver, "name", textboxy, "test comment")

UnitTestUtil.close(CurrentDriver)