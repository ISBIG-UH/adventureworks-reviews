import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
from generate_stores import tech_stores, clothing_stores
from tqdm import tqdm


tech_products = [
"TechPro Laptop AB-1234","HyperTech Monitor XY-9876","NeoCompute SSD QW-4567","ElectroMax Keyboard ZT-3456",
"CyberWare Mouse MN-2345","ComputeX Printer GH-5678","TechPro Router JK-6789","HyperTech Webcam LP-1234",
"NeoCompute Laptop QR-4321","ElectroMax Desktop ST-8765","CyberWare Monitor UV-3456","ComputeX Headset WX-7890",
"TechPro SSD YZ-2345","HyperTech Keyboard AB-5678","NeoCompute Mouse CD-6789","ElectroMax Printer EF-1234",
"CyberWare Router GH-4321","ComputeX Webcam IJ-8765","TechPro Laptop KL-3456","HyperTech Monitor MN-7890",
"NeoCompute SSD OP-2345","ElectroMax Keyboard QR-5678","CyberWare Mouse ST-6789","ComputeX Printer UV-1234",
"TechPro Router WX-4321","HyperTech Webcam YZ-8765","NeoCompute Laptop AB-3456","ElectroMax Desktop CD-7890",
"CyberWare Monitor EF-2345","ComputeX Headset GH-5678","TechPro SSD IJ-6789","HyperTech Keyboard KL-1234",
"NeoCompute Mouse MN-4321","ElectroMax Printer OP-8765","CyberWare Router QR-3456","ComputeX Webcam ST-7890",
"TechPro Laptop UV-2345","HyperTech Monitor WX-5678","NeoCompute SSD YZ-6789","ElectroMax Keyboard AB-1234",
"CyberWare Mouse CD-4321","ComputeX Printer EF-8765","TechPro Router GH-3456","HyperTech Webcam IJ-7890",
"NeoCompute Laptop KL-2345","ElectroMax Desktop MN-5678","CyberWare Monitor OP-6789","ComputeX Headset QR-1234",
"TechPro SSD ST-4321","HyperTech Keyboard UV-8765","NeoCompute Mouse WX-3456","ElectroMax Printer YZ-7890",
"CyberWare Router AB-2345","ComputeX Webcam CD-5678","TechPro Laptop EF-6789","HyperTech Monitor GH-1234",
"NeoCompute SSD IJ-4321","ElectroMax Keyboard KL-8765","CyberWare Mouse MN-3456","ComputeX Printer OP-7890",
"TechPro Router QR-2345","HyperTech Webcam ST-5678","NeoCompute Laptop UV-6789","ElectroMax Desktop WX-1234",
"CyberWare Monitor YZ-4321","ComputeX Headset AB-8765","TechPro SSD CD-3456","HyperTech Keyboard EF-7890",
"NeoCompute Mouse GH-2345","ElectroMax Printer IJ-5678","CyberWare Router KL-6789","ComputeX Webcam MN-1234",
"TechPro Laptop OP-4321","HyperTech Monitor QR-8765","NeoCompute SSD ST-3456","ElectroMax Keyboard UV-7890",
"CyberWare Mouse WX-2345","ComputeX Printer YZ-5678","TechPro Router AB-6789","HyperTech Webcam CD-1234",
"NeoCompute Laptop EF-4321","ElectroMax Desktop GH-8765","CyberWare Monitor IJ-3456","ComputeX Headset KL-7890",
"TechPro SSD MN-2345","HyperTech Keyboard OP-5678","NeoCompute Mouse QR-6789","ElectroMax Printer ST-1234",
"CyberWare Router UV-4321","ComputeX Webcam WX-8765","TechPro Laptop YZ-3456","HyperTech Monitor AB-7890",
"NeoCompute SSD CD-2345","ElectroMax Keyboard EF-5678","CyberWare Mouse GH-6789","ComputeX Printer IJ-1234",
"TechPro Router KL-4321","HyperTech Webcam MN-8765","NeoCompute Laptop OP-3456","ElectroMax Desktop QR-7890",
"CyberWare Monitor ST-2345","ComputeX Headset UV-5678","TechPro SSD WX-6789","HyperTech Keyboard YZ-1234",
"NeoCompute Mouse AB-4321","ElectroMax Printer CD-8765","CyberWare Router EF-3456","ComputeX Webcam GH-7890",
"TechPro Laptop IJ-2345","HyperTech Monitor KL-5678","NeoCompute SSD MN-6789","ElectroMax Keyboard OP-1234",
"CyberWare Mouse QR-4321","ComputeX Printer ST-8765","TechPro Router UV-3456","HyperTech Webcam WX-7890",
"NeoCompute Laptop YZ-2345","ElectroMax Desktop AB-5678","CyberWare Monitor CD-6789","ComputeX Headset EF-1234",
"TechPro SSD GH-4321","HyperTech Keyboard IJ-8765","NeoCompute Mouse KL-3456","ElectroMax Printer MN-7890",
"CyberWare Router OP-2345","ComputeX Webcam QR-5678","TechPro Laptop ST-6789","HyperTech Monitor UV-1234",
"NeoCompute SSD WX-4321","ElectroMax Keyboard YZ-8765","CyberWare Mouse AB-3456","ComputeX Printer CD-7890",
"TechPro Router EF-2345","HyperTech Webcam GH-5678","NeoCompute Laptop IJ-6789","ElectroMax Desktop KL-1234",
"CyberWare Monitor MN-4321","ComputeX Headset OP-8765","TechPro SSD QR-3456","HyperTech Keyboard ST-7890",
"NeoCompute Mouse UV-2345","ElectroMax Printer WX-5678","CyberWare Router YZ-6789","ComputeX Webcam AB-1234",
"TechPro Laptop CD-4321","HyperTech Monitor EF-8765","NeoCompute SSD GH-3456","ElectroMax Keyboard IJ-7890",
"CyberWare Mouse KL-2345","ComputeX Printer MN-5678","TechPro Router OP-6789","HyperTech Webcam QR-1234",
"NeoCompute Laptop ST-4321","ElectroMax Desktop UV-8765","CyberWare Monitor WX-3456","ComputeX Headset YZ-7890",
"TechPro SSD AB-2345","HyperTech Keyboard CD-5678","NeoCompute Mouse EF-6789","ElectroMax Printer GH-1234",
"CyberWare Router IJ-4321","ComputeX Webcam KL-8765","TechPro Laptop MN-3456","HyperTech Monitor OP-7890",
"NeoCompute SSD QR-2345","ElectroMax Keyboard ST-5678","CyberWare Mouse UV-6789","ComputeX Printer WX-1234",
"TechPro Router YZ-4321","HyperTech Webcam AB-8765","NeoCompute Laptop CD-3456","ElectroMax Desktop EF-7890",
"CyberWare Monitor GH-2345","ComputeX Headset IJ-5678","TechPro SSD KL-6789","HyperTech Keyboard MN-1234",
"NeoCompute Mouse OP-4321","ElectroMax Printer QR-8765","CyberWare Router ST-3456","ComputeX Webcam UV-7890",
"TechPro Laptop WX-2345","HyperTech Monitor YZ-5678","NeoCompute SSD AB-6789","ElectroMax Keyboard CD-1234",
"CyberWare Mouse EF-4321","ComputeX Printer GH-8765","TechPro Router IJ-3456","HyperTech Webcam KL-7890",
"NeoCompute Laptop MN-2345","ElectroMax Desktop OP-5678","CyberWare Monitor QR-6789","ComputeX Headset ST-1234",
"TechPro SSD UV-4321","HyperTech Keyboard WX-8765","NeoCompute Mouse YZ-3456","ElectroMax Printer AB-7890",
"CyberWare Router CD-2345","ComputeX Webcam EF-5678","TechPro Laptop GH-6789","HyperTech Monitor IJ-1234",
"NeoCompute SSD KL-4321","ElectroMax Keyboard MN-8765","CyberWare Mouse OP-3456","ComputeX Printer QR-7890",
"TechPro Router ST-2345","HyperTech Webcam UV-5678","NeoCompute Laptop WX-6789","ElectroMax Desktop YZ-1234",
"CyberWare Monitor AB-4321","ComputeX Headset CD-8765","TechPro SSD EF-3456","HyperTech Keyboard GH-7890",
"NeoCompute Mouse IJ-2345","ElectroMax Printer KL-5678","CyberWare Router MN-6789","ComputeX Webcam OP-1234"
]

