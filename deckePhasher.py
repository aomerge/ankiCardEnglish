import genanki
import random

model_id = random.randrange(1 << 30, 1 << 31)
my_model = genanki.Model(
  model_id,
  'phrasal verbs',
  fields=[
    {'name': 'Verbo'},
    {'name': 'Significado'},
    {'name': 'Presente'},
    {'name': 'Pasado'},
    {'name': 'Futuro'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<h1 style="text-align: center;">{{Verbo}}</h2>',
      'afmt': '{{FrontSide}}<br>{{Significado}}<hr id="answer"><b>Presente:</b><br>{{Presente}}<br><b>Pasado:</b><br>{{Pasado}}<br><b>Futuro:</b><br>{{Futuro}}',
    },
  ])

deck_id = random.randrange(1 << 30, 1 << 31)
my_deck = genanki.Deck(
    deck_id,
    'phrasal verbs')

phrasal_verbs_con_ejemplos = [
        ('look for', 'buscar',
         'I look for my lost keys. (Busco mis llaves perdidas.)',
         'He looked for his missing book. (Él buscó su libro perdido.)',
         'We will look for a new apartment. (Buscaremos un nuevo apartamento.)'),
        ('run into', 'encontrarse con',
         'I ran into my old friend at the store. (Me encontré con mi viejo amigo en la tienda.)',
         'She ran into her neighbor this morning. (Ella se encontró con su vecino esta mañana.)',
         'They might run into some trouble on their journey. (Podrían encontrarse con algunos problemas en su viaje.)'),
        ('give up', 'rendirse',
         "Don't give up on your dreams. (No te rindas en tus sueños.)",
         "She refused to give up, no matter what. (Ella se negó a rendirse, pase lo que pase.)",
         "They won't give up easily in the face of challenges. (No se rendirán fácilmente ante los desafíos.)"),
        ('set up', 'configurar',
         'I need to set up my new computer. (Necesito configurar mi nueva computadora.)',
         'He helped me set up the meeting. (Él me ayudó a configurar la reunión.)',
         'We will set up the equipment for the presentation. (Configuraremos el equipo para la presentación.)'),
        ('turn on', 'encender',
         'Can you turn on the lights? (¿Puedes encender las luces?)',
         'She turned on the TV to watch the news. (Ella encendió la televisión para ver las noticias.)',
         'They will turn on the heater when it gets cold. (Encenderán la calefacción cuando haga frío.)'),
        ('pick up', 'recoger',
         'I will pick up groceries on my way home. (Recogeré comestibles de camino a casa.)',
         'She picked up her children from school. (Recogió a sus hijos de la escuela.)',
         'They can pick up the package from the post office. (Pueden recoger el paquete en la oficina de correos.)'),
        ('go on', 'continuar',
         'The show must go on, no matter what. (El espectáculo debe continuar, pase lo que pase.)',
         'She went on talking for hours. (Siguió hablando durante horas.)',
         'They plan to go on their journey despite the challenges. (Planean continuar su viaje a pesar de los desafíos.)'),
        ('turn off', 'apagar',
         'Please remember to turn off the lights when you leave. (Por favor, recuerda apagar las luces cuando te vayas.)',
         'He turned off his phone during the meeting. (Apagó su teléfono durante la reunión.)',
         'They will turn off the engine to save fuel. (Apagarán el motor para ahorrar combustible.)'),
        ('show up', 'presentarse',
         'I hope everyone will show up to the party. (Espero que todos se presenten a la fiesta.)',
         'She showed up at the meeting on time. (Se presentó a la reunión puntualmente.)',
         'They always show up when you need them. (Siempre se presentan cuando los necesitas.)'),
         ('look after', 'cuidar',
         'I look after my younger brother. (Cuido a mi hermano menor.)',
         'She looked after the kids yesterday. (Ella cuidó a los niños ayer.)',
         "They will look after the pets while we're away. (Ellos cuidarán a las mascotas mientras estamos fuera.)"),
]

for verbo, significado, presente, pasado, futuro in phrasal_verbs_con_ejemplos:
        note = genanki.Note(
                model=my_model,
                fields=[verbo, significado, presente, pasado, futuro])
        my_deck.add_note(note)

genanki.Package(my_deck).write_to_file('phrasal_verbs.apkg')