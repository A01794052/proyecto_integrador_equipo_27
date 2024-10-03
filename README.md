Predicción de Código HTS de 6 Dígitos a partir de Lenguaje Natural
Este proyecto tiene como objetivo predecir un código HTS (Harmonized Tariff Schedule) de 6 dígitos basándose en una entrada de lenguaje natural proporcionada por el usuario. Esto facilita la clasificación de productos en el comercio internacional.

Tabla de Contenidos
Requisitos Previos
Instalación
1. Clonar el Repositorio
2. Instalar Paquetes Necesarios
3. Instalar Ollama y el Modelo Llama 2
4. Instalar ChromeDriver (Opcional)
a. Verificar la Versión de Google Chrome
b. Descargar ChromeDriver
c. Configurar ChromeDriver
Contribuciones
Licencia
Requisitos Previos
Python 3.x instalado en su sistema.
Google Chrome instalado.
Ollama y el modelo Llama 2 instalados. (Ver sección de instalación)
Instalación
1. Clonar el Repositorio
Abra una terminal y clone el repositorio:

bash
Copy code
git clone https://github.com/usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
2. Instalar Paquetes Necesarios
Instale las dependencias listadas en requirements.txt:

bash
Copy code
pip install -r requirements.txt
3. Instalar Ollama y el Modelo Llama 2
Este proyecto utiliza Ollama para ejecutar el modelo Llama 2 localmente. Siga estos pasos para instalar ambos:

a. Instalar Ollama
Visite el sitio oficial de Ollama: https://ollama.com/

En macOS:

Ollama se puede instalar utilizando Homebrew:

bash
Copy code
brew install ollama/tap/ollama
En Windows y Linux:

A partir de octubre de 2023, Ollama ofrece soporte limitado para Windows y Linux. Por favor, consulte la documentación oficial para obtener instrucciones específicas y actualizaciones.

b. Instalar el Modelo Llama 2
Una vez que Ollama esté instalado, puede descargar e instalar el modelo Llama 2 ejecutando:

bash
Copy code
ollama pull llama2
Este comando descargará el modelo y lo preparará para su uso con Ollama.

4. Instalar ChromeDriver (Opcional)
Nota: Este paso es necesario solo si desea volver a crear el diccionario utilizando técnicas de web scraping con Selenium.

a. Verificar la Versión de Google Chrome
Es importante que la versión de ChromeDriver coincida con la versión de Google Chrome instalada en su sistema.

En Windows:

Abra Google Chrome.
Haga clic en el ícono de tres puntos verticales en la esquina superior derecha.
Vaya a Ayuda > Información de Google Chrome.
Anote el número de versión (por ejemplo, 117.0.5938.62).
En macOS:

Abra Google Chrome.
En la barra de menú superior, haga clic en Chrome > Acerca de Google Chrome.
Anote el número de versión.
En Linux:

Abra Google Chrome.
Haga clic en el ícono de tres puntos verticales.
Vaya a Ayuda > Acerca de Google Chrome.
Anote el número de versión.
b. Descargar ChromeDriver
Visite el sitio oficial de descargas de ChromeDriver:

https://googlechromelabs.github.io/chrome-for-testing/

En la sección Stable Releases, busque la versión que coincida con su versión de Chrome.
Descargue el archivo correspondiente a su sistema operativo:
Windows: chromedriver-win64.zip
macOS (Intel): chromedriver-mac-x64.zip
macOS (Apple Silicon): chromedriver-mac-arm64.zip
Linux: chromedriver-linux64.zip
Extraiga el contenido del archivo ZIP descargado.
c. Configurar ChromeDriver
En Windows:

Mueva chromedriver.exe a una carpeta de su elección, por ejemplo, C:\webdrivers.
Agregue la ruta de la carpeta a la variable de entorno PATH:
Presione Win + R, escriba sysdm.cpl y presione Enter.
Vaya a la pestaña Opciones avanzadas y haga clic en Variables de entorno.
En Variables del sistema, seleccione Path y haga clic en Editar.
Haga clic en Nuevo y agregue la ruta C:\webdrivers.
Confirme todas las ventanas abiertas con Aceptar.
En macOS/Linux:

Mueva chromedriver a /usr/local/bin/:
bash
Copy code
sudo mv chromedriver /usr/local/bin/
Asegúrese de que el archivo sea ejecutable:
bash
Copy code
sudo chmod +x /usr/local/bin/chromedriver
Contribuciones
¡Las contribuciones son bienvenidas! Por favor, siga estos pasos:

Haga un fork del repositorio.
Cree una rama con una descripción clara de su función o corrección: git checkout -b mi-nueva-funcionalidad.
Haga commit de sus cambios: git commit -am 'Agrega nueva funcionalidad'.
Empuje a la rama: git push origin mi-nueva-funcionalidad.
Abra un Pull Request en GitHub.
Licencia
Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.






