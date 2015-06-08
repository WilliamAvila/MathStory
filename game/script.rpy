# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
image  trans = "transition.png"
image angela ="images/layout hackaton-04 (copy).png"
image person ="images/layout hackaton-01-2.png"


init python:
    exercicesList  = ["15x^2 +52x + 45",  "48x^2 +14x + 1", "21x^2 -x -2", "8x^2 -25x +18", "6x^2 -21x +9"]
    answers =['(3x + 5)(5x + 9)','(8x +1)(6x+1)','(7x +2)(3x-1)','(8x-9)(x-2)','3(x-3)(2x-1)']

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define e = Character('Eileen', color="#c8ffc8")
define g=Character('Girl',color="#99FF33")
define angie = Character('Angela de la Vega',color="#CC0099")
define professor =Character('Profesor',color="#FFFFFF")

define persona=Character('Person',color="#0066FF")
#style.say_who_window.background = Frame("Backgrounds/BG Entrada del Aula MAT101.png", 15, 15) #Background skin
# The game starts here.
# - El juego comienza aquí.
label start:
    scene bg facultad
    show angela at left
    angie  "Este es mi primer año de universidad.
                Confieso que siento un poco de ansiedad respecto a la novedad de la situación."
                
    angie "¿Cómo serán los compañeros? ¿Las clases son tan difíciles como advertían en el colegio? ¿La universidad es otro nivel?"
    
    angie "Pensando en todo eso, doy mi primer paso para entrar a la facultad"
    angie "Vuelvo a ver mi hoja de confirmación buscando coincidir 
                el código de clase con el aula al mismo tiempo que camino con prisa por el pasillo ¡No quiero llegar tarde el primer día!"
                
    show person at right
    angie "Doy vuelta aceleradamente por uno de los pasillos y de golpe sin saber nada veo que todo dá gira a mi alrededor. "
    angie "Al abrir los ojos todo está descalabrado por el suelo, incluyendo mi persona, pertenencias y... ¿Otra persona? ¡Rayos! ¿Qué hago?" 
    
    

    menu:
    
        "No decir nada, recoger mis cosas e irme":
            
            angie "De la verguenza volteo a ver para otro lado, recojo todo lo más rápido posible y salgo corriendo hacia la clase."
            jump mat101
            
        "Preguntarle sí se encuentra bien":
            
            angie "De la verguenza volteo a ver para otro lado, recojo todo lo más rápido posible y salgo corriendo hacia la clase."
            jump charla    
            
        "Ayudarle de inmediato a recoger las cosas":
            angie "Sin decir nada me doy prisa y pongo todas sus cosas desperdigadas en su regazo, me levanto de inmediato, hago un gesto de disculpa y salgo a buscar mi clase."
            jump mat101
                      
        "Me molesto y le digo que debería de ver por donde camina":
            jump molestar
            
    return
    
label charla:
    show person
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


    
    
label mat101:
    scene bg aula101
    show person at right
    professor "Buenas tardes joven"
    persona "Después de dar unas vueltas, encuentro el aula que coincide con mi hoja de confirmación y entro. Saludo al profesor."
    persona "Buen día, con permiso"
    professor "Buenas tardes joven"
    professor "Por favor tome asiento y guarde silencio"
    persona "Asiento ligeramente con la cabeza al mismo tiempo que sonrío y procedo a sentarme."
    persona "No había terminado de colocar mi mochila al lado del asiento... ¡Cuando noto que ella estaba en el asiento a mi lado!"
    
    menu:
    
        "Seguir como si nada":
            jump lista
       
        "Voltear a ver":
            jump lista
         
    return

    
label seguir:
   angie "Regreso la mirada a mis asuntos, saco mi cuaderno del bolsón y pongo atención a la clase. "
   return
   
label voltear:
    angie "Volteo a ver y nuestras miradas se encuentran por un segundo, reímos, sacamos nuestros materiales de clase y ponemos atención en la pizarra."
    return
    
label test:
    "El profesor termina de pasar la lista y camina hasta estar justo enfrente de los alumnos y en medio de la pizarra."
    professor "¡Bienvenidos a su clase de Álgebra 101!"
    professor "Haremos un chequeo de sus habilidades"
    professor "Quiero que recuerden su nivel que tienen en Matemáticas antes de empezar el curso y cuando terminen comparen sus habilidades para que vean cuánto han avanzado"

    professor "Empecemos" 
    "El tipo enciende el proyector y nos dice que anotemos los ejercicios en el cuaderno al mismo tiempo que mide con el reloj y dice. Tienen X minutos para resolver el primer test ¡Comiencen!"

    "El test se desarrolla en varias fases y esta es la primera"

    jump exercise

    return
    
#Esta parte del juego se puede repetir unas 10 veces. El desafío termina cuando el jugador falla un ejercicio. Dependiendo qué número de ejercicio falló, el profesor le dice en que level se encuentra.

label exercise:
    "El primer problema es 15x^2 +52x + 45"
    
    "Después de trabajar en la hoja creo que la respuesta es:"
    
    menu:
        '(x + 5)(5x + 9)':
            professor "InCorrecto"
        '(5x + 5)(3x + 9)':
            professor "InCorrecto"
        '(2x + 5)(5x + 9)':
            professor "InCorrecto"
        '(3x + 5)(5x - 9)':
            professor "InCorrecto"
        '(3x + 5)(5x + 9)':
            professor "Correcto"
        
    
    return

label lista:
    professor "Cómo es el primer día de clases, he sido permisivo con el tiempo de entrada."
    professor "No será la norma así que vayan ajustando su horario ¿eh?"
    professor "Ahora vamos a pasar lista.
    
    Unas cuantas personas después dice mi nombre y respondo"
    professor "Presente"
    professor "Angela De La Vega"
    angie "Presente"
    angie "Pueden decirme Angie"
    
    persona "..."
    professor "Hrrmm-Hrmm"
    professor "Roberta"
    "¡Aquí!"
    professor "Cirilo"
    "¡Presente!"
    jump test

