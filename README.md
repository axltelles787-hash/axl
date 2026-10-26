# Publicar HidroTrack en GitHub Pages

1. Crea un repositorio en GitHub llamado `hidrotrack` y selecciona visibilidad pública.
2. Descomprime este ZIP en tu computadora.
3. Sube el contenido de la carpeta al repositorio: `index.html` debe quedar en la raíz, junto con los otros archivos y la carpeta `fichas`. No subas el ZIP sin descomprimir.
4. En el repositorio entra en Settings → Pages.
5. En Source elige Deploy from a branch. Selecciona la rama main y la carpeta /(root), luego Save.
6. Espera a que termine la publicación. La dirección será https://TU-USUARIO.github.io/hidrotrack/.

No requiere instalación ni compilación. Incluye el simulador, la vista 3D, el plano y las 19 fichas. Para probar localmente, ejecuta `python -m http.server 8000` en esta carpeta y abre http://localhost:8000. Los módulos JavaScript necesitan un servidor HTTP: abrir el HTML con doble clic puede bloquearlos.

El sitio simula el movimiento; no controla un PLC real.

---

# HidroTrack

Simulador web para el control de desplazamiento de un carruaje en un banco hidrométrico.

## Alcance

- Vista superior SVG de piscina, rieles, carruaje y sensor.
- Avance, retroceso, detención, retorno al inicio y parada de emergencia simulada con restablecimiento.
- Consigna de velocidad de 0.05 a 1 m/s, posición, tiempo y distancia simulados.
- Longitud y posición inicial configurables; 8 m es un ejemplo editable, no una medida confirmada del proyecto.
- Registro de eventos en la pestaña y exportación CSV. No hay persistencia al recargar.
- Detención de la simulación al ocultar la pestaña.

## Equipo previsto

Siemens S7-1200, CPU 1214C. No hay una integración física implementada ni conexiones a PLC. Una implementación real requerirá especificar firmware, comunicaciones, accionamiento, posición, sensores e interbloqueos, así como un servicio local y validación del sistema. La parada de emergencia web no sustituye el circuito de seguridad.

## Estructura

Sitio estático en . index.html contiene la interfaz; style.css el diseño adaptable; app.mjs vincula los controles; engine.mjs implementa la simulación. No requiere proceso de build.

## Catálogo y vista del instrumento

La revisión incorpora vistas superior y lateral, seis ilustraciones vectoriales seleccionables y profundidad visual de montaje. Elegir otro instrumento detiene la simulación y registra el cambio. La posición de ambas vistas sigue el mismo motor de simulación.

Tipos: molinete de hélice, molinete de cazoletas, correntómetro electromagnético, ADV, ADCP y sonda multiparámetro auxiliar. No existe una afirmación de compatibilidad universal. El ADCP requiere revisar profundidad y reflexiones; la sonda multiparámetro no se calibra por desplazamiento. Las referencias primarias de OTT, USGS y YSI/SonTek están enlazadas en el catálogo.

El deslizador de inmersión representa la geometría de un montaje manual en una sección ilustrativa de agua; no introduce órdenes verticales al PLC.


## Diseño conceptual del carruaje
- `diseno.html`: modelo 3D de geometría en Canvas con giro, zoom, vistas ortogonales, cotas, rieles y vástago opcionales. No requiere servicios o bibliotecas 3D externas.
- `carruaje-plano.svg`: lámina vectorial acotada e imprimible, generada por `scripts/generate-plan.py`.
- Piscina: largo indicado por usuario 8000 mm; ancho 1200, profundidad 1000 y nivel de agua 800 mm son propuestas.
- Bastidor 1600 x 650 mm, centros de ruedas separados 1400 mm transversalmente y 450 mm longitudinalmente, ruedas Ø120. Vástago Ø20 x 1050.
- Cota 0 en contacto de rodadura, supuesto 100 mm sobre borde. Motor esquemático hasta +440, extremo inferior del vástago/eje del molinete a -800: inmersión 500 mm.
- Es una propuesta visual sin comprobación estructural, potencia calculada ni certificación de calibración. Plano y modelo no sirven directamente para fabricación. El diseño no modifica los parámetros del simulador de supervisión.


## Fichas integradas en 3D
- 19 fichas: 10 piezas mecánicas, 3 de accionamiento/sensores y los 6 instrumentos.
- Cada pieza tiene grupo de geometría seleccionable. El clic sobre una cara usa selección en la proyección actual; una tarjeta también resalta su componente. Los instrumentos cambian la geometría del montaje.
- Referencias consultadas el 26/10/2026: encoder OMRON E6B2-CWZ5B 1000P/R 0.5M (1000 ppr, A/B/Z, PNP, 12–24 VCC, cuerpo40/eje6), familia Oriental Motor BLH (24 VCC, ejemplo30W sin dimensionar), familia OMRON D4N. Enlaces oficiales en cada ficha.
- Ruedas, ejes, soportes y demás piezas a medida son propuestas, no fichas comerciales ni selección para compra. Eje ilustrado corregido a Ø25 mm; adaptación a Ø6 mm de encoder pendiente.
- HTML imprimible por ficha en `fichas/`; regenerar con `node scripts/generate-component-sheets.mjs` tras editar `componentes.mjs`.
