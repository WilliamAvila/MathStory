# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
image  trans = "transition.png"
image angela ="images/layout hackaton-04 (copy).png"
image person ="images/layout hackaton-01-2.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define e = Character('Eileen', color="#c8ffc8")
define g=Character('Girl',color="#99FF33")
define angie = Character('Angela de la Vega',color="#CC0099")
define professor =Character('Profesor',color="#FFFFFF")

define persona=Character('Person',color="#0066FF")

# The game starts here.
# - El juego comienza aquí.
label start:
    show angela at left
    angie  "Este es mi primer año de universidad.
                Confieso que siento un poco de ansiedad respecto a la novedad de la situación."
                
    angie "¿Cómo serán los compañeros? ¿Las clases son tan difíciles como advertían en el colegio? ¿La universidad es otro nivel?"
    
    angie "Pensando en todo eso, doy mi primer paso para entrar a la facultad -Vuelvo a ver mi hoja de confirmación buscando coincidir 
                el código de clase con el aula al mismo tiempo que camino con prisa por el pasillo ¡No quiero llegar tarde el primer día!
                "
    show person at right
    angie "Doy vuelta aceleradamente por uno de los pasillos y de golpe sin saber nada veo que todo dá gira a mi alrededor. 
                Al abrir los ojos todo está descalabrado por el suelo, incluyendo mi persona, pertenencias y... ¿Otra persona? ¡Rayos! ¿Qué hago?" 
    
    

    menu:
    
        "No decir nada, recoger mis cosas e irme":
            
            angie "De la verguenza volteo a ver para otro lado, recojo todo lo más rápido posible y salgo corriendo hacia la clase."
            jump mat01
            
        "Preguntarle sí se encuentra bien":
            
            angie "De la verguenza volteo a ver para otro lado, recojo todo lo más rápido posible y salgo corriendo hacia la clase."
            jump mat01    
            
        "Ayudarle de inmediato a recoger las cosas":
            jump mat01
                      
        "Me molesto y le digo que debería de ver por donde camina":
            angie "Sin decir nada me doy prisa y pongo todas sus cosas desperdigadas en su regazo, me levanto de inmediato, hago un gesto de disculpa y salgo a buscar mi clase."
            jump mat01
            
    return
    
label charla:
    persona "Creo que sí... disculpame."
    persona" No miraba por donde caminaba"
    angie "No hay pena, yo tampoco estaba poniendo atención."
    angie "¿Necesitas ayuda?"
    persona "Estoy bien, ya recogí mis cosas."
    persona "De nuevo ¡Lo siento!  y salió caminando de nuevo con velocidad"
    jump mat01
    
    return
    
label molestar:
    angie "¡Oye deberías de tener más cuidado!"
    persona "¡Lo siento!"
    persona "Aunque lo mismo digo para tí..."
    angie "Sí tú hubieras ido viendo por donde caminas no estaríamos en esta situación
    Digo mientras nos levantamos del suelo."
    persona "¡Jum!"
    angie "¡Jum!"
    angie "Al retirarme del lugar me pongo a pensar que a pesar de todo, era buen material la tipa."


    
    
label mat01:
   # professor: "Buenas tardes joven"
         
    menu:
        e "Ayudame a resolver esta ecuacion: 4x + 3x^2 -x +2 =38 "
        
        
        "x=3, -4":
            jump opcion1
           
        "x=-3, 4 ":
            e "Elegiste opcion 2"
            
        "x = -3, 4":
            e "Elegiste opcion 3"
    return
    
label seguir:
   angie "Regreso la mirada a mis asuntos, saco mi cuaderno del bolsón y pongo atención a la clase. "
   return
   
label voltear:
    angie "Volteo a ver y nuestras miradas se encuentran por un segundo, reímos, sacamos nuestros materiales de clase y ponemos atención en la pizarra."


label lista:
    professor "Cómo es el primer día de clases, he sido permisivo con el tiempo de entrada."
    professor "No será la norma así que vayan ajustando su horario ¿eh?"
    professor "Ahora vamos a pasar lista.
    
    Unas cuantas personas después dice mi nombre y respondo"
    professor "Presente"
    professor "Angela De La Vega"
    angie "Presente"
    angie "Pueden decirme Angie"
    
    person "..."
    professor "Hrrmm-Hrmm"
    professor "Roberta"
    "¡Aquí!"
    professor "Cirilo"
    "¡Presente!"
    
label opcion1:
    e "Llegaste a la opcion 1"
    return
    
label opcion2:
    g "Llegaste a la opcion 2"
    return