You said:
Utilizaste Llama 2, Cambialo por Llama3
ChatGPT

Thought for 27 seconds

Predicción de Código HTS de 6 Dígitos a partir de Lenguaje Natural
Este proyecto tiene como objetivo predecir un código HTS (Harmonized Tariff Schedule) de 6 dígitos basándose en una entrada de lenguaje natural proporcionada por el usuario. Esto facilita la clasificación de productos en el comercio internacional.

Tabla de Contenidos
Requisitos Previos
Instalación
1. Clonar el Repositorio
2. Instalar Paquetes Necesarios
3. Instalar Ollama y el Modelo Llama 3
4. Instalar ChromeDriver (Opcional)
a. Verificar la Versión de Google Chrome
b. Descargar ChromeDriver
c. Configurar ChromeDriver
Contribuciones
Licencia
Requisitos Previos
Python 3.x instalado en su sistema.
Google Chrome instalado.
Ollama y el modelo Llama 3 instalados. (Ver sección de instalación)
Instalación
1. Clonar el Repositorio
Abra una terminal y clone el repositorio:

bash
Copy code
git clone https://github.com/usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
2. Instalar Paquetes Necesarios
Instale las dependencias listadas en requirements.txt:

bash
Copy code
pip install -r requirements.txt
3. Instalar Ollama y el Modelo Llama 3
Este proyecto utiliza Ollama para ejecutar el modelo Llama 3 localmente. Siga estos pasos para instalar ambos:

a. Instalar Ollama
Visite el sitio oficial de Ollama: https://ollama.com/

En macOS:

Ollama se puede instalar utilizando Homebrew:

bash
Copy code
brew install ollama/tap/ollama
En Windows y Linux:

A partir de octubre de 2024, Ollama ofrece soporte completo para Windows y Linux. Por favor, consulte la documentación oficial para obtener instrucciones específicas y actualizaciones.

b. Instalar el Modelo Llama 3
Una vez que Ollama esté instalado, puede descargar e instalar el modelo Llama 3 ejecutando:

bash
Copy code
ollama pull llama3
Este comando descargará el modelo y lo preparará para su uso con Ollama.

4. Instalar ChromeDriver (Opcional)
Nota: Este paso es necesario solo si desea volver a crear el diccionario utilizando técnicas de web scraping con Selenium.

a. Verificar la Versión de Google Chrome
Es importante que la versión de ChromeDriver coincida con la versión de Google Chrome instalada en su sistema.

En Windows:

Abra Google Chrome.
Haga clic en el ícono de tres puntos verticales en la esquina superior derecha.
Vaya a Ayuda > Información de Google Chrome.
Anote el número de versión (por ejemplo, 117.0.5938.62).
En macOS:

Abra Google Chrome.
En la barra de menú superior, haga clic en Chrome > Acerca de Google Chrome.
Anote el número de versión.
En Linux:

Abra Google Chrome.
Haga clic en el ícono de tres puntos verticales.
Vaya a Ayuda > Acerca de Google Chrome.
Anote el número de versión.
b. Descargar ChromeDriver
Visite el sitio oficial de descargas de ChromeDriver:

https://googlechromelabs.github.io/chrome-for-testing/

En la sección Stable Releases, busque la versión que coincida con su versión de Chrome.
Descargue el archivo correspondiente a su sistema operativo:
Windows: chromedriver-win64.zip
macOS (Intel): chromedriver-mac-x64.zip
macOS (Apple Silicon): chromedriver-mac-arm64.zip
Linux: chromedriver-linux64.zip
Extraiga el contenido del archivo ZIP descargado.
c. Configurar ChromeDriver
En Windows:

Mueva chromedriver.exe a una carpeta de su elección, por ejemplo, C:\webdrivers.
Agregue la ruta de la carpeta a la variable de entorno PATH:
Presione Win + R, escriba sysdm.cpl y presione Enter.
Vaya a la pestaña Opciones avanzadas y haga clic en Variables de entorno.
En Variables del sistema, seleccione Path y haga clic en Editar.
Haga clic en Nuevo y agregue la ruta C:\webdrivers.
Confirme todas las ventanas abiertas con Aceptar.
En macOS/Linux:

Mueva chromedriver a /usr/local/bin/:
bash
Copy code
sudo mv chromedriver /usr/local/bin/
Asegúrese de que el archivo sea ejecutable:
bash
Copy code
sudo chmod +x /usr/local/bin/chromedriver
Contribuciones
¡Las contribuciones son bienvenidas! Por favor, siga estos pasos:

Haga un fork del repositorio.
Cree una rama con una descripción clara de su función o corrección: git checkout -b mi-nueva-funcionalidad.
Haga commit de sus cambios: git commit -am 'Agrega nueva funcionalidad'.
Empuje a la rama: git push origin mi-nueva-funcionalidad.
Abra un Pull Request en GitHub.
Licencia
Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.
