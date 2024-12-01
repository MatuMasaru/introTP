#:kivy==2.3.0   kivymd==2.0.1.dev0
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivymd.app import MDApp
import requests

# Definir las pantallas
class MainScreen(Screen):
    pass

class DetalleScreen(Screen):
    def get_reserva_detalle(self, code , name):
        if not code or not name:
            self.ids.detalle_label.text = "*Necesitamos sus datos para continuar"
            return
        try:
            response = requests.get(f'http://127.0.0.1:3648/api/reserva/{code}/{name}') 
            if response.status_code == 200:
                datas = response.json()
                data=datas[0]
                self.ids.detalle_label.text =( 
                    f"Cliente: {data['cliente_apellido']}\n"
                    f"Estado de la reserva: {data['estado']}\n"
                    f"Llegada: {data['llegada']}\n"
                    f"Salida: {data['salida']}\n"
                    f"USD: {data['precio']}\n"
                    f"ID habitacion: {data['id_habitacion']}\n"
                    f"fecha de cancelacion: {data['fecha_cancelacion']}\n"
                    f"codigo de reserva: {data['id']}\n"
                )
            if response.status_code == 404:
                self.ids.detalle_label.text = "*RESERVA NO ENCONTRADA"   
        except requests.exceptions.RequestException:
            self.ids.detalle_label.text = "*ERROR AL INTENTAR ACCEDER A LA RESERVA"

class CancelScreen(Screen):
    def cancel_reserva(self, code, name):
        if not code or not name:
            self.ids.cancel_label.text = "*Necesitamos sus datos para cancelar."
            return 
        url = f"http://127.0.0.1:3648/api/reserva/{code}/{name}"
        try:
            response = requests.put(url)
            if response.status_code == 200:            
                self.ids.cancel_label.text = "-Reserva cancelada exitosamente."
            if response.status_code == 400:
                self.ids.cancel_label.text = "-Su reserva ya se encuentra cancelada."
            if response.status_code ==404:
                self.ids.cancel_label.text = "*Su codigo de reserva y/o su usuario no existe"
        except requests.exceptions.RequestException:
            self.ids.cancel_label.text = "*Error al cancelar la reserva."

class ServicioScreen(Screen):
    def get_detalles_servicios(self, id):
        if not id:
            self.ids.detalle_servicio_label.text = "*Necesitamos su id hotel para continuar."
            return 
        url = f"http://127.0.0.1:3648/api/servicios/hotel/{id}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                datas=response.json()
                detalles_servicios = ""  # Inicializa la variable para almacenar los detalles.
                for data in datas:
                    detalles_servicios += (
                        f"id: {data['id_servicio']} | "
                        f"USD: {data['precio']}\n"
                        f"{data['servicio']} | "
                        f"Clase: {data['tipo']}\n"
                    )
                self.ids.detalle_servicio_label.text = detalles_servicios  # Asigna la cadena a la etiqueta.
            if response.status_code == 400:
                 self.ids.detalle_servicio_label.text= "No hay servicios para reservar en esta habitacion"
            if response.status_code == 404:
                 self.ids.detalle_servicio_label.text= "ID de hotel no existe"   
        except requests.exceptions.RequestException:
                 self.ids.detalle_servicio_label.text= "Error al intentar ver los servicios"                  

