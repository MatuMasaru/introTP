#:kivy 1.0.9   installed kivymd-2.0.1.dev0
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivymd.app import MDApp
import requests


# pantallas
class MainScreen(Screen):
    pass

class DetailsScreen(Screen):
    def get_reservation_details(self, code):
        response = requests.get(f'http://127.0.0.1:3648/api/reserva/detalles/{code}')
        if response.status_code == 200:
            datas = response.json()
            data=datas[0]
            self.ids.details_label.text =(
                f"Nombre: {data['nombre']}\n"
                f"Correo: {data['correo']}\n"
                f"Llegada: {data['llegada']}\n"
                f"Salida: {data['salida']}\n"
                f"Estado: {data['estado']}\n"
            )
        else:
            self.ids.details_label.text = "Reserva no encontrada."

class CancelScreen(Screen):
    def cancel_reservation(self, code, name):
        url = f"http://127.0.0.1:3648/api/reserva/cancelar/{code}/{name}"
        response = requests.post(url)
        if response.status_code == 200:
            self.ids.cancel_label.text = "Reserva cancelada exitosamente."
        elif response.status_code == 400:
            self.ids.cancel_label.text = "Su reserva ya se encuentra cancelada"
        else:
            self.ids.cancel_label.text = "Error al cancelar la reserva."

# gestor de pantallas
class ReservationApp(MDApp):
    def build(self):
        return Builder.load_file('desig.kv')

if __name__ == '__main__':
    ReservationApp().run()
