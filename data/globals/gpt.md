Sí. He revisado fuentes españolas e internacionales y hay material bastante bueno para montar exactamente el sistema que describes: curvas de referencia por sexo y edad y, encima, ir añadiendo las mediciones de tu bebé.

La conclusión principal es que **yo no me limitaría a una única referencia española**. Para construir el sistema usaría **OMS como referencia principal**, porque publica datos muy estructurados y reproducibles, y añadiría **Orbegozo 2011 / Estudios Españoles de Crecimiento** como segunda referencia para comparar con población española. En la práctica española conviven ambas referencias: AEPap incluye tanto curvas OMS como las de Orbegozo entre sus herramientas, y GuíaSalud/SNS utiliza curvas OMS en documentación clínica.

| Fuente | Población | Peso | Longitud/talla | Perímetro craneal | Formato útil para programar | Mi valoración |
| --- | --- | ---: | ---: | ---: | --- | --- |
| **WHO Child Growth Standards** | Internacional, 6 países | ✅ 0–5 a | ✅ 0–5 a | ✅ 0–5 a | XLSX, percentiles y z-scores | **Referencia principal** |
| **CDC mirror de WHO** | Los mismos datos OMS | ✅ 0–24 m | ✅ 0–24 m | ✅ 0–24 m | **CSV + L/M/S** | **La forma más cómoda para empezar** |
| **Fundación Orbegozo 2011** | Vizcaya, España | ✅ 0–18 a | ✅ 0–18 a | ✅ 0–18 a | PDF/tablas P3…P97 | **Muy buena comparación española** |
| **Estudio Español de Crecimiento 2008/2010** | Multicéntrico España | ✅ | ✅ | Limitado | PDF/tablas | **Muy buena segunda referencia española** |
| **CDC 2000** | EE. UU. | ✅ | ✅ | ✅ 0–36 m | CSV/XLS + L/M/S | Útil como contraste |
| **INTERGROWTH-21st** | Internacional | ✅ | ✅ | ✅ | tablas/calculadores | Especialmente relevante si hubo prematuridad |

### 1. La fuente que usaría como base: OMS

La OMS publica las curvas completas de **peso para la edad**, **longitud/talla para la edad** y **perímetro craneal para la edad**, separadas por sexo. Para peso hay tablas desde nacimiento hasta 5 años; para longitud, nacimiento–2 años, y talla de pie, 2–5 años; para perímetro craneal, nacimiento–5 años. Además publica los valores tanto como **percentiles** como **z-scores**, y dispone de Excel descargables.