clothing_products = [
"Classic Cotton T-Shirt","Slim Fit Jeans","Leather Jacket","Hooded Sweatshirt","Crew Neck Sweater",
"Casual Polo Shirt","Denim Shorts","Chino Pants","Striped Long Sleeve Shirt","Graphic Tee",
"Floral Summer Dress","Maxi Dress","Pleated Skirt","A-Line Skirt","Button-Up Shirt",
"V-Neck Sweater","Wool Coat","Puffer Jacket","Trench Coat","Bomber Jacket",
"Leather Boots","Canvas Sneakers","Running Shoes","Loafers","Sandals",
"Silk Blouse","Chiffon Top","Tank Top","Ribbed Turtleneck","Cropped Hoodie",
"Track Pants","Joggers","Cargo Pants","Leggings","Yoga Pants",
"Windbreaker Jacket","Raincoat","Denim Jacket","Cardigan Sweater","Peacoat",
"Faux Fur Coat","Blazer","Business Suit Jacket","Dress Pants","Slim Fit Shorts",
"Striped Socks","Ankle Socks","Crew Socks","Knee-High Socks","Sports Socks",
"Beanie Hat","Baseball Cap","Fedora","Sun Hat","Wool Scarf",
"Leather Belt","Canvas Belt","Crossbody Bag","Tote Bag","Backpack",
"Leather Gloves","Knitted Gloves","Sports Watch","Analog Watch","Digital Watch",
"Summer Romper","Playsuit","Denim Overalls","Jumpsuit","Kimono Cardigan",
"Ripped Jeans","High Waist Jeans","Bootcut Jeans","Skinny Jeans","Mom Jeans",
"Polo Dress","Sweatshirt Dress","Tunic Dress","Wrap Dress","Shirt Dress",
"Peasant Blouse","Off-Shoulder Top","Halter Top","Bandeau Top","Crop Top",
"Track Jacket","Fleece Jacket","Softshell Jacket","Down Jacket","Hiking Jacket",
"Slip-On Sneakers","High-Top Sneakers","Running Trainers","Casual Loafers","Dress Shoes",
"Espadrilles","Flip Flops","Chelsea Boots","Combat Boots","Ankle Boots",
"Silk Scarf","Cotton Scarf","Wool Hat","Bucket Hat","Headband",
"Leather Wallet","Clutch Bag","Hobo Bag","Messenger Bag","Mini Backpack",
"Leg Warmers","Fingerless Gloves","Leather Jacket with Zipper","Denim Shirt Jacket","Corduroy Jacket",
"Stretch Dress Pants","Pleated Trousers","Cargo Shorts","Bermuda Shorts","Skater Skirt",
"Tie-Dye T-Shirt","Graphic Hoodie","Embroidered Sweatshirt","Patchwork Denim","Faux Leather Pants",
"Chino Shorts","Button-Front Skirt","High-Low Dress","Midi Dress","Mini Dress",
"Velvet Blazer","Sequined Top","Satin Blouse","Ruffled Shirt","Pleated Top",
"Track Suit Set","Matching Hoodie Set","Pajama Set","Nightgown","Robe",
"Winter Coat","Down Vest","Wool Blazer","Corduroy Pants","Leather Skirt",
"Pleated Maxi Skirt","Patterned Leggings","Denim Overall Dress","Fleece Pullover","Sporty Crop Top",
"Mesh Top","Sheer Blouse","Hooded Dress","Cardigan Dress","Polo Shirt Dress",
"Peacoat with Buttons","Double-Breasted Blazer","Trench Coat with Belt","Bomber Jacket with Pockets","Faux Fur Vest",
"Chunky Sneakers","Slip-On Loafers","Combat Boots with Laces","Chelsea Boots with Heel","Running Shoes with Cushion",
"Knitted Beanie","Baseball Cap with Logo","Wide-Brim Sun Hat","Fedora Hat","Winter Headband",
"Striped Knit Socks","Solid Color Ankle Socks","Patterned Crew Socks","Thermal Socks","Sports Tube Socks",
"Leather Backpack","Canvas Tote Bag","Crossbody Bag with Buckle","Mini Shoulder Bag","Hobo Bag with Strap",
"Leather Gloves with Lining","Knitted Mittens","Touchscreen Gloves","Wool Gloves","Fingerless Knitted Gloves",
"Analog Watch with Leather Strap","Digital Sports Watch","Chronograph Watch","Smartwatch","Classic Watch",
"Denim Romper","Cotton Playsuit","Floral Jumpsuit","Silk Kimono","Patterned Romper",
"High-Waist Bootcut Jeans","Ripped Skinny Jeans","Mom Fit Jeans","Flared Jeans","Straight Leg Jeans",
"Cotton Polo Dress","Fleece Sweatshirt Dress","Tunic Shirt Dress","Wrap Shirt Dress","Mini Shirt Dress",
"Boho Blouse","Off-Shoulder Crop Top","Halter Neck Top","Bandeau Crop Top","Sleeveless Crop Top",
"Lightweight Track Jacket","Fleece Zip-Up Jacket","Softshell Rain Jacket","Down Quilted Jacket","Hiking Windbreaker",
"Slip-On Trainers","High-Top Canvas Shoes","Running Sneakers","Casual Loafers","Leather Dress Shoes",
"Summer Espadrilles","Flip Flops with Straps","Chelsea Ankle Boots","Lace-Up Combat Boots","Suede Ankle Boots",
"Silk Neck Scarf","Cotton Head Scarf","Wool Hat with Pom","Bucket Hat with Print","Knitted Headband",
"Leather Crossbody Bag","Clutch Purse","Hobo Shoulder Bag","Messenger Satchel","Mini Rucksack",
"Leg Warmers Knit","Fingerless Wool Gloves","Zippered Leather Jacket","Denim Shirt Jacket with Pockets","Corduroy Blazer",
"Stretchy Dress Pants","Pleated Trousers with Belt","Cargo Shorts for Men","Bermuda Shorts for Women","Mini Skater Skirt",
"Tie-Dye Hoodie","Graphic Crewneck Sweatshirt","Embroidered Pullover","Patchwork Jeans","Faux Leather Leggings",
"Chino Summer Shorts","Button-Front A-Line Skirt","High-Low Midi Dress","Silk Midi Dress","Mini Party Dress",
"Velvet Blazer Jacket","Sequined Crop Top","Satin Evening Blouse","Ruffled Work Shirt","Pleated Office Top",
"Matching Track Set","Hoodie and Jogger Set","Cotton Pajama Set","Silk Nightgown","Bathrobe"
]

