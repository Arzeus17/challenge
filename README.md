CHALLENGER MERCADO LIBRE
Se presenta un Reporte General y detallado de todas las acciones llevadas a cabo para lograr los 
objetivos, y de las herramientas empleadas, puede ubicarlo en: Reporte.ipynb, en el presente Repositorio.


Primera Parte - SQL
Objetivo
A partir de la siguiente necesidad, se requiere diseñar un DER que responda al modelo del
negocio. En la Carpeta Parte1a_DER se tiene el archivo DER_Ventas.mwb, y ademas se presenta
una imagen en la carpeta img llamado DER.jpg, con el diagrama propuesto.

Luego, se debe responder mediante SQL diferentes preguntas.

Para eso de generó el script DDL para la creación de cada una de las tablas representadas en
el DER. Se encuentra en la carpeta Parte1b_DDL con el nombre “create_tables.sql”.

Y para responder las Consultas, se generó el código SQL para responder cada una de las situaciones mencionadas
anteriormente sobre el modelo diseñado. Se encuentra en la carpeta Parte1b_DDL con el nombre: “respuestas_negocio.sql”

Para la Segunda Parte - APIs (Deseable)
Objetivo: Realizar un análisis sobre la oferta/vidriera de las opciones de productos que responden a
distintas búsquedas en el sitio Mercadolibre.com.ar

1) Barrer una lista de más de 150 ítems ids en el servicio público:
https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json
para poder comparar dispositivos portátiles.
2) Por cada resultado, se realizó el correspondiente GET por Item_Id al recurso público:
https://api.mercadolibre.com/items/{Item_Id}
3) Se escribio los resultados en un archivo plano delimitado por comas, desnormalizando
el JSON obtenido en el paso anterior, en tantos campos como sea necesario para
guardar las variables que te interesen modelar. Se guardó como: API.py, ademas se presenta otro archivo de scripts
con el nombre Exploratorios.py, donde se presentan los codigos de los analisis exlporatorio de los datos obtenidos.
Ambos archivos no estan en carpetas.

Finalmente se presenta un documento pdf llamado Dashboards.pdf, donde se muestran los paneles creados en PowerBI, para
el analisis de los resultados, asi como tambien el archivo llamado testMeLi.pbix, donde se llevó a cabo la elaboracion 
de los dashboards.
