
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
from PIL import Image
import os

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


photo_list = [{"name": "PRODUCT DEMO 1", 'img': 'photo1.jpg'},
              {"name": "PRODUCT DEMO 2", 'img': 'photo2.jpg'} ]


def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data['load']['products']


def save(bot):
    print("Save")
    if not bot.find( "save", matching=0.97, waiting_time=10000):
        not_found("save")
    bot.click()


def get_image(product_name):
    for photo in photo_list:
        if photo['name'] == product_name:
            return photo['img']

def click_produtos(bot, products):
    print("Click produtos")
    
    
    image_path = get_image(product_name=products['name'])

    if os.path.exists(image_path):
        try:
            print(f"Imagem válida encontrada: {image_path}")
        except Exception as e:
            print(f"Erro ao abrir a imagem {image_path}: {e}")
            return  

    if not bot.find( "select_picture", matching=0.97, waiting_time=10000):
        not_found("select_picture")
    bot.click()

    if not bot.find( "image_selected", matching=0.97, waiting_time=10000):
        not_found("image_selected")
    bot.click()
    bot.paste(image_path)
    
    if not bot.find( "close_bttn", matching=0.97, waiting_time=10000):
        not_found("close_bttn")
    bot.click()
    
    
    bot.wait(3000)

    save(bot)
   





def products_list(bot,products):
    bot.wait(5000)
    for product in products:
        if not bot.find( "click_produtos", matching=0.97, waiting_time=10000):
            not_found("click_produtos")
        bot.click()
    
        if not bot.find( "item_number", matching=0.97, waiting_time=10000):
            not_found("item_number")
        bot.click()
        bot.paste(product['item_number'])
            
        if not bot.find( "nome", matching=0.97, waiting_time=10000):
            not_found("nome")
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
            
            
        if not bot.find( "allowance", matching=0.97, waiting_time=10000):
            not_found("allowance")
        bot.click()
        bot.paste(product['allowance'])
            
        if not bot.find( "stock", matching=0.97, waiting_time=10000):
            not_found("stock")
        bot.click()
        bot.paste(product['stock'])
        
        print(product)
        click_produtos(bot,product)
        


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
    
    bot.wait(3000)

    products = read_json_file(r'resources\desafio03.json')
    
    products_list(bot, products)
    


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







