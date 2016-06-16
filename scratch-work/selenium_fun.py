#! python3
'''2048 launches the webpage (https://gabrielecirulli.github.io/2048/) and plays
 the game for you by sending automated left, up, right, down (in that order) commands
 and then restarts the process when the game ends.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def openBrowser(browser):
    site = 'https://gabrielecirulli.github.io/2048/' # defines the site were going to open
    browser.get(site) # Opens Firefox to the desired site
    print('This is game 1!') # Prints "This is game 1!" and shortly after the game begins
    #try:
    #    gameElem = browser.find_element_by_class_name('grid-container')
    #    print('Found <%s>' %(gameElem.tag_name))
    #except:
    #    print('<%s> was not found' % (gameElem.tag_name))

def keyClicks(browser):
    gameElem = browser.find_element_by_class_name('grid-container') # Finds the main game container to send commands
    gameRetry = browser.find_element_by_class_name('retry-button') # Finds the game retry button to press when it becomes visible
    #gameRestart = browser.find_element_by_class_name('restart-button')
    gameCounter = 1 # Creating a game counter so we know what # game is being played


    while (gameRetry.is_displayed()) == False: # While the game retry button is not visible, it carries out the following commands
        gameElem.send_keys(Keys.LEFT)
        gameElem.send_keys(Keys.UP)
        gameElem.send_keys(Keys.RIGHT)
        gameElem.send_keys(Keys.DOWN)
        print(gameRetry.is_displayed()) # This is only here to help me debug a problem "LINE TO BE DELETED"

        #try:
        #    print('Found <%s>' % (gameRetry.is_displayed()))
        #except:
        #    print('Not Found')
        if (gameRetry.is_displayed()) == True: # When the game retry button is visible, this clicks the button to restart the process
            print(gameRetry.is_displayed()) # This is only here to help me debug a problem "LINE TO BE DELETED"
            gameRetry.click() # Clicks the retry button
            gameCounter += 1 # Increments the game counter
            print('Game Retry Clicked! This is game %s!' %(gameCounter)) # Prints that the retry button has been pressed and what game is being played
            #try:
            #    gameRetry.click()
            #    gameCounter += 1
            #    print('Game Retry Clicked! This is game %s!' % (gameCounter))
            #except:
            #    if (gameRetry.is_displayed()) != False:
            #        gameRestart.click()
            #        gameCounter += 1
            #        print('New Game Button Clicked! This is game %s!' % (gameCounter))

def main():
    browser = webdriver.Firefox()
    openBrowser(browser)
    keyClicks(browser)

if __name__ == '__main__':
    main()