bike_products = [
    # Bicycles (Types & Models)
    "Trek Marlin 7",
    "Specialized Rockhopper",
    "Cannondale Trail SE",
    "Giant Talon 2",
    "Scott Aspect 950",
    "Santa Cruz Chameleon",
    "Orbea Alma M50",
    "Canyon Spectral 125",
    "Kona Fire Mountain",
    "Diamondback Overdrive",
    "Pivot Mach 4 SL",
    "Salsa Timberjack",
    "Yeti ARC",
    "Ghost Kato 5",
    "GT Avalanche Comp",
    "BMC Fourstroke",
    "Marin Bobcat Trail",
    "Norco Fluid FS",
    "Merida Big Nine 300",
    "Ibis Ripley AF",

    # Bike Components
    "Shimano Deore XT Rear Derailleur",
    "SRAM GX Eagle Cassette",
    "Shimano Ultegra Crankset",
    "SRAM Red AXS Chain",
    "Race Face Aeffect Pedals",
    "Shimano Dura-Ace Brake Calipers",
    "SRAM XX1 Chainring",
    "Shimano SLX Shifter",
    "FSA Gossamer Stem",
    "Chris King Headset",
    "DT Swiss M1700 Wheelset",
    "Maxxis Minion DHF Tire",
    "Continental Grand Prix 5000 Tire",
    "Schwalbe Racing Ralph Tire",
    "WTB Volt Saddle",
    "Brooks B17 Saddle",
    "Ergon GP3 Grips",
    "Jagwire Pro Brake Cable Kit",
    "Hope Tech 4 V4 Disc Brakes",

    # Accessories
    "Lezyne Classic Floor Drive Pump",
    "Topeak JoeBlow Sport Pump",
    "CamelBak M.U.L.E. Hydration Pack",
    "Specialized Air Tool Pump",
    "Bontrager Ion 200 RT Light",
    "Knog Blinder Mini Light",
    "Garmin Edge 530 GPS",
    "Wahoo Elemnt Bolt GPS",
    "Cateye Velo Wireless Computer",
    "Quad Lock Phone Mount",
    "Park Tool Chain Checker",
    "Feedback Sports Bike Stand",
    "Pedro's Chain Lube",
    "Muc-Off Bike Cleaner",
    "Finish Line Wet Chain Lube",
    "Park Tool Tire Levers",
    "Crankbrothers Multi-Tool",
    "Topeak Alien II Multi-Tool",
    "Elite Fly Water Bottle",
    "Tacx Ciro Bottle Cage",

    # Clothing & Safety Gear
    "Giro Syntax MIPS Helmet",
    "Bell Super Air R Helmet",
    "POC Tectal Race Helmet",
    "Specialized Align II Helmet",
    "Giro Empire Shoes",
    "Shimano RC7 Shoes",
    "Five Ten Freerider Pro Shoes",
    "Pearl Izumi Quest Jersey",
    "Castelli Aero Race Jersey",
    "Fox Ranger Shorts",
    "Endura Hummvee Shorts",
    "Gore Wear C5 Gloves",
    "Specialized Body Geometry Gloves",
    "Pearl Izumi Elite Gel Gloves",
    "Assos Mille GT Bib Shorts",
    "Rapha Classic Bib Shorts",
    "Oakley Radar EV Sunglasses",
    "Smith Wildcat Sunglasses",
    "100% Speedcraft Sunglasses",
    "POC Devour Sunglasses",

    # Maintenance & Tools
    "Park Tool Repair Stand",
    "Feedback Sports Pro Elite Stand",
    "Pedro's Pedal Wrench",
    "Park Tool Cassette Lockring Tool",
    "Shimano Bleed Kit",
    "SRAM Bleed Kit",
    "Finish Line Grease",
    "Park Tool Chain Whip",
    "Pedro's Y-Wrench",
    "Crankbrothers Mini Pump",
    "Lezyne CO2 Inflator",
    "Park Tool Torque Wrench",
    "Topeak SmartGauge D2",
    "Park Tool Bottom Bracket Tool",
    "Muc-Off Disc Brake Cleaner",
    "Finish Line Super Bike Wash",
    "Stan's NoTubes Sealant",
    "Orange Seal Tubeless Sealant",
    "Park Tool P-Handle Hex Set",
    "Feedback Sports Rotor Truing Fork"
]



