# Aventura de una persona cotidiana

opcion = input("¿Qué eliges? (beber/futbol/2p2): ").strip().upper()

if opcion == "beber":
    print("\nsales a beber. con tu panas y pasarla bien. pero un pana te tiene la ganas, escuchas que esta hablando mal tuyo. ¿Quieres hablarle clarlo o IGNORAR lo que esta hablando tuyo?")
    
    opcion = input("¿Qué haces? (hablale claro/IGNORAR lo que esta hablando tuyo): ").strip().upper()
    
    if opcion == "hablale claro":
        print("\nTe acercas con un que fue mano y descubre que el pana si esta hablando tuyo . Afortunadamente, tienes a tu banda y logras darle miedo. Sigues hablando pa dejar en problema y buscas la solucion. ¡estas resolviendo en problema! Fin del juego.")
    elif opcion == "IGNORAR lo que esta tuyo y evitar":
        print("\nDecides ignorar lo que esta hablando tuyo y sigues bebiendo. Sin darte cuenta, el pana te tira una botella por detrás. Fin del juego.")
    else:
        print("\nNo elegiste una opción válida. Te quedas ahi pegado y el pana te tira una botella. Fin del juego.")

elif opcion == "futbol":
    print("\nCoges jugar futbol. Parece ser que en partido es lejo. ¿Quieres ir a jugar o quedarte?")
    
    opcion = input("¿Qué haces? (jugar/quedarte): ").strip().upper()

    if opcion == "jugar":
        print("\vas a jugar. Encuentras una  manera de ir. ¡ya tienes como ir invitas a uno pana que tiene moto! Fin del juego.")
    elif opcion == "quedarte":
        print("\nDecides quedarte a jugar con consola, pero se va la luz y no encuentras nada que hacer en tu casa. Fin del juego.")
    else:
        print("\nNo elegiste una opción válida. Te quedaste si luz y aburrido y sin nada que hacer. Fin del juego.")

elif opcion == "2p2":
    print("\nCoges ir pa 2p2 y vas. ese 2p2 tiene una sompresa: 'Busca ah alguien'. ¿Quieres BUSCAR ah alguien o no ir pa 2p2?")
    
    opcion = input("¿Qué haces? (BUSCAR a alguien/O No IR PA 2p2): ").strip().upper()
    
    if opcion == "BUSCAR a alguien":
        print("\nDecides buscar busca alguien paque 3p3. Después de buscar, lo encuentras. Enciendes en carro te alista y cuadras pa salir con ellas. ¡Has sido salvado por el! Fin del juego.")
    elif opcion == "no ir pa 2p2":
        print("\decides no ir y te quedas en viendo serie . Nadie viene decirte nada por apagar en telefono. Fin del juego.")
