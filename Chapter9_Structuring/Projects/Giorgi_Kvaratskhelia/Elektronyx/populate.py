from Elektronyx import app
from flask_sqlalchemy import SQLAlchemy
from Elektronyx.models import Case, PSU, Motherboard, CPU, GPU, RAM, Storage

item_dictionary = \
    {'case':
        [
            {'manufacturer': 'Cooler Master',
             'model': 'Cosmos C700P',
             'color': 'Black',
             'height': '63cm',
             'width': '30cm',
             'depth': '65cm',
             'price': 349,
             'quantity': 4,
             'img': 'c700p.jpg'
             },
            {'manufacturer': 'Corsair',
             'model': 'Carbide 275R',
             'color': 'White',
             'height': '46cm',
             'width': '21cm',
             'depth': '45cm',
             'price': 85,
             'quantity': 8,
             'img': 'carbide275r.jpg'
             },
            {'manufacturer': 'Phanteks',
             'model': 'Evolv X',
             'color': 'Black',
             'height': '24cm',
             'width': '52cm',
             'depth': '51cm',
             'price': 207,
             'quantity': 2,
             'img': 'evolvX.jpg'
             },
            {'manufacturer': 'Corsair',
             'model': 'Obsidian 1000D',
             'color': 'Black',
             'height': '27cm',
             'width': '12cm',
             'depth': '27cm',
             'price': 499,
             'quantity': 1,
             'img': 'obsidian1000d.png'
             },
            {'manufacturer': 'NZXT',
             'model': 'H400i',
             'color': 'Black & Red',
             'height': '27cm',
             'width': '12cm',
             'depth': '27cm',
             'price': 150,
             'quantity': 1,
             'img': 'H400i.png'
             },
            {'manufacturer': 'Thermaltake',
             'model': 'Versa N27',
             'color': 'Black',
             'height': '50cm',
             'width': '20cm',
             'depth': '47cm',
             'price': 80,
             'quantity': 2,
             'img': 'versaN27.jpg'
             }

        ],
        'psu':
            [
                {'manufacturer': 'Corsair',
                 'model': 'TX750M',
                 'efficiency': '80+ Gold',
                 'wattage': 750,
                 'price': 119,
                 'quantity': 9,
                 'img': 'tx750m.png'
                 },
                {'manufacturer': 'EVGA',
                 'model': 'SuperNOVA 850',
                 'efficiency': '80+ Gold',
                 'wattage': 850,
                 'price': 159,
                 'quantity': 10,
                 'img': 'supernova850.jpg'
                 },
                {'manufacturer': 'Corsair',
                 'model': 'HX1000',
                 'efficiency': '80+ Platinum',
                 'wattage': 1000,
                 'price': 378,
                 'quantity': 7,
                 'img': 'hx1000.jpg'
                 },
                {'manufacturer': 'Asus',
                 'model': 'ROG Thor 850',
                 'efficiency': '80+ Platinum',
                 'wattage': 850,
                 'price': 380,
                 'quantity': 3,
                 'img': 'rogthor850.png'
                 },
                {'manufacturer': 'EVGA',
                 'model': '550 B5',
                 'efficiency': '80+ Bronze',
                 'wattage': 850,
                 'price': 80,
                 'quantity': 19,
                 'img': 'evga550b.jpg'
                 }
            ],
        'motherboard':
            [
                {'manufacturer': 'Asus',
                 'model': 'ROG STRIX Z490-E',
                 'socket_type': 'LGA 1200',
                 'memory_type': 'DDR4',
                 'memory_slots': 4,
                 'max_memory': 128,
                 'price': 300,
                 'quantity': 20,
                 'img': 'StrixZ490-E.png'
                 },
                {'manufacturer': 'MSI',
                 'model': 'MPG Z490',
                 'socket_type': 'LGA 1200',
                 'memory_type': 'DDR4',
                 'memory_slots': 4,
                 'max_memory': 128,
                 'price': 200,
                 'quantity': 10,
                 'img': 'MPGZ490.png'
                 },
                {'manufacturer': 'Asus',
                 'model': 'ROG STRIX X299-E',
                 'socket_type': 'LGA 2066',
                 'memory_type': 'DDR4',
                 'memory_slots': 4,
                 'max_memory': 128,
                 'price': 600,
                 'quantity': 3,
                 'img': 'STRIXX299.jpg'
                 },
                {'manufacturer': 'Gigabyte',
                 'model': 'GA-B250M-D3H',
                 'socket_type': 'LGA 1151',
                 'memory_type': 'DDR4',
                 'memory_slots': 4,
                 'max_memory': 64,
                 'price': 180,
                 'quantity': 12,
                 'img': 'GA-B250M-D3H.jpg'
                 }
            ],
        'cpu':
            [
                {'manufacturer': 'Intel',
                 'model': 'Core i7-10700K',
                 'socket_type': 'LGA1200',
                 'core_count': 8,
                 'core_clock': '3.8Ghz',
                 'power_draw': 125,
                 'price': 380,
                 'quantity': 5,
                 'img': '10700K.jpg'
                 },
                {'manufacturer': 'Intel',
                 'model': 'Core i5-10600K',
                 'socket_type': 'LGA1200',
                 'core_count': 6,
                 'core_clock': '4.1Ghz',
                 'power_draw': 125,
                 'price': 270,
                 'quantity': 2,
                 'img': 'i510600K.jpg'
                 },
                {'manufacturer': 'Intel',
                 'model': 'Core i9-10900K',
                 'socket_type': 'LGA1200',
                 'core_count': 8,
                 'core_clock': '3.7Ghz',
                 'power_draw': 125,
                 'price': 520,
                 'quantity': 5,
                 'img': 'i910900K.jpg'
                 },
                {'manufacturer': 'AMD',
                 'model': 'Ryzen 5 2600X',
                 'socket_type': 'AM4',
                 'core_count': 6,
                 'core_clock': '4.2Ghz',
                 'power_draw': 95,
                 'price': 196,
                 'quantity': 12,
                 'img': 'Ryzen2600X.jpg'
                 },
                {'manufacturer': 'AMD',
                 'model': 'Ryzen 8 2700X',
                 'socket_type': 'AM4',
                 'core_count': 8,
                 'core_clock': '3.7Ghz',
                 'power_draw': 105,
                 'price': 289,
                 'quantity': 5,
                 'img': 'Ryzen82700X.jpg'
                 }
            ],
        'gpu':
            [
                {'manufacturer': 'MSI',
                 'model': 'GeForce GTX 1660 Super',
                 'vram': 6,
                 'vram_type': 'GDDR6',
                 'power_draw': 125,
                 'length': '247mm',
                 'price': 500,
                 'quantity': 2,
                 'img': 'GeForceGTX1660Super.jpg'
                 },
                {'manufacturer': 'ASUS',
                 'model': 'GeForce RTX 2060',
                 'vram': 6,
                 'vram_type': 'GDDR6',
                 'power_draw': 160,
                 'length': '204mm',
                 'price': 460,
                 'quantity': 1,
                 'img': 'GeForceRTX2060.jpg'
                 },
                {'manufacturer': 'ASUS',
                 'model': 'GeForce RTX 2080',
                 'vram': 11,
                 'vram_type': 'GDDR6',
                 'power_draw': 250,
                 'length': '305mm',
                 'price': 1800,
                 'quantity': 4,
                 'img': 'GeForceRTX2080.jpg'
                 },
                {'manufacturer': 'ASUS',
                 'model': 'GeForce RTX 3090',
                 'vram': 24,
                 'vram_type': 'GDDR6',
                 'power_draw': 125,
                 'length': '320mm',
                 'price': 2100,
                 'quantity': 1,
                 'img': 'GeForceRTX3090.jpg'
                 },
                {'manufacturer': 'EVGA',
                 'model': 'GeForce GTX 1070',
                 'vram': 8,
                 'vram_type': 'GDDR5',
                 'power_draw': 267,
                 'length': '247mm',
                 'price': 689,
                 'quantity': 2,
                 'img': 'GeForceGTX1070.jpg'
                 }
            ],
        'ram':
            [
                {'manufacturer': 'G.Skill',
                 'model': 'TridentZ Series',
                 'memory_type': 'DDR4',
                 'memory_speed': 3200,
                 'memory_size': '16GB',
                 'price': 90,
                 'quantity': 12,
                 'img': 'TridentZSeries.jpg'
                 },
                {'manufacturer': 'Corsair',
                 'model': 'Vengeance LPX',
                 'memory_type': 'DDR4',
                 'memory_speed': 2666,
                 'memory_size': '8GB',
                 'price': 50,
                 'quantity': 24,
                 'img': 'VengeanceLPX.png'
                 },
                {'manufacturer': 'Corsair',
                 'model': 'Vengeance LP',
                 'memory_type': 'DDR3',
                 'memory_speed': 1600,
                 'memory_size': '8GB',
                 'price': 40,
                 'quantity': 8,
                 'img': 'VengeanceLP.jpg'
                 },
                {'manufacturer': 'Kingston',
                 'model': 'HyperX Fury',
                 'memory_type': 'DDR4',
                 'memory_speed': 2400,
                 'memory_size': '32GB',
                 'price': 150,
                 'quantity': 4,
                 'img': 'HyperXFury.jpg'
                 }
            ],
        'storage':
            [
                {'manufacturer': 'Seagate',
                 'model': 'Barracuda 8TB',
                 'storage_type': 'HDD',
                 'storage_capacity': '8TB',
                 'price': 150,
                 'quantity': 120,
                 'img': 'Barracuda8TB.jpg'
                 },
                {'manufacturer': 'HST',
                 'model': 'Ultrastar 7K4000',
                 'storage_type': 'HDD',
                 'storage_capacity': '4TB',
                 'price': 70,
                 'quantity': 80,
                 'img': 'Ultrastar7K4000.jpg'
                 },
                {'manufacturer': 'Samsung',
                 'model': '860 EVO Series',
                 'storage_type': 'SSD',
                 'storage_capacity': '500GB',
                 'price': 54,
                 'quantity': 240,
                 'img': 'samsungEVO.jpg'
                 },
                {'manufacturer': 'Western Digital',
                 'model': 'Blue 3D NAND',
                 'storage_type': 'SSD',
                 'storage_capacity': '500GB',
                 'price': 65,
                 'quantity': 40,
                 'img': 'Blue3DNAND.jpg'
                 }
            ],
        'computers':
            [
                {'manufacturer': 'Corsair',
                 'model': 'ONE i160',
                 'motherboard': 'Z370 Mini-ITX',
                 'cpu': 'Intel Core i9-9900k',
                 'gpu': 'NVIDIA GeForce RTX 2080 Ti',
                 'ram': '2x16GB DDR4-2666',
                 'ssd storage': '480GB M.2 NVMe SSD',
                 'hdd storage': '2TB 5400RPM 2.5” HDD',
                 'power supply': 'CORSAIR SF600, 80 Plus Gold',
                 'price': 3400,
                 'quantity': 1,
                 'img': 'CORSAIRONEi160.png'
                 }
            ],
        'accessories':
            [
                {'manufacturer': 'Kingston',
                 'model': 'Alloy Core RGB',
                 'accessory type': 'keyboard',
                 'backlighting': 'rgb',
                 'form factor': 'full size',
                 'price': 130,
                 'quantity': 5,
                 'img': 'hyperXkeyboard.jpg'
                 }
            ],
        'laptops':
            [
                {'manufacturer': 'ASUS',
                 'model': 'ROG Strix G17',
                 'cpu': 'AMD Ryzen 9 5900HX',
                 'gpu': 'NVIDIA GeForce RTX 3070 8GB GDDR6',
                 'ram': '16GB DDR4',
                 'ssd storage': '1TB PCIe SSD',
                 'price': 1800,
                 'quantity': 1,
                 'img': 'asusROGstrix.jpg'
                 },
                {'manufacturer': 'HP',
                 'model': 'Omen 15 28Z62EA',
                 'cpu': 'AMD Ryzen 5 4600H',
                 'gpu': 'NVIDIA GeForce GTX 1650 Ti 4GB GDDR6',
                 'ram': '16GB DDR4',
                 'ssd storage': '512GB M.2 SSD',
                 'price': 1300,
                 'quantity': 1,
                 'img': 'hpomen.jpg'
                 }
            ],
        'phones':
            [
                {'manufacturer': 'Xiaomi',
                 'model': 'Poco X3 NFC Dual Sim',
                 'cpu': 'Qualcomm SM7150-AC Snapdragon 732G',
                 'gpu': 'Adreno 618',
                 'storage': '128GB',
                 'ram': '6GB',
                 'main camera': '64MP, 13MP, 2MP, 2MP',
                 'selfie camera': '20MP',
                 'battery': 'Li-Po 5160mAH',
                 'price': 200,
                 'quantity': 6,
                 'img': 'pocophone.png'
                 }
            ],
        'tablets':
            [
                {'manufacturer': 'Samsung',
                 'model': 'Galaxy Tab S7 11',
                 'cpu': 'Qualcomm Snapdragon 865+',
                 'gpu': 'Adreno 650',
                 'storage': '128GB',
                 'ram': '6GB',
                 'main camera': '13MP, 5MP',
                 'selfie camera': '8MP',
                 'battery': 'Li-Po 8000mAh',
                 'price': 800,
                 'quantity': 2,
                 'img': 'galaxytab.png'
                 }
            ]
    }


db = SQLAlchemy(app)
for category in item_dictionary:
    for items in item_dictionary[category]:
        if category == 'case':
            product = Case(**items)
            db.session.add(product)
            db.session.commit()
        elif category == 'psu':
           product = PSU(**items)
           db.session.add(product)
           db.session.commit()
        elif category == 'motherboard':
           product = Motherboard(**items)
           db.session.add(product)
           db.session.commit()
        elif category == "cpu":
           product = CPU(**items)
           db.session.add(product)
           db.session.commit()
        elif category == "gpu":
           product = GPU(**items)
           db.session.add(product)
           db.session.commit()
        elif category == "ram":
           product = RAM(**items)
           db.session.add(product)
           db.session.commit()
        elif category == 'storage':
           product = Storage(**items)
           db.session.add(product)
           db.session.commit()