from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
#Esta es la opcion mejorada para opbtener automaticamente el driver y colocarlo en un folder temporal
# Configurar las opciones del navegador
options = webdriver.ChromeOptions()
# Opcional: establecer el directorio de descarga
download_dir = os.path.join(os.getcwd(), 'WebScrap_PDFs')
# Crear el directorio si no existe
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

prefs = {
    'download.default_directory': download_dir,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'plugins.always_open_pdf_externally': True,
    'plugins.plugins_disabled': ['Chrome PDF Viewer'],
    'profile.default_content_setting_values.automatic_downloads': 1,
    'profile.default_content_settings.popups': 0,
}
options.add_experimental_option('prefs', prefs)

# Inicializar el WebDriver (en este caso, Chrome)
driver = webdriver.Chrome(options=options)

try:
    # Navegar a la página web donde se encuentra el enlace
    url = 'https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2022-edition/hs-nomenclature-2022-edition.aspx'
    driver.get(url)

    # Esperar a que la página cargue completamente
    time.sleep(5)

    # Encontrar todos los enlaces que apunten a archivos PDF
    pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, '_2022e.pdf')]")

    # Verificar si se encontraron enlaces
    if pdf_links:
            print(f'Se encontraron {len(pdf_links)} enlaces PDF.')
            for index, pdf_link in enumerate(pdf_links):
                # Obtener el texto del elemento padre (segundo <td>)
                parent_td = pdf_link.find_element(By.XPATH, '../../td[2]')
                nombre_archivo = parent_td.text.strip()
                nombre_archivo = nombre_archivo.removesuffix('.')
                #On Windows, not a good idea to store very large name files
                nombre_archivo = nombre_archivo[:100]

                # Obtener la URL completa del PDF
                pdf_url = pdf_link.get_attribute('href')
                print(f'Descargando archivo {index + 1}: {pdf_url}')

                # Navegar directamente al enlace del PDF para iniciar la descarga
                driver.execute_script("window.open(arguments[0], '_blank');", pdf_url)
                driver.switch_to.window(driver.window_handles[-1])

                # Esperar hasta que el archivo aparezca en el sistema de archivos
                file_name = pdf_url.split('/')[-1]
                file_name = file_name.removesuffix('?la=en')

                #Concatenamos la descripcion del link + el nombre del PDF (ejemplo 0101_2022e.pdf)
                file_path = os.path.join(download_dir, file_name)

                wait_time = 0
                while not os.path.exists(file_path) and wait_time < 5:
                    time.sleep(5)
                    wait_time += 1

                if os.path.exists(file_path):
                    print(f'Archivo {file_name} descargado exitosamente.')                
                    new_name = file_name.split('.pdf')[0] + '_'+ nombre_archivo  +'.pdf'
                    os.rename(os.path.join(download_dir, file_name), 
                              os.path.join(download_dir, new_name))
                else:
                    print(f'Error al descargar el archivo {file_name}.')

                # Cerrar la pestaña actual y volver a la pestaña principal
                #driver.close()
                driver.switch_to.window(driver.window_handles[0])

            print('Descargas completadas.')
    else:
        print('No se encontraron enlaces PDF.')

finally:
    # Cerrar el navegador
    driver.quit()



#<a href="/-/media/wco/public/global/pdf/topics/nomenclature/instruments-and-tools/hs-nomenclature-2022/2022/0100_2022e.pdf?la=en" target="_blank">0100-2022E</a>