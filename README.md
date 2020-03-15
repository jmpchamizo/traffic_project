# Traffic Project
## Proyecto
<p>En este proyecto se desarrolla la detección y clasificación de señales de tráfico.</p>
<p>Para ello se ha usado Opencv (Haar Cascade) para la detección de señales de tráfico y una red neuronal convolucional para su identificación.</p>

## Contenido en las carpetas
<p>En la carpeta data/traffic_cascades se encuentran los haar cascades.</p>
<p>En la carpeta model, los modelos entrenados para clasificar las señales.</p>
<p>Se han entrenado con el dataset https://www.kaggle.com/valentynsichkar/traffic-signs-preprocessed data8.pickle</p>

## Descripción de la api
<p>Endpoints:</p>
<pre><code>/image/signs</code></pre>
<p>Almacena una imagen con la carpeta static con las señales de la foto recuadradas</p>
<ul>
    <li>Method: POST</li>
    <li>Param: image</li>
    <li>Return: ruta de la imagen con las detecciones</li>
</ul>
<pre><code>/upload/image</code></pre>
<p>Sube una imagen a la carpeta static</p>
<ul>
    <li>Method: POST</li>
    <li>Param: image</li>
    <li>Return: filename</li>
</ul>

## Resultados

<p>Adjunto capturas de fotos de prueba</p>
<p>Stop</p>

![Stop](static/detect_1007_bn9_four_waystopjpg_1.29.00.jpeg)
<p>Limite velocidad</p>

![Circle](static/detect_Limite-velocidad-ciudades-1.jpg)
<p>Precaución:</p>

![Triangle](static/detect_peaton.jpeg)