class RandomRating:

    def __init__(self):
        self.weights = self.__random_weights()

    def next(self):
        return random.choices([1,2,3,4,5], weights=self.weights, k=1)[0]
    
    def __random_weights(self):
        limit = 100
        weights = []
        for _ in range(4):
            r = random.randint(0, limit)
            weights.append(r)
            limit -= r
        weights.append(limit)
        return [w / 100 for w in weights]
    
bike_stores_df = pd.read_csv('data/input/stores.csv')
bike_stores = list(bike_stores_df['storeName'])

products_df = pd.read_csv('data/input/products.csv')

products = list(products_df['Name']) + tech_products + clothing_products + bike_products
products_random_ratings = {p: RandomRating() for p in products }


users_df = pd.read_csv('data/output/users.csv')
users_id_map = dict(zip(list(users_df['email']), list(users_df['id'])))


stores_df = pd.read_csv('data/output/stores.csv')
stores_id_map = dict(zip(list(stores_df['name']), list(stores_df['id'])))


sales_by_person_df = pd.read_csv('data/input/sales_by_person.csv')
sales_by_person_df.sample(frac=0.6)

fake = Faker()

user_reviews = []

def get_review(userid, product, storeid, start_date):


    rating = products_random_ratings[product].next()

    end_date = start_date + timedelta(days=90)
    date = fake.date_time_between(start_date=start_date, end_date=end_date)

    user_reviews.append({'id': len(user_reviews) + 1, 'userid': userid, 'storeid': storeid, 'product': product, 'rating': rating, 'date': date.strftime('%d/%m/%Y')})



