# Predicción de Código HTS de 6 Dígitos a partir de Lenguaje Natural

Este proyecto tiene como misión desarrollar un sistema avanzado de predicción del código HTS (Harmonized Tariff Schedule) de 6 dígitos, empleando técnicas de procesamiento de lenguaje natural (NLP) para analizar y comprender entradas textuales proporcionadas por el usuario. Aprovechando la riqueza semántica y la capacidad de inferencia de modelos de lenguaje de última generación, este sistema está diseñado para optimizar y automatizar el proceso de clasificación arancelaria de productos en el comercio internacional.

Al permitir la interpretación inteligente de descripciones en lenguaje natural, esta solución no solo reduce la complejidad inherente a la clasificación de productos dentro de los marcos regulatorios globales, sino que también mejora la precisión y la eficiencia del proceso. Este enfoque innovador tiene el potencial de transformar la forma en que las empresas navegan por las complejidades del comercio internacional, reduciendo la incertidumbre asociada con los códigos HTS y facilitando el cumplimiento normativo con una precisión excepcional.

![RAG-Index creation](https://github.com/user-attachments/assets/d00770fd-9688-4319-b037-b2e592f85758)

## Introducción

Este proyecto implementa un sistema de **Recuperación Aumentada con Generación (RAG)**. RAG combina técnicas de **búsqueda basada en recuperación** y **generación de texto** mediante modelos de lenguaje natural. La idea principal es que el modelo de generación se apoya en información relevante recuperada de una base de conocimiento o documentos externos para generar respuestas más precisas y contextuales a las preguntas del usuario.

## ¿Cómo funciona RAG?

El sistema RAG consta de dos componentes principales:

1. **Recuperador de información**: 
   - Cuando se recibe una consulta, el sistema busca en una base de datos (puede ser una base de conocimientos, documentos, etc.) para recuperar los fragmentos más relevantes. Esta base se encuentra localmente en Chromadb, donde los documentos han sido previamente indexados. 
   
2. **Generador basado en un modelo de lenguaje**: 
   - Una vez que se recuperan los fragmentos relevantes, estos se pasan al generador (como un modelo de lenguaje basado en Transformer, por ejemplo, GPT) que utiliza esa información para generar una respuesta coherente y precisa a la consulta inicial.

### Pasos de procesamiento:

1. **Input del usuario**: El sistema recibe una consulta en lenguaje natural.
2. **Recuperación de documentos**: Se buscan los documentos o fragmentos más relevantes a la consulta.
3. **Incorporación de la información recuperada**: La información obtenida se introduce al modelo de lenguaje.
4. **Generación de respuesta**: El modelo genera una respuesta final que integra tanto el contexto de la consulta como la información recuperada.
5. **Devolución de la respuesta al usuario**: Codigo HTS a 6 digitos (Capitulo, parte y subparte) o bien, 3 posibles codigos a ser utilizados en caso de recibir una entrada muy ambigüa.

## Estructura del Proyecto

```
/RAG_Project
│
├── /data/                # Contiene los documentos que serán indexados para la recuperación
├── /index/               # Contiene el o los Index creados a partir del data
├── /retriever/           # Código del recuperador (búsqueda)
├── /scripts/             # Scripts de apoyo diversos (web_scrap, indexación, etc.)
├── README.md             # Este archivo
└── requirements.txt      # Dependencias del proyecto
```

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
  - [1. Clonar el Repositorio](#1-clonar-el-repositorio)
  - [2. Instalar Paquetes Necesarios](#2-instalar-paquetes-necesarios)
  - [3. Instalar Ollama y el Modelo Llama 3](#3-instalar-ollama-y-el-modelo-llama-3)
  - [4. Instalar CUDA 11.6](#5-instalar-cuda-116)
    - [a. Instalar PyTorch con Soporte CUDA](#a-instalar-pytorch-con-soporte-cuda)
    - [b. Verificar la Instalación de PyTorch y CUDA](#b-verificar-la-instalación-de-pytorch-y-cuda)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Requisitos Previos

- **Python 3.11** instalado en su sistema.
- **Google Chrome** instalado.
- **Ollama** y el modelo **Llama 3** instalados. (Ver sección de instalación)
- **CUDA 11.6** instalado si utiliza una GPU NVIDIA compatible.

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

### 4. Instalar CUDA 11.6

Si su sistema cuenta con una GPU NVIDIA compatible, puede instalar CUDA 11.6 para acelerar el procesamiento.

#### a. Verificar Compatibilidad

Asegúrese de que su GPU NVIDIA sea compatible con CUDA 11.6. Puede consultar la lista de GPUs compatibles en el sitio oficial de NVIDIA.

#### b. Descargar CUDA 11.6

Visite el siguiente enlace para descargar CUDA 11.6:

[Descargar CUDA 11.6](https://developer.nvidia.com/cuda-11-6-2-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)

Seleccione las opciones que correspondan a su sistema operativo:

- **Sistema Operativo:** Windows / Linux
- **Arquitectura:** x86_64
- **Versión:** 11.6
- **Tipo de Instalador:** Local

#### c. Instalar CUDA 11.6

**En Windows:**

1. Ejecute el instalador descargado (`cuda_11.6.*_win10.exe`).
2. Siga las instrucciones en pantalla.
   - Seleccione "Custom (Advanced)" si desea personalizar la instalación.
   - Asegúrese de instalar los componentes necesarios como los controladores, herramientas de desarrollo y bibliotecas.
3. Reinicie el sistema si se le solicita.

**En Linux:**

1. Otorgue permisos de ejecución al instalador:

   ```bash
   chmod +x cuda_11.6.*_linux.run
   ```

2. Ejecute el instalador:

   ```bash
   sudo ./cuda_11.6.*_linux.run
   ```

3. Siga las instrucciones en pantalla.
   - Acepte los términos y condiciones.
   - Seleccione los componentes que desea instalar.
4. Configure las variables de entorno agregando las siguientes líneas al final de su archivo `~/.bashrc` o `~/.bash_profile`:

   ```bash
   export PATH=/usr/local/cuda-11.6/bin:$PATH
   export LD_LIBRARY_PATH=/usr/local/cuda-11.6/lib64:$LD_LIBRARY_PATH
   ```

5. Actualice el entorno:

   ```bash
   source ~/.bashrc
   ```

#### d. Verificar la Instalación

Para verificar que CUDA se instaló correctamente, ejecute en la terminal:

```bash
nvcc --version
```

Debería mostrar información sobre la versión de CUDA instalada.

#### a. Instalar PyTorch con Soporte CUDA

Después de instalar CUDA, es necesario instalar PyTorch con soporte para CUDA. Ejecute el siguiente comando:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```

**Nota:** Aunque hemos instalado CUDA 11.6, el índice `cu117` corresponde a CUDA 11.7. Asegúrese de que la versión de PyTorch sea compatible con su versión de CUDA. Si necesita instalar una versión específica para CUDA 11.6, puede consultar las instrucciones en la [página de instalación de PyTorch](https://pytorch.org/get-started/locally/).

#### b. Verificar la Instalación de PyTorch y CUDA

Para comprobar que PyTorch reconoce su GPU y que está utilizando CUDA correctamente, puede ejecutar el siguiente script:

```python
import torch
import torch.nn as nn

# Check if CUDA is available
print(f"CUDA Available: {torch.cuda.is_available()}")

# Print CUDA device name
if torch.cuda.is_available():
    print(f"Device Name: {torch.cuda.get_device_name(0)}")
```

Guarde este código en un archivo llamado `check_cuda.py` y ejecútelo:

```bash
python check_cuda.py
```

Debería obtener una salida similar a:

```
CUDA Available: True
Device Name: NVIDIA GeForce GTX 1080
```

Si `CUDA Available` es `True`, significa que PyTorch está configurado correctamente para utilizar CUDA.

## Contribuciones

¡Las contribuciones son bienvenidas! Por favor, siga estos pasos:

1. Haga un fork del repositorio.
2. Cree una rama con una descripción clara de su función o corrección: `git checkout -b mi-nueva-funcionalidad`.
3. Haga commit de sus cambios: `git commit -am 'Agrega nueva funcionalidad'`.
4. Empuje a la rama: `git push origin mi-nueva-funcionalidad`.
5. Abra un Pull Request en GitHub.

## Derechos y Uso Académico

Este proyecto ha sido desarrollado como parte de un trabajo académico para el Tec de Monterrey en el curso de "Proyecto Integrador" bajo la supervisión de Horacio Martínez Alfaro. Su uso está limitado exclusivamente a fines educativos y no se autoriza su explotación comercial ni su distribución fuera del ámbito académico sin el consentimiento expreso de los autores y la universidad.

Cualquier referencia o reutilización de este trabajo deberá ser debidamente citada y acreditada a los autores originales. Para consultas o solicitudes de uso, por favor contactar con los autores a través de los canales oficiales de la universidad.