[OMS — peso para la edad](https://www.who.int/tools/child-growth-standards/standards/weight-for-age?utm_source=chatgpt.com)  
[OMS — longitud/talla para la edad](https://www.who.int/toolkits/child-growth-standards/standards/length-height-for-age?utm_source=chatgpt.com)  
[OMS — perímetro craneal para la edad](https://www.who.int/tools/child-growth-standards/standards/head-circumference-for-age?utm_source=chatgpt.com)

Estas curvas proceden del WHO Multicentre Growth Reference Study, con unos 8.440 niños de Brasil, Ghana, India, Noruega, Omán y Estados Unidos. La idea es importante: **no pretenden describir el niño promedio de cada país**, sino servir como estándar de cómo crecen niños sanos en condiciones favorables, utilizando además al lactante amamantado como modelo normativo. España no formó parte de la muestra.

Para tu proyecto esto es una ventaja: tienes una referencia estable, internacional y reproducible.

### 2. Hay una versión todavía mejor para trabajar con código: WHO en CSV

Curiosamente, para tus necesidades una de las fuentes más prácticas es el CDC estadounidense, que redistribuye los **datos de las curvas WHO** en CSV.

Para nacimiento–24 meses ofrecen por separado niños y niñas para peso, longitud y perímetro craneal. Y lo más interesante es que los CSV contienen **L, M y S**, además de percentiles seleccionados.

[CDC — WHO Growth Charts Data Files, CSV/XLS](https://www.cdc.gov/growthcharts/who-data-files.htm?utm_source=chatgpt.com)

Desde esa página puedes descargar directamente:

- Weight-for-age, Boys/Girls.
- Length-for-age, Boys/Girls.
- Head circumference-for-age, Boys/Girls.
- Weight-for-length, Boys/Girls.

Esta sería probablemente **mi primera descarga**.

Los archivos incluyen P3, P5, P10, P25, P50, P75, P90, P95 y P97 y los parámetros LMS. El CDC indica además que se dan a intervalos mensuales y que, si quieres trabajar a una resolución temporal más fina, puedes interpolar los parámetros.

### 3. Por qué los parámetros LMS te interesan mucho

Para simplemente dibujar las líneas P3, P10, P50, P90 y P97 basta con tener columnas de percentiles.

Pero con **L, M y S** puedes hacer algo mucho más potente: dado cualquier peso, longitud o perímetro craneal de tu bebé, puedes calcular automáticamente su **z-score y su percentil exacto**.

Para una medida \(X\), si \(L \neq 0\):

\[
z = \frac{(X/M)^L-1}{L\,S}
\]

y después:

\[
percentil = \Phi(z)
\]

donde \(\Phi\) es la CDF de la distribución normal. El propio CDC documenta estas ecuaciones y los parámetros.

Esto significa que tu dataset de mediciones puede ser muy sencillo:

```text
date
age_days
age_months
weight_kg
length_cm
head_circumference_cm
weight_z
weight_percentile
length_z
length_percentile
head_z
head_percentile
```

Y yo conservaría **z-score además del percentil**. Para analizar evolución en el tiempo resulta más cómodo comparar, por ejemplo, `z_weight = -0.3 → -0.2 → -0.1` que percentiles que tienen una escala muy no lineal en los extremos.

### 4. Referencia española: Orbegozo 2011

Aquí hay datos especialmente interesantes para lo que quieres hacer.

La Fundación Faustino Orbegozo publica gratuitamente en su web el **Estudio de Crecimiento de Bilbao 2011**, y contiene exactamente tus tres variables:

**longitud/talla, peso y perímetro craneal**, separadas para niños y niñas. Las tablas incluyen `n`, media, desviación estándar, P3, P10, P25, P50, P75, P90 y P97.

[Fundación Orbegozo — página de tablas y gráficas](https://www.fundacionorbegozo.com/el-instituto-de-investigacion-del-crecimiento-y-desarrollo/graficas-y-tablas/?utm_source=chatgpt.com)  
[Orbegozo — Estudio de Crecimiento de Bilbao 2011, PDF completo](https://www.fundacionorbegozo.com/wp-content/uploads/pdf/estudios_2011.pdf?utm_source=chatgpt.com)

El estudio transversal contiene **6.443 sujetos de 0 a 18 años**, de los cuales 3.496 eran varones y 2.947 mujeres; los datos fueron recogidos entre noviembre de 2000 y octubre de 2001. Para 1 mes–3 años procedían de consultas pediátricas, guarderías y centros infantiles de distintas zonas de Vizcaya, y la selección de centros pretendía ser representativa de la población de Vizcaya.

Para bebés, las tablas son especialmente fáciles de transformar en dataset porque utilizan aproximadamente:

```text
RN
3 meses
6 meses
9 meses
12 meses
15 meses
18 meses
21 meses
24 meses
```

Por ejemplo, la tabla masculina de peso incluye a los 12 meses P3=8,55 kg, P50=10,32 kg y P97=12,74 kg; y continúa con todos los demás percentiles.  La correspondiente tabla de perímetro craneal incluye igualmente nacimiento, 3, 6, 9, 12, 15, 18, 21 y 24 meses.

Es decir, ese PDF se puede convertir fácilmente a algo como:

```text
source,sex,metric,age_months,p3,p10,p25,p50,p75,p90,p97
orbegozo2011,M,weight,0,...
orbegozo2011,M,weight,3,...
orbegozo2011,M,weight,6,...
...
orbegozo2011,F,head_circumference,24,...
```

Hay, sin embargo, una diferencia respecto a WHO: aunque Orbegozo indica que utilizó el método **LMS** para el ajuste de las curvas, las tablas públicas presentan los percentiles resultantes, no un dataset sencillo de parámetros L/M/S como el CSV WHO.

Para **dibujar P3/P10/P25/P50/P75/P90/P97**, esto no es ningún problema.

Para calcular cualquier percentil intermedio o z-score exacto, WHO resulta bastante más cómodo.

También hay una cuestión de licencia: el PDF de 2011 lleva copyright y señala que no puede reproducirse total o parcialmente sin autorización; AEPap explica además las condiciones de autorización de la Fundación para publicar sus curvas. Por tanto, lo usaría tranquilamente como fuente de consulta y para un análisis privado, pero **no asumiría que es un dataset open-data redistribuible** si algún día publicas tu aplicación o los datos derivados.

### 5. Una referencia española todavía más amplia: Estudio Español 2008/2010

También merece mucho la pena incorporarlo.

El **Estudio transversal español de crecimiento 2008** analizó peso, talla e IMC de **32.064 sujetos**, incluyendo Andalucía, Barcelona, Bilbao y Zaragoza. Incluía 5.796 recién nacidos a término y 23.701 niños y adolescentes desde 0,25 hasta 18 años. El artículo es de acceso abierto bajo licencia Creative Commons y contiene las tablas percentiladas.

[Estudio Español de Crecimiento 2008 — Parte II, tablas de talla/peso/IMC](https://www.analesdepediatria.org/es-download-pdf-S1695403308702054?utm_source=chatgpt.com)

Es particularmente rico en percentiles: aparecen P2, P3, P10, P15, P20, P25, P50, P75, P80, P85, P90, P97 y P98. Por ejemplo, la tabla masculina de peso comienza en nacimiento y continúa a 0,25, 0,50, 0,75, 1,00 años, etc.

Después se creó **Estudios Españoles de Crecimiento 2010**, combinando estudios realizados en Andalucía, Aragón, Cataluña, Madrid y País Vasco; el estudio transversal conjunto llegó a 38.461 sujetos. La Asociación Española de Pediatría mantiene disponible públicamente el documento.

[AEP — Estudios Españoles de Crecimiento 2010, PDF](https://static.aeped.es/eecweb14_09_10_6686e74f01.pdf?utm_source=chatgpt.com)

Para tus tres charts, sin embargo, hay un matiz: **Orbegozo es más útil para perímetro craneal**, mientras que el gran estudio español es especialmente interesante para peso y longitud/talla.

### 6. Si quieres una referencia externa adicional: CDC

Los CDC también publican los datos de sus propias curvas estadounidenses directamente en **CSV y Excel**, con parámetros LMS.

Incluyen nacimiento–36 meses para peso, longitud y perímetro craneal, además de peso para longitud.

[CDC Growth Charts — data files CSV/XLS con LMS](https://www.cdc.gov/growthcharts/cdc-data-files.htm?utm_source=chatgpt.com)

Yo no los usaría como tu referencia clínica principal estando en España, pero sí pueden ser muy interesantes para un análisis tipo:

```text
mi bebé
vs WHO
vs España / Orbegozo
vs CDC EEUU
```

y comprobar cuánto depende el percentil de la referencia elegida.

### 7. Caso especial: si nació prematuro

Si hubo prematuridad, añadiría otra fuente antes de empezar a interpretar las curvas ordinarias: **INTERGROWTH-21st**.

Tiene estándares específicos postnatales de prematuros para **peso, longitud y perímetro craneal**, con centiles y z-scores descargables. El proyecto además permite descargar tablas, gráficas y calculadores y señala que sus charts pueden utilizarse libremente.

Si no hubo prematuridad, no necesitas complicarlo con esto.

### Cómo lo montaría yo

Haría una pequeña arquitectura de datos que mantuviera separadas **referencias** y **mediciones del bebé**:

```text
reference_curves.csv

source
sex
metric
age_days
age_months
percentile
value
```

Así tendrías, por ejemplo:

```text
WHO,M,weight,365,12,3,7.8
WHO,M,weight,365,12,15,...
WHO,M,weight,365,12,50,...
ORBEGOZO,M,weight,365,12,3,8.55
ORBEGOZO,M,weight,365,12,50,10.32
...
```

Y aparte:

```text
baby_measurements.csv

date
age_days
weight_kg
length_cm
head_circumference_cm
```

Tu pipeline podría entonces:

1. descargar y normalizar WHO;
2. transformar Orbegozo y/o Estudio Español a la misma estructura;
3. calcular edad **exacta en días** desde la fecha de nacimiento;
4. calcular z-score/percentil WHO para cada medida;
5. interpolar la curva de referencia para la edad exacta;
6. dibujar P3/P10/P25/P50/P75/P90/P97;
7. superponer las mediciones reales;
8. opcionalmente mostrar simultáneamente WHO y España.

Para el cálculo automatizado WHO también existe el paquete oficial **`anthro` de R**, que calcula z-scores de peso, longitud/talla y perímetro craneal, entre otros indicadores, para menores de 5 años.

[R/CRAN — paquete WHO anthro](https://CRAN.R-project.org/package=anthro?utm_source=chatgpt.com)

Una consideración importante: en bebés conviene distinguir **longitud tumbado** de **altura/talla de pie**. WHO usa longitud recumbente hasta los 2 años y altura a partir de los 2 años; no conviene mezclarlas sin tener en cuenta el protocolo de medición.

Y desde el punto de vista del análisis, me interesaría mucho más **la trayectoria** que un punto aislado. Las propias guías españolas advierten de que una medida aislada —e incluso dos muy próximas— no permite determinar por sí sola si el crecimiento es adecuado; las gráficas son una herramienta de seguimiento, no un diagnóstico.

**El siguiente paso que haría es ya totalmente práctico:** descargar los CSV WHO, extraer las tablas de **Orbegozo 2011** y del **Estudio Español 2008** y dejarte un único dataset limpio con algo como `source / sex / metric / age / percentile / value`. A partir de ahí podemos construir en Python un primer notebook que genere automáticamente los tres charts —**peso, longitud y perímetro craneal**— y al que solo tengas que ir añadiendo las mediciones de tu bebé.
