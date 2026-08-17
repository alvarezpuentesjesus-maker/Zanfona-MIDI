# Zanfona-MIDI

En este repositorio se recogen tanto los archivos de fabricación mecánica como el software y los esquemas electrónicos para la fabricación de un prototipo funcional de una zanfona MIDI. Este proyecto ha sido desarrollado como TFG para el grado en Robótica en la Universidad de Santiago de Compostela.

## [Archivos_MIDI](Archivos_MIDI)

Para que el instrumento produzca sonido, es necesario conectarlo a un software de producción musical. En este caso se ha escogido [LMMS Studio](https://lmms.io/). 

Se han preparado archivos diferentes en esta carpeta, para interpretar varios instrumentos, gracias a la web de [Musical Artifacts](https://musical-artifacts.com/), que proporciona samples gratuitos.

## [Electrónica](Electrónica) 

En esta carpeta están contenidos los diferentes esquemáticos utilizados en este proyecto. Además, se ha añadido el archivo de simulación empleado para la placa Resitor_Ladder, llamdo Simulación_Resistor_Ladder.txt.
Para emplear este archivo correctamente es necesario cargarlo en el simulador de circuitos de [MasterPLC](https://masterplc.com/simulador/).

Se adjunta aquí mismo una tabla con las conexiones de la placa principal para mayor facilidad de lectura:

<div align="center">

| Pin | Nombre | Conexión |
| :---: | :---: | :---: |
| 1 | GP0 | Manivela SDA |
| 2 | GP1 | Manivela SCL |
| 3 | GND | |
| 4 | GP2 | Display cuerdas 1 |
| 5 | GP3 | Display cuerdas 2 |
| 6 | GP4 | Display cuerdas 3 |
| 7 | GP5 | Display cuerdas 4 |
| 8 | GND | |
| 9 | GP6 | Display cuerdas 5 |
| 10 | GP7 | Display cuerdas 6 |
| 11 | GP8 | Display cuerdas 7 |
| 12 | GP9 | Display cuerdas 8 |
| 13 | GND | |
| 14 | GP10 | Display cuerdas 9 |
| 15 | GP11 | Display cuerdas Estado |
| 16 | GP12 | CLK Encoder Cuerdas |
| 17 | GP13 | DT Encoder Cuerdas |
| 18 | GND | |
| 19 | GP14 | SW Encoder Cuerdas |
| 20 | GP15 | CLK Encoder Perro |
| 21 | GP16 | DT Encoder Perro |
| 22 | GP17 | SW Encoder Perro |
| 23 | GND | |
| 24 | GP18 | CLK Encoder Bending |
| 25 | GP19 | DT Encoder Bending |
| 26 | GP20 | SW Encoder Bending |
| 27 | GP21 | NC |
| 28 | GND | |
| 29 | GP22 | NC |
| 30 | RUN | NC |
| 31 | GP26 A0 | Teclado Resistencias |
| 32 | GP27 A1 | NC |
| 33 | ADC GND | |
| 34 | GP28 A2 | Bending |
| 35 | ADV Vref | NC |
| 36 | 3v3 Vout | |
| 37 | 3v3 En | NC |
| 38 | GND | |
| 39 | VSYS 5V* | NC |
| 40 | VBUS 5V | |

</div>

## [Hardware](Hardware)

Aquí se ven contenidos los archivos de fabricación mecánica. Como archivo principal Archivo_Corte.CDR, permite el uso de una cortadora láser para fabricar todas las piezas necesarias en MDF de 3mm. Se facilitan también los archivos individuales de cada pieza en formato DXF en la carpeta [Piezas_individuales](Hardware/Piezas_individuales)

## [Software](Software)

Este proyecto se ha desarrollado utilizando una Raspberry Pi Pico como microcontrolador principal. A su vez, se ha necesitado el firmware de [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) para poder utilizarla como USB nativo, además de poder cargarle las librerías necesarias de [Adafruit_MIDI](https://github.com/adafruit/Adafruit_CircuitPython_MIDI). En este caso se deben tener incluidas las librerías: adafruit_bus_device, adafruit_midi y adafruit_register.

Una vez configurada la Raspberry, es necesario copiar en el interior de su carpeta el archivo [code.py](Software/code.py) y la carpeta [dependencias](Software/dependencias), para el correcto funcionamiento de la zanfona.

Por otra parte, se facilita un archivo llamado [MEDIAS.py](Software/MEDIAS.py), que se utiliza para medir el rango de tensión de cada tecla pulsada y completar la tabla contenida en el archivo [variables.py](Software/dependencias/variables.py).


## BOM

En la siguiente tabla se puede ver el BOM tanto de elementos de hardware como electrónica para todo lo necesario en este proyecto:

<div align="center">

| Categoría | Referencia | Descripción | Cantidad | Precio ud | Precio Total | Proveedor |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| Electrónica | SC0915 | Microcontrolador Raspberry Pi Pico | 1 | 3,51 € | 3,51 € | [TME](https://www.tme.eu/es/details/sc0915/raspberry-pi-sistemas-embebidos/raspberry-pi/raspberry-pi-pico/) |
| Electrónica | CF1/4W-10K | Resistencia 10K 100ud | 1 | 0,87 € | 0,87 € | [TME](https://www.tme.eu/es/details/cf1_4w-10k/resistencias-tht/sr-passives/) |
| Electrónica | CF1/4W-150R | Resistencias 150Ω 100ud | 1 | 0,90 € | 0,90 € | [TME](https://www.tme.eu/es/details/cf1_4w-150r/resistencias-tht/sr-passives/) |
| Electrónica | CF1/4W-2K | Resistencias teclado 2K 100ud | 1 | 0,74 € | 0,74 € | [TME](https://www.tme.eu/es/details/cf1_4w-2k/resistencias-tht/sr-passives/) |
| Electrónica | TAL220B | Galga extensiométrica 5Kg | 1 | 9,49 € | 9,49 € | [Amazon](https://www.amazon.es/QUARKZMAN-Digital-Precisi%C3%B3n-Electr%C3%B3nica-Port%C3%A1til/dp/B0G6Z576YL?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3MXEXNLLG8ZYZ&dib=eyJ2IjoiMSJ9.YhST5GRXG6aw1tRz0bgUr-2E3-8ofKzEYWXDyEjprn12wi5UHXDlIB_pFqkgrtp0MtVtB_g-kR-8Ex5Rw3CZTbA200MN584rLLaxsyuNY8G6uuHpe6Hq_O_wARUQTBW8l-3AZOeJvB1u7nAOmHoUv6PnSoK9zrxsarHeapq7c4UcgWILs3MsMasmjlfNeS_gjrpjbF132InFCBMqrfz_BkvXCyda6HUVDKD3SWe_ul63vbSC9NdY6ROrNAjyrXrlTovx7AyRXuar3GgZqe5uBzK-WzHEHMDzfTC3_bXxYmw.4rc_Jw3I51aTTrwmcEHa3ISVoW8TCyM5r_KPQqgSTRQ&dib_tag=se&keywords=sensor+peso+5kg&qid=1784124820&refinements=p_n_condition-type%3A15144009031%2Cp_36%3A-8000&rnid=2493681031&sprefix=sensor+peso+5kg%2Caps%2C84&sr=8-4) |
| Electrónica | AD620 | Amplificador Galga | 1 | 5,79 € | 5,79 € | [Funduino](https://funduinoshop.com/es/modulos-electronicos/otros/amplificador/amplificador-de-tension-milivoltios-ad620) |
| Electrónica | OSX10201-R | Barra Led 10 segmentos Roja | 1 | 0,82 € | 0,82 € | [TME](https://www.tme.eu/es/details/osx10201-r/pantallas-led-otros/optosupply/) |
| Electrónica | EC11E12-15P30C-SW | Encóders | 3 | 1,42 € | 4,26 € | [TME](https://www.tme.eu/es/details/ec11e12-15p30c-sw/codificadores-incrementales/sr-passives/) |
| Electrónica | AS5600 | Sensor Magneto resistivo | 1 | 0,99 € | 0,99 € | [Aliexpress](https://es.aliexpress.com/item/1005006349632569.html?spm=a2g0o.productlist.main.3.1e9b4d710cXNPK&algo_pvid=bd5f913e-d705-4a1f-97da-167c0424a91f&algo_exp_id=bd5f913e-d705-4a1f-97da-167c0424a91f-45&pdp_ext_f=%7B%22order%22%3A%22544%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21EUR%212.00%210.99%21%21%2116.24%218.04%21%40211b80d117609526132433478e8a14%2112000038573167261%21sea%21ES%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Af52a33eb%3Bm03_new_user%3A-29895%3BpisId%3A5000000187636417&curPageLogUid=AERfdpVlDqbp&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006349632569%7C_p_origin_prod%3A) |
| Electrónica | XY308-2P 2.54MM GREEN | Conector Bloque Terminal 10ud | 1 | 2,29 € | 2,29 € | [TME](https://www.tme.eu/en/details/xy308-2p-2.54-gn/pcb-terminal-blocks/xinya/xy308-2p-2-54mm-green/) |
| Electrónica | XHP-3 | Conector JST 3 pines 2.5mm Hembra | 4 | 0,06 € | 0,24 € | [TME](https://www.tme.eu/es/details/xhp-3/conectores-de-senal-raster-2-50mm/jst/) |
| Electrónica | B3B-XH-A (LF)(SN) | Conector JST 3 pines 2.5mm Macho | 4 | 0,09 € | 0,36 € | [TME](https://www.tme.eu/es/details/b3b-xh-a/conectores-de-senal-raster-2-50mm/jst/b3b-xh-a-lf-sn/) |
| Electrónica | XHP-4 | Conector JST 4 pines 2.5mm Hembra | 2 | 0,07 € | 0,14 € | [TME](https://www.tme.eu/es/details/xhp-4/conectores-de-senal-raster-2-50mm/jst/) |
| Electrónica | B4B-XH-A (LF)(SN) | Conector JST 4 pines 2.5mm Macho | 2 | 0,11 € | 0,22 € | [TME](https://www.tme.eu/es/details/b4b-xh-a/conectores-de-senal-raster-2-50mm/jst/b4b-xh-a-lf-sn/) |
| Electrónica | XHP-5 | Conector JST 5 pines 2.5mm Hembra | 6 | 0,06 € | 0,36 € | [TME](https://www.tme.eu/es/details/xhp-5/conectores-de-senal-raster-2-50mm/jst/) |
| Electrónica | B5B-XH-A (LF)(SN) | Conector JST 5 pines 2.5mm Macho | 6 | 0,16 € | 0,96 € | [TME](https://www.tme.eu/es/details/b5b-xh-a/conectores-de-senal-raster-2-50mm/jst/b5b-xh-a-lf-sn/) |
| Electrónica | Cable AWG 26 | Bobina de cable para usos varios | 1 | 8,99 € | 8,99 € | [Amazon](https://www.amazon.es/HAAMNING7-conexi%C3%B3n-el%C3%A9ctrico-bricolaje-maquetas/dp/B0G6BPVY99?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=17BTDANXSN8RN&dib=eyJ2IjoiMSJ9.0h_exdMRcrVrHEM88xtfHpvq8BqVwnhMpijX6NhHbx8-qdEP8_tj4EalpWsMere1suuscVAAS4fwilQePXeeZNBFdoaa-QIve4Zxbn36fAFhckwP3aY_PHUI6BphLcQ98f0K6iccVkjImN8j2hspmW0gQ-RLx6-aVyCsuwvHHOAbJaWMc0QoIhThil_CUNIXU_jYFnh9k7K26MVUCx3Oq8fTFWSfs0l68y-WBgVGMilbPd5aEl-g8OUunQFFU4bDv78VP8ZD7dGkv_NHWES1HOKGRebYwm5PujQC6Wb-oPI.7SrV8tzonUWxU0Tc8xvZ8OP7qK-2wsvPxJzMTf_FtSo&dib_tag=se&keywords=bobina%2Bcable%2Bawg%2B26&qid=1784206180&sprefix=bobina%2Bcable%2Bawg%2B2%2Caps%2C156&sr=8-11&th=1) |
| Electrónica | PCBs | Coste producción PCBs | 3 | 5,00 € | 15,00 € | [PCBWay](https://www.pcbway.es/) |
| **Subtotal Electrónica** | | | | | **55,93 €** | |
| Hardware | B5X10/BN3 | Tornillos M5 10mm 100ud | 1 | 3,18 € | 3,18 € | [TME](https://www.tme.eu/es/details/b5x10_bn3/tornillos/bossard/1004077/) |
| Hardware | M3X20/D912-A2 | Tornillos M3 20mm 100ud | 1 | 2,63 € | 2,63 € | [TME](https://www.tme.eu/es/details/m3x20_d912-a2/tornillos/kraftberg/) |
| Hardware | M3X30/D912-A2 | Tornillos M3 30mm 100ud | 1 | 3,10 € | 3,10 € | [TME](https://www.tme.eu/es/details/m3x30_4762_8bl/tornillos/reca/00823-30-000-1000/) |
| Hardware | B3/BN124 | Tuercas M3 5,5mm 100ud | 1 | 0,63 € | 0,63 € | [TME](https://www.tme.eu/es/details/b3_bn124/tuercas/bossard/1090615/) |
| Hardware | ST-093/1 | Punteras conexiones teclas M3 20ud | 2 | 1,09 € | 2,18 € | [TME](https://www.tme.eu/es/details/st-093_1/conectores-no-aislados/ninigi/) |
| Hardware | Eje de acero 8mm x 200mm | Eje de acero 8mm x 200mm | 1 | 3,71 € | 3,71 € | [Amazon](https://www.amazon.es/precisi%C3%B3n-inoxidable-ondulado-endurecido-adicional/dp/B07VMSMGLC?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dib=eyJ2IjoiMSJ9.Dq0ttiRY_IAvZR_LSr9g17DEy049-9YktrDO8zThRrzpgm1gFQNSJYn-iHZKp1uF6kWMEmhD8SZ2OS57KQkCBMU0Fjs1_4M1iXfkMLfg1At-iGaXG5_kTwlqDa7kh_EIvA1uTtQYg5OQebS6CxXLdbS89J1mD_4iWD5hu6f2xvL3e_UtEcESD6jd1PMf3kddwk5gJpNnvwyFm_5Pv0u_J5Lzp-Cs_QjMX8nHkisKeUuXSOR6FP6oLSLFBdTDD3RY0uJmzY5xc1J2RoiTi6IfriU6jqmulrQlEpgVd4Jwwy4.pJJ34NgrKn7T5YyfY85mBQhOZzEaSONguxZl0Va2ly8&dib_tag=se&keywords=eje%2Bde%2Bacero%2B8mm&qid=1784107376&s=industrial&sr=1-4&th=1) |
| Hardware | Cable de acero 1mm | Cable de acero 1mm | 1 | 2,49 € | 2,49 € | [Leroy Merlin](https://www.leroymerlin.es/productos/cable-de-acero-galvanizado-de-1mm-de-y-10-m-de-longitud-89125664.html) |
| Hardware | Clavijas 3L3R | Clavijas Guitarra | 1 | 8,45 € | 8,45 € | [Amazon](https://www.amazon.es/QWORK-clavijero-Afinaci%C3%B3n-el%C3%A9ctricas-galvanizada/dp/B0B2JW5N1K?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1T6JP1RVTXKHE&dib=eyJ2IjoiMSJ9.ZFoxj1ZE7Yd1N5iFiT0F2qPO8FO8q2W2mJroCLn5fZB8uhEv7TlV1dTbYMsniFDkespERv85w4q09bBeuxqMz3nt553N_1gNw88uazjQSStAFCyWpWAffmwsxQZsyUKohHgD2rrrxBO6T-GJGCxjX8_egteHTjK_zQTcs7Q-z0vRNfuVwKzRMmqbB4qbutDfNCzUwz63ZUovIRzVFsSQq1DLYNEs2ifR5Y6Y9aT_DljOOqQzQ3WrmgHvjM1TMig7l0CPlhvyzdMgeNL5KIevmqTCMrXH5uH9_G97F5vI8bY.8T8ZWLvt-H2eX7lnRf-LIEptAu6B-B6KNwYXSU_Rqic&dib_tag=se&keywords=clavijas+guitarra&qid=1784739201&sprefix=calvijas+guitarra%2Caps%2C97&sr=8-2) |
| Hardware | TABLERO MDF 120X60X0,3CM | Madera en plancha 120x60x0,3cm | 1 | 6,30 € | 6,30 € | [Obramat](https://www.obramat.es/productos/tablero-mdf-120x60x0-3cm-10114503.html) |
| Hardware | Hilo elástico 0,5mm | Hilo elástico 0,5mm | 1 | 0,94 € | 0,94 € | [Amazon](https://www.amazon.es/Hilo-Nailon-el%C3%A1stico-Transparente-50mm/dp/B09ZHVVFNJ?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=AP8QOEKXXYKX&dib=eyJ2IjoiMSJ9.-F9HX3cAMIWRFaTXHI-jL-WJRwOL9PJchJO3HlyY81zCmZlqaZOzh6kIIB2X6mCcpt7YDk6M_MnXz4g6oLk93aYT0AeVK4NqLc3R9OAALGWwNK9v721Uja_o7D_SUap6Nw3LnYQWIgMDUQ0berTlQ-QTGmLC2Q88lgU0kRMdr1T9Wvz4ZnbKcQ2KjRhD9Gr8N6QIAPFdCtaVl59NEObp7a8Kpuq8HcJkV-Pn3PTjINzABbketh8j-JcmGU2R_5CXTToEPVnalD_8Mr93cDIOZpqAUSekfpAGavt2jLjNk-g.kQUfOlpyXJvpm5AG-Rm5oh8vY-7Kr-sv3NUq9CivPaA&dib_tag=se&keywords=hilo%2Belastico%2Btransparente%2B0.5mm&qid=1784204916&sprefix=hilo%2Belastico%2Btransparente%2B0.5m%2Caps%2C157&sr=8-5&th=1) |
| **Subtotal Hardware** | | | | | **33,61 €** | |
| **Coste Total de fabricación** | | | | | **89,54 €** | |

</div>

Los precios pueden variar con el tiempo o incluso no tener existencias, se recomienda utilizar la referencia y buscar enlaces de compra adaptados a la disponibilidad del momento.


