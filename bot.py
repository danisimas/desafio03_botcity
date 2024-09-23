"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data['load']['products']

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    bot.execute(r"C:\Program Files\Fakturama2\Fakturama.exe")

    bot.maximize_window()
    
    bot.wait(6000)

    products = read_json_file(r'resources\desafio03.json')
    
    if not bot.find( "click_produto", matching=0.97, waiting_time=10000):
        not_found("click_produto")
    bot.click()
    
    
    bot.wait(5000)
    
    
    for product in products:
        if not bot.find( "item_number", matching=0.97, waiting_time=10000):
            not_found("item_number")
        bot.click()
        bot.paste(product['item_number])
   

        if not bot.find( "name", matching=0.97, waiting_time=10000):
            not_found("name")
        bot.click()
        bot.paste(product['name'])
        
        if not bot.find( "category", matching=0.97, waiting_time=10000):
            not_found("category")
        bot.click()
        bot.paste(product['category'])
        
        if not bot.find( "gtin", matching=0.97, waiting_time=10000):
            not_found("gtin")
        bot.click()
        bot.paste(product['gtin'])
        
        if not bot.find( "supplier_code", matching=0.97, waiting_time=10000):
            not_found("supplier_code")
        bot.click()
        bot.paste(product['supplier_code'])
        
        if not bot.find( "description", matching=0.97, waiting_time=10000):
            not_found("description")
        bot.click()
        bot.paste(product['description'])
        
        if not bot.find( "price", matching=0.97, waiting_time=10000):
            not_found("price")
        bot.click()
        bot.paste(product['price'])
        
        if not bot.find( "cost", matching=0.97, waiting_time=10000):
            not_found("cost")
        bot.click()
        bot.paste(product['cost'])
        
        
        
        # bot.paste(product['allowance'])
        
        
        
       
        # bot.paste(product['stock'])
        

    


    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()




