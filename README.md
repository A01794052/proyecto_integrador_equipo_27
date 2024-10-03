# Predicción de Código HTS de 6 Dígitos a partir de Lenguaje Natural

Este proyecto tiene como objetivo predecir un código HTS (Harmonized Tariff Schedule) de 6 dígitos basándose en una entrada de lenguaje natural proporcionada por el usuario. Esto facilita la clasificación de productos en el comercio internacional.

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
  - [1. Clonar el Repositorio](#1-clonar-el-repositorio)
  - [2. Instalar Paquetes Necesarios](#2-instalar-paquetes-necesarios)
  - [3. Instalar Ollama y el Modelo Llama 3](#3-instalar-ollama-y-el-modelo-llama-3)
  - [4. Instalar ChromeDriver (Opcional)](#4-instalar-chromedriver-opcional)
    - [a. Verificar la Versión de Google Chrome](#a-verificar-la-versión-de-google-chrome)
    - [b. Descargar ChromeDriver](#b-descargar-chromedriver)
    - [c. Configurar ChromeDriver](#c-configurar-chromedriver)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos Previos

- **Python 3.x** instalado en su sistema.
- **Google Chrome** instalado.
- **Ollama** y el modelo **Llama 3** instalados. (Ver sección de instalación)

## Instalación

### 1. Clonar el Repositorio

Abra una terminal y clone el repositorio:

```bash
git clone https://github.com/usuario/nombre-del-repositorio.git
cd nombre-del-repositorio
```

### 2. Instalar Paquetes Necesarios

Instale las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Instalar Ollama y el Modelo Llama 3

Este proyecto utiliza **Ollama** para ejecutar el modelo **Llama 3** localmente. Siga estos pasos para instalar ambos:

#### a. Instalar Ollama

Visite el sitio oficial de Ollama: [https://ollama.com/](https://ollama.com/)

- **En macOS:**

  Ollama se puede instalar utilizando **Homebrew**:

  ```bash
  brew install ollama/tap/ollama
  ```

- **En Windows y Linux:**

  A partir de octubre de 2024, Ollama ofrece soporte completo para Windows y Linux. Por favor, consulte la [documentación oficial](https://github.com/jmorganca/ollama#readme) para obtener instrucciones específicas y actualizaciones.

#### b. Instalar el Modelo Llama 3

Una vez que Ollama esté instalado, puede descargar e instalar el modelo **Llama 3** ejecutando:

```bash
ollama pull llama3
```

Este comando descargará el modelo y lo preparará para su uso con Ollama.

### 4. Instalar ChromeDriver (Opcional)

**Nota:** Este paso es necesario **solo si** desea volver a crear el diccionario utilizando técnicas de web scraping con Selenium.

#### a. Verificar la Versión de Google Chrome

Es importante que la versión de ChromeDriver coincida con la versión de Google Chrome instalada en su sistema.

- **En Windows:**
  1. Abra Google Chrome.
  2. Haga clic en el ícono de tres puntos verticales en la esquina superior derecha.
  3. Vaya a **Ayuda** > **Información de Google Chrome**.
  4. Anote el número de versión (por ejemplo, `117.0.5938.62`).

- **En macOS:**
  1. Abra Google Chrome.
  2. En la barra de menú superior, haga clic en **Chrome** > **Acerca de Google Chrome**.
  3. Anote el número de versión.

- **En Linux:**
  1. Abra Google Chrome.
  2. Haga clic en el ícono de tres puntos verticales.
  3. Vaya a **Ayuda** > **Acerca de Google Chrome**.
  4. Anote el número de versión.

#### b. Descargar ChromeDriver

Visite el sitio oficial de descargas de ChromeDriver:

[https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

1. En la sección **Stable Releases**, busque la versión que coincida con su versión de Chrome.
2. Descargue el archivo correspondiente a su sistema operativo:
   - **Windows:** `chromedriver-win64.zip`
   - **macOS (Intel):** `chromedriver-mac-x64.zip`
   - **macOS (Apple Silicon):** `chromedriver-mac-arm64.zip`
   - **Linux:** `chromedriver-linux64.zip`
3. Extraiga el contenido del archivo ZIP descargado.

#### c. Configurar ChromeDriver

- **En Windows:**
  1. Mueva `chromedriver.exe` a una carpeta de su elección, por ejemplo, `C:\webdrivers`.
  2. Agregue la ruta de la carpeta a la variable de entorno `PATH`:
     - Presione `Win + R`, escriba `sysdm.cpl` y presione Enter.
     - Vaya a la pestaña **Opciones avanzadas** y haga clic en **Variables de entorno**.
     - En **Variables del sistema**, seleccione `Path` y haga clic en **Editar**.
     - Haga clic en **Nuevo** y agregue la ruta `C:\webdrivers`.
     - Confirme todas las ventanas abiertas con **Aceptar**.

- **En macOS/Linux:**
  1. Mueva `chromedriver` a `/usr/local/bin/`:
     ```bash
     sudo mv chromedriver /usr/local/bin/
     ```
  2. Asegúrese de que el archivo sea ejecutable:
     ```bash
     sudo chmod +x /usr/local/bin/chromedriver
     ```

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, siga estos pasos:

1. Haga un fork del repositorio.
2. Cree una rama con una descripción clara de su función o corrección: `git checkout -b mi-nueva-funcionalidad`.
3. Haga commit de sus cambios: `git commit -am 'Agrega nueva funcionalidad'`.
4. Empuje a la rama: `git push origin mi-nueva-funcionalidad`.
5. Abra un Pull Request en GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo [LICENSE](LICENSE) para más detalles.
