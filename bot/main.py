from modules import *

# Clear the screen for a fresh start
os.system('cls' if os.name == 'nt' else 'clear')

# Program will automatically close if required files are not found
# Handled in readData() function

# finalResult will contain complete object, along with status of completion
finalResult = list()

try:
    driver = initalizeDriver()
    driver.get("https://www.opensea.io")
    waitForLogin()
    # o contains objects, which are returned by readData() 
    for idx, o in enumerate(readData()):
        print("Currently attempting to visit the below url: ")
        print(idx + 1, o)
        url = o.get("url", None)
        price = o.get("price", None)
        if url and price:
            try:
                case = None
                error = False
                errorType = None

                print("Handles: ", driver.window_handles)
                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[1])
                
                driver.get(url)
                # Click on Sell button
                # or append 'sell' in the url
                sellBtnXpath = "//div[@class='OrderManager--cta-container']//a[contains(., 'Sell')]"
                lowerPriceBtnXpath = "//div[@class='OrderManager--cta-container']/button[@type='button' and contains(., 'Lower price')]"

                sellBtn = getElements(5, sellBtnXpath, driver)
                lowerPriceBtn = getElements(5, lowerPriceBtnXpath, driver)

                if sellBtn:
                    # selling case
                    print("Case: Sell")
                    case = "sell"
                    sellBtn = sellBtn[0] # first element is the sell button
                    sellBtn.click()
                    # Send price to input
                    getElement(5,"//input[@name='price']", driver).send_keys(price)
                    # Click on Complete listing button
                    # THIS HAS BEEN COMMENTED OUT SO WE DO NOT CONFIRM
                    getElement(5, "//button[@type='submit']", driver).click()

                    # testing code - for metamask
                    time.sleep(10)
                    handles = driver.window_handles
                    print(f"Handles are: {handles}")
                    if len(handles) > 1:
                        driver.switch_to.window(driver.window_handles[1])
                        getElement(10, "//button[contains(@class, 'request-signature__footer__sign-button')]", driver).click()
                        time.sleep(2)
                        driver.switch_to.window(driver.window_handles[0])
                    else:
                        print("Can not connect to Metamask.")
                        error = True
                        errorType = "Can not open Metamask."

                elif lowerPriceBtn:
                    # lowerPrice case
                    print("Case: Lower Price")
                    case = "lower price"
                    lowerPriceBtn = lowerPriceBtn[0] # first element is the lower price button
                    lowerPriceBtn.click()
                    currentAmount = None
                    AmountInput = getElement(5, "//input[@id='newAmount']", driver)
                    currentAmount = AmountInput.get_attribute('placeholder')
                    if currentAmount:
                        currentAmount = float( currentAmount )
                        priceAmount = float( price )
                        if currentAmount == priceAmount:
                            # print("same, igone")
                            error = True
                            errorType = "Price same, no need to lower."
                        if currentAmount < priceAmount:
                            # print("current amount less than price, ignore.")
                            error = True
                            errorType = "OpenSea amount is lesser than the amount you are trying to input."
                        if currentAmount > priceAmount:
                            # print("current amount higher than price.")
                            print("Current Amount: ", currentAmount)
                            print("Price: ", price)
                            AmountInput.clear()
                            AmountInput.send_keys(price)
                            ## Click Set New Price
                            getElement(5, "//button[@type='submit' and contains(., 'Set new price')]", driver).click()

                else:
                    print("Case: Neither sell case nor lower case.")
                    case = "neither"
                    error = True
                    errorType = "Neither sell case nor lower case."

            except:
                error = True
                errorType = traceback.format_exc()
                print(traceback.format_exc())
            finally:
                o.update({'status': 'OK' if not error else 'Not OK'})
                o.update({'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
                o.update({'case': case})
                o.update({'errorType': errorType})
                finalResult.append(o)
                print(f"Status: {'OK' if not error else 'Not OK'}")
                print(o)
        else:
            txt = f"Either url or price not found for row {idx+1}."
            color = "yellow"
            text = colored(txt, color)
            print(text)
            print("Thus, it is being skipped.")
        print("-------------------------------------------------")
    driver.quit()
except Exception as e:
    print("There was a general error.")
    print(f"Error details {traceback.format_exc()}.")
finally:
    # print(finalResult)
    # This needs to be saved to a file
    writeData(finalResult)
    print("Thankyou for using the bot, have a good day!")
    raise SystemExit