class ContratarScreen(Screen):
    def contratar_servicio(self, id_reserva, id_servicio):
        if not id_reserva or not id_servicio:
            self.ids.contratar_label.text = "Necesitamos su id de servicio y el del hotel"
            return
        url_contratar = f"http://127.0.0.1:3648/api/servicio/{id_reserva}/{id_servicio}"
        try:
            response = requests.post(url_contratar)
            if response.status_code == 200:
                self.ids.contratar_label.text = "Reserva del servicio agregada exitosamente."
            if response.status_code == 400:
                self.ids.contratar_label.text = "Su servicio ya se encuentra agregada."
            if response.status_code == 404:
                self.ids.contratar_label.text = "Su código de reserva y/o el id del servicio no existe."
        except requests.exceptions.RequestException:
            self.ids.contratar_label.text = "Error al agregar el servicio."

    def cancelar_servicio(self, id_reserva,id_servicio):
        if not id_reserva or not id_servicio:
            self.ids.contratar_label.text = "Necesitamos su id de servicio y el del hotel"
            return
        url= f"http://127.0.0.1:3648/api/reserva/servicio/{id_reserva}/{id_servicio}"   
        try:
            response = requests.delete(url)
            if response.status_code == 200:            
                self.ids.contratar_label.text = "Reserva  del servicio cancelda exitosamente."
            if response.status_code == 400:
                self.ids.contratar_label.text = "Su servicio no se encuentra registrado"
            if response.status_code ==404:
                self.ids.contratar_label.text = "su codigo de reserva y/o el id del servicio no existe"    
        except requests.exceptions.RequestException as e:
            self.ids.contratar_label.text = "Error al cancelar el servicio."

class HotelesScreen(Screen):
    def get_hoteles_detalles(self):
        url="http://127.0.0.1:3648/api/hoteles"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                datas = response.json()
                detalles_hotel = ""
                for data in datas:
                    detalles_hotel += (
                        f"id hotel: {data['id']}\n"
                        f"Nombre: {data['nombre']}\n"
                        f"Region: {data['region']}\n"
                    )
                self.ids.detalles_hotel_label.text = detalles_hotel
        except requests.exceptions.RequestException as e:
            self.ids.detalles_hotel_label.text = "OCURRIO UN ERROR"

class MiservicioSreen(Screen):
    def get_ver_servicios_reserva(self, id_reserva):
        if not id_reserva:
            self.ids.detalles_servicios_label.text =  "Necesitamos su id de reserva"
            return
        url=f"http://127.0.0.1:3648/api/reserva/servicios/{id_reserva}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                datas = response.json()
                detalles_servico = ""  
                for data in datas:
                    detalles_servico += (
                        f"Codigo R/S: {data['id']}\n"
                        f"ID Reserva: {data['id_reserva']} | "
                        f"ID Servicio: {data['id_servicio']}\n"
                    )
                self.ids.detalles_servicios_label.text = detalles_servico
            if response.status_code == 400:
                self.ids.detalles_servicios_label.text =  "No hay sevicios reservados"
            if response.status_code == 404:
                self.ids.detalles_servicios_label.text =  "ID de reserva no existe"            
        except requests.exceptions.RequestException as e:
            self.ids.detalles_servicios_label.text = "Error al intentar ver los servicios agregados"
            
    def get_ver_servicios_gratuitos(self, id_habitacion):
        if not id_habitacion:
            self.ids.detalles_servicios_label.text = "Necesitamos su id habitacion"
            return
        url=f"http://127.0.0.1:3648/api/servicios/habitacion/{id_habitacion}"
        try:
            if not id_habitacion:
                self.ids.detalles_servicios_label.text = "Complete los campos"
            response = requests.get(url)
            if response.status_code == 200:
                datas=response.json()
                detalles_servicios = "" 
                for data in datas:
                    detalles_servicios += (
                        f"id: {data['id_servicio']} | "
                        f"USD: {data['precio']}\n"
                        f"{data['servicio']} | "
                        f"Clase: {data['tipo']}\n"
                    )
                self.ids.detalles_servicios_label.text = detalles_servicios
            if response.status_code == 400:
                 self.ids.detalles_servicios_label.text= "No hay servicios gratuitos incluidos en esta habitacion"
            if response.status_code == 404:
                 self.ids.detalles_servicios_label.text= "ID de habitacion no existe"   
        except requests.exceptions.RequestException as e:
                 self.ids.detalles_servicios_label.text= "Error al intentar ver los servicios"
       
# Crear el gestor de pantallas
class HoteleriaApp(MDApp):
    def build(self):
        return Builder.load_file('desig.kv')

if __name__ == '__main__':
    HoteleriaApp().run()
