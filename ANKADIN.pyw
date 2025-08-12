from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
import datetime

# Pencere boyutunu ayarla
Window.size = (500, 700)
Window.resizable = False  # Boyut değiştirilemesin

# Konum Sınıfı
class Konum:
    def __init__(self):
        self.enlem = None
        self.boylam = None
        self.zaman = None

    def konumAl(self):
        # Örnek konum: Tandoğan
        self.enlem = 38.334217  # Örnek: İnönü Üniversitesi enlemi
        self.boylam = 38.438061  # Örnek: İnönü Üniversitesi boylamı
        self.zaman = datetime.datetime.now()

    def bilgi_goster(self):
        return f"Enlem: {self.enlem}\nBoylam: {self.boylam}\nZaman: {self.zaman}"

    def __str__(self):
        return f"Enlem: {self.enlem}, Boylam: {self.boylam}, Zaman: {self.zaman}"

# Menü Sayfası
class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Boşluk ekleyerek butonları alta kaydırma
        layout.add_widget(Label(size_hint=(1, 0.5))) 

        # Başlık
        bold_font_path = './ARIALBD.TTF'
        title = Label(text="ANKADIN", font_size=80, font_name=bold_font_path, color=[0, 0, 0.502, 1], size_hint=(1, None))
        title.height = 120  # Başlık yüksekliğini ayarlıyoruz
        layout.add_widget(title)

        # Alt metin
        subtitle = Label(text="'Küllerinden Doğan Kadınlar'", font_size=30, font_name=bold_font_path, color=[0, 0, 0, 1], size_hint=(1, None))
        subtitle.height = 0  # Alt metin yüksekliğini ayarlıyoruz
        layout.add_widget(subtitle)

        image = Image(source='D:\Projelerim\ANKADIN\logo.com.png', size_hint=(1, None), size=(450, 450)) 
        layout.add_widget(image)

        # Boşluk ekleyerek butonları alta kaydırma
        layout.add_widget(Label(size_hint=(1, 0.5)))  # Bu boşluk butonu aşağıya itecektir

        # Bilgi Sayfasına geçiş butonu
        button = Button(text="GİRİŞ", size_hint=(0.3, None), height=100, font_name=bold_font_path, background_color=(0, 0, 0.502, 1), pos_hint={"center_x": 0.5}, on_press=self.go_to_info_page)
        layout.add_widget(button)

        # Arkaplan rengi
        with self.canvas.before:
            Color(0.537, 0.812, 0.941, 1)  # Bebe mavisi rengi
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def go_to_info_page(self, instance):
        self.manager.current = "info"


