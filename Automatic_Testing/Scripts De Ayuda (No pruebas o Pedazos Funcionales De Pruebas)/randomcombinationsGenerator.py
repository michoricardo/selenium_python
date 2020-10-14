import string
import random
from random import choice
from string import ascii_uppercase
from string import ascii_lowercase

animals= ["'perrito', 'carne','animal','jugo','gato', 'Halcón','Hiena','Hipopótamo','Hormiga','Hurón','Hámster',Aardvark","Albatross","Alligator","Alpaca","Ant","Anteater","Antelope","Ape","Armadillo","Donkey","Baboon","Badger","Barracuda","Bat","Bear","Beaver","Bee","Bison","Boar","Buffalo","Butterfly","Camel","Capybara","Caribou","Cassowary","Cat","Caterpillar","Cattle","Chamois","Cheetah","Chicken","Chimpanzee","Chinchilla","Chough","Clam","Cobra","Cockroach","Cod", "Cormorant","Coyote","Crab","Crane","Crocodile","Crow","Curlew","Deer","Dinosaur","Dog","Dogfish","Dolphin","Dotterel","Dove","Dragonfly","Duck","Dugong","Dunlin","Eagle","Echidna","Eel","Eland","Elephant","Elk","Emu","Falcon","Ferret","Finch","Fish","Flamingo","Fly","Fox","Frog","Gaur","Gazelle","Gerbil","Giraffe","Gnat","Gnu","Goat","Goldfinch","Goldfish","Goose","Gorilla","Goshawk","Grasshopper","Grouse","Guanaco","Gull","Hamster","Hare","Hawk","Hedgehog","Heron","Herring","Hippopotamus","Hornet","Horse","Human","Hummingbird","Hyena","Ibex","Ibis","Jackal","Jaguar","Jay","Jellyfish",
    "Kangaroo","Kingfisher","Koala","Kookabura","Kouprey","Kudu","Lapwing","Lark","Lemur","Leopard","Lion","Llama","Lobster","Locust""Loris","Louse","Lyrebird","Magpie","Mallard","Manatee","Mandrill","Mantis","Marten","Meerkat","Mink","Mole","Mongoose","Monkey","Moose","Mosquito","Mouse","Mule","Narwhal","Newt","Nightingale","Octopus",
    "Okapi","Opossum","Oryx","Ostrich","Otter","Owl","Oyster","Panther","Parrot","Partridge","Peafowl","Pelican","Penguin","Pheasant","Pig","Pigeon","Pony","Porcupine","Porpoise","Quail","Quelea","Quetzal","Rabbit","Raccoon","Rail","Ram","Rat","Raven","Red deer",
    "Red panda","Reindeer","Rhinoceros","Rook","Salamander","Salmon","Sand Dollar","Sandpiper","Sardine","Scorpion","Seahorse","Seal","Shark","Sheep","Shrew","Skunk","Snail","Snake","Sparrow","Spider","Spoonbill","Squid","Squirrel","Starling","Stingray","Stinkbug","Stork","Swallow","Swan","Tapir","Tarsier","Termite","Tiger","Toad","Trout","Turkey",
    "Turtle","Viper","Vulture","Wallaby","Walrus""Wasp","Weasel","Whale","Wildcat","Wolf","Wolverine","Wombat","Woodcock","Woodpecker","Worm","Wren","Yak","Zebra"]
def randomGen(tipo):
    if tipo == 'sku':
        first=(''.join(choice(ascii_uppercase) for i in range(4)))
        num = str(random.randint(-1000,1000))
        second=(''.join(choice(ascii_uppercase) for i in range(4)))
        randSku= first + num + second
        print(randSku)
        return randSku
    if tipo == 'desc':
        description=(' '.join(choice(animals) for i in range(6)))
        print(description)
        return description
    if tipo == 'nombre':
        name_only=('-'.join(choice(animals) for i in range(2)))
        num = str(random.randint(-10,10))
        finalname=name_only+num
        print(finalname)
        return finalname
    if tipo =='categoria':
        initial=(''.join(choice(ascii_lowercase) for i in range(2)))
        animalword=name_only=('-'.join(choice(animals) for i in range(1)))
        finalcat=initial+animalword
        print(finalcat)
        return finalcat
    
              
randomGen('sku')
randomGen('desc')
randomGen('nombre')
randomGen('categoria')

