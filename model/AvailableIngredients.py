import model.Constants
from model.Menu import Ingredient

# Available ingredients seem difficult to parse and use. Some examples are provided here.
QUESO = Ingredient("Queso").add_tag(model.Constants.LACTOSE)
MOZZARELLA = Ingredient("Mozzarella").add_tag(model.Constants.LACTOSE)
JAMON = Ingredient("Jamón").add_tag(model.Constants.MEAT)
TOCINO = Ingredient("Tocino").add_tag(model.Constants.MEAT)
LONGANIZA_PICANTE = Ingredient("Longaniza picante").add_tag(model.Constants.SPICY)
PIÑA = Ingredient("Piña").add_tag(model.Constants.PURE_EVIL)
