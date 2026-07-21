# Metodología FV® de validación

La revisión se ejecuta en dos niveles:

1. **Estructura del CFDI:** tipo de comprobante, método de pago, forma de pago, fecha, proveedor y UUID.
2. **Relación de pagos:** separación PUE/PPD, existencia de complemento y detección de combinaciones incoherentes.

El semáforo está diseñado para operación diaria:

- **Verde:** sin incidencias en las reglas implementadas.
- **Amarillo:** requiere seguimiento o documento relacionado.
- **Rojo:** inconsistencia o dato obligatorio faltante.

La salida debe revisarse por un profesional antes de generar layouts definitivos o modificar sistemas externos.