def apply_get_review_to_sales_by_person(r):
    userid = users_id_map[r['EmailAddress']]
    storeid = stores_id_map['AdventureWorks']
    product = r['productName']
    start_date = datetime.fromisoformat(r['DueDate'])
    get_review(userid,product, storeid, start_date)


sales_by_person_df.apply(apply_get_review_to_sales_by_person, axis=1)


sales_by_store_df = pd.read_csv('data/input/sales_by_store.csv')


users_ids = list(users_id_map.values())

def apply_get_review_to_sales_by_store(r):
    userids = random.choices(users_ids, k=random.randint(0, r['OrderQty']))
    storeid = stores_id_map[r['storeName']]
    product = r['productName']

    for idx in userids:
        start_date = datetime.fromisoformat(r['DueDate']) + timedelta(days=20)
        get_review(idx, product, storeid, start_date)

sales_by_store_df.apply(apply_get_review_to_sales_by_store, axis=1)




for stores, products in [(bike_stores, bike_products), (tech_stores, tech_products), (clothing_stores, clothing_products)]:
    for s in tqdm(stores):
        storeid = stores_id_map[s]
        random_products = random.choices(products, k=random.randint(1, 100))
        for p in random_products:
            random_users = random.choices(users_ids, k=random.randint(1, 100))
            for u in random_users:
                start_date = fake.date_between_dates(datetime(2011,1,1), datetime(2014,12,31))
                get_review(u, p, storeid, start_date)


user_reviews_df = pd.DataFrame(user_reviews)
user_reviews_df.to_csv('data/output/reviews.csv', index=False)