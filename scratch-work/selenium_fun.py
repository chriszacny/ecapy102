#! python3
'''2048 launches the webpage (https://gabrielecirulli.github.io/2048/) and plays
 the game for you by sending automated left, up, right, down (in that order) commands
 and then restarts the process when the game ends.'''

# TODO Have it solve the game using a graph model
# TODO Mention closing references to firefox

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def openBrowser(browser):
    site = 'https://gabrielecirulli.github.io/2048/' # defines the site were going to open
    browser.get(site) # Opens Firefox to the desired site
    print('This is game 1!') # Prints "This is game 1!" and shortly after the game begins


def keyClicks(browser):
    gameElem = browser.find_element_by_class_name('grid-container') # Finds the main game container to send commands
    gameRetry = browser.find_element_by_class_name('retry-button') # Finds the game retry button to press when it becomes visible
    gameCounter = 1 # Creating a game counter so we know what # game is being played

    while True:
        if not gameRetry.is_displayed():
            gameElem.send_keys(Keys.LEFT)
            #print('Left')
            gameElem.send_keys(Keys.UP)
            #print('Up')
            gameElem.send_keys(Keys.RIGHT)
            #print('Right')
            gameElem.send_keys(Keys.DOWN)
            #print('Down')
        else:
            gameRetry.click() # Clicks the retry button
            gameCounter += 1 # Increments the game counter
            print('Game Retry Clicked! This is game %s!' %(gameCounter)) # Prints that the retry button has been pressed and what game is being played

    print('Run complete!')


def main():
    browser = webdriver.Firefox()
    openBrowser(browser)
    keyClicks(browser)


if __name__ == '__main__':
    main()