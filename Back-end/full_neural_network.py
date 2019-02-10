from numpy import array, random, dot, exp

class XarxaN():
    def __init__(self):
        # Que el nombre random sigui el mateix:
        random.seed(1)

        # Modelacio d'una neurona amb tres inputs i un output.
        # Assignem valors aleatoris a una matriu 3 X 1, amb valors de -1 a 1.
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    # Normalitzem la suma dels pesos dels inputs entr 0 i 1
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # Confianca del pes actual (derivada de la Sigma).
    def __sigmoid_derivative(self, x):
        return x * (1 - x)


    # Prova-error per entrenar la xarxa neuronal (ajustant els pesos cada vegada)
    def train(self, dades_TS_inputs, dades_TS_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Analitzem les proves a traves de la xarxa, una sola neurona
            output = self.think(dades_TS_inputs)

            # Calculem l'error:
            error = dades_TS_outputs - output

            # Ajustem mes els pesos en que confiem menys, aixi els inputs zeros no modifiquen els pesos.
            adjustment = dot(dades_TS_inputs.T, error * self.__sigmoid_derivative(output))

            # Ara ajustem els pesos:
            self.synaptic_weights += adjustment

    # Proces pel que passa la xarxa, per on enviem els inputs (neurones soles):
    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":
    xarxa = XarxaN() # xarxa d'una unica neurona

    print("Pesos sinaptics inicials aleatoris: ")
    print(xarxa.synaptic_weights)
    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.

    # Exemple de dades d'events:
    """
    {
      "actiu": true,
      "creador": 4444,
      "day": 20,
      "descripcio": "BIG TIME BOET",
      "esport_participants": 8,
      "esport_rang": "6-12",
      "etiqueta_A": 92, -> 0.97
      "etiqueta_B": 97,
      "etiqueta_C": 0,
      "hora": "17:00",
      "month": 2,
      "tipus": "Esports",
      "titol": "FUNCIONA",
      "ubicacio": 25,
      "year": 2019
    },
    {
      "actiu": true,
      "creador": 4444,
      "day": 25,
      "descripcio": "3x3 MATARO. Palau esportiu Mora",
      "esport_participants": 8,
      "esport_rang": "6-12",
      "etiqueta_A": 92,
      "etiqueta_B": 108,
      "etiqueta_C": 0,
      "hora": "17:00",
      "month": 2,
      "tipus": "Esports",
      "titol": "3x3 Mataro",
      "ubicacio": 25
      "year": 2019
    }
    """

    # Dades externes que s'haurien de passar donada la transformacio del json proporcionat a l'API
    #
    # Cada exemple conte 3 inpus i un 1 output.
    # ULTIMES ACTIVITATS D'USUARI:
    # INPUT (solucio senzilla): etiqueta A, etiqueta_B, etiqueta_C
    #
    # Inputs: etiqueta_A (la principal),
    # Outputs: RANGS D'ACTIVITATS -> identificacio percentual
    dades_TS_inputs = array(
        [
            [0.13, 0.45, 0.23],
            [0.23, 0.23, 0.23],
            [0.45, 0.65, 0.32],
            [0.64, 0.45, 0.67],
            [0.12, 0.65, 0.14],
            [0.8, 0.45, 0.94],
            [0.42, 0.82, 0.2]
        ]
    )

    dades_TS_outputs = array([[0.25, 0.5, 0.75, 1, 0.50, 0.75, 0.25]]).T

    # Entrenem la xarxa a traves del TS executant-lo 100000 vegades fent modificacions cada vegada:
    xarxa.train(dades_TS_inputs, dades_TS_outputs, 100000)

    print("Resultats del training ():")
    print(xarxa.synaptic_weights)


    #Testejos del training:
    print("Considerem la situacio [0.1, 0.95, 0.43] -> ?: ")
    print("Valor dels rangs d'activitat:")
    print(xarxa.think(array([0.1, 0.95, 0.43])))
    print("Considerem la situacio [0.4, 0.34, 0.28] -> ?: ")
    print("Valor dels rangs d'activitat:")
    print(xarxa.think(array([0.4, 0.34, 0.28])))
