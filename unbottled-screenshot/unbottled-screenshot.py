import asyncio
from pyppeteer import launch

async def take_screenshot(url, output_file):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot({'path': output_file})
    await browser.close()

async def main():
    websites = [
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-gommage-corps-gel-douche-abricot?view=product-bundle', 'output': 'duo-gommage-corps-gel-douche-abricot'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/pack-famille-deo?view=product-bundle', 'output': 'pack-famille-deo'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-de-deos-fleuri-cheri-menthe-ole?view=product-bundle', 'output': 'duo-de-deos-fleuri-cheri-menthe-ole'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/deodorant-menthe-ole?view=old', 'output': 'deodorant-menthe-ole'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/deodorant-fleuri-cheri?view=old', 'output': 'deodorant-fleuri-cheri'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/pack-gel-douche-abricot-intime-gommage?view=product-bundle', 'output': 'pack-gel-douche-abricot-intime-gommage'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-gommage-corps-gel-douche-avoine?view=product-bundle', 'output': 'duo-gommage-corps-gel-douche-avoine'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/pack-routine-visage-complete?view=product-bundle', 'output': 'pack-routine-visage-complete'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-douceur?view=product-bundle', 'output': 'duo-douceur'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/pack-gel-douche-soin-intime-rasage?view=product-bundle', 'output': 'pack-gel-douche-soin-intime-rasage'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/trio-gels-douche-avoine-abricot-bebe?view=product-bundle', 'output': 'trio-gels-douche-avoine-abricot-bebe'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/kit-dessai-shampoing-cheveux-gras-porte-savon-filet-malin?view=old', 'output': 'kit-dessai-shampoing-cheveux-gras-porte-savon-filet-malin'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/kit-dessai-shampoing-cuir-sensible-porte-savon-filet-malin?view=old', 'output': 'kit-dessai-shampoing-cuir-sensible-porte-savon-filet-malin'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/kit-dessai-shampoing-porte-savon-filet-malin?view=old', 'output': 'kit-dessai-shampoing-porte-savon-filet-malin'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-shampoing-cheveux-colores-apres-shampoing?view=old', 'output': 'duo-shampoing-cheveux-colores-apres-shampoing'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-shampoing-cuir-chevelu-sensible-apres-shampoing?view=product-bundle', 'output': 'duo-shampoing-cuir-chevelu-sensible-apres-shampoing'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/shampoing-solide-tout-nu-cuir-chevelu-sensible?view=old', 'output': 'shampoing-solide-tout-nu-cuir-chevelu-sensible'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/shampoing-solide-tout-nu-cheveux-colores?view=old', 'output': 'shampoing-solide-tout-nu-cheveux-colores'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-nettoyants-detox-super-doux?view=product-bundle', 'output': 'duo-nettoyants-detox-super-doux'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/nettoyant-masque-detox?view=old', 'output': 'nettoyant-masque-detox'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/savon-neutre-bebes-grands?view=old', 'output': 'savon-neutre-bebes-grands'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-de-bougies-vegetales-parfumees?view=product-bundle', 'output': 'duo-de-bougies-vegetales-parfumees'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/bougie-framboise-feve-tonka?view=old', 'output': 'bougie-framboise-feve-tonka'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/bougie-bergamote-romarin?view=old', 'output': 'bougie-bergamote-romarin'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/cotons-lavables?view=old', 'output': 'cotons-lavables'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/trio-demaquillant-nettoyant-gommage-visage?view=product-bundle', 'output': 'trio-demaquillant-nettoyant-gommage-visage'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-demaquillant-nettoyant-visage?view=product-bundle', 'output': 'duo-demaquillant-nettoyant-visage'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/demaquillant-efface-tout?view=old', 'output': 'demaquillant-efface-tout'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-gommages-visage-corps?view=product-bundle', 'output': 'duo-gommages-visage-corps'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/gommage-corps-peau-neuve?view=old', 'output': 'gommage-corps-peau-neuve'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/gommage-visage-peau-radieuse?view=old', 'output': 'gommage-visage-peau-radieuse'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/gels-douche-x2-soin-lavant-intime?view=old', 'output': 'gels-douche-x2-soin-lavant-intime'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-gel-douche-abricot-soin-lavant-intime?view=product-bundle', 'output': 'duo-gel-douche-abricot-soin-lavant-intime'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-gel-douche-avoine-soin-lavant-intime?view=product-bundle', 'output': 'duo-gel-douche-avoine-soin-lavant-intime'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/eco-trousse-x3?view=old', 'output': 'eco-trousse-x3'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/eco-trousse?view=old', 'output': 'eco-trousse'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-shampoing-cheveux-secs-apres-shampoing?view=product-bundle', 'output': 'duo-shampoing-cheveux-secs-apres-shampoing'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-shampoing-cheveux-gras-apres-shampoing?view=product-bundle', 'output': 'duo-shampoing-cheveux-gras-apres-shampoing'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-shampoing-tout-type-de-cheveux-apres-shampoing?view=product-bundle', 'output': 'duo-shampoing-tout-type-de-cheveux-apres-shampoing'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/pack-famille?view=product-bundle', 'output': 'pack-famille'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/pack-famille-nombreuse?view=product-bundle', 'output': 'pack-famille-nombreuse'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/apres-shampoing-solide-cheveux-soyeux?view=old', 'output': 'apres-shampoing-solide-cheveux-soyeux'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/porte-savon-en-gypse-naturel-terracotta?view=old', 'output': 'porte-savon-en-gypse-naturel-terracotta'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/porte-savon-en-gypse-naturel-ocre?view=old', 'output': 'porte-savon-en-gypse-naturel-ocre'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-de-savons-mains-surgras-et-leurs-porte-savons?view=product-bundle', 'output': 'duo-de-savons-mains-surgras-et-leurs-porte-savons'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-gels-douche-avoine-abricot?view=product-bundle', 'output': 'duo-gels-douche-avoine-abricot'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/gel-douche-sans-bouteille-abricot-karite?view=old', 'output': 'gel-douche-sans-bouteille-abricot-karite'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/shampoing-solide-tout-nu-cheveux-secs?view=old', 'output': 'shampoing-solide-tout-nu-cheveux-secs'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/shampoing-solide-tout-nu-cheveux-gras?view=old', 'output': 'shampoing-solide-tout-nu-cheveux-gras'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/la-recy-trousse?view=old', 'output': 'la-recy-trousse'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/duo-mini-corps-cheveux-et-la-recy-trousse?view=product-bundle', 'output': 'duo-mini-corps-cheveux-et-la-recy-trousse'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/porte-savon-magique-x3?view=old', 'output': 'porte-savon-magique-x3'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/trio-de-maxi-gels-douche?view=product-bundle', 'output': 'trio-de-maxi-gels-douche'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/maxi-savon-neutre-bebes-grands?view=old', 'output': 'maxi-savon-neutre-bebes-grands'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/porte-savon-magique?view=old', 'output': 'porte-savon-magique'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/maxi-gel-douche-abricot-karite?view=old', 'output': 'maxi-gel-douche-abricot-karite'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/maxi-gel-douche-avoine-amande?view=old', 'output': 'maxi-gel-douche-avoine-amande'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/sauve-savon?view=old', 'output': 'sauve-savon'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/gel-douche-sans-bouteille?view=old', 'output': 'gel-douche-sans-bouteille'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/nettoyant-visage-super-doux?view=old', 'output': 'nettoyant-visage-super-doux'},
    {'url': 'https://nm6ysqkf3ow3hrzv-32127058055.shopifypreview.com/products/shampoing-solide-tout-nu?view=old', 'output': 'shampoing-solide-tout-nu'}
]

    tasks = []
    for website in websites:
        url = website['url']
        output_file = website['output']
        tasks.append(take_screenshot(url, output_file))

    await asyncio.gather(*tasks)

asyncio.get_event_loop().run_until_complete(main())
