# **Estancias del Sol (APP MOBILE)**
## **DESCRIPCIÓN**

*Aplicación móvil que permite a los usuarios gestionar sus reservas de manera sencilla y eficiente. Con esta app, los usuarios pueden consultar o cancelar sus respectivas reservas existentes, como también agregar o cancelar servicios adicionales a sus reservas.*

## INDICE
-[Características](#Características)<br>
-[Funcionamiento](#funcionamiento)<br>
-[conexion entre vistas](#conexion)<br>
-[Funciones Internas](#internas)<br>
-[Tecnologías Utilizadas](#tec)<br>
-[instalación](#instalacion)<br>
-[Requerimientos](#Requerimientos)<br>
-[Contacto](#Contactos)<br>
-[Creditos](#creditos)<br>

## [Características](#Características)

*La app cuenta con las siguientes características:*<br>

- **Ver reservas**: Los usuarios pueden visualizar todas sus reservas activas o canceladas.

- **Cancelar reserva**: Los usuarios tienen la posibilidad de cancelar sus reservas realizadas en la web.

- **Agregar servicios**: Los usuarios tienen la posibilidad de agregar servicios extras a su reserva de acuerdo con la disponibilidad del servicio según el hotel.

- **Cancelar servicio**: Los usuarios también tienen la posibilidad de cancelar los servicios agregados.

- **Ver servicios**: Los usuarios pueden visualizar sus servicios agregados, así como los servicios gratuitos incluidos en su reserva para una mayor comodidad.

- **Código del hotel**: Los usuarios tienen la posibilidad de consultar el ID del hotel en caso de no conocerlo.

## [Funcionamiento](#funcionamiento)

A continuación, una breve explicación para el correcto funcionamiento:

**1.** - **__Inicializar__** <br>
Inicia la aplicación en tu dispositivo móvil o emulador.

<br>

**2.** - **__Home (primera vista)__** <br>
Comenzarás con una pantalla de inicio que indica que para ver tu reserva debes completar el formulario con tus datos: apellido del usuario y el código de reserva.<br>

Luego de completar los datos solicitados, para continuar debes presionar el botón de __"**consultar**"__ y esto te llevará a la segunda vista (*DETALLES*).<br>

Si lo que quieres es __cancelar__ la reserva, solo tienes que presionar el botón de __"**cancelar reserva**"__ y esto te llevará a la tercera vista (*CANCEL*).

<br>

**3.** - **__Detalles (segunda vista)__** <br>
__IMPORTANTE: es necesario completar el formulario de la vista anterior (Home)__.

Si no completaste los datos, te mostrará un mensaje: __Necesitamos sus datos para continuar__.

Si completaste con datos no registrados o cualquier tipo de dato que no sea correcto, mostrará como mensaje: __RESERVA NO ENCONTRADA__.

Si completaste con los datos correctos, mostrará todos los __detalles de tu reserva__.

La vista también cuenta con un __pequeño formulario__ en el que debes ingresar el ID de hotel (__dato necesario para la siguiente vista__). Luego debes presionar el botón de __ver servicios__.

Finalmente, cuenta con 3 botones:

- Un botón de __**volver**__ (vuelve a la vista anterior)

- Un botón para __**ver servicios**__ (te lleva a la cuarta vista)

- Un botón de consulta __**¿ID hotel?**__ (te lleva a la 6ta vista {hotel}, esto solo en caso de no recordar el ID de hotel)

<br>

**4.** - **__Cancel (tercera vista)__** <br>
La vista cuenta con un formulario para cancelar la reserva. Los datos pedidos son: código de reserva y apellido del usuario. Para proceder con la cancelación, presiona el botón **cancelar**.

Los resultados se muestran como mensaje en la misma pantalla en rojo.

Si completaste con cualquier tipo de dato, el mensaje será:
__"Su código de reserva y/o su usuario no existe"__.

Si no completaste los datos, será:
__Necesitamos sus datos para cancelar__.

Si ya cancelaste la reserva:
__"Su reserva ya se encuentra cancelada."__

Si los datos son correctos:
__Reserva cancelada exitosamente__.

Finalmente, cuenta con 2 botones:

- Un botón de __**volver**__ (vuelve a la vista anterior)

- Un botón para __**cancelar**__ (realiza la cancelación)

<br>

**5.** - **__Servicios (cuarta vista)__** <br>
Lista y muestra los servicios disponibles para agregar a la reserva presionando el botón de __continuar__.

__IMPORTANTE: Es necesario completar el miniformulario de la vista anterior (DETALLES) para listar los servicios que están disponibles según el hotel elegido.__

Si no completaste los datos o con cualquier dato, el mensaje será: 
__ID de hotel no existe__.

Si completaste con datos correctos:
__Listará los servicios disponibles__.

Finalmente, cuenta con 2 botones:

- Un botón de __**volver**__ (vuelve a la vista anterior)

- Un botón para __**continuar**__: para ir a agregar los servicios (te lleva a la 5ta vista {contratar})

<br>

**6.** - **__Contratar (quinta vista)__** <br>
CONTIENE dos formularios importantes para finalizar con la reserva:

1. Formulario para agregar, cancelar y ver tu servicio

   Datos solicitados:
   código de reserva y código del servicio.

   __NOTA: el código de servicio se obtiene de la vista anterior (cuarta vista) (servicios): se listan los detalles de los servicios junto a su ID__.

   Cuenta con 3 botones:

   - **Agregar**: para agregar el servicio a la reserva.

   - **Cancelar**: para cancelar el servicio agregado.

   - **Ver servicios agregados**: para ver todos los servicios que agregaste.

   El resultado se muestra en la pantalla en forma de mensaje en rojo.

   ///**Dependiendo de cómo completaste los datos, mostrarán:**/// 

       ´Reserva del servicio agregada exitosamente´

       'Reserva del servicio cancelada exitosamente' 

        'Su servicio ya se encuentra agregado'

        'Su servicio no se encuentra registrado'

        'Su código de reserva y/o el ID del servicio no existe'

   Para el caso del botón __ver servicios agregados__, te lleva a otra vista (miservicio) (7ma vista).

   Si tienes servicios agregados, los mostrará, pero si no tienes ningún servicio agregado, no mostrará nada.

2. Formulario simple para ver servicios gratuitos.
   Contiene un miniformulario que pide el ID de habitación.

   Cuenta con 1 solo botón __ver__ (te lleva a la 7ma vista) (miservicio).

<br>

**7.** - **__Hoteles (6ta vista)__** <br>
Vista simple informativa, para aquellos usuarios que no se acuerdan del ID de su hotel.

Lista los hoteles con su ID.

Finalmente, cuenta con un botón de __volver__.

<br>

**8.** - **__Miservicio (7ma vista)__** <br>
Vista simple informativa, dependiendo del botón presionado, mostrará diferentes informaciones.

Si llegaste a esta vista con el botón:

- __**Mis reservas**__: se listan los servicios agregados anteriormente.

- __**Ver**__: se listan los servicios gratuitos incluidos en tu reserva. Solo lista los servicios agregados a la reserva.

Finalmente, también cuenta con un botón de __volver__.

__IMPORTANTE: es necesario completar con los datos válidos para listar servicios agregados en la vista anterior (Contratar) (quinta vista)__

~~**NOTA**:~~ Se mostrará un mensaje de error si ocurre un problema no mencionado.

<br>

## [conexion entre vistas](#conexion)
    la app mobile cuenta con 7 vistas.

    MainScreen:
        name: 'main'
    DetalleScreen:
        name: 'detalle'
    CancelScreen:
        name: 'cancel'
    ServicioScreen:
        name: 'servicio'
    ContratarScreen:
        name: 'contratar'        
    HotelesScreen:
        name: 'hoteles'
    MiservicioSreen:
        name: 'miservicio


__PARA VER RESERVA Y GESTIONAR TUS SERVICOS__

menu-->ver detalles reserva-->agregar/cancelar servcio -->ver servicos agregados/gratuitos 

MainScreen==>DetalleScreen==>ServicioScreen==>ContratarScreen==>MiservicioSreen

__PARA CANCELAR RESERVA__

menu-->cancelar reserva

MainScreen==>CancelScreen
      
__PARA CONSULTAR ID HOTEL__

menu-->ver detalles reserva-->consular id hotel

MainScreen==>DetalleScreen==>HotelesScreen


## [Tecnologías Utilizadas](#tec)

- **kivy**

- **kivymd**

- **python**

       ARCHIVOS: main.PY y desig.KV

## [Instalación](#instalacion)

### Para emulador:

1. *Crea un ambiente virtual:*

    ```bash
    pip3 install virtualenv
    virtualenv kivy_venv
    source kivy_venv/bin/activate
    ```

2. *Instala dentro del entorno virtual:*

    ```bash
    pip install kivy
    pip install kivymd
    pip install requests
    ```

   a. Este comando te instalará una versión de KivyMD que no funciona.

   b. Al momento de ejecutar `app.py`, no funcionará y saldrá una advertencia:

       ```
       [warning] pip install http://github.com/... ---------------------
       ```

   c. Copia el comando recomendado y ejecútalo.

   d. Te instalará la versión `kivymd==2.0.1.dev0`:

    ```bash
    pip install https://github.com/kivymd/KivyMD/archive/master.zip#sha256=ab18d4cc36e2d53ea87f463d01299c39c75bae66cc1950f9bc6397f23317c848
    ```
    e. Ubica los archivos main.py y design.kv dentro de tu ambiente virtual y ejecútalo.
<br>

### Para usar en celular:

*Instala el APK "hotelería" de la app_mobile:*

*Nota: recuerda dar los permisos necesarios para su correcto funcionamiento.*

Permitir la instalación de archivos de fuentes desconocidas en el celular.

## [Requerimientos](#Requerimientos)

asyncgui==0.6.3

asynckivy==0.6.4

certifi==2024.8.30

charset-normalizer==3.4.0

docutils==0.21.2

idna==3.10

Kivy==2.3.0

Kivy-Garden==0.1.5

kivymd==2.0.1.dev0

materialyoucolor==2.0.9

pillow==11.0.0

Pygments==2.18.0

requests==2.32.3

urllib3==2.2.3

Python==3.12.3


## [Contacto](#Contactos)

´´´correo

    artufran.sanchez@gmail.com


## [Creditos](#creditos)
INTEGRANTE: ARTURO SANCHEZ

nombre GITHUP: arturo252


## [Funciones Internas](#internas)


     ver  funcionamiento.txt