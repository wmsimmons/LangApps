// spec.js
describe('Protractor Demo App', function() {
    it('should have a title', function() {
      browser.get('http://localhost:4200');
  
      expect(browser.getTitle()).toEqual('Papahana');
      browser.sleep(7000);
      var newElem = element(by.id("boxx"));
      newElem.sendKeys('Rapa Nui');
      browser.sleep(3000);
      element(by.id("buttony")).click();
      console.log(newElem.getText());
    
    });
  });