# Bilgi Sayfası
class Info(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        bold_font_path = './ARIALBD.TTF'

        # Ana içerik düzeni
        content_layout = BoxLayout(orientation='vertical', padding=40, spacing=40)



        info_layout = GridLayout(cols=2, size_hint=(1, None), height=300, spacing=10)
        # Kişisel Bilgiler
        personal_info_layout = BoxLayout(orientation='vertical', spacing=5)
        health_info_layout = BoxLayout(orientation='vertical', spacing=5)
        personal_info_layout.add_widget(Label(text="Kişisel Bilgiler", font_size=20, font_name=bold_font_path, size_hint_y=None, height=40, color=(0, 0, 0.502, 1)))
        health_info_layout.add_widget(Label(text="Sağlık Bilgileri", font_size=20, font_name=bold_font_path, size_hint_y=None, height=40, color=(0, 0, 0.502, 1)))
        self.ad_input = TextInput(hint_text="İsim (ad-soyad)", size_hint_y=None, height=40)
        self.kimlik_input = TextInput(hint_text="Kimlik Numarası", size_hint_y=None, height=40)
        self.cinsiyet_input = TextInput(hint_text="Cinsiyet (Kadın, Erkek)", size_hint_y=None, height=40)
        self.yas_input = TextInput(hint_text="Yaş", size_hint_y=None, height=40)
        self.dogum_input = TextInput(hint_text="Doğum Tarihi(gg.aa.yy)", size_hint_y=None, height=40)
        self.telefon_input = TextInput(hint_text="Telefon Numarası", size_hint_y=None, height=40)
        self.kanGrubu_input = TextInput(hint_text="Kan Grubu", size_hint_y=None, height=62.5)
        self.alerji_input = TextInput(hint_text="Alerjiler", size_hint_y=None, height=62.5)
        self.alinanIlac_input = TextInput(hint_text="Alınan İlaçlar", size_hint_y=None, height=62.5)
        self.hastalikBilgisi_input = TextInput(hint_text="Hastalıklar", size_hint_y=None, height=62.5)


        personal_info_layout.add_widget(self.ad_input)
        personal_info_layout.add_widget(self.kimlik_input)
        personal_info_layout.add_widget(self.cinsiyet_input)
        personal_info_layout.add_widget(self.yas_input)
        personal_info_layout.add_widget(self.dogum_input)
        personal_info_layout.add_widget(self.telefon_input)     
        health_info_layout.add_widget(self.kanGrubu_input)
        health_info_layout.add_widget(self.alerji_input)
        health_info_layout.add_widget(self.alinanIlac_input)
        health_info_layout.add_widget(self.hastalikBilgisi_input)

        # Kişisel ve Sağlık Bilgilerini yatayda ekle
        info_layout.add_widget(personal_info_layout)
        info_layout.add_widget(health_info_layout)

        content_layout.add_widget(info_layout)

        # Acil Durum Kişileri
        acil_durum_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        acil_durum_layout.add_widget(Label(text="Acil Durum Kişileri", font_size=20, font_name=bold_font_path,size_hint_y=None, height=40, color=(0, 0, 0.502, 1)))

        # Acil Durum Kişisi 1
        self.acil_ad1_input = TextInput(hint_text="1. Kişi: İsim-Yakınlık Derecesi-Telefon Numarası", multiline=False, size_hint_y=None, height=40)
        acil_durum_layout.add_widget(self.acil_ad1_input)

        # Acil Durum Kişisi 2
        self.acil_ad2_input = TextInput(hint_text="2. Kişi: İsim-Yakınlık Derecesi-Telefon Numarası", multiline=False, size_hint_y=None, height=40)
        acil_durum_layout.add_widget(self.acil_ad2_input)

        # Acil Durum Kişisi 3
        self.acil_ad3_input = TextInput(hint_text="3. Kişi: İsim-Yakınlık Derecesi-Telefon Numarası", multiline=False, size_hint_y=None, height=40)
        acil_durum_layout.add_widget(self.acil_ad3_input)

        content_layout.add_widget(acil_durum_layout)

        # Butonlar (alt kısımda, yan yana)
        buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=80, spacing=20)

        # Menüye dönme butonu
        back_button = Button(text="MENÜ", size_hint=(0.5, None), height=60, font_name=bold_font_path, background_color=(0, 0, 0.502, 1), pos_hint={"center_x": 0.5}, on_press=self.go_to_menu_page)
        buttons_layout.add_widget(back_button)

        # Acil Yardım butonu
        acil_button = Button(text="ACİL YARDIM", size_hint=(0.5, None), height=60, font_name=bold_font_path, background_color=(0, 0, 0.502, 1), pos_hint={"center_x": 0.5}, on_press=self.acil_yardim)
        buttons_layout.add_widget(acil_button)

        content_layout.add_widget(buttons_layout)
        layout.add_widget(content_layout)

        # Arkaplan rengi
        with self.canvas.before:
            Color(0.537, 0.812, 0.941, 1)  # Bebe mavisi rengi
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def go_to_menu_page(self, instance):
        self.manager.current = "menu"

    def acil_yardim(self, instance):
        konum = Konum()
        konum.konumAl()  # Konum bilgisi alınıyor
        self.goster_bilgiler(konum)

    def goster_bilgiler(self, konum):
        # Bilgileri popup penceresinde göster
        bilgi = f"Kişisel Bilgiler:\nİsim: {self.ad_input.text}\nKimlik Numarası: {self.kimlik_input.text}\nCinsiyet: {self.cinsiyet_input.text}\nYaş: {self.yas_input.text}\nDoğum Tarihi: {self.dogum_input.text}\nTelefon Numarası: {self.telefon_input.text}\n\n"
        bilgi += f"Sağlık Bilgileri:\nKan Grubu: {self.kanGrubu_input.text}\nAlerjiler: {self.alerji_input.text}\nAlınan İlaçlar: {self.alinanIlac_input.text}\nHastalıklar: {self.hastalikBilgisi_input.text}\n\n"
        bilgi += f"Acil Durum Kişileri:\nKişi 1: {self.acil_ad1_input.text}\n"
        bilgi += f"Kişi 2: {self.acil_ad2_input.text}\n"
        bilgi += f"Kişi 3: {self.acil_ad3_input.text}\n\n"
        bilgi += f"Konum Bilgisi:\n{konum.bilgi_goster()}"
        popup = Popup(title="Kullanıcı Bilgileri", content=Label(text=bilgi), size_hint=(None, None), size=(400, 600))
        popup.open()


# Uygulama Sınıfı
class Uygulama(App):
    def build(self):
        # Ekran yöneticisi
        sm = ScreenManager()

        # Ekranlar
        sm.add_widget(Menu(name="menu"))
        sm.add_widget(Info(name="info"))

        return sm


if __name__ == "__main__":
    Uygulama().run()