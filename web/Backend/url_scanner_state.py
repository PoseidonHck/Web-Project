import reflex as rx
import requests as req
import os
import base64
from dotenv import load_dotenv

### Cargamos el contenido del archivo .env
load_dotenv()

class UrlScannerState(rx.State):
    """
    Este State manejará la lógica del escáner de URLs.
    """
    url: str = ""
    result: str = ""

    def scan_url(self):
        api_key = os.getenv("API_KEY_VT")
        if not api_key:
            raise ValueError("Error de configuación")
        
        headers = {
            "x-apikey": api_key,
            "accept": "application/json"
        }

        url_id = base64.urlsafe_b64encode(f"{self.url}".encode()).decode().strip("=") ### Proceso de codificación de la url para la API

        vt_url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

        try:
            response = req.get(vt_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                stats = data["data"]["attributes"]["last_analysis_stats"]
                malicious = stats["malicious"]
                suspicious = stats["suspicious"]
                harmless = stats["harmless"]

                self.result = f"""
                ✅ Análisis completado:
                - Maliciosos: {malicious}
                - Sospechosos: {suspicious}
                - Inofensivos: {harmless}
                """
            else:
                self.result = f"❌ Error: {response.status_code} - {response.reason}"
        except Exception as e:
            self.result = f"❌ Fallo en el análisis: {str(e)}"